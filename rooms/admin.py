from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definitions """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ RoomAdmin Admin Definitions """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ PhotoAdmin Admin Definitions """

    pass
