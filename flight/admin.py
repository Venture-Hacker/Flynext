from django.contrib import admin
from .models import *
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Place)
admin.site.register(Week)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Ticket)