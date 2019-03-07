from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Fibonacci.as_view(), name='fibonacci'),
]
