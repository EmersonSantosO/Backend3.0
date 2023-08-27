from django.shortcuts import render, HttpResponse
from core.models import Library, Book

l = Library()
def home(request):
    return render(request, 'home.html')

def book_list(request):
    context = {"context":l.book_list}
    return render(request,"book_list.html",context)