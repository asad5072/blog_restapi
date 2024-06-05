from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'post': serializer.data})