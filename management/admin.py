from django.contrib import admin
from .models import *
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Reviews)