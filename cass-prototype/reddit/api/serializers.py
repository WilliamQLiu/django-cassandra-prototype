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

    def update(self, instance, validated_data):
        # import pdb
        # pdb.set_trace()

        # instance.blog_id = validated_data.get('blog_id', instance.blog_id)
        # instance.created_at = validated_data.get('created_at', instance.created_at)
        # instance.user = validated_data.get('user', instance.user)
        # instance.description = validated_data.get('description', instance.description)
        # return instance


        # raise_errors_on_nested_writes('update', self, validated_data)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


