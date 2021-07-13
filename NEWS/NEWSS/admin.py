from django.contrib import admin
from NEWSS.models import *


class ThemeAdmin(admin.ModelAdmin):
    list_display = "title"
    search_fields = "title"
    list_editable = "title"


class NewsAdmin(admin.ModelAdmin):
    display_fields = [
        "name",
        "id",
        "description",
        "date_of_creation",
        "date_of_update",
        "status",
        "theme",
        "image",
    ]
    # search_fields = (
    #     "name",
    #     "description",
    #     "date_of_creation",
    #     "date_of_update",
    #     "status",
    #     " theme",
    #     "image",
    # )
    # list_editable = (
    #     "name",
    #     "description",
    #     "date_of_creation",
    #     "date_of_update",
    #     "status",
    #     " theme",
    #     "image",
    # )
    # list_filter = (
    #     "name",
    #     "theme",
    #     "status",
    # )


admin.site.register(NEWSS,NewsAdmin)
