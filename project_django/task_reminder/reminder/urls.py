from django.urls import path
from .views import create_reminder_view

urlpatterns = [
    path('', create_reminder_view, name='create_reminder'),
]
