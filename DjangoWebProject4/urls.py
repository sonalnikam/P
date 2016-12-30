"""
Definition of urls for DjangoWebProject4.
"""

from datetime import datetime
from django.conf.urls import url,include
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
	url(r'^',include("app.urls")),

        ]