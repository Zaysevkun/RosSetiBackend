from django.urls import path, include
from rest_framework import routers

from api import views
from .views import CustomAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'requests', views.RequestViewSet)
router.register(r'digital_categories', views.DigitalCategoriesViewSet)

urlpatterns = [
    path('token', CustomAuthToken.as_view(), name='token'),
    path('questions_in_category/<int:category_pk>', views.QuestionsInCategoryView.as_view()),
    path('comments_on_question/<int:question_pk>', views.CommentsOnQuestionView.as_view()),
    path('', include(router.urls)),
]
