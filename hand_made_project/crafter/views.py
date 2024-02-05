from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CrafterPerson
from .serializers import CrafterSerializer


class CrafterPersonViewSet(viewsets.ModelViewSet):
    queryset = CrafterPerson.objects.all()
    serializer_class = CrafterSerializer
