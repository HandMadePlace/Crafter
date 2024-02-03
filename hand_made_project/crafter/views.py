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
        serializer.save()

        return Response({'crafter': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = CrafterPerson.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = CrafterSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'crafter': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = CrafterPerson.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        instance.delete()

        return Response({'crafter': f'{instance.name} has been removed'})


