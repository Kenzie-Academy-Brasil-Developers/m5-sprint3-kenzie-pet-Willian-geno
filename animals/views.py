from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import status, APIView, Response, Request
from animals.models import Animal
from animals.serializer import AnimalSerializer


class AnimalView(APIView):
    def post(self, req:Request):
        serialized = AnimalSerializer(data=req.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get(self, req:Request):
        animals = Animal.objects.all()
        serialized = AnimalSerializer(instance=animals, many=True)
       
        return Response({"Animals":serialized.data}, status.HTTP_200_OK)

class AnimalIdView(APIView):
    def get(self, req:Request, animal_id):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
            serialized = AnimalSerializer(animal)

            return Response(serialized.data, status.HTTP_200_OK)
        except Http404:
            return Response({"details":"Animal not found"}, status.HTTP_404_NOT_FOUND)
        
    def patch(self, req:Request, animal_id):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
            serialized = AnimalSerializer(animal, req.data, partial=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status.HTTP_200_OK)
        except Http404:
            return Response({"details":"Animal not found"}, status.HTTP_404_NOT_FOUND)

    def delete(self, req:Request, animal_id):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
            animal.delete()

            return Response({},status.HTTP_200_OK)
        except Http404:
            return Response({"details":"Animal not found"}, status.HTTP_404_NOT_FOUND)
            



