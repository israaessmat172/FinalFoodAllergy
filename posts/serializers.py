from rest_framework import serializers
from .models import Post, Comment
from django.contrib.contenttypes.models import ContentType

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        # Check if the user is a doctor
        user = self.context['request'].user
        if user.is_doctor:
            validated_data['owner'] = user
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("Only doctors can create comments")

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = { 'likes':{'read_only':True}}


    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(pk=request.user.pk).exists()
        return False