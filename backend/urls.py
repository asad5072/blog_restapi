
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.post_list, name='post-list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
