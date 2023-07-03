from django.db import models
from datetime import datetime

# Create your models here.
class AuthorModel(models.Model):
     name=models.CharField(max_length=150,default='')
     f_name=models.CharField(max_length=150,default='')
     date_birth=models.DateField(default=datetime.now)
     country=models.CharField(max_length=100,default='')

     def __str__(self):
        return self.name

     class Meta:
        db_table='Author'

class BookCategoryModel(models.Model):
    name=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table='book_category'


class BookModel(models.Model):
     author=models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
     name=models.CharField(max_length=133,default='')
     category=models.ForeignKey(BookCategoryModel,on_delete=models.SET_NULL,null=True)
     page=models.PositiveSmallIntegerField(default=1)
     price=models.PositiveIntegerField(default='')


     def __str__(self):
         return self.name

     class Meta:
         db_table='book'
