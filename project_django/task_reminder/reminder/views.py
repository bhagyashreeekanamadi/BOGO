from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from .models import Reminder
from .tasks import send_reminder


def create_reminder_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        remind_at = parse_datetime(request.POST.get('remind_at'))
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        notification_type = request.POST.get('notification_type')

        reminder = Reminder.objects.create(
            title=title,
            description=description,
            remind_at=remind_at,
            email=email,
            phone=phone,
            notification_type=notification_type
        )

        # Schedule Celery task
        send_reminder.apply_async((reminder.id,), eta=remind_at)

        return redirect('create_reminder')

    return render(request, 'reminders/reminder_form.html')
