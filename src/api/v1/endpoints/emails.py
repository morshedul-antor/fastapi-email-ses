from fastapi import APIRouter
import boto3

router = APIRouter()


@router.post('/email')
def send_ses_email():
    sender = "antor.morshedul@healthxbd.com"  # verified domain
    recipient = "antor.morshedul@gmail.com"
    subject = "Test email from SES"
    html_body = """
        <html>
            <body>
                <h1>Congratulations</h1>
                <p>Your registraion successfull at HEALTHx</p>
            </body>
        </html>
    """
    AWS_REGION = "ap-southeast-1"

    # SES client
    client = boto3.client("ses", region_name=AWS_REGION)

    try:
        response = client.send_email(
            Source=sender,
            Destination={"ToAddresses": [recipient]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Html": {"Data": html_body}}
            }
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {"status": "success", "message": "Email sent successfully"}
        else:
            return {"context": "Somethibg went wrong!", "error": "Sending failed!"}

    except Exception as e:
        return {"context": "Email sending failed!", "error": str(e)}
