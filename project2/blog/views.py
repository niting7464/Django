from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_details(request, post_id):
    return HttpResponse(f"Post details : {post_id}")

def user_profile(request, user_name):
    return HttpResponse(f"User profile : {user_name}")

def post_by_year(request, year, month):
    return HttpResponse(f"Post by year : {year} and month : {month}")
def article_details(request, **kwargs):
    return HttpResponse(f"Article details : {kwargs}")