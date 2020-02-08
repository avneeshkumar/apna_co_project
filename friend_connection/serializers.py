
from friend_connection.models import Friends
from rest_framework import serializers

class FriendConnectionSerializer(serializers.Serializer):
    friend1 = serializers.IntegerField(min_value=1)
    friend2 = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        temp_friend1 = validated_data.get("friend1")
        temp_friend2 = validated_data.get("friend2")
        if temp_friend1==temp_friend2:
            raise serializers.ValidationError('Invalid Data.')

        if temp_friend1 > temp_friend2:
            t = temp_friend1
            temp_friend2 = temp_friend1
            temp_friend1 = t

        validated_data["friend1"] = temp_friend1
        validated_data["friend2"] = temp_friend2
        return Friends.objects.create(**validated_data)


class ListSerializer(serializers.Serializer):
    list = serializers.ListField()









