"""
URL configuration for VTP project.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views
from django.urls import include, path
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.contrib.sitemaps import Sitemap as WagtailSitemap
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("enquiry/", include("apps.enquiry.urls")),
    path(
        "sitemap.xml",
        sitemap_views.sitemap,
        {"sitemaps": {"wagtail": WagtailSitemap}},
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    # Wagtail catch-all — must be last
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns = staticfiles_urlpatterns() + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
    except ImportError:
        pass
