from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('forum', views.forum),
    path('storage', views.storage),
    path('tutors/', include('tutors.urls')),
    path('MyProfile', views.MyProfile, name="profile"),
    path('signup', views.SignUp.as_view(), name="signup"),
]