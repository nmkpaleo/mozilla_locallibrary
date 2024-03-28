import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    author__first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name contains')
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'author__first_name', 'genre', 'language']
    
class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']