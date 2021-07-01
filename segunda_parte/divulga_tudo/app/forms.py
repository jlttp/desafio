from django import forms

class DateInput(forms.DateInput):
    input_type = "date";

class AnunciosForm(forms.Form):
    nome_anuncio = forms.CharField(label="Nome do anúncio", widget=forms.TextInput(attrs={"placeholder": "Nome do anúncio"}));
    nome_cliente = forms.CharField(label="Nome de cliente", widget=forms.TextInput(attrs={"placeholder": "Nome do cliente"}));
    data_inicio = forms.DateField(widget=DateInput);
    data_fim = forms.DateField(widget=DateInput);
    investimento_dia = forms.DecimalField(initial="1.00", decimal_places=2);