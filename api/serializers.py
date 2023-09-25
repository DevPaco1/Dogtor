from rest_framework import serializers

# Modelos
from vet.models import PetOwner, Pet


# HTTP -> body
# Serializadores -> Representacion de nuestra API
class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer."""

    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "phone",
            "created_at",
        ]


class PetsSerializer(serializers.HyperlinkedModelSerializer):
    """Pet serializer."""

    owner = serializers.PrimaryKeyRelatedField(
        queryset=PetOwner.objects.all(), many=False
    )

    class Meta:
        model = Pet
        fields = [
            "name",
            "type",
            "created_at",
            "owner",  # foreign key
        ]


class OwnersListSerializer(serializers.ModelSerializer):
    """Serializer to list all Pet Owners."""

    class Meta:
        model = PetOwner
        fields = ["id","first_name", "last_name"]
"""

class OwnersDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetOwner
        fields = "__all__"

class OwnersCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetOwner
        fields = "__all__"

class OwnersUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetOwner
        fields = "__all__"

class OwnersDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetOwner
        fields = "__all__"
"""

class OwnerRUDAPIViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetOwner
        fields = "__all__"