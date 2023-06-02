from django.urls import path, include
from . import views
from users import views as users_views
from django.contrib import auth

urlpatterns = [
    path('', views.index, name="index"),
    path('forum', views.forum),
    path('storage', views.storage),
    path('tutors/', include('tutors.urls')),
    path('profile', users_views.profile, name="profile"),#views.MyProfile
    path('signup',users_views.register , name="signup"),#views.SignUp.as_view()
    path('register/', users_views.register, name='register'),
    # path('profile/', user_views.profile, name='profile'),
    path('login/', auth.views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth.views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]