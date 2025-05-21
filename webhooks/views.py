import json

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import response, status, views
from services.callmebot import CallMeBot

from .messages import outflow_message
from .models import Webhooks


class WebhooksOrderView(views.APIView):
    def post(self, request):
        data = request.data

        Webhooks.objects.create(
            event_type=data.get("event_type"),
            event=json.dumps(data, ensure_ascii=False),
        )

        product_name = data.get("product")
        quantity = data.get("quantity")
        product_cost_price = data.get("product_cost_price")
        product_selling_price = data.get("product_selling_price")
        total_value = product_selling_price * quantity
        profit_value = total_value - (product_cost_price * quantity)

        message = outflow_message.format(
            product_name,
            quantity,
            total_value,
            profit_value,
        )

        callmebot = CallMeBot()
        callmebot.send_message(message)

        data["total_value"] = total_value
        data["profit_value"] = profit_value

        send_mail(
            subject="Nova Saída (SGE)",
            message="",
            from_email=f"SGE <{settings.EMAIL_HOST_USER}>",
            recipient_list=[settings.EMAIL_ADMIN_RECEIVER],
            fail_silently=False,
            html_message=render_to_string(template_name="outflow.html", context=data),
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
