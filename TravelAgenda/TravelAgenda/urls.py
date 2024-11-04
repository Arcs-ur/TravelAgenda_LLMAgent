from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    # Website main page
    re_path(r'^$', lambda request: render(request, 'accounts/index.html')),
    # Login, register
    path('accounts/', include('accounts.urls')),
    # Dashboard
    path('dashboard/', include('dashboard.urls')),
    # Destinations
    path('destinations/', include('destinations.urls')),
    # Agenda
    path('agenda/', include('agenda.urls')),
    # Posts
    path('posts/', include('posts.urls')),
    # notifications
    path('notifications/', include('notifications.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 handler
def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

# Assign the custom 404 view
handler404 = custom_404
