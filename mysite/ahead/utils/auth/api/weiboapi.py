# -*- coding: utf-8 -*-
from weibo import APIClient
from django.conf import settings

client = APIClient(app_key=settings.WEIBO['APP_KEY'], app_secret=settings.WEIBO['APP_SECRET'],
                    redirect_uri=settings.WEIBO['CALLBACK_URL'])


def get_authorize_url():
    return client.get_authorize_url()


def get_user_info(code):
    r = client.request_access_token(code)
    client.set_access_token(r.access_token, r.expires_in)
    return [client.users.show.get(uid=r.uid), r]


def send_weibo(access_token, expires_in, context):
    client.set_access_token(access_token, expires_in)
    return client.statuses.update.post(status=context)