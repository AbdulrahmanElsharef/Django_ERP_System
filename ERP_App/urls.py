from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('books', views.books, name="books"),
    # path('update', views.books, name="update"),
    # path('delete', views.books, name="delete"),
]
