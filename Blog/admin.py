from django.contrib import admin
from .models import Posts,Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("type",)}

admin.site.register(Posts)
admin.site.register(Category,CategoryAdmin)

