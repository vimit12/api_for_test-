from django.contrib import admin
from django.urls import path,re_path,include
from . import views as search_bar_view
urlpatterns = [
    path('', search_bar_view.search_bar, name='search'),
    # re_path(r'^api/(\w+)+',
    #         search_bar_view.product_detail_api, name='api-data'),
    re_path(r'^api/',
            search_bar_view.product_detail_api, name='api-data'),
    re_path(r'^apifull/',
            search_bar_view.product_detail_api_full, name='api-data-full'),
   
]
