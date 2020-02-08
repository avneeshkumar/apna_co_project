from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from friend_connection.models import Friends
from friend_connection.serializers import FriendConnectionSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse


class AllFriendList(APIView):
    def get(self, request, format=None):
        queryset = Friends.objects.all()
        serializer = FriendConnectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = FriendConnectionSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


