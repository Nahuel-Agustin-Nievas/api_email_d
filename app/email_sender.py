import smtplib
from email.mime.text import MIMEText

def send_email(recipient: str, content: str):
    sender = "your-email@example.com"
    password = "your-email-password"

    msg = MIMEText(content)
    msg["Subject"] = "Extracted PDF Content"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:  # Example with Mailtrap
        server.login("your-mailtrap-username", "your-mailtrap-password")
        server.sendmail(sender, recipient, msg.as_string())
