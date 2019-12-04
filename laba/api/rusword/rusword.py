from rest_framework import generics
from laba.serializer.RusWordSerializer import RusWordSerializer
from laba.models import RusWord


class RusList(generics.ListCreateAPIView):
    queryset = RusWord.objects.all()
    serializer_class = RusWordSerializer


class RusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RusWord.objects.all()
    serializer_class = RusWordSerializer
