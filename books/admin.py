from django.contrib import admin
from books.models import Categories, Books, Years, CoverTypes, Publisher, Statuses

# Register your models here.

admin.site.register(Categories)
admin.site.register(Years)
admin.site.register(CoverTypes)
admin.site.register(Publisher)
admin.site.register(Statuses)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    class Meta:
        fields = ('title', 'author', 'cover', 'year', 'coverType', 'publisher',
                  'status', 'description', 'category', 'exchange', 'sale', 'price')


    # user_insert(self, request)
    # list_display = ('title', 'author', 'cover', 'year', 'coverType', 'publisher',
    #                 'status', 'description', 'category', 'exchange', 'sale', 'price', 'user')
    # list_display_links = ('title', 'author', 'cover', 'year', 'coverType', 'publisher',
    #                       'status', 'description', 'category', 'exchange', 'sale', 'price', 'user')
    # list_editable = ('title', 'author', 'cover', 'year', 'coverType', 'publisher',
    #                  'status', 'description', 'category', 'exchange', 'sale', 'price', 'user')
