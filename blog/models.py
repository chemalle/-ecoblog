from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django import forms
from django_pandas.managers import DataFrameManager




CHOICES = (
    ('media', 'media'),
    ('pequena','pequena'),
)


PLANOS = (
    ('STARTUP', 'Startup, apenas R$ 49,90 mensais!'),
    ('Business','Business, Apenas R$ 199,00 mensais!'),
    ('Corporate','Corporate, Um preço especial, uma super oferta no seu e-mail!'),
)

MOEDAS = (
    ('S', 'S'),
    ('N','N'),
)

REG = (
    ('0000', '0000'),
)

LECD = (
    ('LECD', 'LECD'),
)


SEGMENTO = (
    ('SERVIÇOS', 'SERVIÇOS'),
    ('INDUSTRIA','INDUSTRIA'),
    ('COMÉRCIO', 'COMÉRCIO'),
    ('AGRONEGÓCIO','AGRONEGÓCIO'),
    ('STARTUP', 'STARTUP'),
)


DICAS = (
    ('S', 'SIM'),
    ('N','NÃO'),
)


EstCivil = (
    ('Casado', 'Casado'),
    ('Solteiro','Solteiro'),
    ('Divorciado', 'Divorciado'),
    ('Desquitado','Desquitado'),
    ('Viúvo', 'Viúvo'),
)


INSTRUCAO = (
    ('Analfabeto', 'Analfabeto'),
    ('Ensino Fundamental Incompleto','Ensino Fundamental Incompleto'),
    ('Ensino Fundamental Completo','Ensino Fundamental Completo'),
    ('Ensino Médio Incompleto','Ensino Médio Incompleto'),
    ('Ensino Médio Completo','Ensino Médio Completo'),
    ('Superior completo (ou Graduação)','Superior completo (ou Graduação)'),
    ('Pós-Graduação','Pós-Graduação'),
    ('Mestrado','Mestrado'),
    ('Doutorado','Doutorado'),
    ('PHD','PHD'),

)

PAGAMENTO = (
    ('MENSAL', 'MENSAL'),
    ('QUINZENAL','QUINZENAL'),
    ('SEMANAL','SEMANAL'),
)


TIPO_SALARIO = (
    ('MENSALISTA', 'MENSALISTA'),
    ('HORISTA','HORISTA'),
)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='templates/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


# Create your models here.


class Document(models.Model):
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description



class Balance_Sheet(models.Model):
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description



class Input(models.Model):
    r = models.CharField(max_length=10, help_text='10 characters max.')
    # n = models.CharField(max_length=10, help_text='10 characters max.')


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.CharField(max_length=10, unique=True,
                            default="question")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



class Accounting(models.Model):
    history = models.CharField(max_length=200)
    date = models.DateField()
    debit = models.CharField(max_length=30)
    credit = models.CharField(max_length=30)
    amount = models.FloatField()
    pdobjects = DataFrameManager()
    class Meta:
        unique_together = ['history','amount','date']


    def __str__(self):
        return self.history



class Site(models.Model):
    site = models.CharField(max_length=10, help_text='10 characters max.')

    def __str__(self):
        return self.site


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = '__all__'


