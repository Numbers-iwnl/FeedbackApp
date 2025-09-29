from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'student_name', 'operator_name',
            'type', 'subject',
            'course_name', 'class_name',
            'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4})
        }
from django import forms
from .models import Feedback

class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=Feedback.STATUS_CHOICES)
