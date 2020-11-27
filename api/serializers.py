from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer

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
