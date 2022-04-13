from django.contrib import admin
from library.models import Book, Borrowing, Reader

admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Reader)

admin.site.name = '图书馆信息管理'
admin.site.site_header = '图书馆信息管理'
