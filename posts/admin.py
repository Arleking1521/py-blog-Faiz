from django.contrib import admin
from .models import Post, Post_Attachments, Comment
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(Post)
class CustomPostAdmin(TranslationAdmin):
    fieldsets = (
        (_('Author'), {'fields': ('author',)}),
        (_('Information on russian'), {'fields': ('title_ru', 'content_ru',)}),
        (_('Information on kazakh'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Information on english'), {'fields': ('title_en', 'content_en',)}),
        (_('Additionaly information'), {'fields': ('edited',)}),
    )
    add_fieldsets = (
        (_('Author'), {'fields': ('author',)}),
        (_('Information on russian'), {'fields': ('title_ru', 'content_ru',)}),
        (_('Information on kazakh'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Information on english'), {'fields': ('title_en', 'content_en',)}),
    )
    list_display = (
        'title',
        'date',
        'edited',
    )

admin.site.register(Post_Attachments)
admin.site.register(Comment)
