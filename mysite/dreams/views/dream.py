# -*- coding: utf-8 -*-
from django.utils import timezone

import json
from weibo import APIError

from ..models import Dream
from ahead.utils.lazy import *
from ahead.utils.auth.api.weiboapi import send_weibo


def index(request):
    dreams = Dream.objects.filter(private=0).order_by('-create_at')
    return render(request, "dreams/index.html", {'dreams': dreams})


@csrf_exempt
@login_required
def create(request):
    if request.method != 'POST' and not request.is_ajax():
        return HttpResponse(json.dumps({'error': 1, 'info': 'fuck u~.~'}))

    # One Day One Dream
    if Dream.objects.filter(user=request.user, date=timezone.now().date()).first():
        return HttpResponse(json.dumps({'error': 1, 'info': '您今天已经记过梦了'}))

    if request.method == 'POST':
        text = request.POST.get('text', None)
        private = True if request.POST.get('private', None) else False
        weibo = True if request.POST.get('weibo', None) else False
        if not len(text):
            return HttpResponse(json.dumps({'error': 1, 'info': '请输入内容'}))

        dream = Dream.objects.create(user=request.user, text=text, private=private)

        # sync to weibo
        if weibo and not private:
            url = ' http://julytwilight.com/dream/%d/' % dream.id  # 微博链接url
            max_length = 140 * 2 - len(url)  # 微博字数 * 2 - url字数
            counter = 0 
            weibo_text = ''

            text = request.POST.get('text', None).strip()
            for i in text:
                if ord(i) < 128:
                    counter += 1
                else:
                    counter += 2

                if counter > max_length:
                    break
                
                weibo_text += i
            weibo_text += url

            account = request.user.account_set.all()[0]
            try:
                send_weibo(account.access_token, account.expires_in, weibo_text)
            except APIError, e:
                pass
        # request.user.dreams = request.user.dream_set.count()
        # request.user.save()

        return HttpResponse(json.dumps({'error': 0}))


def show(request, id):
    dream = get_object_or_404(Dream, id=id, private=0)
    return render(request, "dreams/show.html", {'dream': dream})