# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from ahead.models import Account

class WeiboOAuth2(object):

    def authenticate(self, user_id=None, access_token=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = self.get_user(user_id)
            if Account.objects.get(user=user, access_token=access_token):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)
        except Account.DoesNotExist:
            pass


    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None