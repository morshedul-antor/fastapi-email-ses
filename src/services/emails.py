from utils import EmailUtils
import boto3


class EmailService:

    def sendsmtp_email(self, subject: str, to_email: str, body: str):
        mail = EmailUtils.sendsmtp_email(
            subject=subject, to_email=to_email, body=body)
        return mail


email_service = EmailService()
