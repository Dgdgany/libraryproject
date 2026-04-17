from django.shortcuts import render
from .models import Book
from django.db.models import Q

def add_test_books(request):
    Book.objects.create(title='Harry Potter', author='J. K. Rowling', price=120.00, edition=3)
    Book.objects.create(title='DUNE', author='Frank Herbert', price=97.00, edition=2)
    Book.objects.create(title='Alice in Wonderland', author='Lewis Carroll', price=100.00, edition=4)
    return render(request, 'bookmodule/index.html', {'msg': '3 Books added successfully to the database!'})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
   
def lookup_query(request):
    books = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2)

    return render(request, 'bookmodule/bookList.html', {'books': books})

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Harry Potter', 'author': 'J. K. Rowling'}
    book2 = {'id': 56788765, 'title': 'DUNE', 'author': 'Frank Herbert'}
    book3 = {'id': 43211234, 'title': 'Alice in Wonderland', 'author': 'Lewis Carroll'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        
        
       
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and string in item['author'].lower(): 
                contained = True
            
            if contained: 
                newBooks.append(item)
        
        return render(request, 'bookmodule/search.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def links(request):
    return render(request, 'bookmodule/links.html')