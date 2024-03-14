from django.urls import path
from . import views

urlpatterns = [

    path('movies/', views.MovieCreateListeView.as_view(), name='move-create-list'),
    path('movies/<int:pk>/', views.MoveRetrieveDestroyAPIView.as_view(), name='movies-deteal-view'),

]