from rest_framework.serializers import ModelSerializer, CharField, EmailField, ValidationError, StringRelatedField
from .models import *
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('username', 'email', 'password', 'user_type')



class userProfileSerializer(ModelSerializer):
    # user=StringRelatedField(read_only=True)
    class Meta:
        model=User
        fields='__all__'


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username',)
      

# class RegistrationSerializer(ModelSerializer):
#     # password = serializers.CharField( write_only=True)

#     class Meta:
#         model = User
#         fields = ( 'username', 'email', 'password', 'user_type', )
      

    # def create(self, validated_data):
    #     user= get_user_model().objects.create(
    #         username= validated_data['username'],
    #         email = validated_data['email'],
    #         # password = validated_data['password'],
    #         user_type=validated_data['user_type'],
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     token = Token.objects.get(user=user).key
    #     return user

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username=CharField(required=False, allow_blank=True)
    email = EmailField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ( 'username', 'email', 'password', 'token')
    def validate(self, data):
        user_obj=None
        email=data.get('email', None)
        username=data.get('username', None)
        password = data.get('password')
        if not email and not username:
            raise ValidationError('A username or email is required to login')

        user= User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()

        if user.exists() and user.count() ==1:
            user_obj=user.first()

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError ('Incorect password please try again')

        data['token'] = 'random'

        return data



