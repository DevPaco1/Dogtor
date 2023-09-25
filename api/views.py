from django.shortcuts import render
from rest_framework import viewsets, generics

# Models
from vet.models import PetOwner, Pet

# Serializers
from .serializers import OwnersSerializers

# Create your views here.
from .serializers import OwnersSerializers, OwnerRUDAPIViewSerializer


# LIST -> GET - check
# RETRIEVE -> GET
# UPDATE -> PUT
# CREATE -> POST
# DELETE -> DELETE


# TODOS LOS ENDPOINTS DE PETS
# TODOS LOS ENDPOINTS DE PETDATES


# class OwnersViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo PetOwner."""

#     # 1. queryset que se va a realizar -> ORM
#     # 2. El serializador

#     # Obtener todos los owners -> PetOwners.objects.all()
#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializers


# class PetsViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo Pet."""

#     queryset = Pet.objects.all()
#     serializer_class = PetsSerializer


#class ListOwnersAPIView(generics.ListAPIView):
 #   """List Owners Api View."""

#    queryset = PetOwner.objects.all().order_by("created_at")
#    serializer_class = OwnersListSerializer

"""
class RetrieveOwnersAPIView(generics.RetrieveAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer

class CreateOwnersAPIView(generics.CreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = OwnersCreateSerializer
    
    
class UpdateOwnersAPIView(generics.UpdateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = OwnersUpdateSerializer

class DeleteOwnersAPIView(generics.DestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDeleteSerializer
"""
class RetrieveUpdateDestroyOwnersAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = PetOwner.objects.all()
    serializer_class = OwnerRUDAPIViewSerializer

class ListCreatOwnerAPIView(generics.ListCreateAPIView):
    
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersSerializers