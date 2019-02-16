from django.conf.urls import url
from fibonacci import views as views

urlpatterns = [
    url(r'^api/fibonacci/$', views.FibonacciView.as_view()),
]
