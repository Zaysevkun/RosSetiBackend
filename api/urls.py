from django.urls import path, include
from rest_framework import routers

from api import views
from .views import CustomAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'requests', views.RequestViewSet)
router.register(r'digital_categories', views.DigitalCategoriesViewSet)
router.register(r'messages', views.MessagesViewSet)

urlpatterns = [
    path('token', CustomAuthToken.as_view(), name='token'),
    path('requests/<int:request_pk>/comments', views.RequestCommentView.as_view()),
    path('questions_in_category/<int:category_pk>', views.QuestionsInCategoryView.as_view()),
    path('comments_on_question/<int:question_pk>', views.CommentsOnQuestionView.as_view()),
    path('messages/', views.MessageView.as_view()),
    path('pdf/', views.get_pdf_view),
    path('doc/', views.get_doc_view),
    path('send_email/<int:pk>', views.SendEmailToExpert.as_view()),
    path('', include(router.urls)),
]
