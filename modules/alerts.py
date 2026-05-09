import smtplib
from email.mime.text import MIMEText

from config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    RECEIVER_EMAIL
)


class AlertManager:

    def send_email_alert(self, subject, message):

        msg = MIMEText(message)

        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECEIVER_EMAIL

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.sendmail(
            EMAIL_ADDRESS,
            RECEIVER_EMAIL,
            msg.as_string()
        )

        server.quit()

        print("Email alert sent successfully!")