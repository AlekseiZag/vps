from django.urls import path

from vps_app.views import VPSView

app_name = 'krod_v3'
urlpatterns = [
    path('vps/', VPSView.as_view()),
    path('vps/<str:uid>/', VPSView.as_view()),

]
