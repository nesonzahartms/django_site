from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello),
    path('books', views.get_all_books),
    path('stores', views.get_all_stores),
    path('stores_expensive_books', views.get_stores_with_expensive_books),
    path('publishers', views.get_all_publishers),
    path('publishers_expensive_books', views.get_publishers_with_expensive_books),
    path('books/<book_id>', views.get_book_by_id),
    path('expensive_books', views.get_expensive_books),
    path('all_authors', views.get_all_authors),
    path('authors_with_expensive_books', views.get_authors_with_expensive_books),
    path('publisher_by_id', views.get_publisher_by_id),
    path('store_by_id', views.get_store_by_id),
    path('author_by_id', views.get_author_by_id),
    path('hello_v2', views.hello_v2),
    path('first_three_books', views.get_first_three_books),
    path('all_books_v2', views.get_all_books_v2),
    path('only_books_with_authors', views.get_only_books_with_authors),
    path('use_form', views.get_use_form),
    path('user/save', views.add_user),
    path('create_publisher', views.add_publisher),
    path('create_book', views.add_book)
]