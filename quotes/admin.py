from django.contrib import admin

from . models import quoteCategory
from . models import Quote

admin.site.register(quoteCategory)
admin.site.register(Quote)
