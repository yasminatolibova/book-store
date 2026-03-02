from django.contrib import admin

# Register your models here.
from .models import Comment, CommentLike, Rating
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Rating)