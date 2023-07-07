from rest_framework import serializers
from .models import Post,WineKinds

class PostSerializer(serializers.ModelSerializer):
  class Meta:
      model = Post
      fields = (
          'id',
          'title',
          'description',
          'created_at'
      )
      read_only_fields = ('created_at',)

class WineKindsSerializer(serializers.ModelSerializer):
  class Meta:
      model = WineKinds
      fields = (
          'id',
          'name'
      )
      # read_only_fields = ('created_at',)