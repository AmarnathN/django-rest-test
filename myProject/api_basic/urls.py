from django.urls import path,include
from .views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')


urlpatterns = [
    # path('article/', article_list),
    # path('article/<int:pk>/', article_detail)

    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetailsAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/',include(router.urls))
    
]