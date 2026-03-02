from .views import CommentViewSet, RatingViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('comments', CommentViewSet, basename='comments')
router.register('rating', RatingViewSet, basename='rating')
urlpatterns=router.urls