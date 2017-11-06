from django import forms


from .models import UserPersonalModel, UserFinancialModel


class PersonalForm(forms.ModelForm):
    name = forms.CharField(max_length=25, label="", widget=forms.TextInput(
        attrs={"placeholder": "Nombre"}))
    apellidos = forms.CharField(max_length=50, label="", widget=forms.TextInput(
        attrs={"placeholder": "Apellidos"}))
    dni = forms.CharField(max_length=9, label="", widget=forms.TextInput(
        attrs={"placeholder": "DNI"}))
    nacimiento = forms.DateField(label="", widget=forms.DateInput(
        attrs={"placeholder": "Nacimiento (mm/dd/yyyy)"}))

    class Meta:
        model = UserPersonalModel
        fields = [
            "name",
            "apellidos",
            "dni",
            "nacimiento"
        ]


class FinancialForm(forms.ModelForm):
    titular = forms.CharField(max_length=80, label="", widget=forms.TextInput(
        attrs={"placeholder": "Titular de la Tarjeta"}))
    caducidad = forms.DateField(label="", widget=forms.DateInput(
        attrs={"placeholder": "Caducidad (mm/dd/yyyy)"}))
    codigo_cvv = forms.IntegerField(label="", widget=forms.TextInput(
        attrs={"placeholder": "Codigo CVV"}))
    numero_tarjeta = forms.IntegerField(label="", widget=forms.TextInput(
        attrs={"placeholder": "N.º de tarjeta"}))
    direccion = forms.CharField(max_length=80, label="", widget=forms.TextInput(
        attrs={"placeholder": "Dirección"}))
    ciudad = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={"placeholder": "Ciudad"}))
    provincia = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={"placeholder": "Provincia"}))
    codigo_postal = forms.IntegerField(label="", widget=forms.TextInput(
        attrs={"placeholder": "Código postal"}))

    class Meta:
        model = UserFinancialModel
        fields = [
            "titular",
            "caducidad",
            "codigo_cvv",
            "numero_tarjeta",
            "direccion",
            "ciudad",
            "provincia",
            "codigo_postal",
        ]
