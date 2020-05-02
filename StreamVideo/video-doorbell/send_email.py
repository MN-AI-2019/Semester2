import sendgrid
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import os
import base64

def send_email_api(email, message):
    sg = sendgrid.SendGridAPIClient("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")
    message = Mail(
    from_email='dowliang@gmail.com',
    to_emails=email,
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>' + message + '</strong>')
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
    
def send_attachment_api(email, message, data):
    sg = sendgrid.SendGridAPIClient("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")
    message = Mail(
    from_email='dowliang@gmail.com',
    to_emails=email,
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>' + message + '</strong>')
    
    attachment = Attachment()
    #attachment.content = data #base64.b64encode(data).decode()
    #attachment.type = 'image/jpeg'
    #attachment.filename = 'motion.jpg'
    #attachment.disposition = 'attachment'
    #message.add_attachment(attachment)    
    encoded = base64.b64encode(data).decode()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('image/jpeg')
    attachment.file_name = FileName('motion.jpg')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('MotionPic')
    message.attachment = attachment    

    response = sg.send(message)
    print(response.status_code, response.body, response.headers)    

#send_email_api("dowliang@gmail.com", "This is a test email")
#send_email("apikey", "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", "dowliang@gmail.com", "Test", "Test")
