from django.shortcuts import render
from django.views import View
from .models import Book

class BooksListView(View):
    def get(self,request):
        search = request.GET.get('search')
        if not search:
            books = Book.objects.all()
            context = {'books': books ,'search':search}
            return render(request, 'library.html', context)
        else:
            books = Book.objects.filter(title__icontains=search)
            if books:
                context = {'books': books, 'search':search}
                return render(request, 'library.html', context)
            else:
                return render(request, 'not_found_page.html')






class BooksDetailView(View):
    def get(self,request,id):
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request,'bookdetail.html',context)