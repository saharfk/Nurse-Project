from django.urls import path
from .views import Signup
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', Signup, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page': 'home'}, name='logout'),
]
