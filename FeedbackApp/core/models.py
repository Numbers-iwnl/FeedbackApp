from django.db import models

class Feedback(models.Model):
    TIPO_CHOICES = [
        ('elogio', 'Elogio'),
        ('reclamacao', 'Reclamação'),
        ('sugestao', 'Sugestão'),
    ]
    ASSUNTO_CHOICES = [
        ('financeiro', 'Financeiro'),
        ('atendimento', 'Atendimento'),
        ('plataforma', 'Plataforma'),
        ('conteudo', 'Conteúdo'),
        ('eventos', 'Eventos'),
        ('outros', 'Outros'),
    ]
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_analise', 'Em análise'),
        ('resolvido', 'Resolvido'),
    ]

    student_name  = models.CharField('Nome do aluno', max_length=160)
    operator_name = models.CharField('Operador responsável', max_length=160, blank=True, null=True)

    type        = models.CharField('Tipo de feedback', max_length=12, choices=TIPO_CHOICES)
    course_name = models.CharField('Curso', max_length=160, blank=True, null=True)
    class_name  = models.CharField('Turma', max_length=160, blank=True, null=True)
    subject     = models.CharField('Assunto', max_length=20, choices=ASSUNTO_CHOICES)

    description = models.TextField('Descrição', blank=True, null=True)

    status      = models.CharField('Status', max_length=12, choices=STATUS_CHOICES, default='pendente')
    resolved_at = models.DateTimeField('Resolvido em', blank=True, null=True)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'#{self.id} - {self.student_name} - {self.type}'

class FeedbackAttachment(models.Model):
    feedback   = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='attachments')
    file       = models.FileField(upload_to='feedbacks/%Y/%m/')
    mime_type  = models.CharField(max_length=120, blank=True, null=True)
    file_size  = models.IntegerField(blank=True, null=True)
    duration_seconds = models.IntegerField(blank=True, null=True)  # opcional p/ áudios
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Attachment {self.id} of #{self.feedback_id}'

class FeedbackComment(models.Model):
    feedback     = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='comments')
    author_name  = models.CharField('Autor', max_length=160, blank=True, null=True)
    comment_text = models.TextField('Comentário')
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.id} of #{self.feedback_id}'
