# -*- coding: utf-8 -*-
from ahead.utils.lazy import *

from ..models import Dream, Comment 


@login_required
def create(request, id):
    dream = get_object_or_404(Dream, id=id)
    
    text = request.POST.get('text', None)
    if not len(text):
        return HttpResponse('Please full content')
    Comment.objects.create(user=request.user, dream=dream, text=text)

    dream.comments = dream.comment_set.count()
    dream.save()

    return redirect('dream:show', id=id)