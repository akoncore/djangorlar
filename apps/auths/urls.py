from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/',views.RegisterView.as_view({'post':'create'}),name = 'register'),
    path('login/',views.LoginView.as_view({'get':'post'}),name = 'login'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]
