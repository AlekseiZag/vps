from rest_framework import serializers

from vps_app.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    """VPS model Serializer"""

    class Meta:
        model = VPS
        fields = '__all__'
