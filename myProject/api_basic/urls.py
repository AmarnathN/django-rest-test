from django.urls import path
from .views import ArticleAPIView,ArticleDetailsAPIView,GenericAPIView

urlpatterns = [
    # path('article/', article_list),
    # path('article/<int:pk>/', article_detail)

    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetailsAPIView.as_view()),
    path('generic/article/<int:id>/',GenericAPIView.as_view())
    
]