from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<movie_id>', views.detail, name='')
]
