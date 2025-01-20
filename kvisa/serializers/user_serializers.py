from rest_framework import serializers
from django.contrib.auth import get_user_model

from kvisa.constants import VISA_CHOICES
from kvisa.models.comment import Comment
from kvisa.models.post import Post
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'full_name',
            'phone_number',
            'nationality',
            'visa_type',
            'visa_expiry_date',
            'terms_agreed'
        ]


class PostSerializer(serializers.ModelSerializer):
    visa_type = serializers.MultipleChoiceField(choices=VISA_CHOICES)
    avg_rating = serializers.FloatField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

        read_only_fields = [
            'id',
            'created_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']
