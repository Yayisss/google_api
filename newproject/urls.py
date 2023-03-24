from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

#Mapear los url para la app
urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]