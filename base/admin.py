from django.contrib import admin

# Register your models here.

class BaseModelAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form_class = super().get_form(request, obj, **kwargs)
        class FormWithUser(form_class):
            def __init__(self, *args, **kwargs):
                kwargs['user'] = request.user
                super().__init__(*args, **kwargs)

        return FormWithUser