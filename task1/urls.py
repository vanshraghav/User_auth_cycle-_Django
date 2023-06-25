from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.signup),
    path('signup-data',views.signup_data),
    path('after_login',views.login_check),
    path('logout',views.logout),
    path('login',views.login),
    path('create',views.create),
    path('publish',views.publish),
    path('view_post',views.view_post,name='view_post'),
    path('all_posts',views.all,name="all_posts"),
    path('view_spec/<str:pk>',views.view_spec),
    path('view_draft/<str:pk>',views.view_draft),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)