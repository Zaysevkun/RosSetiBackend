from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from api.models import User, Category, Question, Comment, Request


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name')
    search_fields = ('email', 'full_name')
    ordering = ('email',)


admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Request)
