from django.conf.urls import url
from userdetails import views

urlpatterns = [
    url(r'^form/$', views.Model_Form),
]