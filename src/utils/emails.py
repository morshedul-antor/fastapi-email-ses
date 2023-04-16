from smtplib import SMTPException, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from db.core import settings


class EmailUtils:

    @staticmethod
    def sendsmtp_email(subject: str, to_email: str, body: str):
        msg = MIMEMultipart()
        msg['From'] = settings.SMTP_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            smtp_server = SMTP_SSL(settings.SMTP_SERVER, settings.SMTP_PORT)
            smtp_server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            smtp_server.sendmail(settings.SMTP_USERNAME,
                                 to_email, msg.as_string())
            smtp_server.quit()
            return True
        except SMTPException:
            return False

    def sendgrid_email(subject: str, to_email: str, body: str):
        message = Mail(from_email=settings.SMTP_USERNAME,
                       to_emails=to_email, subject=subject, html_content=body)
        try:
            sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return True
        except Exception as e:
            print(e)
            return False
