from django.shortcuts import render

from rest_framework import viewsets

from friend_connection.models import Friends
from friend_connection.serializers import FriendConnectionSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def all_friend_list(request):
    if request.method == 'GET':
        queryset = Friends.objects.all()
        serializer = FriendConnectionSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FriendConnectionSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def friend_list(request, friendId):
    if request.method == 'GET':
        queryset = Friends.objects.filter(friend1=friendId)
        queryset |= Friends.objects.filter(friend2=friendId)
        serializer = FriendConnectionSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)



# Create your views here.
