from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CrafterPerson
from .serializers import CrafterSerializer


# class CrafterAPIView(generics.ListAPIView):
#     queryset = CrafterPerson.objects.all()
#     serializer_class = CrafterSerializer


class CrafterAPIView(APIView):
    def get(self, request):
        lst = CrafterPerson.objects.all()
        return Response({'crafters': CrafterSerializer(lst, many=True).data})

    def post(self, request):
        serializer = CrafterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        crafter_new = CrafterPerson.objects.create(
            name=request.data['name'],
            phone_number=request.data['phone_number'],
            category_id=request.data['category_id']
        )
        return Response({'crafter': CrafterSerializer(crafter_new).data})
