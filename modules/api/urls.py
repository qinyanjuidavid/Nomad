from django.urls import path
from django.views.generic import TemplateView
from modules.accounts.views import (
    AdminRegistrationViewSet,
    LoginViewSet,
    NomadRegistrationViewSet,
    PasswordResetTokenCheck,
    RefreshViewSet,
    RequestPasswordResetEmail,
    SetNewPasswordAPIView,
    VerifyEmail,
)
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "api"
routes = SimpleRouter()

routes.register(r"login", LoginViewSet, basename="login")
routes.register(r"register", NomadRegistrationViewSet, basename="register")
routes.register(r"admin/sign-up", AdminRegistrationViewSet, basename="admin-register")
routes.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
routes.register(
    "password-reset", RequestPasswordResetEmail, basename="requestPasswordReset"
)
routes.register(
    "password-reset-complete", SetNewPasswordAPIView, basename="password-reset-complete"
)


urlpatterns = [
    *routes.urls,
    path("activate/", VerifyEmail, name="email-verify"),
    path(
        "password-reset/<uidb64>/<token>",
        PasswordResetTokenCheck,
        name="password-reset-confirm",
    ),
    path(
        "password-reset-successful/",
        TemplateView.as_view(template_name="accounts/password_reset_success.html"),
        name="passwordResetSuccess",
    ),
]
