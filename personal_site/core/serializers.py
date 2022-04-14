import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Skill, Feedback


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'id', 'name', 'slug', 'description', 'time_create',
            'time_update', 'is_published', 'it_area', 'work')
        read_only_fields = ['user', ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'time_create', 'time_update', 'description',
                  'category', 'age_confirmation', 'content', 'user',)
        read_only_fields = ['user', ]

    def validate_description(self, description):
        cyrillic = re.compile('[а-яА-Я]')
        if bool(re.search(cyrillic, description)):
            raise ValidationError('Description must not contain cyrillic symbols')
        return description

    def validate(self, attrs):
        if attrs['age_confirmation'] is not True:
            raise ValidationError('Age confirmation must be True')
        return attrs
