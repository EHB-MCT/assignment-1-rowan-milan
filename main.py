from email_automation.responder import process_emails
import time
import logging

if __name__ == "__main__":
    logging.info("Email Auto Responder started.")
    while True:
        process_emails()
        # Check inbox every 60 seconds
        time.sleep(60)
