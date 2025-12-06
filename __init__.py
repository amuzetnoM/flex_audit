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
# Flex Audit - Package Initialization
# Copyright (c) 2025 ARTIFACT virtual
# ══════════════════════════════════════════════════════════════════════════════
"""
Flex Audit - Enterprise Software Auditing Framework

A comprehensive, extensible, modular static auditor for analyzing any codebase
with enterprise-grade reporting and branded output.
"""

__version__ = "2.0.0"
__author__ = "ARTIFACT virtual"
__copyright__ = "Copyright (c) 2025 ARTIFACT virtual"
__license__ = "MIT"

from .src.scanner import Scanner
from .src.report_generator import ReportGenerator
from .src.templates import (
    ARTIFACT_VIRTUAL_BANNER,
    SIRIUS_ALPHA_BANNER,  # backwards compatibility
    FLEX_AUDIT_BANNER,
    get_report_header,
    get_report_footer,
    get_grade
)
from .src.constants import SECRET_PATTERNS, VULNERABILITY_PATTERNS

__all__ = [
    "Scanner",
    "ReportGenerator", 
    "ARTIFACT_VIRTUAL_BANNER",
    "SIRIUS_ALPHA_BANNER",  # backwards compatibility
    "FLEX_AUDIT_BANNER",
    "get_report_header",
    "get_report_footer",
    "get_grade",
    "SECRET_PATTERNS",
    "VULNERABILITY_PATTERNS",
]
