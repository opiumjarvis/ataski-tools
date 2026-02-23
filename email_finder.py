#!/usr/bin/env python3
"""
Email Finder - Find emails from domains
"""

import re
import json

def find_emails(domain):
    """Generate likely email patterns for a domain"""
    
    patterns = [
        f"info@{domain}",
        f"contact@{domain}",
        f"hello@{domain}",
        f"support@{domain}",
        f"sales@{domain}",
        f"admin@{domain}",
        f"marketing@{domain}",
    ]
    
    return patterns

def validate_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def guess_first_last(email):
    """Guess first/last name from email"""
    local = email.split('@')[0]
    
    if '.' in local:
        parts = local.split('.')
        return parts[0], parts[-1]
    elif '_' in local:
        parts = local.split('_')
        return parts[0], parts[-1]
    else:
        return local, ''

if __name__ == "__main__":
    domain = input("Enter domain (e.g., example.com): ").strip()
    
    emails = find_emails(domain)
    print(f"\nPossible emails for {domain}:\n")
    for email in emails:
        valid = validate_email(email)
        status = "✓" if valid else "✗"
        print(f"{status} {email}")
