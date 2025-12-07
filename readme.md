
```
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
```

<div align="center">

# FLEX AUDIT v2.0

### Software Security & Quality Auditing Framework

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*A fully self-guiding, extensible, modular, static auditor capable of scanning ANY codebase and fabricate industry-grade reporting.*

</div>

---

## Features

### Comprehensive Security Scanning
- **20+ Secret Patterns**: API keys, AWS credentials, GCP service accounts, Azure tokens, JWT secrets, Stripe keys, database passwords, private keys, and more
- **Vulnerability Detection**: SQL injection, XSS, command injection, path traversal, SSRF, insecure deserialization
- **Configuration Auditing**: Docker, Kubernetes, CI/CD pipelines, dependency files

### Multi-Language Support
- **Python**: AST-based analysis with import validation, exec/eval detection
- **JavaScript/TypeScript**: Security anti-patterns, DOM XSS, prototype pollution
- **Go**: Unsafe pointer usage, TLS bypass, command execution
- **Rust**: Unsafe blocks, raw pointer operations
- **Java**: JDBC injection, deserialization, cryptography weaknesses
- **C/C++**: Buffer overflows, format strings, memory corruption
- **Shell**: Command injection, privilege escalation patterns
- **SQL**: Injection vulnerabilities, privilege issues
- **And many more...**

### Report Formats
- **HTML Reports**: Standalone, styled reports with interactive navigation
- **Markdown Reports**: GitHub-compatible with tables
- **JSON Reports**: Machine-readable for CI/CD integration
- **SARIF Reports**: GitHub Security tab compatible

### Enterprise Metrics
- Security Score (0-100) with letter grades (A-F)
- Severity breakdown (Critical/High/Medium/Low/Info)
- Files scanned, lines analyzed, findings categorized
- Historical trend tracking support

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/flex_audit.git
cd flex_audit

# Install dependencies
pip install -r requirements.txt

# Run directly
python -m flex_audit.src /path/to/repository
```

---

## Usage

### Basic Scan
```bash
python -m flex_audit.src /path/to/your/project
```

### With Options
```bash
# Generate HTML reports only
python -m flex_audit.src /path/to/project --format html --output ./reports

# Exclude directories
python -m flex_audit.src /path/to/project --exclude node_modules,venv,dist

# Set minimum severity to report
python -m flex_audit.src /path/to/project --min-severity high

# Quiet mode (no banner)
python -m flex_audit.src /path/to/project --quiet

# CI mode - fail on high+ findings
python -m flex_audit.src /path/to/project --fail-on high
```

### CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output` | Output directory for reports | `audit_output` |
| `-f, --format` | Report format: `all`, `markdown`, `html`, `json` | `all` |
| `-e, --exclude` | Comma-separated patterns to exclude | None |
| `-q, --quiet` | Suppress banner and progress output | False |
| `-v, --verbose` | Show detailed scanning progress | False |
| `--min-severity` | Minimum severity to report | `info` |
| `--fail-on` | Severity that causes non-zero exit | `critical` |
 
## Community

We welcome contributions from the open-source community. See:

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to file issues and submit PRs
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — community expectations
- [`SECURITY.md`](SECURITY.md) — how to report security vulnerabilities
- [`LICENSE`](LICENSE) — licensing information

If you'd like to get involved, open a PR or start by submitting an issue.

---

## Report Examples

### Security Score Card
```
+--------------------------------+
|     SECURITY SCORE: 78/100     |
|     GRADE: C - Needs Work      |
+--------------------------------+

Findings by Severity:
   [!!] Critical: 2
   [!]  High:     5
   [*]  Medium:   12
   [-]  Low:      8
   [.]  Info:     15
```

### HTML Report Features
- Executive summary with risk assessment
- Domain-based analysis (Security, Code Quality, Operations)
- File-by-file findings with syntax highlighting
- Remediation roadmap with prioritized actions
- Full ARTIFACT virtual branding

---

## Architecture

```
flex_audit/
+-- __init__.py           # Package initialization
+-- auditor.py            # Legacy auditor (v1)
+-- requirements.txt      # Dependencies
+-- README.md             # This file
+-- template.md           # Audit framework template
+-- src/
    +-- __init__.py       # Module initialization
    +-- __main__.py       # Main CLI entry point (v2)
    +-- constants.py      # Patterns, thresholds, configurations
    +-- templates.py      # HTML/Markdown report templates
    +-- scanner.py        # Core scanning engine
    +-- report_generator.py  # Report generation system
```

---

## Configuration

### Custom Exclude Patterns
```bash
python -m flex_audit.src ./project --exclude "*.min.js,dist/*,coverage/*"
```

### Environment Variables
```bash
export FLEX_AUDIT_OUTPUT=./reports
export FLEX_AUDIT_FORMAT=html
export FLEX_AUDIT_QUIET=1
```

---

## CI/CD Integration

### GitHub Actions
```yaml
name: Security Audit
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Run Flex Audit
        run: |
          pip install jinja2 colorama rich
          python -m flex_audit.src . --format all --fail-on high
      
      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: audit-report
          path: audit_output/
```

### Exit Codes
| Code | Meaning |
|------|---------|
| 0 | Audit passed |
| 1 | Audit failed (configurable threshold) |
| 2 | Critical issues found |

---

## Detected Pattern Categories

### Secrets & Credentials
- AWS Access Keys & Secret Keys
- Google Cloud Platform Service Accounts
- Azure Client Secrets & Tokens
- GitHub Personal Access Tokens
- Stripe API Keys
- SendGrid API Keys
- Twilio Auth Tokens
- JWT Secrets
- Private Keys (RSA, DSA, EC, PGP)
- Database Connection Strings
- Generic API Keys & Passwords

### Security Vulnerabilities
- SQL Injection
- Command Injection
- XSS (Cross-Site Scripting)
- Path Traversal
- SSRF (Server-Side Request Forgery)
- Insecure Deserialization
- XML External Entity (XXE)
- LDAP Injection
- Template Injection

### Code Quality Issues
- Hardcoded Credentials
- Debug Code in Production
- Missing Input Validation
- Insecure Random Number Generation
- Deprecated Function Usage
- Memory Safety Issues

---

## Feature Checklist

| Feature | v1 | v2 |
|---------|----|----|
| Multi-language scanning | Yes | Yes |
| No hard-coded assumptions | Yes | Yes |
| Plugin architecture | Yes | Yes |
| Deep AST checks | Yes | Yes Enhanced |
| Full secret detection | Yes | Yes 20+ patterns |
| SQL/Mongo/JS eval detection | Yes | Yes |
| Vulnerability scoring | Yes | Yes Enhanced |
| Markdown output | Yes | Yes Branded |
| JSON output | Yes | Yes |
| HTML output | No | Yes NEW |
| SARIF output | No | Yes NEW |
| Executive summaries | No | Yes NEW |
| Remediation roadmap | No | Yes NEW |
| CI/CD integration | No | Yes NEW |

---

## License

MIT License - Copyright (c) 2025 ARTIFACT virtual

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

---

<div align="center">

**Built by ARTIFACT virtual**

*"Security is not a product, but a process."*

</div>

---

## Legacy v1 Information

The original `auditor.py` is still available for backwards compatibility:

```bash
python auditor.py /path/to/repo --out audit
```

### Project Roadmap
- AI-guided code fixer
- Automated refactorer
- Automated documentation generator
- Automated dependency auditor
- Automated pipeline tester
- CVE scanner
- Grafana-style dashboard for audits
- Discord reporter
- Notion auto-syncer

