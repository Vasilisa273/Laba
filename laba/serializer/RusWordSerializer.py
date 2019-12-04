from rest_framework import serializers
from laba.models import RusWord


class RusWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = RusWord
        exclude = ()