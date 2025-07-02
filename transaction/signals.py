from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from user.middleware import get_current_user
from .models import Invoice, Credit, InvoiceItem
from .variables import SYSTEMATIC_CREDIT_REASON_CHOICE, CREDIT_TYPE_CHOICE, INVOICE_TYPE_CHOICE


@receiver(post_delete, sender=InvoiceItem)
@receiver(post_save, sender=InvoiceItem)
def create_credit(sender, instance, **kwargs):
    current_user = get_current_user()
    if instance.invoice.invoice_type == INVOICE_TYPE_CHOICE[1][0]:
        if kwargs.get('created', False):
            Credit.objects.create(
                customer=instance.invoice.customer,
                invoice=instance.invoice,
                credit_type=CREDIT_TYPE_CHOICE[1][0], # negative
                amount=instance.invoice.calculate_invoice_total_price,
                reason=SYSTEMATIC_CREDIT_REASON_CHOICE[0].format(instance.id),
                created_by=current_user,
                updated_by=current_user,
            )
        else:
            try:
                credit = Credit.objects.get(invoice=instance.invoice)
                credit.amount = instance.invoice.calculate_invoice_total_price
                credit.reason = SYSTEMATIC_CREDIT_REASON_CHOICE[1].format(instance.id)
                credit.updated_by = current_user
                credit.created_by = current_user
                credit.save()
            except Credit.DoesNotExist:
                Credit.objects.create(
                    customer=instance.invoice.customer,
                    invoice=instance.invoice,
                    credit_type=CREDIT_TYPE_CHOICE[1][0],  # negative
                    amount=instance.invoice.calculate_invoice_total_price,
                    reason=SYSTEMATIC_CREDIT_REASON_CHOICE[0].format(instance.id),
                    created_by=current_user,
                    updated_by=current_user,
                )