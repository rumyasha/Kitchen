from django.urls import path
from .views import hello, create_proposal, album
from . import views

urlpatterns = [
    path('', hello, name='Hello'),
    path('about', create_proposal, name='about'),
    path('album', album, name='album'),
    path('Kitchen', views.authors_list, name='Kitchen'),
    path('Kitchen_2', views.AuthorsListView.as_view(), name='Kitchen_2'),
]