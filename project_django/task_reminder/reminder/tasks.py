from celery import shared_task
from django.core.mail import send_mail
from .models import Reminder

@shared_task
def send_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        if reminder.notification_type == 'email':
            send_mail(
                subject=f"Reminder: {reminder.title}",
                message=reminder.description,
                from_email=None,
                recipient_list=[reminder.email],
            )
        elif reminder.notification_type == 'sms':
            print(f"[SMS SENT] To: {reminder.phone} | Message: {reminder.description}")
        reminder.status = 'sent'
    except Exception as e:
        print(f"Error: {e}")
        reminder.status = 'failed'
    reminder.save()