from django.contrib import admin

from petstagram.main.models import Pet, Pet_photo


class PetInlineAdmin(admin.StackedInline):
    model = Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

@admin.register(Pet_photo)
class PetPhotoAdmin(admin.ModelAdmin):
    pass