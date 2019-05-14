from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'Images'),
    url(r'^search/', views.search_page, name='search_page'),
    url(r'^image/(\d+)', views.single_image, name = 'single_image'),
    url(r'^locations/sorted/$', views.sortby_locations, name = 'sortby_locations'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

