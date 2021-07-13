from django.contrib.auth.models import User
from rest_framework import serializers
from NEWSS.models import *
from django.db import models
from NEWSS.filter import *


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["url", "username", "email", "is_staff"]
#
#
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = (
            "id",
            "title",
        )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        name = models.CharField(max_length=150, verbose_name="title")
        model = NEWSS
        fields = [
            "id",
            "name",
            "description",
            "date_of_creation",
            "date_of_update",
            "status",
            "theme",
            "image",
        ]

        filter_fields = "date_of_creation", "theme", "date_of_update", "decription"
        search_fields = "theme", "description"
