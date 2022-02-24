import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main.validators import validate_only_letters, validate_file_max_size, MaxFileSizeValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x )for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length= FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )

    )
    last_name = models.CharField(
        max_length= LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length= max(len(g) for g, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
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
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    #Many-to-many relations

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user_profile', 'name')
    def __str__(self):
        return f'{self.name} - {self.type}'


class Pet_photo(models.Model):
    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'


    photo = models.ImageField(
        upload_to= IMAGE_UPLOAD_TO_DIR,
        validators=(
            MaxFileSizeValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
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