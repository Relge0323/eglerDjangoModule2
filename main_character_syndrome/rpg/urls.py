from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.character_list, name='character_list'),
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
]