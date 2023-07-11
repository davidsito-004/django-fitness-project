from django.urls import path
import accounts.views

urlpatterns = [
    path('register/', accounts.views.register_user, name='register-user'),
    path('login/', accounts.views.CustomLoginView.as_view(
        template_name='accounts/login.html'), name="login-user"),
    path('logout/', accounts.views.CustomLogoutView.as_view(
        template_name='accounts/logout.html'), name='logout-user')
]
