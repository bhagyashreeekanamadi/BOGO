# monitoring/management/commands/simulate_metrics.py
import psutil
from django.core.management.base import BaseCommand
from monitoring.models import Node, Metric

class Command(BaseCommand):
    help = 'Collect real system metrics from host machine using psutil'

    def handle(self, *args, **kwargs):
        localhost_nodes = Node.objects.filter(ip_address__in=['127.0.0.1', 'localhost'])
        if not localhost_nodes.exists():
            self.stdout.write(self.style.WARNING("⚠️ No localhost node found (127.0.0.1 or localhost)."))
            return

        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        for node in localhost_nodes:
            Metric.objects.create(
                node=node,
                cpu_usage=cpu,
                memory_usage=mem,
                disk_usage=disk
            )

        self.stdout.write(self.style.SUCCESS("✅ Real-time system metrics collected using psutil."))
