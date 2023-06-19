from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.signup),
    path('signup-data',views.signup_data),
    path('after_login',views.login_check),
    path('logout',views.logout),
    path('login',views.login)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)