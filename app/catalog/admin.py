from django.contrib import admin
from import_export.admin import ImportExportModelAdmin   # Import the  class
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)


admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    #Defines format of inline book insertion (used in AuthorAdmin)"""

    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):# Use ImportExportModelAdmin instead of ModelAdmin
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

    def display_genre(self, obj):
        return ', '.join(genre.name for genre in obj.genre.all())

    display_genre.short_description = 'Genre'

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(ImportExportModelAdmin):# Use ImportExportModelAdmin instead of ModelAdmin
    list_display = ('book_title', 'status', 'borrower', 'due_back', 'id')#use book_title instead of book
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

    def book_title(self, obj):
        return obj.book.title

    book_title.short_description = 'Book Title'
