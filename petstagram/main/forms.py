from django import forms

from petstagram.common.helpers import BootstrapFormMixin, DisabledFieldsForMixin
from petstagram.main.models import Pet, Pet_photo


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()
    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1920, 2023)),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
    class Meta:
        model = Pet
        exclude = ('user_profile',)
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1920, 2023))

        }

class DeletePetForm(BootstrapFormMixin, DisabledFieldsForMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        Pet_photo.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ()
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1920,2022)

            )
        }

class CreatePetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet_photo
        fields = ('photo', 'description', 'tagged_pets')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
        }

class EditPetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet_photo
        fields = ('description','tagged_pets')
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'rows': 5,
                }
            ),
        }


