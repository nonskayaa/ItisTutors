from django.urls import path
from .views import (
    SubjectListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SubjectPostListView

)
from . import views

urlpatterns = [
    path('', SubjectListView.as_view(), name='storage-home'),
    path('/subject/<int:pk>', SubjectPostListView.as_view(), name='subject-posts'),
    path('/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('/new/', PostCreateView.as_view(), name='post-create'),
    path('/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]