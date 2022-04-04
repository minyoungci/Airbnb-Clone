from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.HouseRule, models.Facility, models.Aminity)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass


# Register your models here.
