from django import forms
from .models import Document

class Upload_data(forms.ModelForm):
    class Meta:
        model= Document
        fields= ('Excel_file','ChromePath','ColumnName','ImagePath','No_of_models')