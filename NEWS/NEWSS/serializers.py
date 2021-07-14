from rest_framework import serializers
from NEWSS.models import *
from django.db import models
from NEWSS.filter import *


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:

        model = Themes
        fields = (
            "id",
            "title",
            )


class NewsSerializer(serializers.ModelSerializer):
    date_of_creation = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", required=False, read_only=True
    )
    date_of_update = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", required=False, read_only=True
    )

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

        filter_fields = "date_of_creation", "theme", "date_of_update", "description"
        search_fields = "theme", "description"