class MyPlan(models.Model):
    Nome_da_Empresa = models.CharField(max_length=200,help_text='Qual o nome da sua empresa',blank=False)
    email = models.EmailField(max_length=200,help_text='Qual o seu e-mail?',blank=False)
    motivo = models.CharField(max_length=40,help_text='Resumidamente diga como nos conheceu?',blank=False)
    Contrato_Social = models.FileField(blank=True, null=True,help_text='Faça o upload do seu contrato social',
    upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    cnpj = models.CharField(max_length=19,help_text='Digite com pontos e barra, exemplo 000.000.000/0000-00',blank=False)
    lifetime = models.CharField(max_length=20,help_text='Quanto tempo de vida tem sua empresa?',blank=False)
    funcionarios = models.CharField(max_length=20,help_text='Quantos funcionarios voce tem?',blank=False)
    Nome_do_socio = models.CharField(max_length=50,help_text='Qual o nome do principal socio?',blank=False)
    cpf = models.CharField(max_length=14,help_text='Qual o CPF do principal socio, preencha com pontos e traço',blank=False)
    tamanho = models.CharField(max_length=10, choices=CHOICES)
    confirmacao_do_plano = models.CharField(max_length=10, choices=PLANOS)


    def __str__(self):
        return self.cnpj


DATE_INPUT_FORMATS = ('%d%m%Y')

class ECD01(models.Model):
    INITIAL = models.CharField(max_length=1, blank=True)
    REG = models.CharField(max_length=4,choices=REG)
    LECD =  models.CharField(max_length=4,choices=LECD)
    DT_INI = models.DateField()
    DT_FIN = models.DateField()
    Nome_da_Empresa = models.CharField(max_length=200,help_text='Qual o nome da sua empresa',blank=False)
    CNPJ = models.CharField(max_length=14,help_text='Qual o CNPJ ',blank=False)
    UF = models.CharField(max_length=2,help_text='Qual a sua UF',blank=False)
    IM = models.CharField(max_length=40,help_text='Qual a sua inscricao municipal',blank=False)
    IN_SIT_ESP = models.CharField(max_length=1,help_text='SITUACAO ESPECIAL, SIM OU NAO? (S OU N)',blank=False)
    IND_SIT_INI_PER = models.CharField(max_length=1,help_text='SITUACAO ESPECIAL, SIM OU NAO? (S OU N)',blank=False)
    IND_NIRE = models.CharField(max_length=1,help_text='POSSUI NIRE, NAO OU SIM (0 OU 1)',blank=False)
    IND_FIN_ESC = models.CharField(max_length=1,help_text='ESCRITURACAO ORIGINAL OU SUBSTITUTA? (0 - ORIGINAL E 1 - SUBSTITUTA)',blank=False)
    COD_HASH_SUB = models.CharField(max_length=40,help_text='CODIGO DO HASH ANTERIOR',blank=True)
    IND_GRANDE_PORTE = models.CharField(max_length=1,help_text='Empresa de grande porte 1 ou de pequeno porte 0',blank=False)
    TIP_ECD = models.CharField(max_length=1, help_text="Indicador do tipo de ECD: 0 – ECD de empresa não participante de SCP como sócio ostensivo, 1 – ECD de empresa participante de SCP como sócio ostensivo, 2 – ECD da SCP",blank=False)
    COD_SCP = models.CharField(max_length=14, blank=True)
    IDENT_MF = models.CharField(max_length=1, choices=MOEDAS,help_text='S caso utilize moeda funcional')
    IND_ESC_CONS = models.CharField(max_length=1, choices=MOEDAS,help_text='Caso a contabilidade seja consolidada na controladroa')
    CLOSING = models.CharField(max_length=1,blank=True)
    pdobjects = DataFrameManager()


    def __str__(self):
        return self.Nome_da_Empresa



class Prediction(models.Model):
    CNPJ = models.CharField(max_length=14,help_text='Qual o CNPJ sem pontos ou barras ?',blank=False)
    Nome_da_Empresa = models.CharField(max_length=200,help_text='Qual o nome da sua empresa?',blank=False)
    email = models.EmailField(max_length=200,help_text='Qual o seu e-mail?',blank=False)
    Seu_nome = models.CharField(max_length=200,help_text='Qual o seu nome?',blank=False)
    Seu_cargo = models.CharField(max_length=200,help_text='Qual o seu cargo?',blank=False)
    Segmento = models.CharField(max_length=12, choices=SEGMENTO,help_text='Insira seu segmento')
    Faturamento_Ultimo_Mes = models.FloatField(null=True, blank=True, default=None,help_text='Insira o faturamento Liquido sem impostos')
    Faturamento_Penultimo_Mes = models.FloatField(null=True, blank=True, default=None,help_text='Insira o faturamento Liquido sem impostos')
    Faturamento_Antepenultimo_mes = models.FloatField(null=True, blank=True, default=None,help_text='Insira o faturamento Liquido sem impostos')
    Despesas_Ultimo_Mes = models.FloatField(null=True, blank=True, default=None,help_text='Insira as despesas totais sem impostos')
    Despesas_Penultimo_Mes = models.FloatField(null=True, blank=True, default=None,help_text='Insira as despesas totais sem impostos')
    Despesas_Antepenultimo_Mes = models.FloatField(null=True, blank=True, default=None,help_text='Insira as despesas totais sem impostos')
    pdobjects = DataFrameManager()


    def __str__(self):
        return self.Nome_da_Empresa





class Dolar(models.Model):
    Date = models.DateField()
    Value = models.FloatField(null=True, blank=True, default=None)
    pdobjects = DataFrameManager()


    def __float__(self):
        return self.Value



class IGPM(models.Model):
    Date = models.DateField()
    Value = models.FloatField(null=True, blank=True, default=None)
    pdobjects = DataFrameManager()


    def __float__(self):
        return self.Value


class Selic(models.Model):
    Date = models.DateField()
    Value = models.FloatField(null=True, blank=True, default=None)
    pdobjects = DataFrameManager()


    def __float__(self):
        return self.Value



class Stocks(models.Model):
    Asset = models.CharField(max_length=10,help_text='Qual o ativo voce quer analisar? Exemplo: petr4 para analisar Petrobras',blank=False)
    Nome_da_Empresa = models.CharField(max_length=200,help_text='Qual o nome da sua empresa?',blank=False)
    email = models.EmailField(max_length=200,help_text='Qual o seu e-mail?',blank=False)
    Seu_nome = models.CharField(max_length=200,help_text='Qual o seu nome?',blank=False)
    Seu_cargo = models.CharField(max_length=200,help_text='Qual o seu cargo?',blank=False)
    Segmento = models.CharField(max_length=12, choices=SEGMENTO,help_text='Insira seu segmento')
    Dicas =  models.CharField(max_length=12,choices=DICAS, help_text='Gostaria de receber dicas de Investimento?')

    pdobjects = DataFrameManager()


    def __str__(self):
        return self.Nome_da_Empresa



class employees(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome completo do colaborador',blank=False)
    pai = models.CharField(max_length=100,help_text='Nome completo do pai do colaborador',blank=False)
    mae = models.CharField(max_length=100,help_text='Nome completo da mãe do colaborador',blank=False)
    carteira = models.CharField(max_length=100,help_text='Numero da carteira profissional seguido da série da mesma',blank=False)
    data_carteira = models.DateField(help_text='Data da carteira inseria Mes,Dia e Ano, exemplo 12/23/1973')
    reservista = models.CharField(max_length=100,help_text='Numero Reservista caso aplicável',blank=True)
    categoria = models.CharField(max_length=100,help_text='Qual a categoria',blank=True)
    titulo_eleitor = models.CharField(max_length=100,help_text='Titulo se aplicável',blank=True)
    exame_admissional = models.CharField(max_length=10,help_text='Exame',blank=True)
    exame_medico = models.CharField(max_length=10,help_text='Exame medico',blank=True)
    cart_identidade = models.CharField(max_length=10,help_text='No. Identidade',blank=False)
    emissao_identidade = models.DateField()
    Org_emissor = models.CharField(max_length=10,help_text='sigla do orgao emissor da carteira',blank=False)
    CPF = models.CharField(max_length=11,help_text='Numero sem pontos e traços com 11 digitos',blank=False)
    PIS = models.CharField(max_length=50,help_text='Numero sem pontos e traços',blank=False)
    Data_Cadastro_PIS = models.DateField()
    Sigla_Conselho_Regional = models.CharField(max_length=50,help_text='por exemplo: CRA, caso aplicavel. Para fins de contribuicao sindical',blank=True)
    Numero_Reg_Conselho = models.CharField(max_length=50,help_text='Caso aplicavel. Para fins de contribuicao sindical',blank=True)
    Regiao_Registro_Conselho = models.CharField(max_length=50,help_text='Caso aplicavel. Para fins de contribuicao sindical',blank=True)
    Data_Nascimento = models.DateField()
    Local_Nascimento = models.CharField(max_length=50,help_text='Município e Estado onde nasceu',blank=False)
    Estado_Civil = models.CharField(max_length=30, choices=EstCivil,help_text='Estado Civil colaborador',blank = False)
    Grau_Instrucao = models.CharField(max_length=30, choices=INSTRUCAO,help_text='Escolaridade do colaborador',blank = False)
    Nacionalidade = models.CharField(max_length=12, help_text='Brasileiro ou Estrangeiro',blank = False)
    Sexo = models.CharField(max_length=12, help_text='Masculino ou Feminino',blank = False)
    Cor = models.CharField(max_length=12, help_text='Cor de pele',blank = False)
    Altura = models.CharField(max_length=12, help_text='Altura',blank = False)
    Peso = models.CharField(max_length=12, help_text='Peso do colaborador',blank = False)
    Cabelos = models.CharField(max_length=12, help_text='Cor dos cabelos',blank = False)
    Olhos = models.CharField(max_length=12, help_text='Cor dos olhos',blank = False)
    Defeitos = models.CharField(max_length=12, help_text='Caso aplicavel',blank=True)
    Endereço = models.CharField(max_length=200, help_text='Rua e numero da casa ou apartamento',blank = False)
    Bairro = models.CharField(max_length=12, help_text='Bairro',blank = False)
    Cidade = models.CharField(max_length=12, help_text='Cidade', blank = False)
    Estado = models.CharField(max_length=12, help_text='Estado onde reside', blank = False)
    CEP = models.CharField(max_length=9, help_text='numeros com traço', blank = False)
    Registro_Geral = models.CharField(max_length=50, help_text='Caso seja estrangeiro Naturalizado', blank = True)
    Filhos = models.CharField(max_length=50, help_text='No caso de estrageniro, reponser Sim caso possua filhos brasileiros', blank = True)
    Data_Chegada_Brasil = models.DateField(blank = True,null=True)
    N_Carteira_Mod_19 = models.CharField(max_length=50, help_text='No caso de estrageiro, informar o numero', blank = True,null=True)
    Validade_Cart_Identidade_Estrangeiro = models.DateField(blank = True,null=True)
    Tipo_Visto_Estrageiro = models.CharField(max_length=50, help_text='No caso de estrangeiro informar o tipo de visto obtido', blank = True)
    Validade_Carteira_Trabalho = models.DateField(blank = True,null=True)
    Data_Admissao = models.DateField()
    Data_Opção_FGTS= models.DateField(blank = True,null=True, help_text='Mesma data da admissão')
    Forma_Pagamento= models.CharField(max_length=50, choices=PAGAMENTO, blank = False)
    Cargo_Atual= models.CharField(max_length=50, help_text='Cargo do colaborador', blank = False)
    Salario = models.FloatField()
    Tipo_Salario = models.CharField(max_length=50, choices = TIPO_SALARIO, blank = False)
    Local_Trabalho = models.CharField(max_length=50, help_text='Endereço completo do local de trabalho', blank = False)
    Membro_Cipa = models.CharField(max_length=50, help_text='Membro da Cipa? Sim ou Nao', blank = False)
    Dependendentes1 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes2 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes3 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes4 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes5 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Salario_Familia = models.CharField(max_length=200, help_text='Preenchido posteriormente pela nossa equipe', blank = True)
    Imposto_Renda = models.CharField(max_length=200, help_text='Preenchido posteriormente pela nossa equipe', blank = True)
    Salario_Educacao = models.CharField(max_length=200, help_text='Preenchido posteriormente pela nossa equipe', blank = True)


    pdobjects = DataFrameManager()


    def __str__(self):
        return self.nome




class holerite(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome completo do colaborador',blank=False)
    salario = models.FloatField()
    descanso = models.FloatField()
    comissoes = models.FloatField()
    salario_familia = models.FloatField()
    adic_sal_familia = models.FloatField()
    horas_extras_55 = models.FloatField()
    vale_transporte = models.FloatField()



    pdobjects = DataFrameManager()


    def __str__(self):
        return self.nome
