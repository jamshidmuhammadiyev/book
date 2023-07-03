 from django.urls import path
 from .views import BookView,DetailBookView,UpdateBookView
 urlpatterns=[
     path('',BookView.as_view()),
     path('<int:book_id>',DetailBookView.as_view()),
     path('update/<int:book_id>/',UpdateBookView.as_view()),

]