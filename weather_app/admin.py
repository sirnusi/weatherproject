from django.contrib import admin
from .models import Note, Category
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Note, NoteAdmin)
admin.site.register(Category)