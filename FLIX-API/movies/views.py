from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieModelSerializer



class MovieCreateListeView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MoveRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer