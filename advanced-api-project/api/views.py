from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import mixins
from .forms import BookForm


class BookListView(generics.ListAPIView):
    '''for retrieving all books.'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    '''for retrieving a single book by ID.'''
    serializer_class = BookSerializer

    def get_object(self):
        obj = Book.objects.get(pk=self.kwargs['ID']) #retrieve a book instance by its ID
        return obj 
    
class BookCreateView(generics.CreateAPIView):
    '''for adding a new book'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_book(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                return 'OK'

class BookUpdateView(mixins.UpdateModelMixin, 
                     generics.GenericAPIView):
    '''for modifying an existing book.'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)
    
    def get_book(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                return 'OK'
    
class BookDeleteView(mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    '''for removing a book.'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)