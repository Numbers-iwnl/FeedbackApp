from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core import views as core_views

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Auth
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # App (home -> lista)
    path("",                    core_views.feedback_list,   name="home"),
    path("feedbacks/",         core_views.feedback_list,   name="feedback_list"),
    path("feedbacks/novo/",    core_views.feedback_create, name="feedback_create"),
    path("feedbacks/<int:pk>/",core_views.feedback_detail, name="feedback_detail"),

    # Exports
    path("export/csv/",  core_views.export_csv,   name="export_csv"),
    path("export/xlsx/", core_views.export_excel, name="export_excel"),
    path("export/pdf/",  core_views.export_pdf,   name="export_pdf"),

    # Dashboard + stats APIs
    path("dashboard/",       core_views.dashboard,       name="dashboard"),
    path("stats/summary/",   core_views.stats_summary,   name="stats_summary"),
    path("stats/breakdown/", core_views.stats_breakdown, name="stats_breakdown"),

    # Health
    path("ping/", core_views.ping, name="ping"),
]

# Media files (DEV only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
