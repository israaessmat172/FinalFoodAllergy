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

# class LikeSerializer(serializers.ModelSerializer):
#     # user = serializers.ReadOnlyField(source='user.username')

#     # def create(self, validated_data):
#     #     validated_data['user_type'] = ContentType.objects.get_for_model(self.context['request'].user).pk
#     #     validated_data['user_id'] = self.context['request'].user.pk
#     #     return super().create(validated_data)

    # class Meta:
    #     model = Like
    #     fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = { 'likes':{'read_only':True}}

