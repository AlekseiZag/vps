from rest_framework import serializers

from vps_app.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    """Сериализатор модели VPS"""

    class Meta:
        model = VPS
        fields = '__all__'
