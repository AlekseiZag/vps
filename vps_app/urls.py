from django.urls import path

from vps_app.views import VPSView, VPSListView

urlpatterns = [
    path('vps/', VPSListView.as_view()),
    path('vps/<str:uid>/', VPSView.as_view()),

]
