from django.contrib import admin

# Register your models here.


from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_modified',)
    search_fields = ('title', 'status', 'date_modified',)
    ordering = ('status',)
    list_editable = ('status',)


admin.site.register(Post, PostAdmin)
