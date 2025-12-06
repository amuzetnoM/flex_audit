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
Core Scanning Engine for Flex Audit

Handles all file scanning, pattern matching, and issue detection.
"""

import os
import fnmatch
import ast
import hashlib
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Set, Tuple
try:
    from tqdm import tqdm
except Exception:
    tqdm = None
from collections import defaultdict
from datetime import datetime

from .constants import (
    SECRET_PATTERNS, VULNERABILITY_PATTERNS, CODE_QUALITY_PATTERNS,
    CONFIG_PATTERNS, TEXT_EXTENSIONS, BINARY_EXTENSIONS, IGNORE_DIRS,
    Severity, Category
)


@dataclass
class Finding:
    """Represents a single audit finding."""
    file_path: str
    line_number: int
    issue_type: str
    severity: Severity
    category: Category
    description: str
    matched_text: str = ""
    suggestion: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        # Redact matched text when the finding is a security issue to avoid leaking secrets
        matched = self.matched_text or ""
        if self.category == Category.SECURITY and matched:
            # Show only a small hint - no secrets
            matched = "***REDACTED***"

        return {
            "file": self.file_path,
            "line": self.line_number,
            "type": self.issue_type,
            "severity": self.severity.name,
            "category": self.category.value,
            "description": self.description,
            "matched": matched[:100] if matched else "",
            "suggestion": self.suggestion,
        }


@dataclass
class FileAnalysis:
    """Analysis results for a single file."""
    path: str
    relative_path: str
    language: str
    lines: int
    size: int
    findings: List[Finding] = field(default_factory=list)
    hash: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.relative_path,
            "language": self.language,
            "lines": self.lines,
            "size": self.size,
            "findings_count": len(self.findings),
            "hash": self.hash,
        }


@dataclass
class AuditResult:
    """Complete audit results for a repository."""
    repo_path: str
    timestamp: str
    files_analyzed: List[FileAnalysis] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def total_findings(self) -> int:
        return len(self.findings)
    
    @property
    def critical_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.CRITICAL)
    
    @property
    def high_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.HIGH)
    
    @property
    def medium_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.MEDIUM)
    
    @property
    def low_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.LOW)
    
    @property
    def info_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.INFO)
    
    def calculate_score(self) -> int:
        """Calculate overall security score (0-100)."""
        score = 100
        score -= self.critical_count * 15
        score -= self.high_count * 8
        score -= self.medium_count * 3
        score -= self.low_count * 1
        return max(0, min(100, score))
    
    def get_findings_by_category(self) -> Dict[Category, List[Finding]]:
        """Group findings by category."""
        by_category = defaultdict(list)
        for finding in self.findings:
            by_category[finding.category].append(finding)
        return dict(by_category)
    
    def get_findings_by_severity(self) -> Dict[Severity, List[Finding]]:
        """Group findings by severity."""
        by_severity = defaultdict(list)
        for finding in self.findings:
            by_severity[finding.severity].append(finding)
        return dict(by_severity)


class Scanner:
    """
    Core scanning engine for Flex Audit.
    
    Scans repositories for security issues, code quality problems,
    and configuration misconfigurations.
    """
    
    def __init__(self, repo_path: str, exclude_patterns: List[str] = None, show_progress: bool = False):
        self.repo_path = os.path.abspath(repo_path)
        self.exclude_patterns = exclude_patterns or []
        self.show_progress = show_progress and (tqdm is not None)
        self.result = AuditResult(
            repo_path=self.repo_path,
            timestamp=datetime.utcnow().isoformat()
        )
        
        # Statistics
        self._total_lines = 0
        self._total_files = 0
        self._languages: Dict[str, int] = defaultdict(int)
    
    def scan(self) -> AuditResult:
        """Execute full repository scan."""
        print(f"\n🔍 Scanning repository: {self.repo_path}")
        print("=" * 60)
        
        # Build a filtered list of files first if progress is requested
        files_to_scan = []
        if self.show_progress:
                for root, dirs, files in os.walk(self.repo_path):
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
                for filename in files:
                    rel_path = os.path.relpath(os.path.join(root, filename), self.repo_path)
                    if self._should_exclude(rel_path):
                        continue
                    files_to_scan.append((root, filename))
            file_iter = files_to_scan
        else:
            file_iter = []
            for root, dirs, files in os.walk(self.repo_path):
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
                for filename in files:
                    rel_path = os.path.relpath(os.path.join(root, filename), self.repo_path)
                    if self._should_exclude(rel_path):
                        continue
                    file_iter.append((root, filename))

        # Setup progress bars if requested
        if self.show_progress and file_iter:
            total_files = len(file_iter)
            files_bar = tqdm(total=total_files, desc="Files", position=0, dynamic_ncols=True, leave=True)
            lines_bar = tqdm(total=None, desc="Lines", position=1, dynamic_ncols=True, leave=True)
            findings_bar = tqdm(total=None, desc="Findings", position=2, dynamic_ncols=True, leave=True)
        else:
            files_bar = lines_bar = findings_bar = None

        for root, filename in file_iter:
                file_path = os.path.join(root, filename)
                rel_path = os.path.relpath(file_path, self.repo_path)
                
                # Skip excluded patterns
                if self._should_exclude(rel_path):
                    continue
                
                # Analyze file
                analysis = self._analyze_file(file_path, rel_path)
                if analysis:
                    self.result.files_analyzed.append(analysis)
                    self.result.findings.extend(analysis.findings)
                    # Update progress bars
                        if files_bar is not None:
                        files_bar.update(1)
                        if lines_bar is not None:
                        lines_bar.update(analysis.lines)
                        if findings_bar is not None and analysis.findings:
                        findings_bar.update(len(analysis.findings))
        # finalize progress bars
        if files_bar is not None:
            files_bar.close()
        if lines_bar is not None:
            lines_bar.close()
        if findings_bar is not None:
            findings_bar.close()
        
        # Compile statistics
        self.result.stats = {
            "total_files": self._total_files,
            "total_lines": self._total_lines,
            "languages": dict(self._languages),
            "findings_by_severity": {
                "critical": self.result.critical_count,
                "high": self.result.high_count,
                "medium": self.result.medium_count,
                "low": self.result.low_count,
                "info": self.result.info_count,
            },
            "score": self.result.calculate_score(),
        }
        
        print(f"\n✅ Scan complete: {self._total_files} files, {self.result.total_findings} findings")
        return self.result
    
    def _should_exclude(self, path: str) -> bool:
        """Check if path should be excluded."""
        for pattern in self.exclude_patterns:
            try:
                if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
                    return True
            except Exception:
                if pattern in path:
                    return True
        return False
    
    def _analyze_file(self, file_path: str, rel_path: str) -> Optional[FileAnalysis]:
        """Analyze a single file."""
        ext = Path(file_path).suffix.lower()
        
        # Skip binary files
        if ext in BINARY_EXTENSIONS:
            return None
        
        # Skip non-text files
        if ext not in TEXT_EXTENSIONS and not ext == '':
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            return FileAnalysis(
                path=file_path,
                relative_path=rel_path,
                language="unknown",
                lines=0,
                size=0,
                findings=[Finding(
                    file_path=rel_path,
                    line_number=0,
                    issue_type="FILE_READ_ERROR",
                    severity=Severity.INFO,
                    category=Category.CODE_QUALITY,
                    description=f"Could not read file: {str(e)}"
                )]
            )
        
        # Get file stats
        lines = content.count('\n') + 1
        size = len(content)
        language = self._detect_language(ext, file_path)
        file_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        
        self._total_files += 1
        self._total_lines += lines
        self._languages[language] += 1
        
        # Create analysis object
        analysis = FileAnalysis(
            path=file_path,
            relative_path=rel_path,
            language=language,
            lines=lines,
            size=size,
            hash=file_hash
        )
        
        # Run pattern scans
        analysis.findings.extend(self._scan_secrets(content, rel_path))
        analysis.findings.extend(self._scan_vulnerabilities(content, rel_path))
        analysis.findings.extend(self._scan_code_quality(content, rel_path))
        analysis.findings.extend(self._scan_config(content, rel_path, ext))
        
        # Python-specific AST analysis
        if ext == '.py':
            analysis.findings.extend(self._scan_python_ast(content, rel_path))
        
        return analysis
    
    def _detect_language(self, ext: str, filename: str) -> str:
        """Detect programming language from extension."""
        lang_map = {
            '.py': 'Python', '.pyi': 'Python',
            '.js': 'JavaScript', '.jsx': 'JavaScript',
            '.ts': 'TypeScript', '.tsx': 'TypeScript',
            '.java': 'Java', '.kt': 'Kotlin',
            '.go': 'Go', '.rs': 'Rust',
            '.c': 'C', '.cpp': 'C++', '.h': 'C/C++',
            '.cs': 'C#', '.rb': 'Ruby',
            '.php': 'PHP', '.swift': 'Swift',
            '.sh': 'Shell', '.bash': 'Shell',
            '.ps1': 'PowerShell',
            '.sql': 'SQL',
            '.html': 'HTML', '.css': 'CSS',
            '.json': 'JSON', '.yaml': 'YAML', '.yml': 'YAML',
            '.xml': 'XML', '.toml': 'TOML',
            '.md': 'Markdown', '.rst': 'reStructuredText',
        }
        
        base = os.path.basename(filename).lower()
        if base in ('dockerfile', 'containerfile'):
            return 'Dockerfile'
        if base == 'makefile':
            return 'Makefile'
        
        return lang_map.get(ext, 'Other')
    
    def _scan_secrets(self, content: str, file_path: str) -> List[Finding]:
        """Scan for exposed secrets."""
        findings = []
        lines = content.split('\n')
        
        for pattern, name, severity in SECRET_PATTERNS:
            for match in pattern.finditer(content):
                line_num = content[:match.start()].count('\n') + 1
                findings.append(Finding(
                    file_path=file_path,
                    line_number=line_num,
                    issue_type=name,
                    severity=severity,
                    category=Category.SECURITY,
                    description=f"Potential secret detected: {name}",
                    matched_text=match.group()[:50] + "..." if len(match.group()) > 50 else match.group(),
                    suggestion="Remove secret and use environment variables or secret management"
                ))
        
        return findings
    
    def _scan_vulnerabilities(self, content: str, file_path: str) -> List[Finding]:
        """Scan for security vulnerabilities."""
        findings = []
        
        for pattern, name, severity, category, description in VULNERABILITY_PATTERNS:
            for match in pattern.finditer(content):
                line_num = content[:match.start()].count('\n') + 1
                findings.append(Finding(
                    file_path=file_path,
                    line_number=line_num,
                    issue_type=name,
                    severity=severity,
                    category=category,
                    description=description,
                    matched_text=match.group()[:80],
                ))
        
        return findings
    
    def _scan_code_quality(self, content: str, file_path: str) -> List[Finding]:
        """Scan for code quality issues."""
        findings = []
        
        for pattern, name, severity, category, description in CODE_QUALITY_PATTERNS:
            for match in pattern.finditer(content):
                line_num = content[:match.start()].count('\n') + 1
                findings.append(Finding(
                    file_path=file_path,
                    line_number=line_num,
                    issue_type=name,
                    severity=severity,
                    category=category,
                    description=description,
                    matched_text=match.group()[:80],
                ))
        
        return findings
    
    def _scan_config(self, content: str, file_path: str, ext: str) -> List[Finding]:
        """Scan for configuration issues."""
        findings = []
        
        # Only scan relevant config files
        config_exts = {'.dockerfile', '.yaml', '.yml', '.json', '.toml', '.ini', '.env'}
        config_names = {'dockerfile', 'docker-compose', 'requirements', 'package.json', 
                        'pyproject.toml', '.env'}
        
        base_name = os.path.basename(file_path).lower()
        if ext not in config_exts and not any(n in base_name for n in config_names):
            return findings
        
        for pattern, name, severity, category, description in CONFIG_PATTERNS:
            for match in pattern.finditer(content):
                line_num = content[:match.start()].count('\n') + 1
                findings.append(Finding(
                    file_path=file_path,
                    line_number=line_num,
                    issue_type=name,
                    severity=severity,
                    category=category,
                    description=description,
                    matched_text=match.group()[:80],
                ))
        
        return findings
    
    def _scan_python_ast(self, content: str, file_path: str) -> List[Finding]:
        """Perform Python AST analysis for deeper checks."""
        findings = []
        
        try:
            tree = ast.parse(content, filename=file_path)
        except SyntaxError as e:
            findings.append(Finding(
                file_path=file_path,
                line_number=e.lineno or 0,
                issue_type="PYTHON_SYNTAX_ERROR",
                severity=Severity.HIGH,
                category=Category.CODE_QUALITY,
                description=f"Python syntax error: {e.msg}"
            ))
            return findings
        
        # Check for mutable default arguments
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for default in node.args.defaults + node.args.kw_defaults:
                    if default and isinstance(default, (ast.List, ast.Dict, ast.Set)):
                        findings.append(Finding(
                            file_path=file_path,
                            line_number=node.lineno,
                            issue_type="MUTABLE_DEFAULT_ARG",
                            severity=Severity.MEDIUM,
                            category=Category.CODE_QUALITY,
                            description=f"Mutable default argument in function '{node.name}'"
                        ))
            
            # Check for bare except
            if isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    findings.append(Finding(
                        file_path=file_path,
                        line_number=node.lineno,
                        issue_type="BARE_EXCEPT_AST",
                        severity=Severity.MEDIUM,
                        category=Category.CODE_QUALITY,
                        description="Bare except catches all exceptions including SystemExit"
                    ))
            
            # Check for assert statements (removed in optimized mode)
            if isinstance(node, ast.Assert):
                findings.append(Finding(
                    file_path=file_path,
                    line_number=node.lineno,
                    issue_type="ASSERT_USAGE",
                    severity=Severity.LOW,
                    category=Category.CODE_QUALITY,
                    description="Assert statements are removed when Python runs with -O flag"
                ))
        
        return findings
