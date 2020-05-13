from django.urls import path
from . import views
app_name = 'sem'

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/",views.sem, name="sem"),
    path("semester/",views.sem , name="sem"),
    path("subject/<int:pk>/",views.sub,name="sub"),
    path("lecture/",views.lecture,name="lecture")
]
