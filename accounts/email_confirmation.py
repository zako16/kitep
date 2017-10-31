from django.core.mail import send_mail
from django.conf import settings


def EmailSender(email_address):
    secret = 'It is my secret'
    message = 'Message'
    send_mail(message, '%s' % str(secret),
              settings.EMAIL_HOST_USER, ['%s' % email_address],
              fail_silently=False)