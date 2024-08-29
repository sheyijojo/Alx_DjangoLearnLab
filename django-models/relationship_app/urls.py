from django.urls import path
from .views import list_all_books_in_database, LibraryDisplayView

urlpatterns = [
    path('books/', list_all_books_in_database, name='list_books'),
    path('libraries/',LibraryDisplayView.get_template_names, name="library_view" )
]