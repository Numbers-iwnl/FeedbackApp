"""
Definition of urls for FeedbackApp.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core import views as core_views

urlpatterns = [
    # --- Auth ---
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", core_views.logout_view, name="logout"),

    # --- Admin (restores 'admin:index' namespace used in the header) ---
    path("admin/", admin.site.urls),

    # --- App home ---
    path("", core_views.feedback_list, name="home"),

    # --- Feedbacks ---
    path("feedbacks/", core_views.feedback_list, name="feedback_list"),
    path("feedbacks/novo/", core_views.feedback_create, name="feedback_create"),
    path("feedbacks/<int:pk>/", core_views.feedback_detail, name="feedback_detail"),
    path("attachments/<int:pk>/", core_views.attachment_download, name="attachment_download"),

    # --- Exports ---
    path("export/csv/", core_views.export_csv, name="export_csv"),
    path("export/xlsx/", core_views.export_excel, name="export_excel"),
    path("export/pdf/", core_views.export_pdf, name="export_pdf"),

    # --- Stats / dashboard ---
    path("stats/summary/", core_views.stats_summary, name="stats_summary"),
    path("stats/breakdown/", core_views.stats_breakdown, name="stats_breakdown"),
    path("dashboard/", core_views.dashboard, name="dashboard"),

    # --- Health ---
    path("ping/", core_views.ping, name="ping"),
]

# Serve uploaded files in DEV
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
