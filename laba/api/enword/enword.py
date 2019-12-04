from rest_framework import generics
from laba.serializer.EnWordSerializer import EnWordSerializer
from laba.models import EnWord


class EnList(generics.ListCreateAPIView):
    queryset = EnWord.objects.all()
    serializer_class = EnWordSerializer


class EnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnWord.objects.all()
    serializer_class = EnWordSerializer