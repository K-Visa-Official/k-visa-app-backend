from rest_framework import serializers
from django.contrib.auth import get_user_model

from kvisa.constants import VISA_CHOICES
from kvisa.models.post import Post
User = get_user_model()


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
        ]
        read_only_fields = [
            'id',
            'is_admin',
        ]


class PostAdminSerializer(serializers.ModelSerializer):
    visa_type = serializers.MultipleChoiceField(choices=VISA_CHOICES)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = [
            'id',
            'created_at',
        ]
