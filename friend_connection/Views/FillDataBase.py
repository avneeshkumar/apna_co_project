from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from friend_connection.models import Friends
import random
from friend_connection.serializers import FriendConnectionSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse


def checkKey(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False


class FillDataBase(APIView):

    def get(self, request, format=None):
        Friends.objects.all().delete()
        final_friend_list = []
        local_dictionary = {}
        for i in range(1, 1001):
            count = 0
            while count < 30:
                random_friend_id = random.randint(1, 1000)
                if random_friend_id == i:
                    continue
                else:
                    if i < random_friend_id:
                        if checkKey(local_dictionary, str(i) + "_" + str(random_friend_id)):
                            continue
                        else:
                            #print("Inserting " + str(i) + "," + str(random_friend_id))
                            temp_object = Friends(friend1=i, friend2=random_friend_id)
                            final_friend_list.append(temp_object)
                            local_dictionary[str(i) + "_" + str(random_friend_id)] = True
                        count = count+1
                    else:
                        if checkKey(local_dictionary, str(random_friend_id) + "_" + str(i)):
                            continue
                        else:
                            #print("Inserting " + str(random_friend_id) + "," + str(i))
                            temp_object = Friends(friend1=random_friend_id, friend2=i)
                            final_friend_list.append(temp_object)
                            local_dictionary[str(random_friend_id) + "_" + str(i)] = True
                        count = count + 1
        try:
            #print("Inserting " + str(i))
            Friends.objects.bulk_create(final_friend_list)
            final_friend_list = []
        except:
            print("Exception occuerd")




        return Response("{success:True}", status=status.HTTP_201_CREATED)