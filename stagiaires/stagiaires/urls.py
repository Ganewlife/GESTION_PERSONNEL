"""stagiaires URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
import stagiaire_app.views
from django.conf import settings # important pour nos medias
from django.conf.urls.static import static #pour charge nos medias en ligne
from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', stagiaire_app.views.LoginPageView.as_view(), name='login'),
    path('logout/', stagiaire_app.views.logout_user, name='logout'),
    path('home/', stagiaire_app.views.home, name='home'),
    path('signup/', stagiaire_app.views.signup, name='signup'),
    path('user-info/>', stagiaire_app.views.user_profil, name='user_info'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='stagiaire_app/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='stagiaire_app/password_change_done.html'),
         name='password_change_done'
         ),
    path('stagiaire/create', stagiaire_app.views.stagiaire_and_files_upload, name='stagiaire_create'),
    path('stagiaire/<int:stagiaire_info_id>', stagiaire_app.views.view_stagiaire_info, name='view_profil'),
    path('stagaire/<int:stagiaire_info_id>/edit', stagiaire_app.views.edit_stagiaire_info, name='stagiaire_edit'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
