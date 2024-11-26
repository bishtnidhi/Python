import re
from email.parser import Parser
# Example of suspicious URLs or email addresses
suspicious_urls = ['.ru', '.xyz', '.top', 'login', 'verify', 'security']
def check_suspicious_email(email_content):
 # Parse email content to extract links
 urls = re.findall(r'https?://[^\s]+', email_content)
 # Check if any URL is suspicious
 for url in urls:
 for suspicious_url in suspicious_urls:
 if suspicious_url in url:
 print(f"Suspicious URL detected: {url}")
 return True
 return False