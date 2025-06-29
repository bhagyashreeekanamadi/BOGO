from rest_framework import serializers
from .models import Metric,Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Node 
        fields='__all__'


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model=Metric
        fields='__all__'


                        