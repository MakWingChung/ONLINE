from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.views.static import serve

handler404 = "base.views.page_not_found"



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include('base.api.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS}),
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


