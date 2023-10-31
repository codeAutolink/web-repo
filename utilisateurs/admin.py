from django.contrib import admin

# Register your models here.
from .models import Token, Scenario, SSHKey
admin.site.register(Token)
admin.site.register(Scenario)

@admin.register(SSHKey)
class SSHKeyAdmin(admin.ModelAdmin):
    list_display = ['key', 'username', 'ip', 'port']
    list_display = ['username', 'ip', 'port']
    search_fields = ['username', 'ip']