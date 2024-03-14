from django.urls import path
from . import views

urlpatterns = [

    path('actors/', views.ActorCreateListView.as_view(), name='Actos-create-list'),
    path('actors/<int:pk>/', views.ActorRetrievUpdateDestroyView.as_view(), name='actos-deteal-view'),
    path('actors/', views.ActorCreateListView.as_view(), name='Actors-create-list'),
    path('opa/', views.actor_render_list_view, name='Actors-render-list'),

]