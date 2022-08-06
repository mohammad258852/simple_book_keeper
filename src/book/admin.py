from django.contrib import admin

from .models import Book, BookInOrder,Order

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','price_discount','serial_number')
    search_fields = ['name' , 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('time' , 'total_price')

admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(BookInOrder)