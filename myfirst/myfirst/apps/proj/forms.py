from .models import Task
from django.forms import CharField, ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


        # fields = ["title1", "title2", "title3", "title4", "title5", "title6"]
        # widgets = {"title1": TextInput("form-control", "placeholder", "vvedite nazvanie")}
        # widgets = {"title2": TextInput("form-control", "placeholder", "vvedite nazvanie")}
        # widgets = {"title3": TextInput("form-control", "placeholder", "vvedite nazvanie")}
        # widgets = {"title4": TextInput("form-control", "placeholder", "vvedite nazvanie")}
        # widgets = {"title5": TextInput("form-control", "placeholder", "vvedite nazvanie")}
        # widgets = {"title6": TextInput("form-control", "placeholder", "vvedite nazvanie")}
    # name = CharField(
    #     label='Contact Name',
    #     required=True,
    # )
