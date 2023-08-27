from django.shortcuts import render, HttpResponse
from core.models import Library, Book

l = Library()
def home(request):
    return render(request, 'home.html')

def book_list(request):
    context = {"context":l.book_list}
    return render(request,"book_list.html",context)

def book_register(request):
    return render(request,"book_register.html")

def book_created(request):
    isbn = request.POST.get("isbn")
    title = request.POST.get("title")
    year = request.POST.get("year")
    b = Book(isbn,title,year)

    response = l.add_book(b)
    context = {"context":response}
    return render(request,"book_created.html",context)

def book_delete(request):
    isbn = request.POST.get("isbn")
    response = l.delete_book(isbn)
    context = {"context":response}
    return render(request,"book_deleted.html",context)