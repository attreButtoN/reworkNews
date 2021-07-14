from django.urls import path
from NEWSS.views import *

urlpatterns = [

    path("news/<int:pk>/", ModuleNewsCrud.RetrieveNews.as_view()),
    path("news/create/", ModuleNewsCrud.CreateNews.as_view()),
    path("news/update/<int:pk>/", ModuleNewsCrud.UpdateNews.as_view()),
    path("news/delete/<int:pk>/", ModuleNewsCrud.DestroyNews.as_view()),
    path("news/", News.as_view()),

    path("themes/<int:pk>/", ModuleThemeCrud.RetrieveTheme.as_view()),
    path("themes/create/", ModuleThemeCrud.CreateTheme.as_view()),
    path("themes/update/<int:pk>/", ModuleThemeCrud.UpdateTheme.as_view()),
    path("themes/delete/<int:pk>/", ModuleThemeCrud.DeleteTheme.as_view()),
    path('themes/', Theme.as_view()),

    path("themes/<int:pk>/", ThemesDetail.as_view()),
    path("news/<int:pk>/", NewsDetail.as_view()),

]
