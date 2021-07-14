
from django.db import models


class Themes(models.Model):

    title = models.CharField(max_length=100, unique=True)

    def validate_unique(self, exclude="Данная тема уже существует"):
        raise exclude

    def __str__(self):
        return self.title


class NEWSS(models.Model):
    name = models.CharField(max_length=150, verbose_name="Title")
    description = models.CharField(max_length=150, verbose_name="Description")
    date_of_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creation",
        editable=False,

    )
    date_of_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Date of update"
    )
    status = models.BooleanField(auto_created=True, verbose_name="Status")
    theme = models.ForeignKey("Themes", on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to="image/%Y/%m/%d", verbose_name="News Image", blank=True
    )

    def __str__(self):
        return self.name
