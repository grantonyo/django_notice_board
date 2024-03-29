from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticeboard/', include("noticeboard_app.urls")),
    path('accounts/', include("accounts.urls")), 
    # path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include("allauth.urls")),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]
