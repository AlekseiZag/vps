from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from vps_app.models import VPS
from vps_app.serializeres import VPSSerializer


class VPSListView(generics.ListAPIView):
    """Filtering VPS"""
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filterset_fields = ['status', 'hdd', 'cpu', 'ram']
    filter_backends = [DjangoFilterBackend]


class VPSView(APIView):

    def post(self, request):
        """Create new VPS"""
        vps = request.data
        serializer = VPSSerializer(data=vps)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """Return VPS by uid or all"""
        if uid := self.kwargs.get("uid"):
            vps = VPS.objects.get(uid=uid)
            serializer = VPSSerializer(vps)
            return Response(serializer.data)

    def patch(self, request, uid):
        """Update VPS status"""
        vps = get_object_or_404(VPS, uid=uid)
        data = {"status": request.data.get("status")}
        serializer = VPSSerializer(vps, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
