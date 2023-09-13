from django import forms

#Los formularios se tienen que vincular con los modelos

from .models import PetOwner, Pet

#Los formularios se tienen que representar con CLASES

class PetOwnerForm(forms.ModelForm):

    class Meta:
        model = PetOwner
        fields =("first_name", "last_name","address", "email", "phone")

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields =("name", "type","owner")
