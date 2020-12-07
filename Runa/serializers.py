from rest_framework import serializers
from .models import Categories


# class CategoriesListSerializer(serializers.ModelSerializer): #!!!!
#     class Meta:
#         model = Categories
#         fields = ('name')

class FilterCategoriesListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoriesSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterCategoriesListSerializer
        model = Categories
        fields = ("name", "children")