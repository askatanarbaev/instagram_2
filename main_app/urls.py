from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path

urlpatterns = [
    path('', post_list, name='home'),
    path('notebooks/<str:slug>/', NotebookDetailView.as_view(),  name='product_detail_notebook'),
    path('cars/<str:slug>/', CarDetailView.as_view(),  name='product_detail'),
    path('smartphone/<str:slug>/', SmartphoneDetailView.as_view(), name='smartphone_detail'),
    path('create_profile/', NewProfileView.as_view(), name='create_profile'),
    path('my_profile/', my_profile, name='my_profile'),
    path('my_profile/edit_profile/', edit_profile, name='edit_profile'),
    path('category/notebook/', get_category_notebook, name='category_notebook'),
    path('category/smartphones/', get_category_spartphone, name='category_smartphones'),
    path('category/car/', get_category_car, name='category_car'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)