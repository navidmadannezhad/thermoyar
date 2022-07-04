from django.contrib import admin
from .models import state, material, superheat, sub_cold, saturate

admin.site.register(state)
admin.site.register(material)
admin.site.register(superheat)
admin.site.register(sub_cold)
admin.site.register(saturate)

