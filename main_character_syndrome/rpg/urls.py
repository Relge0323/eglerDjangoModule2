from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.character_list, name='character_list'),
    
    # <int:pk> is a path converter that is used to help show which character was clicked in detail.
    # the pk refers to the primary key of the #th record in the table
    path('characters/<int:pk>/', views.character_detail, name='character_detail'),
]