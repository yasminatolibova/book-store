from rest_framework import serializers
from .models import  Comment
from ..accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)

    class Meta:
        model=Comment
        fields=['user', 'book', 'comment', 'rating', 'created_at']
        read_only_fileds=['user', 'created_at']

        def validate_rating(self, value):
            if not 1<=value<=5:
                raise serializers.ValidationError("Rating should be between 1 to 5")
            return value
        
        def get_likes_count(self, obj):
            return  obj.likes.count()

        

