#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════════════════
#    _____ _____________________.___________________  ____________________
#   /  _  \\______   \__    ___/|   \_   _____/  _  \ \_   ___ \__    ___/
#  /  /_\  \|       _/ |    |   |   ||    __)/  /_\  \/    \  \/ |    |   
# /    |    \    |   \ |    |   |   ||     \/    |    \     \____|    |   
# \____|__  /____|_  / |____|   |___|\___  /\____|__  /\______  /|____|   
#         \/       \/                    \/         \/        \/          
#       .__         __               .__                                  
# ___  _|__|_______/  |_ __ _______  |  |                                 
# \  \/ /  \_  __ \   __\  |  \__  \ |  |                                 
#  \   /|  ||  | \/|  | |  |  // __ \|  |__                               
#   \_/ |__||__|   |__| |____/(____  /____/                               
#                                  \/                                     
#
# Flex Audit - Enterprise Software Auditing System
# Copyright (c) 2025 ARTIFACT virtual
# ══════════════════════════════════════════════════════════════════════════════
"""
Report Generator for Flex Audit

Generates comprehensive, beautifully formatted audit reports in
Markdown, HTML, and JSON formats.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any
from collections import defaultdict

from .scanner import AuditResult, Finding
from .constants import Severity, Category
from .templates import (
    get_report_header, get_report_footer,
    get_executive_summary_template, get_metrics_dashboard_template,
    get_recommendations_template,
    HTML_REPORT_TEMPLATE, ARTIFACT_VIRTUAL_BANNER,
    SEVERITY_ICONS, CATEGORY_ICONS, get_grade
)
import hashlib
import json


class ReportGenerator:
    """
    Generates comprehensive audit reports in multiple formats.
    
    Supports:
    - Markdown (GitHub flavored)
    - HTML (standalone with embedded CSS)
    - JSON (machine readable)
    """
    
    def __init__(self, result: AuditResult, output_dir: str):
        self.result = result
        self.output_dir = os.path.abspath(output_dir)
        self.project_name = os.path.basename(result.repo_path)
        
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "suggested_fixes"), exist_ok=True)
    
    def generate_all(self) -> Dict[str, str]:
        """Generate all report formats."""
        paths = {
            "markdown": self.generate_markdown(),
            "html": self.generate_html(),
            "json": self.generate_json(),
        }
        
        # Generate fix suggestions
        self.generate_fix_suggestions()
        # Optional professional format: SARIF
        paths["sarif"] = self.generate_sarif()
        
        return paths
    
    def generate_markdown(self) -> str:
        """Generate comprehensive Markdown report."""
        output_path = os.path.join(self.output_dir, "audit_report.md")
        score = self.result.calculate_score()
        grade, grade_desc, _ = get_grade(score)
        
        report = []
        
        # Header
        report.append(get_report_header(self.project_name))
        
        # Executive Summary
        report.append(self._generate_executive_summary_md(score, grade, grade_desc))
        
        # Metrics Dashboard
        report.append(self._generate_metrics_dashboard_md())
        
        # Detailed Findings by Category
        report.append(self._generate_findings_md())
        
        # Recommendations
        report.append(self._generate_recommendations_md())
        
        # File Analysis Summary
        report.append(self._generate_file_summary_md())
        
        # Footer
        report.append(get_report_footer())
        
        # Write report
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        return output_path
    
    def generate_html(self) -> str:
        """Generate standalone HTML report."""
        output_path = os.path.join(self.output_dir, "audit_report.html")
        score = self.result.calculate_score()
        grade, grade_desc, grade_class = get_grade(score)
        
        # Generate findings HTML
        findings_html = self._generate_findings_html()
        
        # Fill template
        html = HTML_REPORT_TEMPLATE.format(
            project_name=self.project_name,
            ascii_logo=ARTIFACT_VIRTUAL_BANNER,
            date=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
            version="1.0",
            score=score,
            grade=f"{grade} - {grade_desc}",
            grade_class=grade_class,
            total_files=self.result.stats.get("total_files", 0),
            total_lines=f"{self.result.stats.get('total_lines', 0):,}",
            total_issues=self.result.total_findings,
            critical_count=self.result.critical_count,
            findings_html=findings_html
        )
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return output_path
    
    def generate_json(self) -> str:
        """Generate machine-readable JSON report."""
        output_path = os.path.join(self.output_dir, "audit_report.json")
        
        report = {
            "meta": {
                "generator": "Flex Audit v2.0",
                "framework": "ARTIFACT virtual Enterprise",
                "timestamp": self.result.timestamp,
                "repository": self.result.repo_path,
                "project_name": self.project_name,
            },
            "summary": {
                "score": self.result.calculate_score(),
                "grade": get_grade(self.result.calculate_score())[0],
                "total_findings": self.result.total_findings,
                "findings_by_severity": {
                    "critical": self.result.critical_count,
                    "high": self.result.high_count,
                    "medium": self.result.medium_count,
                    "low": self.result.low_count,
                    "info": self.result.info_count,
                },
            },
            "statistics": self.result.stats,
            "findings": [f.to_dict() for f in self.result.findings],
            "files_analyzed": [f.to_dict() for f in self.result.files_analyzed],
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        return output_path

    def generate_sarif(self) -> str:
        """Generate SARIF 2.1.0 output for GitHub Code Scanning and other consumers."""
        sarif_output = {
            "version": "2.1.0",
            "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0.json",
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "Flex Audit",
                            "version": "2.0",
                            "informationUri": "https://github.com/amuzetnoM/flex_audit",
                            "rules": []
                        }
                    },
                    "results": []
                }
            ]
        }

        rules_map = {}
        for f in self.result.findings:
            rid = f.issue_type
            if rid not in rules_map:
                rules_map[rid] = {
                    "id": rid,
                    "shortDescription": {"text": rid},
                    "fullDescription": {"text": f.description},
                    "defaultConfiguration": {"level": f.severity.name.lower()}
                }

        sarif_output["runs"][0]["tool"]["driver"]["rules"] = list(rules_map.values())

        for finding in self.result.findings:
            fp = hashlib.sha1(f"{finding.file_path}:{finding.line_number}:{finding.issue_type}".encode()).hexdigest()
            res = {
                "ruleId": finding.issue_type,
                "level": finding.severity.name.lower(),
                "message": {"text": finding.description},
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": finding.file_path},
                            "region": {"startLine": finding.line_number}
                        }
                    }
                ],
                "properties": {
                    "fingerprint": fp,
                    "category": finding.category.value,
                    "matched_text": (finding.matched_text if finding.category != Category.SECURITY else "***REDACTED***")
                }
            }
            sarif_output["runs"][0]["results"].append(res)

        outpath = os.path.join(self.output_dir, "audit_report.sarif")
        with open(outpath, 'w', encoding='utf-8') as fh:
            json.dump(sarif_output, fh, indent=2)

        return outpath
    
    def generate_fix_suggestions(self) -> None:
        """Generate fix suggestion files for critical issues."""
        fixes_dir = os.path.join(self.output_dir, "suggested_fixes")
        
        # Group by issue type
        by_type = defaultdict(list)
        for finding in self.result.findings:
            if finding.severity in (Severity.CRITICAL, Severity.HIGH):
                by_type[finding.issue_type].append(finding)
        
        for issue_type, findings in by_type.items():
            fix_path = os.path.join(fixes_dir, f"fix_{issue_type.lower()}.md")
            
            content = [
                f"# Fix: {issue_type}",
                "",
                f"**Severity:** {findings[0].severity.name}",
                f"**Category:** {findings[0].category.value}",
                f"**Occurrences:** {len(findings)}",
                "",
                "## Description",
                "",
                findings[0].description,
                "",
                "## Affected Files",
                "",
            ]
            
            for f in findings[:20]:  # Limit to 20
                content.append(f"- `{f.file_path}:{f.line_number}`")
            
            if len(findings) > 20:
                content.append(f"- ... and {len(findings) - 20} more")
            
            content.extend([
                "",
                "## Suggested Fix",
                "",
                self._get_fix_suggestion(issue_type),
                "",
                "---",
                "*Generated by Flex Audit v2.0*"
            ])
            
            with open(fix_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))
    
    def _generate_executive_summary_md(self, score: int, grade: str, grade_desc: str) -> str:
        """Generate executive summary section."""
        by_severity = self.result.get_findings_by_severity()
        
        # Determine overview text
        if score >= 80:
            overview = "The codebase demonstrates strong security practices with minimal critical issues. Continue maintaining current standards and address remaining findings in regular development cycles."
        elif score >= 60:
            overview = "The codebase shows acceptable security posture with some areas requiring attention. Priority should be given to addressing high-severity findings within the next sprint cycle."
        elif score >= 40:
            overview = "Significant security and quality concerns were identified. Immediate remediation of critical findings is required before production deployment."
        else:
            overview = "**CRITICAL:** The codebase has severe security vulnerabilities that must be addressed immediately. Production deployment should be blocked until critical issues are resolved."
        
        template = get_executive_summary_template()
        return template.format(
            score=score,
            grade=f"{grade} - {grade_desc}",
            critical=self.result.critical_count,
            high=self.result.high_count,
            medium=self.result.medium_count,
            low=self.result.low_count,
            info=self.result.info_count,
            overview=overview
        )
    
    def _generate_metrics_dashboard_md(self) -> str:
        """Generate metrics dashboard section."""
        stats = self.result.stats
        languages = stats.get("languages", {})
        lang_str = ", ".join(f"{k}" for k in list(languages.keys())[:5])
        if len(languages) > 5:
            lang_str += f" +{len(languages) - 5} more"
        
        template = get_metrics_dashboard_template()
        return template.format(
            total_files=stats.get("total_files", 0),
            total_lines=f"{stats.get('total_lines', 0):,}",
            languages=lang_str or "N/A",
            dependencies="N/A",
            secrets=self._count_by_type("SECRET"),
            vulnerabilities=self.result.critical_count + self.result.high_count,
            misconfigs=self._count_by_category(Category.CONFIGURATION),
            risk_score=100 - self.result.calculate_score(),
            code_smells=self._count_by_category(Category.CODE_QUALITY),
            todos=self._count_by_type("TODO_MARKER"),
            coverage="N/A",
            doc_coverage="N/A"
        )
    
    def _generate_findings_md(self) -> str:
        """Generate detailed findings section."""
        sections = []
        sections.append("## 🔎 Detailed Findings\n")
        
        by_category = self.result.get_findings_by_category()
        
        for category in Category:
            findings = by_category.get(category, [])
            if not findings:
                continue
            
            icon = CATEGORY_ICONS.get(category.value, "📋")
            sections.append(f"\n### {icon} {category.value}\n")
            sections.append(f"<details>")
            sections.append(f"<summary><b>{len(findings)} issues found</b> - Click to expand</summary>\n")
            
            # Table header
            sections.append("| Severity | Location | Issue | Description |")
            sections.append("|:---------|:---------|:------|:------------|")
            
            # Sort by severity
            findings.sort(key=lambda x: list(Severity).index(x.severity))
            
            for finding in findings[:50]:  # Limit to 50 per category
                sev_icon = SEVERITY_ICONS.get(finding.severity.name, "⚪")
                loc = f"`{finding.file_path}:{finding.line_number}`"
                sections.append(f"| {sev_icon} {finding.severity.name} | {loc} | **{finding.issue_type}** | {finding.description[:80]} |")
            
            if len(findings) > 50:
                sections.append(f"\n*... and {len(findings) - 50} more findings in this category*\n")
            
            sections.append("\n</details>\n")
            sections.append("---")
        
        return '\n'.join(sections)
    
    def _generate_recommendations_md(self) -> str:
        """Generate prioritized recommendations section."""
        immediate = []
        short_term = []
        long_term = []
        
        # Analyze findings and generate recommendations
        if self.result.critical_count > 0:
            immediate.append("- 🔴 **Address all critical security vulnerabilities** - Block deployment until resolved")
        
        if self._count_by_type("SECRET") > 0:
            immediate.append("- 🔑 **Remove all exposed secrets** - Rotate credentials and use environment variables")
        
        if self._count_by_type("EVAL_USAGE") > 0 or self._count_by_type("EXEC_USAGE") > 0:
            immediate.append("- ⚠️ **Remove eval/exec usage** - Replace with safe alternatives")
        
        if self.result.high_count > 0:
            short_term.append("- 🟠 **Address high-severity findings** - Schedule for next sprint")
        
        if self._count_by_type("BARE_EXCEPT") > 0:
            short_term.append("- 🐛 **Fix bare except clauses** - Use specific exception types")
        
        if self._count_by_category(Category.CODE_QUALITY) > 10:
            short_term.append("- 📝 **Improve code quality** - Address code smells and TODO items")
        
        long_term.append("- 📊 **Implement continuous security scanning** in CI/CD pipeline")
        long_term.append("- 🧪 **Increase test coverage** to catch regressions")
        long_term.append("- 📚 **Improve documentation** and code comments")
        
        template = get_recommendations_template()
        return template.format(
            immediate_actions='\n'.join(immediate) if immediate else "- ✅ No immediate actions required",
            short_term_actions='\n'.join(short_term) if short_term else "- ✅ No short-term actions required",
            long_term_actions='\n'.join(long_term)
        )
    
    def _generate_file_summary_md(self) -> str:
        """Generate file analysis summary."""
        sections = [
            "## 📁 Files Analyzed\n",
            "<details>",
            "<summary><b>Click to expand file list</b></summary>\n",
            "| File | Language | Lines | Issues |",
            "|:-----|:---------|------:|-------:|"
        ]
        
        # Sort by issue count descending
        sorted_files = sorted(
            self.result.files_analyzed,
            key=lambda x: len(x.findings),
            reverse=True
        )
        
        for fa in sorted_files[:100]:
            issue_count = len(fa.findings)
            issue_badge = f"🔴 {issue_count}" if issue_count > 0 else "✅ 0"
            sections.append(f"| `{fa.relative_path}` | {fa.language} | {fa.lines} | {issue_badge} |")
        
        if len(sorted_files) > 100:
            sections.append(f"\n*... and {len(sorted_files) - 100} more files*\n")
        
        sections.append("\n</details>\n")
        return '\n'.join(sections)
    
    def _generate_findings_html(self) -> str:
        """Generate findings HTML for the report."""
        sections = []
        by_category = self.result.get_findings_by_category()
        
        for category in Category:
            findings = by_category.get(category, [])
            if not findings:
                continue
            
            icon = CATEGORY_ICONS.get(category.value, "📋")
            
            section = f'''
            <div class="findings-section">
                <div class="findings-header">
                    <div class="findings-title">{icon} {category.value}</div>
                    <span class="findings-count">{len(findings)} issues</span>
                </div>
                <table class="findings-table">
                    <thead>
                        <tr>
                            <th>Severity</th>
                            <th>Location</th>
                            <th>Issue</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
            '''
            
            findings.sort(key=lambda x: list(Severity).index(x.severity))
            for finding in findings[:30]:
                sev_class = f"severity-{finding.severity.name.lower()}"
                section += f'''
                        <tr>
                            <td><span class="severity {sev_class}">{finding.severity.name}</span></td>
                            <td class="file-path">{finding.file_path}:{finding.line_number}</td>
                            <td><strong>{finding.issue_type}</strong></td>
                            <td>{finding.description[:60]}...</td>
                        </tr>
                '''
            
            section += '''
                    </tbody>
                </table>
            </div>
            '''
            sections.append(section)
        
        return '\n'.join(sections)
    
    def _count_by_type(self, issue_type: str) -> int:
        """Count findings by issue type (partial match)."""
        return sum(1 for f in self.result.findings if issue_type in f.issue_type)
    
    def _count_by_category(self, category: Category) -> int:
        """Count findings by category."""
        return sum(1 for f in self.result.findings if f.category == category)
    
    def _get_fix_suggestion(self, issue_type: str) -> str:
        """Get fix suggestion for issue type."""
        suggestions = {
            "EVAL_USAGE": """
```python
# Instead of:
result = eval(user_input)

# Use safe alternatives:
import ast
result = ast.literal_eval(user_input)  # For literals only

# Or use a whitelist approach:
allowed_operations = {"add": lambda x, y: x + y}
result = allowed_operations[operation](a, b)
```
""",
            "EXEC_USAGE": """
```python
# Instead of:
exec(dynamic_code)

# Use structured approaches:
# 1. Configuration-based logic
# 2. Plugin systems with sandboxing
# 3. Domain-specific interpreters
```
""",
            "HARDCODED_PASSWORD": """
```python
# Instead of:
password = "my_secret_password"

# Use environment variables:
import os
password = os.environ.get("DB_PASSWORD")

# Or use a secrets manager:
from your_secrets_lib import get_secret
password = get_secret("db_password")
```
""",
            "SQL_INJECTION": """
```python
# Instead of:
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# Use parameterized queries:
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# Or use an ORM:
User.query.filter_by(id=user_id).first()
```
""",
        }
        
        for key, suggestion in suggestions.items():
            if key in issue_type:
                return suggestion
        
        return "Review the affected code and apply security best practices for your framework."
