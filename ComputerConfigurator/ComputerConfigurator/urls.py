"""ComputerConfigurator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django_registration.backends.one_step.views import RegistrationView

from users.forms import CustomUserForm
from core.views import IndexTemplateView

# Images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),


    # This View is provided by django registration
    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
         ), name="django_registration_register"),

    path("accounts/", include("django_registration.backends.one_step.urls")),

    path("accounts/", include("django.contrib.auth.urls")),

    # Login via browsable API
    path("api/", include("users.api.urls")),

    # Login via browsable API
    path("api-auth/", include("rest_framework.urls")),

    # Login via Rest-API
    path("api/rest-auth/", include("rest_auth.urls")),

    # Registration via Rest-API
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*$', IndexTemplateView.as_view(), name='entry-point')]
