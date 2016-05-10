from django.db.models.query import QuerySet

from rest_framework import generics
from rest_framework import exceptions
from cassandra.cqlengine import ValidationError

from .serializers import BlogSerializer
from ..models import Blog


class BlogListCreate(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get_queryset(self):
        """
        Need to explicitly define get_queryset for Cassandra to find
        """
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer

    def get_object(self):
        """
        Example: /api/reddit/blog/fdd0ba00-13b2-11e6-88a9-0002a5d5c51e/
        Assuming a uuid = fdd0ba00-13b2-11e6-88a9-0002a5d5c51e
        """
        try:
            blog_obj = Blog.objects.get(blog_id=self.kwargs['uuid'])
            return blog_obj
        except ValidationError:
            raise exceptions.NotFound("No Blog found with this uuid")
