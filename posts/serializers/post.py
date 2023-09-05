from rest_framework import serializers
from ..models import Post
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  category = CategorySerializer()
  class Meta:
    model = Post
    fields = ('id', "title", "description", "image", "user", "category", "date")


class PostCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("title", "description", "image", "user", "category", "date")

class PostEditSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("title", "description", "image", "user", "category", "date")

