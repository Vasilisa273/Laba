from rest_framework import serializers
from polls.models import EnWord


class EnWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnWord
        exclude = ()
