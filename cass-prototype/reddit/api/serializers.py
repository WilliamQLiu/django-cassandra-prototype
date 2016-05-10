from reddit.models import Blog

from rest_framework import serializers


class BlogSerializer(serializers.Serializer):
    blog_id = serializers.UUIDField()
    created_at = serializers.DateTimeField()
    user = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        # Taken from: http://www.cdrf.co/3.3/rest_framework.serializers/ModelSerializer.html
        return Blog.objects.create(**validated_data)

    def _validate_created_at(self, validated_data):
        """
        Cassandra creates a timezone unaware DateTime while DRF automatically
        sets the timezone to UTC. We clean the data by removing the UTC
        """
        validated_data['created_at'] = validated_data['created_at'].replace(tzinfo=None)
        return validated_data

    def update(self, instance, validated_data):
        if validated_data.get('created_at', None):
            validated_data = self._validate_created_at(validated_data)  # Clean data

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
