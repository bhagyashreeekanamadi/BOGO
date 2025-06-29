from django.db import models

# Create your models here.
class Node(models.Model):
    name=models.CharField(max_length=100)
    ip_address=models.GenericIPAddressField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ({self.ip_address})"
    
class Metric(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    cpu_usage=models.FloatField()
    disk_usage=models.FloatField()
    memory_usage=models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.node.name} @ {self.timestamp}
