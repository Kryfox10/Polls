from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

#dividers
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Formalities', {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]

# collapse class
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)