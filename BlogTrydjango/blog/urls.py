from django.urls import path
from .views import *

urlpatterns = [
    path('', display, name="blog"),
    path('<int:post_id>', display, name="display"),
    path('create', create , name="create"),
    path('update', update , name="update"),
    path('delete', delete , name="delete"),
    path('search', search, name="search"),
]