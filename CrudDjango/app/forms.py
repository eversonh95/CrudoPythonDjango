from django.forms import ModelForm
from app.models import Carros #nome do seu app e da classe do banco de dados

#create the form class,
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']