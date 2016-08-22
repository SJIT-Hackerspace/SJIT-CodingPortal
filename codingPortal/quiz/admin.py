from django.contrib import admin
from .models import CSEQuestion,ITQuestion,EEEQuestion,ECEQuestion,MECHQuestion

# Register your models here.
admin.site.register(CSEQuestion)
admin.site.register(ITQuestion)
admin.site.register(EEEQuestion)
admin.site.register(ECEQuestion)
admin.site.register(MECHQuestion)

