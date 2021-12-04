from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.core.mail import send_mail

urlpatterns = [
    path("", views.redirectLiveData),
    path("live/", views.liveData, name="live"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
