from rest_framework import serializers
from pages.models import Page


class PageSerializer(serializers.ModelSerializer):
    """Serializer for Page object"""

    class Meta:
        model = Page
        fields = ('id', 'title', 'avatar', 'content', 'created', 'updated', 'created_by', 'is_approved')
        read_only_Fields = ('id',)
