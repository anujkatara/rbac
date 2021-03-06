from rest_framework import serializers
from status.models import Status

'''
Serializers -> JSON
Serializers -> validate data
'''


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]
