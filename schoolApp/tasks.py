from telnetlib import PRAGMA_HEARTBEAT
from celery import shared_task
from school_registration_system import settings
from .models import Teacher
from django.core.mail import send_mail
from school_registration_system import celery

@celery.app.task
def mail_send_function():
    print("Hello###########################################################")
    teacher = Teacher.objects.filter(is_student=False)
    for i in teacher:
        mail_subject = f"Login User Accessed Detailed View of {teacher.username}"
        meassage = "You Opened the Detailed page of Teacher's Login"
        to_email = i.email
        send_mail(
            subject= mail_subject,
            message = meassage,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently= True,
        )
    return "Done"









import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from school_registration_system.settings import SENDGRID_API_KEY


@shared_task(bind=True)
def sendgrid_mail(self, context2):
    message = Mail(from_email="arpan121232@gmail.com",
                    to_emails="arpan.citrusbug@gmail.com",
                    subject="Sending with SendGrid is fun...!",
                    plain_text_content="and easy to do anywhere, even with Python.")
    message.dynamic_template_data={
                                    "school_name":context2.school_name
                                    # "organiser_name":serializer[0].get('organiser_name'),
                                    # "event_name":serializer[0].get('event_name'),
                                    # "event_address":serializer[0].get('event_address'),
                                    # "dates":serializer[1],
                                    # "access_points":serializer[2]
                                    }
    message.template_id='d-d52d61f746494240bd3ca19799e6d6a4'
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("()(((((((((((((")
    except Exception as e:
        print(e.message)