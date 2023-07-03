from rest_framework import serializers
from .models import BookModel,AuthorModel,BookCategoryModel,BookSerializers
from django.shortcuts import get_objects_or_404


class AuthorModelSerializer(serializers.Modelserializers):
    class Meta:
        model=AuthorModel
        field=('name','f_name','date_birth')

class BookCategorySerializer(serializers.Modelserializers):
    class Meta:
        model=BookCategoryModel
        field=('name',)


class BookSerializer(serializers.Modelserializers):
    class Meta:
        model=BookModel
        field=('author','name','category')

