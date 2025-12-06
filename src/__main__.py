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
Flex Audit - Comprehensive Software Auditing Framework

A fully self-guiding, extensible, modular static auditor capable of scanning
ANY codebase with enterprise-grade reporting and analysis.

Usage:
    python -m flex_audit /path/to/repo --output ./audit_output
    python -m flex_audit /path/to/repo --format all
    python -m flex_audit /path/to/repo --severity high

Features:
    - Multi-language support (Python, JS, TS, Go, Rust, Java, C/C++, etc.)
    - Deep secret detection (API keys, passwords, tokens, private keys)
    - Vulnerability scanning (SQL injection, XSS, command injection, etc.)
    - Code quality analysis (complexity, dead code, anti-patterns)
    - Configuration auditing (Docker, K8s, CI/CD, dependencies)
    - Beautiful branded reports (Markdown, HTML, JSON)
    - Prioritized remediation recommendations
    - Auto-generated fix suggestions
"""

import sys
import os
import argparse
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scanner import Scanner
from src.report_generator import ReportGenerator
from src.templates import FLEX_AUDIT_BANNER, ARTIFACT_VIRTUAL_BANNER, get_grade


def print_banner():
    """Print the Flex Audit banner."""
    print("\033[95m" + ARTIFACT_VIRTUAL_BANNER + "\033[0m")
    print("\033[96m" + "=" * 80 + "\033[0m")
    print("\033[96m  FLEX AUDIT v2.0 - Enterprise Software Security & Quality Analysis\033[0m")
    print("\033[96m  Copyright (c) 2025 ARTIFACT virtual\033[0m")
    print("\033[96m" + "=" * 80 + "\033[0m\n")


def print_summary(result):
    """Print audit summary to console."""
    score = result.calculate_score()
    grade, grade_desc, _ = get_grade(score)
    
    # Color coding
    if score >= 80:
        color = "\033[92m"  # Green
    elif score >= 60:
        color = "\033[93m"  # Yellow
    elif score >= 40:
        color = "\033[91m"  # Red
    else:
        color = "\033[95m"  # Magenta (critical)
    
    print("\n" + "=" * 60)
    print("\033[1mAUDIT SUMMARY\033[0m")
    print("=" * 60)
    
    print(f"\n  Files Scanned:    {result.stats.get('total_files', 0):,}")
    print(f"  Lines of Code:    {result.stats.get('total_lines', 0):,}")
    print(f"  Total Findings:   {result.total_findings}")
    
    print(f"\n  {color}┌────────────────────────────────┐\033[0m")
    print(f"  {color}│     SECURITY SCORE: {score:3d}/100     │\033[0m")
    print(f"  {color}│     GRADE: {grade} - {grade_desc:12s}   │\033[0m")
    print(f"  {color}└────────────────────────────────┘\033[0m")
    
    print("\n  Findings by Severity:")
    print(f"     [!!] Critical: {result.critical_count}")
    print(f"     [!]  High:     {result.high_count}")
    print(f"     [*]  Medium:   {result.medium_count}")
    print(f"     [-]  Low:      {result.low_count}")
    print(f"     [.]  Info:     {result.info_count}")
    
    print("\n" + "=" * 60)


def main():
    """Main entry point for Flex Audit CLI."""
    parser = argparse.ArgumentParser(
        description="Flex Audit - Enterprise Software Auditing Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m flex_audit ./my_project
  python -m flex_audit ./my_project --output ./reports
  python -m flex_audit ./my_project --format html
  python -m flex_audit ./my_project --exclude node_modules,venv

Exit Codes:
  0 - Audit passed (score >= 60)
  1 - Audit failed (score < 60)
  2 - Critical issues found (score < 40)
        """
    )
    
    parser.add_argument(
        "repo",
        help="Path to the repository to audit"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="audit_output",
        help="Output directory for reports (default: audit_output)"
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["all", "markdown", "html", "json", "sarif"],
        default="all",
        help="Report format to generate (default: all)"
    )
    
    parser.add_argument(
        "-e", "--exclude",
        help="Comma-separated patterns to exclude"
    )
    
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress banner and progress output"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed scanning progress"
    )

    parser.add_argument(
        "--skip-third-party",
        action="store_true",
        help="Automatically exclude common third-party directories (venv, site-packages, node_modules, build, dist)"
    )
    
    parser.add_argument(
        "--min-severity",
        choices=["critical", "high", "medium", "low", "info"],
        default="info",
        help="Minimum severity to report (default: info)"
    )
    
    parser.add_argument(
        "--fail-on",
        choices=["critical", "high", "medium", "low", "none"],
        default="critical",
        help="Severity level that causes non-zero exit (default: critical)"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Flex Audit v2.0 (ARTIFACT virtual)"
    )
    
    args = parser.parse_args()
    
    # Validate repository path
    if not os.path.isdir(args.repo):
        print(f"\033[91mError: Repository path does not exist: {args.repo}\033[0m")
        sys.exit(1)
    
    # Print banner
    if not args.quiet:
        print_banner()
    
    # Parse exclude patterns
    exclude_patterns = []
    if args.exclude:
        exclude_patterns = [p.strip() for p in args.exclude.split(",")]

    # Optional skip flag: add common third-party directories to excludes
    if args.skip_third_party:
        exclude_patterns.extend(["venv*", "site-packages", "node_modules", "dist", "build"]) 
    
    # Run scan
    scanner = Scanner(args.repo, exclude_patterns)
    result = scanner.scan()
    
    # Generate reports
    generator = ReportGenerator(result, args.output)
    
    if args.format == "all":
        paths = generator.generate_all()
    elif args.format == "markdown":
        paths = {"markdown": generator.generate_markdown()}
    elif args.format == "html":
        paths = {"html": generator.generate_html()}
    elif args.format == "json":
        paths = {"json": generator.generate_json()}
    elif args.format == "sarif":
        paths = {"sarif": generator.generate_sarif()}
    
    # Print summary
    if not args.quiet:
        print_summary(result)
        
        print("\nReports Generated:")
        for fmt, path in paths.items():
            print(f"   * {fmt.upper()}: {path}")
        
        print(f"\nOutput Directory: {args.output}")
        print("\n" + "=" * 60)
        print("\033[96m  Thank you for using Flex Audit by ARTIFACT virtual\033[0m")
        print("=" * 60 + "\n")
    
    # Determine exit code
    score = result.calculate_score()
    fail_thresholds = {
        "critical": result.critical_count > 0,
        "high": result.high_count > 0 or result.critical_count > 0,
        "medium": result.medium_count > 0 or result.high_count > 0 or result.critical_count > 0,
        "low": score < 60,
        "none": False
    }
    
    if fail_thresholds.get(args.fail_on, False):
        sys.exit(2 if result.critical_count > 0 else 1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
