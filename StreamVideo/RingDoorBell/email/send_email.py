import sendgrid
from sendgrid.helpers.mail import Mail
import os

def send_email_api(email, message):
    sg = sendgrid.SendGridAPIClient("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")
    message = Mail(
    from_email='dowliang@gmail.com',
    to_emails=email,
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>' + message + '</strong>')
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

#send_email_api("dowliang@gmail.com", "This is a test email")
#send_email("apikey", "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", "dowliang@gmail.com", "Test", "Test")
