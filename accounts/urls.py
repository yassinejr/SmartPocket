from django.urls import path
from .views import *
from django.contrib.auth.views import *
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name="signup"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='password'),
    path('password_success/', views.password_success, name='password_success'),
    path('<slug:slug>', ProfileView.as_view(), name="my_profile"),
]