from django.contrib import admin
from .models import Subscriber, NewsletterContent
# Register your models here.


class NewsletterContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    ordering = ('-date',)


admin.site.register(Subscriber)
admin.site.register(NewsletterContent, NewsletterContentAdmin)
