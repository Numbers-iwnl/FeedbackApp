from django.contrib import admin
from .models import Feedback, FeedbackAttachment, FeedbackComment

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','student_name','type','subject','course_name','class_name','status','created_at')
    list_filter = ('type','subject','status','course_name','class_name','created_at')
    search_fields = ('student_name','operator_name','description')

@admin.register(FeedbackAttachment)
class FeedbackAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id','feedback','file','mime_type','file_size','created_at')
    list_filter = ('created_at',)

@admin.register(FeedbackComment)
class FeedbackCommentAdmin(admin.ModelAdmin):
    list_display = ('id','feedback','author_name','created_at')
    search_fields = ('author_name','comment_text')
    list_filter = ('created_at',)
