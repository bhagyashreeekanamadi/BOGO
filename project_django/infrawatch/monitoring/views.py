from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Metric,Node
from .serializers import MetricSerializer,NodeSerializer
import psutil
from rest_framework.response import Response
# Create your views here.
class NodeViewSet(viewsets.ModelViewSet):
    queryset=Node.objects.all()
    serializer_class=NodeSerializer

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def create(self, request, *args, **kwargs):
        # Only allow creation for localhost nodes
        try:
            node_id = request.data.get('node')
            node = Node.objects.get(id=node_id)
        except (Node.DoesNotExist, ValueError, TypeError):
            return Response({"error": "Invalid or missing node ID."}, status=status.HTTP_400_BAD_REQUEST)

        if node.ip_address not in ['127.0.0.1', 'localhost']:
            return Response({"error": "Only metrics for localhost can be collected automatically."}, status=status.HTTP_400_BAD_REQUEST)

        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        metric = Metric.objects.create(
            node=node,
            cpu_usage=cpu,
            memory_usage=mem,
            disk_usage=disk
        )
        serializer = self.get_serializer(metric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



