from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]