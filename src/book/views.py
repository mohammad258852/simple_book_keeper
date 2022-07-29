from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Book, BookInOrder,Order
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@login_required
def order(request, order_id):
    book_name = ''
    if 'book_name' in request.GET.keys():
        book_name = request.GET['book_name']
        all_books = get_matched_book(Book.objects.all(),book_name)
    else:
        all_books = Book.objects.all()

    order = Order.objects.get(id=order_id)
    order_books = order.bookinorder_set.all()

    total_price = get_total_price(order)

    template = loader.get_template('order.html')
    context = {
        'all_books' : all_books,
        'order_books' : order_books,
        'order_id' : order_id,
        'book_name' : book_name,
        'total_price' : total_price
    }
    return HttpResponse(template.render(context,request))

def get_total_price(order):
    books_in_order = order.bookinorder_set.all()
    cost = 0
    for book_in_order in books_in_order:
        book = book_in_order.book
        cost += book.price * book_in_order.count
    return cost


def get_matched_book(books ,book_name):
    res = []
    for book in books:
        if(book_matched(book,book_name)):
            res.append(book)

    return res

def book_matched(book, book_name):
    if book_name in book.name:
        return True
    if book_name in book.serial_number:
        return True
    return False

@login_required
def new_order(request):
    order = Order()
    order.save()
    return HttpResponseRedirect('order/{0}'.format(order.id))

@login_required
def add_book(request,order_id,book_id):
    order = Order.objects.get(id=order_id)
    book = Book.objects.get(serial_number=book_id)
    book_in_order = BookInOrder.objects.get_or_create(book=book,order=order)[0]
    book_in_order.count = book_in_order.count + 1
    book_in_order.save()
    return HttpResponseRedirect('/book/order/{0}'.format(order_id))

@login_required
def remove_book(request,order_id,book_id):
    order = Order.objects.get(id=order_id)
    book = Book.objects.get(serial_number=book_id)
    book_in_order = BookInOrder.objects.get(book=book,order=order)
    book_in_order.count = book_in_order.count - 1
    book_in_order.save()
    if book_in_order.count <= 0:
        book_in_order.delete()
    return HttpResponseRedirect('/book/order/{0}'.format(order_id))

@login_required
def finalize(request, order_id):
    total_price = 0
    if('total_price' in request.GET):
        total_price = int(request.GET['total_price'])

    order = Order.objects.get(id=order_id)

    order.total_price = total_price
    order.time = timezone.now()

    order.save()
    
    return HttpResponseRedirect('/book')
