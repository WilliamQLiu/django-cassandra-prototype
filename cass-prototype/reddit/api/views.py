from django.shortcuts import get_object_or_404

from rest_framework import generics

from .serializers import BlogSerializer
from ..models import Blog


class BlogListCreate(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer

    def get_object(self):
        blog_obj = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return blog_obj
