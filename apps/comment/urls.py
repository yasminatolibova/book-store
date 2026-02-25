from .views import CommentViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('comments', CommentViewSet, basename='comments')
urlpatterns=router.urls