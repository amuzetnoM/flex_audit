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
Brand Assets and Report Templates for Flex Audit

Contains all branding elements, headers, footers, and style definitions.
"""

from datetime import datetime

# ══════════════════════════════════════════════════════════════════════════════
# ASCII ART HEADERS
# ══════════════════════════════════════════════════════════════════════════════

ARTIFACT_VIRTUAL_BANNER = r"""
   _____ _____________________.___________________  ____________________
  /  _  \\______   \__    ___/|   \_   _____/  _  \ \_   ___ \__    ___/
 /  /_\  \|       _/ |    |   |   ||    __)/  /_\  \/    \  \/ |    |   
/    |    \    |   \ |    |   |   ||     \/    |    \     \____|    |   
\____|__  /____|_  / |____|   |___|\___  /\____|__  /\______  /|____|   
        \/       \/                    \/         \/        \/          
      .__         __               .__                                  
___  _|__|_______/  |_ __ _______  |  |                                 
\  \/ /  \_  __ \   __\  |  \__  \ |  |                                 
 \   /|  ||  | \/|  | |  |  // __ \|  |__                               
  \_/ |__||__|   |__| |____/(____  /____/                               
                                 \/                                     
"""

# Keep backwards compatibility alias
SIRIUS_ALPHA_BANNER = ARTIFACT_VIRTUAL_BANNER

FLEX_AUDIT_BANNER = r"""
███████╗██╗     ███████╗██╗  ██╗     █████╗ ██╗   ██╗██████╗ ██╗████████╗
██╔════╝██║     ██╔════╝╚██╗██╔╝    ██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
█████╗  ██║     █████╗   ╚███╔╝     ███████║██║   ██║██║  ██║██║   ██║   
██╔══╝  ██║     ██╔══╝   ██╔██╗     ██╔══██║██║   ██║██║  ██║██║   ██║   
██║     ███████╗███████╗██╔╝ ██╗    ██║  ██║╚██████╔╝██████╔╝██║   ██║   
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   
"""

AUDIT_COMPLETE_BANNER = r"""
 █████╗ ██╗   ██╗██████╗ ██╗████████╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗
██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝
███████║██║   ██║██║  ██║██║   ██║       ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗  
██╔══██║██║   ██║██║  ██║██║   ██║       ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝  
██║  ██║╚██████╔╝██████╔╝██║   ██║       ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝        ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝
"""


# ══════════════════════════════════════════════════════════════════════════════
# MARKDOWN TEMPLATES
# ══════════════════════════════════════════════════════════════════════════════

def get_report_header(project_name: str, version: str = "1.0") -> str:
    """Generate branded Markdown report header."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f'''<div align="center">

```
{ARTIFACT_VIRTUAL_BANNER}
```

# FLEX AUDIT REPORT

### Enterprise Software Security & Quality Analysis

---

**Project:** `{project_name}`  
**Version:** `{version}`  
**Generated:** `{timestamp}`  
**Framework:** Flex Audit v2.0

---

</div>

---

'''


def get_report_footer() -> str:
    """Generate branded Markdown report footer."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f'''

---

<div align="center">

---

## Report Metadata

| Property | Value |
|:---------|:------|
| **Generator** | Flex Audit v2.0 |
| **Framework** | ARTIFACT virtual Enterprise |
| **Generated** | {timestamp} |
| **Standards** | OWASP, CWE, SANS Top 25 |

---

```
{ARTIFACT_VIRTUAL_BANNER}
```

**© 2025 ARTIFACT virtual - Enterprise Software Intelligence**

*This report was generated automatically by Flex Audit.*  
*For questions or support, visit: https://github.com/amuzetnoM*

---

</div>
'''


def get_executive_summary_template() -> str:
    """Template for executive summary section."""
    return '''
## Executive Summary

<table>
<tr>
<td width="50%">

### Overall Security Score

<div align="center">

# {score}/100

**{grade}**

</div>

</td>
<td width="50%">

### Risk Distribution

| Severity | Count |
|:---------|------:|
| [!!] Critical | {critical} |
| [!] High | {high} |
| [*] Medium | {medium} |
| [-] Low | {low} |
| [.] Info | {info} |

</td>
</tr>
</table>

### Assessment Overview

{overview}

---
'''


def get_findings_section_template() -> str:
    """Template for detailed findings section."""
    return '''
## Detailed Findings

### {category_icon} {category_name}

<details>
<summary><b>{issue_count} issues found</b> - Click to expand</summary>

{findings_table}

</details>

---
'''


def get_finding_row_template() -> str:
    """Template for individual finding row."""
    return '''| {severity_icon} | `{file}:{line}` | **{issue_type}** | {description} |'''


def get_recommendations_template() -> str:
    """Template for recommendations section."""
    return '''
## Prioritized Recommendations

### Immediate Actions (0-3 days)

{immediate_actions}

### Short-term Actions (1-2 weeks)

{short_term_actions}

### Long-term Actions (1-3 months)

{long_term_actions}

---
'''


def get_metrics_dashboard_template() -> str:
    """Template for metrics dashboard section."""
    return '''
## Code Metrics Dashboard

<table>
<tr>
<td width="33%">

### Repository Stats

| Metric | Value |
|:-------|------:|
| Total Files | {total_files} |
| Lines of Code | {total_lines} |
| Languages | {languages} |
| Dependencies | {dependencies} |

</td>
<td width="33%">

### Security Metrics

| Metric | Value |
|:-------|------:|
| Secrets Found | {secrets} |
| Vulnerabilities | {vulnerabilities} |
| Misconfigs | {misconfigs} |
| Risk Score | {risk_score} |

</td>
<td width="34%">

### Quality Metrics

| Metric | Value |
|:-------|------:|
| Code Smells | {code_smells} |
| TODO/FIXME | {todos} |
| Test Coverage | {coverage} |
| Doc Coverage | {doc_coverage} |

</td>
</tr>
</table>

---
'''


# ══════════════════════════════════════════════════════════════════════════════
# HTML TEMPLATES
# ══════════════════════════════════════════════════════════════════════════════

HTML_REPORT_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flex Audit Report - {project_name}</title>
    <style>
        :root {{
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --secondary: #8b5cf6;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --info: #3b82f6;
            --dark: #1f2937;
            --light: #f9fafb;
            --gray: #6b7280;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
            color: var(--light);
            min-height: 100vh;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        /* Header */
        .header {{
            text-align: center;
            padding: 3rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 2rem;
        }}
        
        .logo {{
            font-family: 'Courier New', monospace;
            font-size: 0.6rem;
            color: var(--primary);
            white-space: pre;
            margin-bottom: 1rem;
            line-height: 1.2;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        
        .header .subtitle {{
            color: var(--gray);
            font-size: 1.1rem;
        }}
        
        .meta-info {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }}
        
        .meta-item {{
            background: rgba(255,255,255,0.05);
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-size: 0.9rem;
        }}
        
        .meta-item span {{
            color: var(--primary);
            font-weight: 600;
        }}
        
        /* Score Card */
        .score-section {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        
        .score-card {{
            background: rgba(255,255,255,0.05);
            border-radius: 1rem;
            padding: 2rem;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }}
        
        .score-value {{
            font-size: 4rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .score-label {{
            font-size: 1.2rem;
            color: var(--gray);
            margin-top: 0.5rem;
        }}
        
        .grade {{
            display: inline-block;
            padding: 0.5rem 1.5rem;
            border-radius: 2rem;
            font-weight: 700;
            font-size: 1.2rem;
            margin-top: 1rem;
        }}
        
        .grade-a {{ background: var(--success); color: white; }}
        .grade-b {{ background: var(--info); color: white; }}
        .grade-c {{ background: var(--warning); color: white; }}
        .grade-d {{ background: var(--danger); color: white; }}
        .grade-f {{ background: #7f1d1d; color: white; }}
        
        /* Stats Grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }}
        
        .stat-item {{
            background: rgba(255,255,255,0.03);
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
        }}
        
        .stat-value {{
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary);
        }}
        
        .stat-label {{
            font-size: 0.85rem;
            color: var(--gray);
            margin-top: 0.25rem;
        }}
        
        /* Severity badges */
        .severity {{
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        
        .severity-critical {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; }}
        .severity-high {{ background: rgba(245, 158, 11, 0.2); color: #fcd34d; }}
        .severity-medium {{ background: rgba(234, 179, 8, 0.2); color: #fde047; }}
        .severity-low {{ background: rgba(59, 130, 246, 0.2); color: #93c5fd; }}
        .severity-info {{ background: rgba(107, 114, 128, 0.2); color: #d1d5db; }}
        
        /* Findings Section */
        .findings-section {{
            background: rgba(255,255,255,0.03);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        
        .findings-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .findings-title {{
            font-size: 1.25rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .findings-count {{
            background: var(--primary);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.85rem;
        }}
        
        .findings-table {{
            width: 100%;
            border-collapse: collapse;
        }}
        
        .findings-table th,
        .findings-table td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}
        
        .findings-table th {{
            color: var(--gray);
            font-weight: 500;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        .findings-table tr:hover {{
            background: rgba(255,255,255,0.02);
        }}
        
        .file-path {{
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            color: var(--primary);
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 3rem 0;
            margin-top: 3rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: var(--gray);
        }}
        
        .footer-logo {{
            font-family: 'Courier New', monospace;
            font-size: 0.5rem;
            color: var(--primary);
            white-space: pre;
            margin-bottom: 1rem;
            line-height: 1.2;
            opacity: 0.7;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            
            .header h1 {{
                font-size: 1.8rem;
            }}
            
            .score-value {{
                font-size: 3rem;
            }}
            
            .logo, .footer-logo {{
                font-size: 0.4rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <pre class="logo">{ascii_logo}</pre>
            <h1>FLEX AUDIT REPORT</h1>
            <p class="subtitle">Enterprise Software Security & Quality Analysis</p>
            <div class="meta-info">
                <div class="meta-item">Project: <span>{project_name}</span></div>
                <div class="meta-item">Date: <span>{date}</span></div>
                <div class="meta-item">Version: <span>{version}</span></div>
            </div>
        </header>
        
        <section class="score-section">
            <div class="score-card">
                <div class="score-value">{score}</div>
                <div class="score-label">Security Score</div>
                <div class="grade {grade_class}">{grade}</div>
            </div>
            <div class="score-card">
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value">{total_files}</div>
                        <div class="stat-label">Files Scanned</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{total_lines}</div>
                        <div class="stat-label">Lines of Code</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{total_issues}</div>
                        <div class="stat-label">Issues Found</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">{critical_count}</div>
                        <div class="stat-label">Critical</div>
                    </div>
                </div>
            </div>
        </section>
        
        {findings_html}
        
        <footer class="footer">
            <pre class="footer-logo">{ascii_logo}</pre>
            <p><strong>© 2025 ARTIFACT virtual</strong> - Enterprise Software Intelligence</p>
            <p style="margin-top: 0.5rem; font-size: 0.85rem;">
                Generated by Flex Audit v2.0 | Standards: OWASP, CWE, SANS Top 25
            </p>
        </footer>
    </div>
</body>
</html>
'''


# ══════════════════════════════════════════════════════════════════════════════
# SEVERITY ICONS AND FORMATTING
# ══════════════════════════════════════════════════════════════════════════════

SEVERITY_ICONS = {
    "CRITICAL": "[!!]",
    "HIGH": "[!]",
    "MEDIUM": "[*]",
    "LOW": "[-]",
    "INFO": "[.]",
}

CATEGORY_ICONS = {
    "Security": "[SEC]",
    "Code Quality": "[CODE]",
    "Architecture": "[ARCH]",
    "Testing": "[TEST]",
    "Documentation": "[DOC]",
    "Dependencies": "[DEP]",
    "Configuration": "[CFG]",
    "Observability": "[OBS]",
    "Performance": "[PERF]",
    "Data Integrity": "[DATA]",
}

GRADE_THRESHOLDS = {
    90: ("A+", "Excellent", "grade-a"),
    80: ("A", "Very Good", "grade-a"),
    70: ("B", "Good", "grade-b"),
    60: ("C", "Acceptable", "grade-c"),
    50: ("D", "Poor", "grade-d"),
    0: ("F", "Critical", "grade-f"),
}


def get_grade(score: int) -> tuple:
    """Get letter grade based on score.

    Iterate the thresholds deterministically (highest to lowest) so the
    grade mapping is robust irrespective of dict insertion order.
    """
    for threshold in sorted(GRADE_THRESHOLDS.keys(), reverse=True):
        if score >= threshold:
            return GRADE_THRESHOLDS[threshold]
    # Fallback
    return GRADE_THRESHOLDS.get(0, ("F", "Critical", "grade-f"))
