from rest_framework import generics
from polls.serializer.EnWordSerializer import EnWordSerializer
from polls.models import EnWord


class EnList(generics.ListCreateAPIView):
    queryset = EnWord.objects.all()
    serializer_class = EnWordSerializer


class EnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnWord.objects.all()
    serializer_class = EnWordSerializer
