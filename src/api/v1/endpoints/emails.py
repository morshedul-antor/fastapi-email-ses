from fastapi import APIRouter
import boto3

router = APIRouter()


@router.post('/email')
def send_ses_email():
    sender = "antor.morshedul@healthxbd.com"
    recipient = "antor.morshedul@gmail.com"
    subject = "This is a test email from ses"
    html_body = """
        <html>
            <head>
                <title>This is a test email</title>
            </head>
            <body>
                <h1>This is a test email</h1>
                <p>This is the body of the email.</p>
            </body>
        </html>
    """
    AWS_REGION = "ap-south-1"

    # Create a SES client
    client = boto3.client("ses", region_name=AWS_REGION)

    try:
        # Send the email
        response = client.send_email(
            Source=sender,
            Destination={"ToAddresses": [recipient]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Html": {"Data": html_body}}
            }
        )

        # Check the response
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {"status": "success", "message": "Email sent successfully"}
        else:
            return {"context": "Somethibg went wrong!", "error": "Sending failed!"}

    except Exception as e:
        return {"context": "Email sending failed!", "error": str(e)}
