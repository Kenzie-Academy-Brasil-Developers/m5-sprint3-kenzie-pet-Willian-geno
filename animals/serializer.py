from animals.models import Animal
from characterisrics.models import Characteristic
from groups.models import Group
from rest_framework import serializers
from characterisrics.serializers import CharacteristicsSerializer
from groups.serializers import GroupSerializers 

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    characteristics = CharacteristicsSerializer(many=True)

    group = GroupSerializers()


    def create(self, validated_data:dict):
        group_name = validated_data.pop("group")
        characteristics = validated_data.pop("characteristics")
       
        group, _ = Group.objects.get_or_create(**group_name)

        animal = Animal.objects.create(**validated_data, group=group)

        for characteristic in characteristics:
            characteristic, _ = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristics.add(characteristic)

        return animal


    def update(self, instance:Animal, validated_data:dict):
        if "sex" in validated_data:
            validated_data.pop("sex")
        if "group" in validated_data:
            validated_data.pop("group")

        if "characteristics" in validated_data:
            characteristics = validated_data.pop("characteristics")

            for characteristic in characteristics:
                characteristic, _ = Characteristic.objects.get_or_create(**characteristic)
                instance.characteristics.add(characteristic)

        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()


        return instance