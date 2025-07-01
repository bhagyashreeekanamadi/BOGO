from django.db import models

class Reminder(models.Model):
    NOTIFY_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    remind_at = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    notification_type = models.CharField(max_length=10, choices=NOTIFY_CHOICES)
    status = models.CharField(max_length=20, default='pending')  # pending, sent, failed
    created_at = models.DateTimeField(auto_now_add=True)
