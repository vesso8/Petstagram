import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Pet(models.Model):
    #Constants
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    NAME_MAX_LENGTH = 30
    PET_TYPES = [(x,x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    #Fields(Columns)
    name = models.CharField(

        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length= max(len(x) for (x, _) in PET_TYPES),
        choices=PET_TYPES,

    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    #One-to-one relations

    #One-to-many relations
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    #Many-to-many relations

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user', 'name')
    def __str__(self):
        return f'{self.name} - {self.type}'


class Pet_photo(models.Model):
    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'


    photo = models.ImageField(
        upload_to= IMAGE_UPLOAD_TO_DIR,
        # validators=(
        #     MaxFileSizeValidator(IMAGE_MAX_SIZE_IN_MB),
        # ),
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )
    description = models.TextField(
        null = True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete= models.CASCADE,
    )