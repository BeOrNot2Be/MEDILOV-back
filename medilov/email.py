from django.conf import settings
from django.core.mail import send_mail, EmailMessage, send_mass_mail

def send_website_email(data):
    for i in data:
        message = EmailMessage(*data)
        message.send(fail_silently=False)

def send_appoitment_registration(to_email, data):
    
    client_title = f"Thank you for getting in touch {data['name']}"
    holder_title = f"{data['job']}" 

    message_to_websiteholder  = \
    f'''
        to me
        {data}
    '''
    
    message_to_client  = \
    f'''
        to client
        {data}
    '''
    
    datatuple = (
        ('Subject', message_to_client, 'from@example.com', [to_email]),
        ('Subject', message_to_websiteholder, 'from@example.com', [settings.WEBSITEHOLDEREMAIL]),
    )
    send_website_email(datatuple)