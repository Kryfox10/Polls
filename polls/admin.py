from django.contrib import admin
from polls.models import Choice, Poll

#dividers
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Formalities', {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]

# collapse class
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#
#admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
#

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)