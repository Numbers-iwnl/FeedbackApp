# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from .models import Feedback

# Allow multiple file selection
class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class FeedbackForm(forms.ModelForm):
    attachments = forms.FileField(
        required=False,
        widget=MultiFileInput(attrs={"multiple": True})
    )

    class Meta:
        model = Feedback
        fields = [
            "student_name", "operator_name", "type", "subject",
            "course_name", "class_name", "description"
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_attachments(self):
        files = self.files.getlist("attachments")
        if not files:
            return files

        max_mb = getattr(settings, "MAX_ATTACHMENT_MB", 10)
        max_bytes = max_mb * 1024 * 1024
        allowed = getattr(settings, "ALLOWED_MIME_TYPES", None)  # None/empty => no MIME check

        for f in files:
            if f.size and f.size > max_bytes:
                raise forms.ValidationError(f"Arquivo '{f.name}' excede {max_mb} MB.")

            ct = getattr(f, "content_type", None)
            if allowed:
                if ct not in allowed:
                    raise forms.ValidationError(f"Tipo de arquivo não permitido: {ct or 'desconhecido'}.")

        return files


class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=Feedback.STATUS_CHOICES)
