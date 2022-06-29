import logging

from rest_framework import serializers

from .models import Post, Rate


class PostsSerializer(serializers.ModelSerializer):
    """Serializer for post model"""

    class Meta:
        model = Post
        fields = ['title', 'rating_average', 'rating_count', ]


class RateSerializer(serializers.ModelSerializer):
    """Serializer for rate model"""

    class Meta:
        model = Rate
        fields = '__all__'

    def create(self, validated_data):
        """Overriding create method to create or update rate model"""
        try:  # update rate model
            rate = Rate.objects.get(user=validated_data.get(
                'user', None), post=validated_data.get('post', None))
            logging.info(f'Duplicate rate was found with post: {rate.post.title} user: {rate.user.username}')
            rate.rate = validated_data.get('rate', None)
            rate.save()
            logging.info(f"Rate updated to {validated_data.get('rate', None)}")
            return rate
        except Rate.DoesNotExist:  # create rate model
            logging.info("New rate created")
            return super().create(validated_data)
