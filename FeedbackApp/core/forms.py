# core/forms.py
from django import forms
from .models import Feedback

# ===== Dropdown options for "Curso" (Curso -> <select>) =====
COURSE_CHOICES = [
    ("", "Selecione o curso"),
    ("RCA360", "RCA360"),
    ("RCA360 INFINITO", "RCA360 INFINITO"),
    ("LIBERAÇÃO FUNCIONAL AVANÇADA", "LIBERAÇÃO FUNCIONAL AVANÇADA"),
    ("MOBILIZAÇÃO NEURAL", "MOBILIZAÇÃO NEURAL"),
    ("PÓS-GRADUAÇÃO", "PÓS-GRADUAÇÃO"),
    ("POWERFISIO", "POWERFISIO"),
    ("MENTORIA BLACK", "MENTORIA BLACK"),
    ("BLACK DIAMOND", "BLACK DIAMOND"),
    ("CONGRESSO RCA", "CONGRESSO RCA"),
]

class FeedbackForm(forms.ModelForm):
    """
    Formulário da página 'Novo Feedback'.
    - Mantém seus campos originais
    - 'attachments' NÃO é mais um campo do formulário. O upload é lido direto de request.FILES.
    """
    class Meta:
        model = Feedback
        fields = [
            "student_name",   # Aluno
            "type",           # Tipo
            "subject",        # Assunto
            "course_name",    # Curso (dropdown)
            "class_name",     # Turma
            "description",    # Descrição
        ]
        widgets = {
            "course_name": forms.Select(choices=COURSE_CHOICES, attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 5, "class": "form-control"}),
        }
        labels = {
            "student_name": "Aluno",
            "type": "Tipo",
            "subject": "Assunto",
            "course_name": "Curso",
            "class_name": "Turma",
            "description": "Descrição",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilos/placeholder básicos (opcional)
        self.fields["student_name"].widget.attrs.setdefault("placeholder", "Nome do aluno")
        self.fields["class_name"].widget.attrs.setdefault("placeholder", "Turma (opcional)")
        for name in ["student_name", "type", "subject", "class_name"]:
            self.fields[name].widget.attrs.setdefault("class", "form-control")

class StatusForm(forms.ModelForm):
    """Usado nas telas que permitem alterar o status."""
    class Meta:
        model = Feedback
        fields = ["status"]
        labels = {"status": "Status"}
        widgets = {"status": forms.Select(attrs={"class": "form-control"})}
