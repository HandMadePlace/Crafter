from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import CrafterPerson, CategoryCrafter
from .serializers import CrafterSerializer


class CrafterPersonViewSet(viewsets.ModelViewSet):
    queryset = CrafterPerson.objects.all()
    serializer_class = CrafterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None) -> Response:
        category = CategoryCrafter.objects.get(pk=pk)

        return Response({'category': category.title})
