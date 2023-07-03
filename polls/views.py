from django.shortcuts import render,get_objects_404
from rest_framework.views import APIView
from .models import BookModel
from .models import BookSerializers
from rest_framework.responce import  Response

# Create your views here.

class BookView(APIView):
    def get(self):
        book=BookModel.object.all()

        serializers=BookSerializers(book,many=True)

class DetailBookView(APIView):
    def get(self,request,*args,**kwargs):
        book = get_objects_404(BookModel, pk=kwargs['book_id'])
        serializer = BookSerializers(book)
        return Response(serializer.data)

class UpdateBookView(APIView):
    def get(self,request,*args,**kwargs):
        book=get_objects_404(BookModel, pk=kwargs['book_id'])
        serializer = BookSerializers(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, )





