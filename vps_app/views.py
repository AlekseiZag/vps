from rest_framework.views import APIView
from rest_framework.response import Response

from vps_app.models import VPS
from vps_app.serializeres import VPSSerializer


class VPSView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, *args, **kwargs):
        uid = self.kwargs.get("uid")
        if uid:
            vps = VPS.objects.get(uid=uid)
            serializer = VPSSerializer(vps)
        else:
            vps = VPS.objects.all()
            serializer = VPSSerializer(vps, many=True)
        return Response(serializer.data)
