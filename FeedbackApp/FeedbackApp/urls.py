"""
Definition of urls for FeedbackApp.
"""

from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from app import views as app_views
from core import views as core_views

urlpatterns = [
    # Public/site pages from the scaffolded 'app'
    path("", app_views.home, name="home"),
    path("contact/", app_views.contact, name="contact"),
    path("about/", app_views.about, name="about"),

    # Auth (templates/registration/login.html)
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),

    # Admin
    path("admin/", admin.site.urls),

    # Core app
    path("ping/", core_views.ping, name="ping"),

    path("feedbacks/", core_views.feedback_list, name="feedback_list"),
    path("feedbacks/novo/", core_views.feedback_create, name="feedback_create"),
    path("feedbacks/<int:pk>/", core_views.feedback_detail, name="feedback_detail"),

    path("attachments/<int:pk>/", core_views.attachment_download, name="attachment_download"),

    path("export/csv/", core_views.export_csv, name="export_csv"),
    path("export/xlsx/", core_views.export_excel, name="export_excel"),
    path("export/pdf/", core_views.export_pdf, name="export_pdf"),

    path("stats/summary/", core_views.stats_summary, name="stats_summary"),
    path("stats/breakdown/", core_views.stats_breakdown, name="stats_breakdown"),
    path("dashboard/", core_views.dashboard, name="dashboard"),
]

# Static media in dev
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
