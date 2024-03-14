from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerialize

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialize

class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Review.objects.all()
    serializer_class = ReviewSerialize
