from rest_framework import generics
from polls.serializer.RusWordSerializer import RusWordSerializer
from polls.models import RusWord


class RusList(generics.ListCreateAPIView):
    queryset = RusWord.objects.all()
    serializer_class = RusWordSerializer


class RusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RusWord.objects.all()
    serializer_class = RusWordSerializer
