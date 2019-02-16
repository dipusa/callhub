from rest_framework.serializers import ModelSerializer
from .models import Sequence


class SequenceSerializer(ModelSerializer):
    class Meta:
        model = Sequence
        fields = ('id', 'series', 'created_at')
