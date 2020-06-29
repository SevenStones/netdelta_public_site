import smtplib
import logging
from www.models import Contacts
from django.core.mail import send_mail, EmailMultiAlternatives


def contactmailnotify(message_dict):

    message = "Subject: contact received\n"
    message += "Contact mail received from " + str(message_dict['name']) + " (" + str(message_dict['email']) + ")\n"
    message += "IP address: " + str(message_dict['ip']) + "\n"
    message += "Message: " + str(message_dict['message'])

    sender = 'info@netdelta.io'
    receivers = ['info@netdelta.io', 'ian.tibble@netdelta.io']

    try:
        send_mail('contact received from www.netdelta.io',
                  message,
                  sender,
                  receivers,
                  fail_silently=False)
        logging.critical("Successfully sent notification email, contact form mail received from %s",
                         str(message_dict['email']))
    except smtplib.SMTPException:
        logging.critical("Error: unable to send notification email, contact form mail received from %s",
                         str(message_dict['email']))
        return False

    return True
