from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from friend_connection.models import Friends
from friend_connection.serializers import FriendConnectionSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
import json


class UserFriendList(APIView):
    def get(self, request, friend_id, format=None):
        depth = 1
        try:
            depth = int(request.query_params["depth"])
        except MultiValueDictKeyError:
            print("No value set")

        json_data = json.dumps(self.__getFriendAtDepth(depth, friend_id))
        return Response(json_data)

    def __getFriendAtDepth(self, depth, friend_id):
        friend_list = self.__getUserFriendList(friend_id)
        while depth > 1:
            friend_list = self.__getListRecursionFriend(friend_list)
            friend_list.remove(friend_id)
            depth = depth - 1

        return friend_list

    def __getListRecursionFriend(self, friend_list):
        finalReturnList = []
        for item in set(friend_list):
            finalReturnList = finalReturnList + (self.__getUserFriendList(item))

        return list(set(finalReturnList))

    def __getUserFriendList(self, friendId):
        list_of_friends = []
        queryset1 = Friends.objects.filter(friend1=friendId)
        for value in queryset1:
            list_of_friends.append(value.friend2)

        queryset2 = Friends.objects.filter(friend2=friendId)
        for value in queryset2:
            list_of_friends.append(value.friend1)

        return list_of_friends
