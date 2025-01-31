from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ `r'^admin/'` এর বদলে সরাসরি 'admin/'
    path('fb_yomamabot/', include('fb_yomamabot.urls')),  # ✅ `r'^fb_yomamabot/'` বাদ
]