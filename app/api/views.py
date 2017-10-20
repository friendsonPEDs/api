from rest_framework import generics
from django.shortcuts import render
from .serializers import StepsSerializer
from .models import Steps

# Create your views here.
class StepsCreateView(generics.ListCreateAPIView):
    """Create step behavior"""
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer

    def perform_create(self, serializer):
        """Save the data when sending in steps"""
        serializer.save(owner=self.request.user)

class StepsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET, PUT, DELETE"""
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer
