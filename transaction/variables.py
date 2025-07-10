INVOICE_TYPE_CHOICE = (
    ("buy", "خرید"),
    ("sell", "فروش")
)


CREDIT_TYPE_CHOICE = (
    ("positive", "مثبت"),
    ("negative", "منفی")
)


SYSTEMATIC_CREDIT_REASON_CHOICE = (
    "ایجاد فاکتور جدید به شماره {}",
    "اپدیت فاکتور به شماره {}",
    "حذف فاکتور به شماره {}",
)

INVOICE_TABLE_FIELDS =  [
    'id', 'customer', 'invoice_type' ,'get_total_invoice_price',
]

CREDIT_TABLE_FIELDS = [
    'customer', 'invoice', 'credit_type', 'amount'
]