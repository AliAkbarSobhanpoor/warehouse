import django_tables2 as tables

class RowNumberColumn(tables.Column):
    def render(self, value, **kwargs):
        bound_row = kwargs.get("bound_row")
        return bound_row.row_counter + 1

class BaseTable(tables.Table):
    row_number = RowNumberColumn(empty_values=(),verbose_name="شماره ردیف", orderable=False)
    operations = tables.Column(empty_values=(), verbose_name="عملیات", orderable=False)
    created_at_by = tables.Column(empty_values=(), verbose_name="تاریخ ایجاد / ایجاد کننده", orderable=False)
    updated_at_by = tables.Column(empty_values=(), verbose_name="تاریخ ویرایش / ویرایش کننده", orderable=False)

    def render_created_at_by(self, value, **kwargs):
        record = kwargs.get("record")
        return f"""
            {record.created_at.strftime("%Y-%m-%d %H:%M:%S")} , {record.created_by}
        """

    def render_updated_at_by(self, value, **kwargs):
        record = kwargs.get("record")
        return f"""
            {record.updated_at.strftime("%Y-%m-%d %H:%M:%S")} , {record.updated_by}
        """