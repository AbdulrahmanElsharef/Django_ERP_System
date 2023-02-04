from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('items', views.items, name="items"),
    # path('update', views.books, name="update"),
    # path('delete', views.books, name="delete"),
]
