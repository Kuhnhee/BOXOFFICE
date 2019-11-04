from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Director, Movie, Comment
# from .forms import *

from IPython import embed #디버깅 용도. interative shell 튀어나온다
from django.http import Http404, HttpResponse, JsonResponse

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from itertools import chain

def index(request):
    return render(request, 'movies/index.html')