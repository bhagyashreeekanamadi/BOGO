from django.contrib import admin
from .models import Node, Metric

admin.site.register(Node)
admin.site.register(Metric)