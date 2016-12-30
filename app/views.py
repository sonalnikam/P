"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext
from datetime import datetime

def s(request):
    return HttpResponse("hello sonal")
