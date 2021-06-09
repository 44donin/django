

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from geekapi.models import Person
from geekapi.serializers import GeekapiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def PersonList(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            persons = persons.filter(name__contains=name)
        serializer = GeekapiSerializer(persons, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = GeekapiSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Person.objects.all().delete()
        return JsonResponse({'message': 'All the person data deleted successfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
