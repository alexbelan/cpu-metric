from rest_framework import serializers
from .models import CPUMetric


class CPUMetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPUMetric
        fields = ['data', 'date']

    def save(self, *args, **kwargs):
        cpu_data = CPUMetric(
            data=self.validated_data['data'],
        )
        cpu_data.save()
        return cpu_data