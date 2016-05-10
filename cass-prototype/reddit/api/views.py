from django.db.models.query import QuerySet

from rest_framework import generics, exceptions
from rest_framework.response import Response
from cassandra.cqlengine import ValidationError
from cassandra.cqlengine.query import DoesNotExist

from .serializers import BlogSerializer, UserSerializer
from ..models import Blog, User


class BlogListCreate(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get_queryset(self):
        """
        GET a list of Blogs
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
        GET on a single Blog
        Example: /api/reddit/blog/fdd0ba00-13b2-11e6-88a9-0002a5d5c51e/
        Assuming a uuid = fdd0ba00-13b2-11e6-88a9-0002a5d5c51e
        """
        try:
            return Blog.objects.get(blog_id=self.kwargs['uuid'])
        except (ValidationError, DoesNotExist):
            raise exceptions.NotFound("No Blog found with this uuid")

    def update(self, request, *args, **kwargs):
        """
        PUT on a single Blog
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset
