# -*- coding: utf-8 -*-
from ..utils.lazy import *

def default(request):
    return render(request, "index.html", {})