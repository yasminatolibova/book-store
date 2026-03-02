from django.db import models

# Create your models here.


from ..book.models import Book
from django.conf import settings
from ..accounts.models import User


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    comment=models.TextField(blank=True, null=True)
    
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
        unique_together=['book', 'user']

    def __str__(self):
        return f"{self.user.username}"
    

class CommentLike(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='rating')
    rating=models.PositiveSmallIntegerField(default=0, choices=[(i,f"{i} yulduz") for i in range(1, 6)])

    class Meta:
        unique_together=['user', 'rating']

    def __str__(self):
        return f"{self.book}"