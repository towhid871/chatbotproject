# yomamabot/fb_yomamabot/urls.py
from django.urls import path, include
from .views import YoMamaBotView
urlpatterns = [
                  path('171536bbc7f3d505f37717f5d25d539fc0e55b8151aa180a5e/', YoMamaBotView.as_view())
]