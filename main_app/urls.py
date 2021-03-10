from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path

urlpatterns = [
    path('', post_list, name='home'),
    # path('products/<str:slug>/', post_detail,  name='product_detail'),
    path('notebooks/<str:slug>/', NotebookDetailView.as_view(),  name='product_detail_notebook'),
    path('cars/<str:slug>/', CarDetailView.as_view(),  name='product_detail'),
    path('smartphone/<str:slug>/', SmartphoneDetailView.as_view(), name='smartphone_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)