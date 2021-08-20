from django.contrib import admin

from .models import *


class CodeImageInLine(admin.TabularInline):
    model = CodeImage
    max_num = 10


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CodeImageInLine, ]


admin.site.register(Reply)

