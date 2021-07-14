from rest_framework import filters as rest_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.permissions import *
from NEWSS.serializers import *
from rest_framework import generics


class ModuleNewsCrud(object):

    class CreateNews(generics.CreateAPIView):
        permission_classes = [AllowAny]
        queryset = NEWSS.objects.all()
        serializer_class = NewsSerializer

    class RetrieveNews(generics.RetrieveAPIView):
        permission_classes = [AllowAny]
        queryset = NEWSS.objects.all()
        serializer_class = NewsSerializer

    class UpdateNews(generics.UpdateAPIView):
        permission_classes = [AllowAny]
        queryset = NEWSS.objects.all()
        serializer_class = NewsSerializer

    class DestroyNews(generics.DestroyAPIView):
        permission_classes = [AllowAny]
        queryset = NEWSS.objects.all()
        serializer_class = NewsSerializer


class ModuleThemeCrud(object):
    class CreateTheme(generics.CreateAPIView):
        queryset = Themes.objects.all()
        permissions_clases = [permissions.AllowAny]
        serializer_class = ThemeSerializer

    class RetrieveTheme(generics.RetrieveAPIView):
        queryset = Themes.objects.all()
        permissions_clases = [permissions.AllowAny]
        serializer_class = ThemeSerializer

    class UpdateTheme(generics.UpdateAPIView):
        queryset = Themes.objects.all()
        permissions_clases = [permissions.AllowAny]
        serializer_class = ThemeSerializer

    class DeleteTheme(generics.DestroyAPIView):
        queryset = Themes.objects.all()
        permissions_clases = [permissions.AllowAny]
        serializer_class = ThemeSerializer


class News(generics.ListAPIView):
    queryset = NEWSS.objects.all()

    permissions_clases = [permissions.AllowAny]
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend, rest_filters.SearchFilter)
    search_fields = ["description", "name", "id"]
    filter_fields = ["date_of_creation", "theme", "date_of_update", "decription"]
    filterset_class = DatesFilter


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NEWSS.objects.all()

    permissions_clases = [permissions.AllowAny]
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend, rest_filters.SearchFilter)
    search_fields = ["description", "name", "id"]
    filter_fields = ["date_of_creation", "theme", "date_of_update", "decription"]

    filterset_class = DatesFilter


class Theme(generics.ListAPIView):
    queryset = Themes.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = ThemeSerializer


class ThemesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Themes.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = ThemeSerializer
