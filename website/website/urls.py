from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django_otp.admin import OTPAdminSite
from django.views.generic.base import TemplateView

#admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('', include('ad.urls', namespace='ad')),
    path('stats/', include('ad_statistics.urls', namespace='ad_statistics')),
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.internal_server_error'
