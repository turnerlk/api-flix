from django.urls import path
from . import views

urlpatterns = [

    path('reviews/', views.ReviewCreateListView.as_view(), name='reviews-creat'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='reviews-detail'),

]