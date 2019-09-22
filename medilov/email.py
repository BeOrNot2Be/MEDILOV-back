from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def get_subjects(data):
    client_title = f"Thank you for getting in touch! AvilonProduction"
    wh_title = f"{data['job']} from {data['name']}" 
    return client_title, wh_title

def get_text_messages(data):
    message_to_websiteholder  = \
    f'''
        Name: {data["name"]}
        Time: {data["dates"]} 
        Job: {data["job"]}
        Job description: 
            {data["description"]}
        
        📧 Email: {data["email"]} 
        📞 Phone: +1{data["phone"]}
    '''
    
    message_to_client  = \
    f'''
        Thank you, {data["name"]} for contatcting us. We will get in touch with you as soon as possible.
        Please check your phone number 📞(+1{data["phone"]}) and email 📧({data["email"]}) again.
    '''

    return message_to_client, message_to_websiteholder

def get_html_message(data):
    return render_to_string('email.html', data)

def send_appoitment_registration(data):
    
    client_text, wh_text = get_text_messages(data)
    client_sub, wh_sub = get_subjects(data)
    client_html_msg = get_html_message(data)
    
    client_msg = EmailMultiAlternatives(client_sub, client_text, settings.EMAIL_HOST_USER, [data['email']])
    wh_msg = EmailMultiAlternatives(wh_sub, wh_text, settings.EMAIL_HOST_USER, [settings.WEBSITEHOLDEREMAIL])
    
    client_msg.attach_alternative(client_html_msg, "text/html")
    try:
        client_msg.send(fail_silently=False)
        wh_msg.send(fail_silently=False)
    except Exception:
        return False
    else:
        return True
        