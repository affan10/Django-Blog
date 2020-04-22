from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class SignupSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model  = User
        fields = ('username', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True} # Security feature
        }

    # Overriding the save method to provide functionality of password confirmation
    def save(self):
        user = User(
            username=self.validated_data['username']
        )

        pass1 = self.validated_data['password']
        pass2 = self.validated_data['confirm_password']

        if pass1 != pass2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        user.set_password(pass1) # Defined inside lib/python3.6/site-packages/django/contrib/auth/models.py
        user.save()
        return user


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)