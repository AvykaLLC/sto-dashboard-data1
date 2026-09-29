## test-security.py - INTENTIONAL VULNERABILITIES FOR TESTING

import os

# CRITICAL: Hardcoded API key
API_KEY = "sk-live-abc123xyz789secret"
DATABASE_PASSWORD = "admin123!"

# HIGH: SQL injection vulnerability
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id  # No parameterization!
    return execute_query(query)

# MEDIUM: Hardcoded config
DEBUG_MODE = True
ADMIN_EMAIL = "admin@company.com"
