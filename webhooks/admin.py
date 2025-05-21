from django.contrib import admin

from .models import Webhooks


class WebhooksAdmin(admin.ModelAdmin):
    list_display = ["id", "event_type", "event"]


admin.site.register(Webhooks, WebhooksAdmin)
