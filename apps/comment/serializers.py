from rest_framework import serializers
from .models import  Comment, Rating
from ..accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)

    class Meta:
        model=Comment
        fields=['user', 'book', 'comment', 'created_at']
        read_only_fileds=['user', 'created_at']

        def get_likes_count(self, obj):
            return  obj.likes.count()

class RatingSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Rating 
        fields=['id', 'user', 'book', 'rating']  

    
