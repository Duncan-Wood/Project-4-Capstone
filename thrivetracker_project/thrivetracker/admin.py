from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserAddiction)
admin.site.register(TimeTracker)
admin.site.register(Note)
admin.site.register(Saving)
admin.site.register(Token)


## Meant to work on After GA! IGNORE FOR NOW!!

# admin.site.register(UserProfile)
# admin.site.register(Step)
# admin.site.register(UserStep)
