from rest_framework import serializers
from polls.models import RusWord


class RusWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = RusWord
        exclude = ()