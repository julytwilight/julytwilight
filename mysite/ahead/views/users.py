# -*- coding: utf-8 -*-
from ..utils.lazy import *
from ..models import User
from dreams.models import Dream

def show(request, id):
    user = get_object_or_404(User, id=id)
    dreams = user.dream_set.order_by('-create_at')
    return render(request, "users/show.html", {'user': user, 'dreams': dreams})