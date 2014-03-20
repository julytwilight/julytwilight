# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.conf import settings

import time
from django.utils import timezone

from ..utils.lazy import *
from ..models import User, Account
from dreams.models import Dream


@login_required
def default(request):
    dreams = request.user.dream_set.order_by('-create_at')
    return render(request, "index.html", {'dreams': dreams})


def binding(request, type):
    request.session['next'] = request.GET.get('next', None)

    if type == 'weibo':
        from ..utils.auth.api.weiboapi import get_authorize_url
        return redirect(get_authorize_url())


def callback(request, type):
    # 获得登陆后跳转的页面
    next = request.session.pop('next')

    if type == 'weibo':
        if request.GET.get('error_code', None):
            return HttpResponse('error_code: %s' % request.GET['error_code'])

        if not request.GET.get('code', None):
            return HttpResponse('No code')

        from ..utils.auth.api.weiboapi import get_user_info
        info, token = get_user_info(request.GET['code'])

        try:
            account = Account.objects.get(link_type=type, link_account=info['id'])
        except Account.DoesNotExist:
            account = Account(link_type=type, link_account=info['id'])
            user = User()
        else:
            user = account.user
        finally:
            user.username = info['name']
            user.avatar = info['avatar_large']
            user.save()
            account.user = user
            account.avatar = info['avatar_large']
            account.avatar_large = info['avatar_hd']
            account.access_token = token['access_token']
            account.expires_in = token['expires_in']
            account.save()

        # 验证 登陆
        current_user = authenticate(user_id=user.id, access_token=account.access_token)
        login(request, current_user)

        return redirect(next if next else "dream:all")