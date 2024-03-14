from django.urls import path
from . import views

urlpatterns = [

    path('genres/', views.GenreCreateListView.as_view(), name='Genre'),
    path('genres/<int:pk>/', views.GenreRetrievUpdateDestroyView.as_view(), name='genre-detail-view'),

]