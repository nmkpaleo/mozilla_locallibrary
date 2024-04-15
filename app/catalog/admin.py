from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Author, Genre, Book, BookInstance, Language



admin.site.register(Genre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

    def display_genre(self, obj):
        return ', '.join(genre.name for genre in obj.genre.all())

    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(ImportExportModelAdmin):
    list_display = ('book_title', 'status', 'borrower', 'due_back', 'id')
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
