from rest_framework import serializers
from laba.models import EnWord


class EnWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnWord
        exclude = ()
