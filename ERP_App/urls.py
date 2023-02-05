from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('items', views.items, name="items"),
    path('add', views.add_item, name="add"),
    # path('update', views.books, name="update"),
    # path('delete', views.books, name="delete"),
]
