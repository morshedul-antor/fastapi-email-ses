from smtplib import SMTPException, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from db.core import Settings


class EmailService:

    def send_email(subject: str, to_email: str, body: str):
        msg = MIMEMultipart()
        msg['From'] = Settings.SMTP_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            smtp_server = SMTP_SSL(Settings.SMTP_SERVER, Settings.SMTP_PORT)
            smtp_server.login(Settings.SMTP_USERNAME, Settings.SMTP_PASSWORD)
            smtp_server.sendmail(Settings.SMTP_USERNAME,
                                 to_email, msg.as_string())
            smtp_server.quit()
            return True
        except SMTPException:
            return False


email_service = EmailService()
