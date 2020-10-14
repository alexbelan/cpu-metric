from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView

# Create your views here.
from rest_framework.views import APIView

from .models import CPUMetric
from .serializers import CPUMetricSerializer


# def index_page(request):
#     return render(request, "index.html")


class CreateCPUMetricView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = CPUMetric.objects.all()
    serializer_class = CPUMetricSerializer

    def get(self, request):
        context = {
            "cpu_metrics": CPUMetric.objects.order_by('-date')[:100]
        }
        return render(request, "index.html", context)

    def post(self, request):
        serializer = CPUMetricSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'data': serializer.data.get('data'),
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors)
