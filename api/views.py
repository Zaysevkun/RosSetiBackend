import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.schemas import ManualSchema

from api.models import User, Category, Question, Comment, Request, DigitalCategory, Chat, Messages
from api.models import User, Category, Question, Comment, Request, DigitalCategory, RequestComment
from api.serializers import (CustomAuthTokenSerializer, UserInfoSerializer, CategorySerializer,
                             QuestionSerializer, CommentSerializer, RequestSerializer,
                             DigitalCategorySerializer, ChatSerializer, MessagesSerializer,
                             DigitalCategorySerializer, RequestCommentSerializer)
from config.settings import STATIC_ROOT


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-last_name')
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionsInCategoryView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        category_pk = self.kwargs['category_pk']
        return Question.objects.filter(category_id=category_pk)


class CommentsOnQuestionView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        question_pk = self.kwargs['question_pk']
        return Comment.objects.filter(question_id=question_pk)


class DigitalCategoriesViewSet(viewsets.ModelViewSet):
    queryset = DigitalCategory.objects.all()
    serializer_class = DigitalCategorySerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessagesInChatView(generics.ListAPIView):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        user1_pk = self.kwargs['user1_pk']
        user2_pk = self.kwargs['user2_pk']
        return Messages.objects.filter(chat__user1_id=user1_pk, chat__user2_id=user2_pk)


class RequestCommentView(generics.CreateAPIView):
    queryset = RequestComment.objects.all()
    serializer_class = RequestCommentSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


def get_pdf_view(request):
    output_filename = os.path.join(STATIC_ROOT, 'pdf/temp.pdf')
    with open(output_filename, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read())
        response['Content-Type'] = 'mimetype/submimetype'
        response['Content-Disposition'] = 'attachment; filename=temp.pdf'
    return response


def get_doc_view(request):
    output_filename = os.path.join(STATIC_ROOT, 'doc/temp.doc')
    with open(output_filename, 'rb') as doc_file:
        response = HttpResponse(doc_file.read())
        response['Content-Type'] = 'mimetype/submimetype'
        response['Content-Disposition'] = 'attachment; filename=temp.doc'
    return response
