from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenresSerializer


class GenreRetrievUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer