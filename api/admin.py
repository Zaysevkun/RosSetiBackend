from django.contrib import admin

from api.models import User, Category, Question, Comment, Request, Messages, RequestComment, Expert

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Request)
admin.site.register(User)
admin.site.register(Messages)
admin.site.register(RequestComment)
admin.site.register(Expert)
