from django import forms


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(BaseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            if not instance.pk:
                instance.created_by = self.user
            instance.updated_by = self.user
        if commit:
            instance.save()

        return instance