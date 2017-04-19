from django.shortcuts import render,render_to_response
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image,ImageDraw,ImageFont
from math import ceil
import random
import os
import sys
import io as cStringIO
from datetime import datetime,timedelta
import hashlib
from django.core.files.storage import default_storage
import json
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import *
from django.db import connection
from django.utils import timezone
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.utils.decorators import available_attrs
from django.views.decorators.http import require_http_methods
import urllib.parse
import urllib.request
import base64
from core.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(req):
    '''
    首页
    '''

    return render(req, 'web/index.html', locals())


def about(req):
    '''
    关于金雷
    '''

    return render(req, 'web/about.html', locals())


def product(req):
    '''
    关于金雷
    '''

    return render(req, 'web/product.html', locals())


def faclity(req):
    '''
    关于金雷
    '''

    return render(req, 'web/faclity.html', locals())


def jobs(req):
    '''
    关于金雷
    '''

    return render(req, 'web/jobs.html', locals())


def contact(req):
    '''
    关于金雷
    '''

    return render(req, 'web/contact.html', locals())


def about_sample(req):
    '''
    关于子页面
    '''

    return render(req, 'web/about_sample.html', locals())


def success(req):
    '''

    '''
    return render(req, 'web/success.html', locals())