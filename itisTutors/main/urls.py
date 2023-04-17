from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('forum', views.forum),
    path('storage', views.storage),
    path('tutorsAbout', views.tutorsAbout),
    path('MyProfile', views.MyProfile, name="profile"),
    path('signup', views.SignUp.as_view(), name="signup"),
]