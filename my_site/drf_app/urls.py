from django.urls import include, path
from rest_framework import routers

from drf_app import views

"""
Lesson Django REST framework: part 1
"""

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
# router.register(r'publishers', views.PublisherViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Lesson Django REST framework: part 2
    path('publishers/', views.publishers_list),
    path('publishers/<int:publisher_id>', views.publisher_by_id),
    path('book_by_id/', views.get_book_by_id),
    path('book_create/', views.create_book)
]

urlpatterns += router.urls
print(urlpatterns)
