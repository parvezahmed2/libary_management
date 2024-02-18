from django.contrib import admin

# Register your models here.
from .models import Book, Review , Category, BorroBook
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    lsit_display = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BorroBook)
 