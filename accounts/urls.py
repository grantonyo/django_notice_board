from django.urls import path
from .views import logout_request, SignUpView


urlpatterns = [
    # path('', include("django.contrib.auth.urls")),
    path("logout/", logout_request, name= "logout"),
    path("signup/", SignUpView.as_view(), name="signup"),

]