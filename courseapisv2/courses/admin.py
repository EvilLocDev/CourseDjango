from django.contrib import admin
from .models import Category, Courses, Lesson, Tag

class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'create_date']
    search_fields = ['subject']
    list_filter = ['id', 'create_date']
    list_editable = ['subject']

    class Media:
        css = {
            'all': ('/static/css/styles.css',)
        }

# Register your models here.
admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)