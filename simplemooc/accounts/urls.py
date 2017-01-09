from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	url(r'^$', dashboard, name='dashboard' ),
	url(r'^entrar/$', auth_views.login,
	{'template_name': 'accounts/login.html'}, name='login' ),
	url(r'^sair/$', auth_views.logout,
	{'next_page': 'core:home'}, name='logout' ),
	url(r'^cadastre-se/$', register, name='register' ),
	url(r'^editar/$', edit, name='edit' ),
	url(r'^editar-senha/$', edit_password, name='edit_password' ),
]