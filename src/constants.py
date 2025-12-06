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
Core Constants and Patterns for Flex Audit

Defines all detection patterns, severity levels, and scoring weights.
"""

import re
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Pattern

# ══════════════════════════════════════════════════════════════════════════════
# SEVERITY AND SCORING
# ══════════════════════════════════════════════════════════════════════════════

class Severity(Enum):
    """Issue severity levels following industry standards."""
    CRITICAL = auto()  # Must fix immediately - security/data breach risk
    HIGH = auto()      # Major risk - fix within 24h
    MEDIUM = auto()    # Moderate risk - fix within sprint
    LOW = auto()       # Minor inefficiency - backlog
    INFO = auto()      # Informational only


class Category(Enum):
    """Audit finding categories."""
    SECURITY = "Security"
    CODE_QUALITY = "Code Quality"
    ARCHITECTURE = "Architecture"
    TESTING = "Testing"
    DOCUMENTATION = "Documentation"
    DEPENDENCIES = "Dependencies"
    CONFIGURATION = "Configuration"
    OBSERVABILITY = "Observability"
    PERFORMANCE = "Performance"
    DATA_INTEGRITY = "Data Integrity"


@dataclass
class ScoringWeight:
    """Weighted scoring for each audit domain."""
    architecture: float = 0.15
    code_quality: float = 0.10
    documentation: float = 0.08
    testing: float = 0.12
    security: float = 0.18
    data_integrity: float = 0.10
    dependencies: float = 0.08
    observability: float = 0.07
    performance: float = 0.06
    devops: float = 0.06


# ══════════════════════════════════════════════════════════════════════════════
# SECRET PATTERNS - Comprehensive Detection
# ══════════════════════════════════════════════════════════════════════════════

SECRET_PATTERNS: List[tuple] = [
    # Generic secrets
    (re.compile(r"(?i)(api[_-]?key|apikey)[\"'\s:=]{1,10}['\"]?[A-Za-z0-9_\-]{16,}['\"]?", re.MULTILINE), 
     "API_KEY", Severity.CRITICAL),
    (re.compile(r"(?i)(secret[_-]?key|secretkey)[\"'\s:=]{1,10}['\"]?[A-Za-z0-9_\-]{16,}['\"]?", re.MULTILINE), 
     "SECRET_KEY", Severity.CRITICAL),
    (re.compile(r"(?i)(access[_-]?token|accesstoken)[\"'\s:=]{1,10}['\"]?[A-Za-z0-9_\-]{16,}['\"]?", re.MULTILINE), 
     "ACCESS_TOKEN", Severity.CRITICAL),
    (re.compile(r"(?i)password\s*[:=]\s*['\"][^'\"]{4,}['\"]", re.MULTILINE), 
     "HARDCODED_PASSWORD", Severity.CRITICAL),
    
    # Private keys
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----", re.MULTILINE), 
     "PRIVATE_KEY", Severity.CRITICAL),
    (re.compile(r"-----BEGIN RSA PRIVATE KEY-----", re.MULTILINE), 
     "RSA_PRIVATE_KEY", Severity.CRITICAL),
    (re.compile(r"-----BEGIN EC PRIVATE KEY-----", re.MULTILINE), 
     "EC_PRIVATE_KEY", Severity.CRITICAL),
    (re.compile(r"-----BEGIN PGP PRIVATE KEY BLOCK-----", re.MULTILINE), 
     "PGP_PRIVATE_KEY", Severity.CRITICAL),
    
    # Cloud provider secrets
    (re.compile(r"(?i)aws[_-]?secret[_-]?access[_-]?key['\"\s:=]+[A-Za-z0-9/+=]{40}", re.MULTILINE), 
     "AWS_SECRET_KEY", Severity.CRITICAL),
    (re.compile(r"AKIA[0-9A-Z]{16}", re.MULTILINE), 
     "AWS_ACCESS_KEY_ID", Severity.CRITICAL),
    (re.compile(r"AIza[0-9A-Za-z\-_]{35}", re.MULTILINE), 
     "GOOGLE_API_KEY", Severity.CRITICAL),
    (re.compile(r"(?i)azure[_-]?(storage|account)[_-]?key['\"\s:=]+[A-Za-z0-9/+=]{40,}", re.MULTILINE), 
     "AZURE_KEY", Severity.CRITICAL),
    
    # Payment/Financial
    (re.compile(r"sk_live_[0-9a-zA-Z]{24,}", re.MULTILINE), 
     "STRIPE_LIVE_KEY", Severity.CRITICAL),
    (re.compile(r"sk_test_[0-9a-zA-Z]{24,}", re.MULTILINE), 
     "STRIPE_TEST_KEY", Severity.HIGH),
    (re.compile(r"sq0atp-[0-9A-Za-z\-_]{22}", re.MULTILINE), 
     "SQUARE_ACCESS_TOKEN", Severity.CRITICAL),
    (re.compile(r"sq0csp-[0-9A-Za-z\-_]{43}", re.MULTILINE), 
     "SQUARE_OAUTH_SECRET", Severity.CRITICAL),
    
    # Communication platforms
    (re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,48}", re.MULTILINE), 
     "SLACK_TOKEN", Severity.CRITICAL),
    (re.compile(r"https://hooks\.slack\.com/services/T[0-9A-Z]+/B[0-9A-Z]+/[a-zA-Z0-9]+", re.MULTILINE), 
     "SLACK_WEBHOOK", Severity.HIGH),
    (re.compile(r"[0-9]+:AA[0-9A-Za-z_-]{33}", re.MULTILINE), 
     "TELEGRAM_BOT_TOKEN", Severity.CRITICAL),
    (re.compile(r"(?i)discord[._-]?(token|webhook)['\"\s:=]+[A-Za-z0-9._-]{50,}", re.MULTILINE), 
     "DISCORD_TOKEN", Severity.CRITICAL),
    
    # Database connection strings
    (re.compile(r"(?i)(mongodb|postgres|mysql|redis|mssql)://[^\s'\"]+:[^\s'\"]+@", re.MULTILINE), 
     "DATABASE_CONNECTION_STRING", Severity.CRITICAL),
    
    # JWT tokens
    (re.compile(r"eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*", re.MULTILINE), 
     "JWT_TOKEN", Severity.HIGH),
    
    # GitHub tokens
    (re.compile(r"ghp_[0-9a-zA-Z]{36}", re.MULTILINE), 
     "GITHUB_PAT", Severity.CRITICAL),
    (re.compile(r"gho_[0-9a-zA-Z]{36}", re.MULTILINE), 
     "GITHUB_OAUTH", Severity.CRITICAL),
    (re.compile(r"ghr_[0-9a-zA-Z]{36}", re.MULTILINE), 
     "GITHUB_REFRESH", Severity.CRITICAL),
]


# ══════════════════════════════════════════════════════════════════════════════
# VULNERABILITY PATTERNS - Code Security Issues
# ══════════════════════════════════════════════════════════════════════════════

VULNERABILITY_PATTERNS: List[tuple] = [
    # Code execution
    (re.compile(r"\beval\s*\(", re.MULTILINE), 
     "EVAL_USAGE", Severity.CRITICAL, Category.SECURITY,
     "Use of eval() can lead to arbitrary code execution"),
    (re.compile(r"\bexec\s*\(", re.MULTILINE), 
     "EXEC_USAGE", Severity.CRITICAL, Category.SECURITY,
     "Use of exec() can lead to arbitrary code execution"),
    (re.compile(r"subprocess\.(call|run|Popen)\s*\([^)]*shell\s*=\s*True", re.MULTILINE), 
     "SHELL_INJECTION", Severity.CRITICAL, Category.SECURITY,
     "Shell=True in subprocess is vulnerable to command injection"),
    (re.compile(r"os\.system\s*\(", re.MULTILINE), 
     "OS_SYSTEM", Severity.HIGH, Category.SECURITY,
     "os.system() is vulnerable to command injection, use subprocess"),
    
    # Unsafe deserialization
    (re.compile(r"pickle\.(load|loads)\s*\(", re.MULTILINE), 
     "UNSAFE_PICKLE", Severity.CRITICAL, Category.SECURITY,
     "Unpickling untrusted data can execute arbitrary code"),
    (re.compile(r"yaml\.load\s*\([^)]*\)", re.MULTILINE), 
     "UNSAFE_YAML", Severity.HIGH, Category.SECURITY,
     "yaml.load() without Loader is unsafe, use safe_load()"),
    (re.compile(r"marshal\.loads?\s*\(", re.MULTILINE), 
     "UNSAFE_MARSHAL", Severity.HIGH, Category.SECURITY,
     "marshal module is not secure for untrusted data"),
    
    # SQL injection
    (re.compile(r"execute\s*\(\s*['\"].*%[sd].*['\"].*%", re.MULTILINE), 
     "SQL_INJECTION_FORMAT", Severity.CRITICAL, Category.SECURITY,
     "String formatting in SQL queries leads to injection"),
    (re.compile(r"execute\s*\(\s*f['\"]", re.MULTILINE), 
     "SQL_INJECTION_FSTRING", Severity.CRITICAL, Category.SECURITY,
     "F-strings in SQL queries lead to injection"),
    (re.compile(r"\{\s*\$where\s*:", re.MULTILINE), 
     "MONGODB_INJECTION", Severity.CRITICAL, Category.SECURITY,
     "$where in MongoDB is vulnerable to NoSQL injection"),
    
    # Path traversal
    (re.compile(r"open\s*\([^)]*\+[^)]*\)", re.MULTILINE), 
     "PATH_TRAVERSAL_RISK", Severity.MEDIUM, Category.SECURITY,
     "String concatenation in file paths may allow traversal"),
    
    # Cryptography issues
    (re.compile(r"(?i)md5\s*\(|hashlib\.md5", re.MULTILINE), 
     "WEAK_HASH_MD5", Severity.MEDIUM, Category.SECURITY,
     "MD5 is cryptographically weak, use SHA-256+"),
    (re.compile(r"(?i)sha1\s*\(|hashlib\.sha1", re.MULTILINE), 
     "WEAK_HASH_SHA1", Severity.MEDIUM, Category.SECURITY,
     "SHA1 is cryptographically weak, use SHA-256+"),
    (re.compile(r"(?i)random\.(random|randint|choice)", re.MULTILINE), 
     "INSECURE_RANDOM", Severity.MEDIUM, Category.SECURITY,
     "random module is not cryptographically secure, use secrets"),
    
    # XSS risks
    (re.compile(r"innerHTML\s*=", re.MULTILINE), 
     "XSS_INNERHTML", Severity.HIGH, Category.SECURITY,
     "innerHTML assignment may lead to XSS"),
    (re.compile(r"document\.write\s*\(", re.MULTILINE), 
     "XSS_DOCUMENT_WRITE", Severity.HIGH, Category.SECURITY,
     "document.write() may lead to XSS"),
    
    # SSRF risks
    (re.compile(r"requests\.(get|post|put|delete)\s*\([^)]*\+", re.MULTILINE), 
     "SSRF_RISK", Severity.MEDIUM, Category.SECURITY,
     "Dynamic URL construction may lead to SSRF"),
]


# ══════════════════════════════════════════════════════════════════════════════
# CODE QUALITY PATTERNS
# ══════════════════════════════════════════════════════════════════════════════

CODE_QUALITY_PATTERNS: List[tuple] = [
    # Debug/TODO markers
    (re.compile(r"(?i)\b(TODO|FIXME|HACK|XXX|BUG)\b", re.MULTILINE), 
     "TODO_MARKER", Severity.INFO, Category.CODE_QUALITY,
     "Development marker found - review and address"),
    (re.compile(r"(?i)\bdebug\s*=\s*True", re.MULTILINE), 
     "DEBUG_ENABLED", Severity.MEDIUM, Category.CONFIGURATION,
     "Debug mode enabled - disable in production"),
    (re.compile(r"print\s*\([^)]*\)", re.MULTILINE), 
     "PRINT_STATEMENT", Severity.LOW, Category.CODE_QUALITY,
     "Print statement found - use logging instead"),
    (re.compile(r"console\.(log|debug|info|warn|error)\s*\(", re.MULTILINE), 
     "CONSOLE_LOG", Severity.LOW, Category.CODE_QUALITY,
     "Console statement found - remove for production"),
    
    # Code smells
    (re.compile(r"except\s*:\s*$", re.MULTILINE), 
     "BARE_EXCEPT", Severity.MEDIUM, Category.CODE_QUALITY,
     "Bare except catches all exceptions including KeyboardInterrupt"),
    (re.compile(r"except\s+Exception\s*:\s*pass", re.MULTILINE), 
     "SILENT_EXCEPTION", Severity.HIGH, Category.CODE_QUALITY,
     "Silently swallowing exceptions hides bugs"),
    (re.compile(r"from\s+\S+\s+import\s+\*", re.MULTILINE), 
     "WILDCARD_IMPORT", Severity.LOW, Category.CODE_QUALITY,
     "Wildcard imports pollute namespace"),
    (re.compile(r"global\s+\w+", re.MULTILINE), 
     "GLOBAL_VARIABLE", Severity.LOW, Category.CODE_QUALITY,
     "Global variables reduce code maintainability"),
]


# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION & MISCONFIGURATION PATTERNS
# ══════════════════════════════════════════════════════════════════════════════

CONFIG_PATTERNS: List[tuple] = [
    # Docker
    (re.compile(r"FROM\s+\S+:latest", re.MULTILINE), 
     "DOCKER_LATEST_TAG", Severity.MEDIUM, Category.CONFIGURATION,
     "Using :latest tag makes builds non-reproducible"),
    (re.compile(r"USER\s+root", re.MULTILINE), 
     "DOCKER_ROOT_USER", Severity.HIGH, Category.SECURITY,
     "Container running as root is a security risk"),
    
    # Dependencies
    (re.compile(r"^\s*[a-zA-Z0-9_-]+\s*$", re.MULTILINE), 
     "UNPINNED_DEPENDENCY", Severity.MEDIUM, Category.DEPENDENCIES,
     "Unpinned dependency - pin to specific version"),
    
    # CORS/Security headers
    (re.compile(r"(?i)access-control-allow-origin['\"\s:=]+\*", re.MULTILINE), 
     "CORS_WILDCARD", Severity.HIGH, Category.SECURITY,
     "Wildcard CORS allows any origin"),
    (re.compile(r"(?i)verify\s*=\s*False", re.MULTILINE), 
     "SSL_VERIFY_DISABLED", Severity.HIGH, Category.SECURITY,
     "SSL verification disabled - vulnerable to MITM"),
]


# ══════════════════════════════════════════════════════════════════════════════
# FILE TYPE DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

TEXT_EXTENSIONS = frozenset({
    # Python
    ".py", ".pyi", ".pyx", ".pxd",
    # JavaScript/TypeScript
    ".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs",
    # Web
    ".html", ".htm", ".css", ".scss", ".sass", ".less",
    # Data formats
    ".json", ".yaml", ".yml", ".toml", ".xml", ".csv",
    # Documentation
    ".md", ".rst", ".txt", ".adoc",
    # Shell
    ".sh", ".bash", ".zsh", ".fish", ".ps1", ".psm1", ".bat", ".cmd",
    # Config
    ".ini", ".cfg", ".conf", ".env", ".properties",
    # Other languages
    ".java", ".kt", ".scala", ".groovy",
    ".go", ".rs", ".rb", ".php",
    ".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hxx",
    ".cs", ".fs", ".vb",
    ".swift", ".m", ".mm",
    ".r", ".R", ".jl",
    ".sql", ".graphql", ".gql",
    # Docker/K8s
    ".dockerfile", ".containerfile",
    # Misc
    ".tf", ".hcl", ".proto", ".thrift",
})

BINARY_EXTENSIONS = frozenset({
    ".pyc", ".pyo", ".so", ".dll", ".exe", ".bin",
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
    ".woff", ".woff2", ".ttf", ".eot",
    ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx",
    ".mp3", ".mp4", ".wav", ".avi", ".mov",
    ".sqlite", ".db", ".lock",
})

IGNORE_DIRS = frozenset({
    ".git", ".svn", ".hg",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "node_modules", "bower_components",
    "venv", ".venv", "env", ".env", "venv312", "site-packages",
    "dist", "build", "target", "out",
    ".idea", ".vscode",
    "coverage", "htmlcov", ".coverage",
    ".tox", ".nox",
    "eggs", "*.egg-info",
})
