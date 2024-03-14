from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer
from django.shortcuts import render

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class ActorRetrievUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

def actor_render_list_view(request):
    actors = Actor.objects.all()
    return render(request=request, template_name='opa.html', context={'actors': actors})
