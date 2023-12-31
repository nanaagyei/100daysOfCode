from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

MY_EMAIL = "prince.agyei.tuffour@gmail.com"
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECIPIENT_ADDRESS = "nanakwameagyeituffour@gmail.com"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_email(self, message):
        # Create a MIMEText object with UTF-8 encoding
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = RECIPIENT_ADDRESS
        msg['Subject'] = "New flight deal alert!"
        msg.attach(MIMEText(message, 'plain', 'utf-8'))  # Use 'plain' for plain text email

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_ADDRESS,
                msg=msg.as_string()  # Convert the MIMEText object to a string
            )
