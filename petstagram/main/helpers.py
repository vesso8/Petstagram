from petstagram.main.models import Profile



def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

class BootstrapFormMixin:
    fields = {}
    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class DisabledFieldsForMixin:
    fields = {}
    disabled_fields = '__all__'
    def _init_disabled_fields(self):
        for name , field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'
