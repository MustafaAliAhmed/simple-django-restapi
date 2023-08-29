from django.urls import path
from .import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('useinfo/', views.current_user, name='useinfo'),
    path('useinfo/update/', views.update_user, name='update_user'),
]
