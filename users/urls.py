from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", views.getRoutes),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.user_register_view, name="register_user"),
    path('me/', views.my_view, name="my_view"),

    path('user/<str:user_id>', views.get_user, name="get_user")
]
