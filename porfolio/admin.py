from django.contrib import admin
from porfolio.models import cliente

class clienteAdmin(admin.ModelAdmin):
    class Meta:
        model = cliente

admin.site.register(cliente, clienteAdmin)