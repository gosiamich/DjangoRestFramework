from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet,basename="authors")
router.register(r'books_api', views.BookViewSet,basename="books_api")

urlpatterns = [
    path('generic_list_book/', views.GenericBookList.as_view()),
    path('generic_detail_book/<int:pk>/', views.GenericBookDetail.as_view()),
    path('', include(router.urls)),
]



