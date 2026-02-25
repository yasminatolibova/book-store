from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions, status
from .models import Comment, CommentLike
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



class CommentViewSet(viewsets.ModelViewSet):
    
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        queryset=Comment.objects.all()
        book_id=self.request.query_params.get('book')

        if book_id:
            queryset=queryset.filter(book_id=book_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, obj, request):
        comment=self.get_object()
        user=request.user
        like, created_at=CommentLike.objects.get_or_create(user=user, comment=comment)

        if not created:
            like.delete()
            return Response({
                'status': 'unliked'
            }, status=status.HTTP_200_OK
            )
        return Response({
            'status': 'liked'
        }, status=status.HTTP_201_CREATED
        )
    



