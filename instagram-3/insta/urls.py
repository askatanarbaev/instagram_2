from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    # path('profile/<int:pk>/', profile_acc, name='profile'),
    path('profile/<int:pk>/', ProfileAccountView.as_view(), name='profile'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)