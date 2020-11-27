from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Category, Question, Comment, Request, Expenses, Stage, Reward, DigitalCategory

from config import settings

User = get_user_model()


class CustomAuthTokenSerializer(AuthTokenSerializer):
    username = None
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'position', 'department', 'education',
                  'date_of_birth', 'experience')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('pk', 'name', 'description', 'author', 'category', 'ask_date')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('pk', 'name', 'description')

    # def get_comments(self, obj):
    #     return


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text', 'author', 'question')


class DigitalCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalCategory
        fields = "__all__"


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = "__all__"


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    expenses = ExpensesSerializer(many=True)
    stages = StageSerializer(many=True)
    rewards = RewardSerializer(many=True)
    
    class Meta:
        model = Request
        fields = ('title', 'is_digital_categories', 'digital_categories', 'description',
                  'characteristic', 'expenses', 'stages', 'expectations', 'authors', 'rewards',
                  'is_saving_money')

    def create(self, validated_data):
        digital_categories_ids = validated_data.pop('digital_categories', [])
        expenses_data = validated_data.pop('expenses', [])
        expense_ids = []
        for expense_data in expenses_data:
            expense = Expenses.objects.create(name=expense_data['name'], cost=expense_data['cost'])
            expense_ids.append(expense.id)
        stages_data = validated_data.pop('stages', [])
        stages_ids = []
        for stage_data in stages_data:
            stage = Stage.objects.create(name=stage_data['name'],
                                         count_of_days=stage_data['count_of_days'])
            stages_ids.append(stage.id)
        authors_ids = validated_data.pop('authors', [])
        rewards_data = validated_data.pop('rewards', [])
        rewards_ids = []
        for reward_data in rewards_data:
            date = rewards_data.get('date')
            reward = Reward.objects.create(
                author=reward_data['author'],
                percentage=reward_data['percentage'],
                date=date
            )
            rewards_ids.append(reward.id)
        request = Request.objects.create(**validated_data)
        request.digital_categories.add(*digital_categories_ids)
        request.expenses.add(*expense_ids)
        request.stages.add(*stages_ids)
        request.authors.add(*authors_ids)
        request.rewards.add(*rewards_ids)
        request.authors.add(*authors_ids)
        return request
