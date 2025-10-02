# FeedbackApp/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

from core import views as core_views


def root_redirect(request):
    """Anonymous -> login; Authenticated -> feedback list."""
    if request.user.is_authenticated:
        return redirect("feedback_list")
    return redirect("login")


urlpatterns = [
    # Root → login (or list if logged in)
    path("", root_redirect, name="root"),

    # Admin
    path("admin/", admin.site.urls),

    # Auth
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Core app
    path("feedbacks/", core_views.feedback_list, name="feedback_list"),
    path("feedbacks/novo/", core_views.feedback_create, name="feedback_create"),
    path("feedbacks/<int:pk>/", core_views.feedback_detail, name="feedback_detail"),

    path("attachments/<int:pk>/", core_views.attachment_download, name="attachment_download"),

    # Exports
    path("export/csv/", core_views.export_csv, name="export_csv"),
    path("export/xlsx/", core_views.export_excel, name="export_excel"),
    path("export/pdf/", core_views.export_pdf, name="export_pdf"),

    # Stats & dashboard
    path("stats/summary/", core_views.stats_summary, name="stats_summary"),
    path("stats/breakdown/", core_views.stats_breakdown, name="stats_breakdown"),
    path("dashboard/", core_views.dashboard, name="dashboard"),
]

# Media in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
