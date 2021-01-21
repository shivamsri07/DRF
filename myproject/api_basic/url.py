from django.urls import path, include
from .views import articlelist, articledetail, ArticleAPIView, ArticleDetailView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
urlpatterns = [

    path('viewsets/', include(router.urls)),
    # path('article/', articlelist),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', articledetail),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),    
]
