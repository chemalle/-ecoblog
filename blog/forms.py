from django import forms

from .models import Post, Comment, Document, Balance_Sheet, MyPlan, ECD01, Prediction, Stocks, employees, holerite

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm





class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text','image',)



        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),

        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class Statements(forms.ModelForm):
    class Meta:
        model = Balance_Sheet
        fields = ('description', 'document')



from django import forms

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)



class MyPlanForm(ModelForm):
     class Meta:
         model = MyPlan
         fields = ['Nome_da_Empresa', 'email', 'motivo','Contrato_Social', 'cnpj','lifetime','funcionarios','Nome_do_socio','cpf', 'tamanho','confirmacao_do_plano']


class ECD01FORM(ModelForm):
     class Meta:
         model = ECD01
         fields = ['REG', 'LECD', 'DT_INI','DT_FIN', 'Nome_da_Empresa','CNPJ','UF','IM','IN_SIT_ESP', 'IND_SIT_INI_PER','IND_NIRE',
                    'IND_FIN_ESC','COD_HASH_SUB','IND_GRANDE_PORTE', 'TIP_ECD','COD_SCP', 'IDENT_MF', 'IND_ESC_CONS']



class predictionFORM(ModelForm):
     class Meta:
         model = Prediction
         fields = ['CNPJ', 'Nome_da_Empresa', 'email','Seu_nome', 'Seu_cargo','Segmento','Faturamento_Ultimo_Mes',
         'Faturamento_Penultimo_Mes','Faturamento_Antepenultimo_mes', 'Despesas_Ultimo_Mes','Despesas_Penultimo_Mes',
         'Despesas_Antepenultimo_Mes']


class stocksFORM(ModelForm):
     class Meta:
         model = Stocks
         fields = '__all__'


class employeesFORM(ModelForm):
     class Meta:
         model = employees
         fields = '__all__'



class holeriteFORM(ModelForm):
     class Meta:
         model = holerite
         fields = '__all__'
