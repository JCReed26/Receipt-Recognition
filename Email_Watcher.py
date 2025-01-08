from datetime import time
import imaplib
import email
import subprocess

EMAIL_ACCOUNT = 'email.email.com'
PASSWORD = 'pass'
IMAP_SERVER = 'imap.email.com'

def check_for_emails():
    # use imap server to .login .select .search
    # get attachments and send to reader

while True:
    check_for_emails()
    time.sleep(60)