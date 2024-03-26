from django.core.mail import send_mail
from django.conf import settings
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



    def get_info(self):
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg
    
    def send(self):
        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )

# class SubForm(forms.Form):
#     name = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     def get_info(self):
#         cl_data = super().clean()        
#         from_email = cl_data.get('email')
#         subject = "ONLINE MEDICINE SUB"
#         msg = "Thank you for your sub stay tuned for news......"
#         return subject, msg, from_email
    
#     def send(self):
#         subject, msg, from_email = self.get_info()

#         send_mail(
#             subject=subject,
#             message=msg,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[from_email]
#         )