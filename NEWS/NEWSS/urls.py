from django.urls import path, include
from django.urls import path
from NEWSS.views import *
from rest_framework import urls
urlpatterns = [
    # path("api-auth/", include("rest_framework.urls")),
    # path("api-news/", include("rest_framework.urls")),
    path("news/<int:pk>/", RetrieveNews.as_view()),
    path("news/create/<int:pk>/", CreateNews.as_view()),
    path("news/update/<int:pk>/", UpdateNews.as_view()),
    path("news/delete/<int:pk>/", DestroyNews.as_view()),
    path("news/", News.as_view()),

    path("themes/<int:pk>/", RetrieveTheme.as_view()),
    path("themes/create/<int:pk>/", CreateTheme.as_view()),
    path("themes/update/<int:pk>/", UpdateTheme.as_view()),
    path("themes/delete/<int:pk>/", DeleteTheme.as_view()),
    path('themes/', ThemesDetail.as_view()),

    path("themes/<int:pk>/", ThemesDetail.as_view()),
    path("news/<int:pk>/", NewsDetail.as_view()),
    # path("api-filters/", include("rest_framework.urls")),
    #path("api/news", RetrieveNews, "news"),
    #path("api/themes", ThemeViewSet, "Themes"),
]