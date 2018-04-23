from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment, MyPlan
from django.utils import timezone
import django_excel as excel
from blog.forms import PostForm, CommentForm, DocumentForm, Statements, MyPlanForm
from .models import InputForm, Question, Choice, Accounting, SiteForm, MyPlan, ECD01
from django.shortcuts import render_to_response
import pandas_datareader.data as web
import numpy as np
from datetime import datetime
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
import pyexcel as pe
from .compute import compute
from django.http import HttpResponse
from django import forms
from django.db.models import Sum

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MyPlanForm
from blog.forms import MyPlanForm, ECD01FORM, predictionFORM, stocksFORM, employeesFORM, holeriteFORM
from blog.models import  MyPlan, ECD01, Prediction, Stocks, employees, holerite

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django_pandas.managers import DataFrameManager
from django_pandas.io import read_frame

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import django_excel as excel
from django.shortcuts import render_to_response
from datetime import datetime
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
import pyexcel as pe
from django.http import HttpResponse
from django import forms
from django.db.models import Sum
import datetime
import numpy as np
from decimal import Decimal
import decimal, simplejson
import json
from django_pandas.io import read_frame

import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import table

import datetime as dt

import numpy as np
import openpyxl

from django.core.files.storage import default_storage

from django.core.files import File
from xlrd import open_workbook

from django.forms import ModelForm

from django.utils.dateformat import format
from django.utils import timezone



now = timezone.now()  # datetime.datetime(2016, 8, 10, 20, 32, 36, 461069, tzinfo=<UTC>)
format(now, 'dd-MM-YYYY')


class AboutView(TemplateView):
    template_name = 'bootstrap.html'




class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html'


    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


    def image_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('blog/post_detail.html')
        else:
            form = PostForm()
        return render(request, 'blog/post_detail.html', {
        'form': form
    })


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_excel(request.FILES['document'])
            writer = pd.ExcelWriter('teste.xlsx')
            filehandle = df.to_excel(writer)
            writer.save()
            return excel.make_response(pe.get_sheet(file_name='teste.xlsx'), "csv",file_name='forecast_2018')

    else:
        form = DocumentForm()
    return render(
        request,
        'blog/model_form_upload.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })

def __str__(self):
   return 'form_upload:' + self.name





@login_required
def Statements_Upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            gengibre_2016 = pd.read_excel(request.FILES['document'])

            classification = []

# For each row in the column,
            for row in gengibre_2016['debito']:
    # if more than a value,
                if row == '3.1.50.030.0060':
        # Append a letter grade
                    classification.append('Honorários Profissionais')
                elif row == '1.1.10.020.0001':
        # Append a letter grade
                    classification.append('Banco Itau')
                elif row == '1.1.20.020.0002':
        # Append a letter grade
                    classification.append('Adiantamento aos Sócios')
                elif row == '1.3.10.010.0001':
        # Append a letter grade
                    classification.append('Adto a Sócios')
                elif row == '1.1.20.022.0999':
        # Append a letter grade
                    classification.append('Clientes')
                elif row == '3.1.20.010.0050':
        # Append a letter grade
                    classification.append('Impostos sobre as vendas')
                elif row == '3.1.50.030.0020':
        # Append a letter grade
                    classification.append('Despesas Bancarias')
                elif row == '3.1.50.020.0025':
        # Append a letter grade
                    classification.append('INSS')
                elif row == '3.1.50.040.0020':
        # Append a letter grade
                    classification.append('Impostos e Taxas')
                elif row == '1.1.10.030.0001':
        # Append a letter grade
                    classification.append('Investimentos')
                elif row == '2.1.20.010.0999':
        # Append a letter grade
                    classification.append('Fornecedores')
                elif row == '3.1.20.010.0050':
        # Append a letter grade
                    classification.append('Impostos sobre as vendas')
                elif row == '2.1.30.040.0013':
        # Append a letter grade
                    classification.append('Impostos a Recolher')
                elif row == 'xxx':
        # Append a letter grade
                    classification.append('PL')
                elif row == 'zzz':
        # Append a letter grade
                    classification.append('Resultado Exercicio')
                else:
                    classification.append('Others')


            conta_deb = classification

            gengibre_2016['conta devedora'] = conta_deb

            classification = []

# For each row in the column,
            for row in gengibre_2016['credito']:
    # if more than a value,
                if row == '3.1.50.030.0060':
        # Append a letter grade
                    classification.append('Honorários Profissionais')
                elif row == '1.1.10.020.0001':
        # Append a letter grade
                    classification.append('Banco Itau')
                elif row == '1.1.20.020.0002':
        # Append a letter grade
                    classification.append('Adiantamento aos Sócios')
                elif row == '1.3.10.010.0001':
        # Append a letter grade
                    classification.append('Adto a Sócios')
                elif row == '1.1.20.022.0999':
        # Append a letter grade
                    classification.append('Clientes')
                elif row == '3.1.20.010.0050':
        # Append a letter grade
                    classification.append('Impostos sobre as vendas')
                elif row == '3.1.50.030.0020':
        # Append a letter grade
                    classification.append('Despesas Bancarias')
                elif row == '3.1.50.020.0025':
        # Append a letter grade
                    classification.append('INSS')
                elif row == '3.1.50.040.0020':
        # Append a letter grade
                    classification.append('Impostos e Taxas')
                elif row == '1.1.10.030.0001':
        # Append a letter grade
                    classification.append('Investimentos')
                elif row == '3.1.10.010.0005':
        # Append a letter grade
                    classification.append('Faturamento')
                elif row == '2.1.30.040.0013':
        # Append a letter grade
                    classification.append('Impostos a Recolher')
                elif row == '3.1.60.020.0001':
        # Append a letter grade
                    classification.append('Receita Financeira')
                elif row == '2.1.20.010.0999':
        # Append a letter grade
                    classification.append('Fornecedores')
                elif row == 'xxx':
        # Append a letter grade
                    classification.append('PL')
                elif row == 'zzz':
        # Append a letter grade
                    classification.append('Resultado Exercicio')
                else:
                    classification.append('Others')

            conta_cred = classification

            gengibre_2016['conta credora'] = conta_cred

            import numpy as np

            table_2016_debito = pd.pivot_table(gengibre_2016, values='valor',columns=['conta devedora'], aggfunc=np.sum)
            table_2016_credito = pd.pivot_table(gengibre_2016, values='valor',columns=['conta credora'], aggfunc=np.sum)

            balance = table_2016_debito - table_2016_credito

            table_2016_debito = pd.concat([table_2016_debito,pd.DataFrame(columns=table_2016_credito.columns)])
            table_2016_credito = pd.concat([table_2016_credito,pd.DataFrame(columns=table_2016_debito.columns)])

            table_2016_credito = table_2016_credito.fillna(0)
            table_2016_debito = table_2016_debito.fillna(0)

            balance = table_2016_debito - table_2016_credito

            Cash = round(balance['Banco Itau'][-1],2)
            Customers = round(balance['Clientes'][-1],2)
            Taxes = round(balance['Impostos a Recolher'][-1],2)
            PL = round(balance['PL'][-1],2)
            #df2 = df['sharpe'][2]
            #writer = pd.ExcelWriter('teste.xlsx')
            #filehandle = df.to_excel(writer)
            #writer.save()
            return render(request, 'index.html',{'Cash':Cash,'Customers':Customers, "Taxes":Taxes, "PL": PL})
#            return excel.make_response(pe.get_sheet(file_name='teste.xlsx'), "csv",file_name='forecast_2018')

    else:
        form = Statements()
    return render(
        request,
        'statements.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })

def __str__(self):
   return 'statements:' + self.name

def download(request):
    context = {

        'submit_btn': "excel"
        }
    return render(request, 'download.html',context)




def excel_download(request):
    fsock = open('teste.xlsx', 'rb')
    response = HttpResponse(fsock, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    return response


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)

    else:
        form = InputForm()


    return render(request, 'var.html', context = {'form': form})






def present_output(form):
        r = form.r
        # n = form.n
        #start = datetime(2012, 7, 10)
        #end = datetime.now()

        citi = web.DataReader(r+'.sa', 'yahoo')
        citi["rets"] = citi["Close"].pct_change()

        P = 10000   # 1,000,000 USD
        c = 0.95  # 99% confidence interval
        mu = np.mean(citi["rets"])
        sigma = np.std(citi["rets"])
        z = compute(P, c, mu, sigma)
        s = '%.2f' % round(z, 2)

#        return render(request, template_name='name.html', context = {'s': s})
        return render_to_response('name.html', context= {'r':r,'s':s})
#        return HttpResponse('Ola! Risco calculado em(%s)= %s ao longo de 12 meses de investimento para cada 10 mil reais investidos.' % (r,s))





def get_data(request):
    if request.method == 'POST':
        form = InputForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            df = present_output(form)
            response = HttpResponse(df, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="chemalle.xls"'
            return response

    else:
        form = InputForm()
    return render(
        request,
        'blog/var.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })

def __str__(self):
   return 'form_upload:' + self.name


class UploadFileForm(forms.Form):
    file = forms.FileField()


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Question, Choice],
                initializers=[None, choice_func],
                mapdicts=[
                    ['question_text', 'pub_date', 'slug'],
                    ['question', 'choice_text', 'votes']]
            )
            return redirect('handson_view')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def handson_table(request):
    return excel.make_response_from_tables(
        [Question, Choice], 'handsontable.html')



def handson_table_accounting(request):
    return excel.make_response_from_tables(
        [Accounting], 'handsontable.html')




def import_Accounting(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Accounting],
                initializers=[None, choice_func],
                mapdicts=[
                    ['history', 'date', 'debit','credit','amount']]
            )
            return redirect('handson_view_accounting')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })



def Statements_Upload_Accounting(request):
    df = pd.DataFrame(list(Accounting.objects.all().values()))
    df2 = pd.DataFrame(list(Accounting.objects.all().values('history', 'date', 'amount')))
    df3 = pd.DataFrame(list(Accounting.objects.aggregate(Sum('amount'))))
    df4 = df['amount'].sum()
    return render_to_response('name.html', context={'df':df,'df2':df2, 'df3':df3,'df4':df4})




def User(request):
    if request.method == 'POST':
        site2 = SiteForm(request.POST or None, request.FILES or None)
        if site2.is_valid():
            site2 = site2.save(commit=False)
            response = HttpResponse(site2)
            print(site2)
            return response


    else:
        site2 = SiteForm()


        return render(request,'user.html', context = {'site2': site2})



from django.core.mail import EmailMultiAlternatives

def email_marketplace(request):
    subject, from_email, to = 'hello', 'from@example.com', 'chemalle@me.com'
    text_content = 'This is an important message. Escutou meu velho?'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render_to_response('blog/thankyou2.html')




from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['chemalle@me.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "blog/email.html", {'form': form})

def thanks(request):
    return render_to_response('blog/thankyou.html')




def plan_form(request):
    if request.method == 'POST':
        form = MyPlanForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('blog/thankyou.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = MyPlanForm()
    return render(request, 'blog/forms.html', {'form': form})






from django.core.mail.message import EmailMessage
#from django.contrib.auth.models import User



def plan_form_mail(request):
        if request.method == 'GET':
            form = MyPlanForm()
        else:
            form = MyPlanForm(request.POST)
            if form.is_valid():
                form.save()
                subject = form.cleaned_data['Nome_do_socio']
                cc_email = form.cleaned_data['email']
                from_email = 'econobilidade@atendimento.com'
                message = str(form.cleaned_data)
                try:
                    send_mail(subject, message, from_email, ['chemalle@me.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('thanks')
        return render(request, "blog/forms.html", {'form': form})

        def thanks(request):
            return render_to_response('blog/thankyou.html')



def plan_form_mail_Business(request):
        if request.method == 'GET':
            form = MyPlanForm()
        else:
            form = MyPlanForm(request.POST)
            if form.is_valid():
                form.save()
                subject = form.cleaned_data['Nome_do_socio']
                cc_email = form.cleaned_data['email']
                from_email = 'econobilidade@atendimento.com'
                message = str(form.cleaned_data)
                try:
                    send_mail(subject, message, from_email, ['chemalle@me.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('thanks')
        return render(request, "blog/forms_business.html", {'form': form})

        def thanks(request):
            return render_to_response('blog/thankyou.html')



def plan_form_mail_Corporate(request):
        if request.method == 'GET':
            form = MyPlanForm()
        else:
            form = MyPlanForm(request.POST)
            if form.is_valid():
                form.save()
                subject = form.cleaned_data['Nome_do_socio']
                cc_email = form.cleaned_data['email']
                from_email = 'econobilidade@atendimento.com'
                message = str(form.cleaned_data)
                try:
                    send_mail(subject, message, from_email, ['chemalle@me.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('thanks')
        return render(request, "blog/forms_corporate.html", {'form': form})

        def thanks(request):
            return render_to_response('blog/thankyou.html')





# def cadastro(request):
#         if request.method == 'GET':
#             form = ECD01FORM()
#         else:
#             form = ECD01FORM(request.POST)
#             if form.is_valid():
#                 form.save()
#         return render(request, "blog/forms_corporate.html", {'form': form})
#
#         def thanks(request):
#             return render_to_response('blog/thankyou2.html')



def cadastro(request):
    if request.method == 'POST':
        form = ECD01FORM(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('blog/thankyou2.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = ECD01FORM()
    return render(request, 'blog/forms.html', {'form': form})


from datetime import datetime
def ECD(request):
    qs = ECD01.pdobjects.all()
    qs2 = Accounting.pdobjects.all()
    df2 = qs.to_dataframe()
    df = qs2.to_dataframe()
    #df2 = df2[-1:]
    columns = ['INITIAL','REG', 'LECD', 'DT_INI','DT_FIN', 'Nome_da_Empresa','CNPJ','UF','IM','IN_SIT_ESP', 'IND_SIT_INI_PER','IND_NIRE',
               'IND_FIN_ESC','COD_HASH_SUB','IND_GRANDE_PORTE', 'TIP_ECD','COD_SCP', 'IDENT_MF', 'IND_ESC_CONS','CLOSING']
    columns2 = ['history','date','debit','credit','amount' ]
    df2['DT_INI'] = pd.to_datetime(df2['DT_INI'], format="%Y-%m-%d")
    df2['DT_FIN'] = pd.to_datetime(df2['DT_FIN'], format="%Y-%m-%d")
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")

    fsock = df2.to_csv('ecd.csv', sep='|', index=False, header=False,columns = columns, date_format='%d%m%Y' )
    fsock2 = df.to_csv('escrita.csv',sep='|',index=False, header=False, columns=columns2,date_format='%d%m%Y' )

    fout=open("out3.csv","w")
    # first file:
    for line in open("ecd.csv"):
        fout.write(line)
    for line in open("escrita.csv"):
        fout.write(line)
    # import csv
    # reader = csv.reader(open('ecd.csv', 'r'))
    # reader1 = csv.reader(open('escrita.csv', 'r'))
    # writer = csv.writer(open('ok_uau.csv', 'w', newline=''))
    # for row in reader:
    #     row1 = next(reader1)
    #     writer.writerow(row)
    #     writer.writerow(row1)

    return render(request, 'download.html')



def download_CSV(request):
    fsock = open('out3.csv', 'rb')
    response = HttpResponse(fsock, content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename="ecd.csv"'
    return response



def Prediction_Data(request):
    if request.method == 'POST':
        form = predictionFORM(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('blog/thankyou3.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = predictionFORM()
    return render(request, 'blog/forms_prediction.html', {'form': form})

    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     message = cleaned_data.get('message')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')



from django.core.mail.message import EmailMessage
from .models import Dolar
from django.http import HttpResponseRedirect
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def data(request):
    if request.method == 'POST' and request.FILES['tnt']:
        myfile = request.FILES['tnt']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        df = pd.read_excel(filename)

        for index,row in df.iterrows():
            if row[0] != 'create_date':
                dolar = Dolar()
                dolar.Date = row[0]
                dolar.Value = row[1]
                dolar.save()

        return render_to_response('blog/thankyou2.html')

    else:
        return render(request, 'blog/import.html')



from django.core.mail.message import EmailMessage
from .models import Selic
from django.http import HttpResponseRedirect
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def data_Selic(request):
    if request.method == 'POST' and request.FILES['tnt']:
        myfile = request.FILES['tnt']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        df = pd.read_excel(filename)

        for index,row in df.iterrows():
            if row[0] != 'create_date':
                selic = Selic()
                selic.Date = row[0]
                selic.Value = row[1]
                selic.save()

        return render_to_response('blog/thankyou2.html')

    else:
        return render(request, 'blog/import.html')




from django.core.mail.message import EmailMessage
from .models import IGPM
from django.http import HttpResponseRedirect
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def data_IGPM(request):
    if request.method == 'POST' and request.FILES['tnt']:
        myfile = request.FILES['tnt']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        df = pd.read_excel(filename)

        for index,row in df.iterrows():
            if row[0] != 'create_date':
                igpm = IGPM()
                igpm.Date = row[0]
                igpm.Value = row[1]
                igpm.save()

        return render_to_response('blog/thankyou2.html')

    else:
        return render(request, 'blog/import.html')



import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn import ensemble
from django_pandas.managers import DataFrameManager
from django_pandas.io import read_frame
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
from sklearn import ensemble
import random

def forecast(request):
    qs = Prediction.pdobjects.order_by('-id')[:3].values('Faturamento_Ultimo_Mes', 'Faturamento_Penultimo_Mes', 'Faturamento_Antepenultimo_mes','Despesas_Ultimo_Mes','Despesas_Penultimo_Mes', 'Despesas_Antepenultimo_Mes' )
    #last_ten_in_ascending_order = reversed(last_ten)
    #qs = Prediction.pdobjects.all().values('Faturamento_Ultimo_Mes', 'Faturamento_Penultimo_Mes', 'Faturamento_Antepenultimo_mes','Despesas_Ultimo_Mes','Despesas_Penultimo_Mes', 'Despesas_Antepenultimo_Mes' )
    qs2 = IGPM.pdobjects.all()
    qs3 = Selic.pdobjects.all()
    qs4 = Dolar.pdobjects.all()
    df = qs.to_dataframe()
    fsock = df.to_csv('prediction.csv', sep=',', index=False, date_format='%d-%m-%Y' )
    mes = df['Faturamento_Ultimo_Mes'].tolist()
    atual = df['Despesas_Ultimo_Mes'].tolist()
    mes_passado = df['Faturamento_Penultimo_Mes'].tolist()
    ontem = df['Despesas_Penultimo_Mes'].tolist()
    mes_retrasado = df['Faturamento_Antepenultimo_mes'].tolist()
    anteotem = df['Despesas_Antepenultimo_Mes'].tolist()
    df = pd.DataFrame({'Faturamento_Ultimo_Mes': [mes,mes_passado,mes_retrasado],
                 'Despesas_Ultimo_Mes':[atual,ontem,anteotem]})
    df.columns = ['Expenses','Revenue']
    df = df[['Revenue','Expenses']]
    df2 = qs2.to_dataframe()
    df2['IGPM'] = df2['Value']
    df3 = qs3.to_dataframe()
    df3['Selic'] = df3['Value']
    df4 = qs4.to_dataframe()
    df4['Dolar'] = df4['Value']
    df = df[-3:]
    df2 = df2[-3:]
    df3 = df3[-3:]
    df4 = df4[-3:]
    IGP = df2['IGPM'].tolist()
    Sel = df3['Selic'].tolist()
    Dol = df4['Dolar'].tolist()
    df['IGPM'] = IGP
    df['Selic'] = Sel
    df['Dolar'] = Dol
    df['Revenue'] = df['Revenue'].str[0]
    df['Expenses'] = df['Expenses'].str[0]

    X, y = [], []
    for index,row in df.iterrows():
        X.append(row[1:-1])
        y.append(row[0])

    X, y = shuffle(X, y, random_state=23)
    num_training = int(0.9 * len(X))
    X_train, y_train = X[:num_training], y[:num_training]
    X_test, y_test = X[num_training:], y[num_training:]
    rf_regressor = RandomForestRegressor(n_estimators=2, max_depth=3,random_state=23)

    rf_regressor.fit(X_train, y_train)
    y_pred = rf_regressor.predict(X_test)

    adaboost_pred = rf_regressor.predict(df.iloc[:,1:-1])

    adaboost_pred = adaboost_pred.reshape(-1,1)

    df['Prediction'] = adaboost_pred


    answers = ['O mercado esta desafiador mas seu faturamento deve girar em torno de R$',
                'Entendemos que o mercado esta repercutindo vagarosamente uma melhora e seu faturamento deve se posicionar em R$',
                'O PIB e outros indicados contextualizam um cenario promissor nos próximos meses, no próximo mês seu faturamento deverá se aproximar de R$',]
    talk = random.choice(answers)
    F = df['Prediction'][2]

    qs2 = Prediction.pdobjects.order_by('-id')[:1].values('email')
    df2 = qs2.to_dataframe()
    df2 = df2['email'].tolist()
    # df = df['Asset'].str[0]
    df2 = df2[0]
    subject, from_email, to = 'Forecast', 'econobilidade@econobilidade.com', str(df2)
    html_content = render_to_string('blog/forecast.html', {'F':F, 'talk':talk}) # render with dynamic value
    text_content = strip_tags(answers) # Strip the html tag. So people can see the pure text at least.

    # create the email, and attach the HTML version as well.
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


    return render_to_response('blog/thankyou3.html')




def Stocks_Data(request):
    if request.method == 'POST':
        form = stocksFORM(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('blog/thankyou2.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = stocksFORM()
    return render(request, 'blog/forms_corporate_stocks.html', {'form': form})

from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
#import pandas_datareader as web-- If you are using python 3.5
#from pandas_datareader import data as web
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
#import pandas_datareader.data as web
from datetime import datetime
import seaborn as sns; sns.set()  # nicer plotting style
    # put all plots in the notebook itself
from pandas_datareader import data as web
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template.loader import get_template



def recommendation(request):
    try:
        qs = Stocks.pdobjects.order_by('-id')[:1].values('Asset')
        df = qs.to_dataframe()
        df = df['Asset'].tolist()
        # df = df['Asset'].str[0]
        df = df[0]
        Df = web.DataReader(df+'.sa', data_source='yahoo')
        Df=Df[['Open','High','Low','Close']]
        Df= Df.dropna()
        #############################################################################

        ###################### Creating input Parameters #########################
        Df['Std_U']=Df['High']-Df['Open']
        Df['Std_D']=Df['Open']-Df['Low']
        Df['S_3'] = Df['Close'].shift(1).rolling(window=3).mean()# pandas 0.19
        Df['S_15']= Df['Close'].shift(1).rolling(window=15).mean()# pandas 0.19
        Df['S_60']= Df['Close'].shift(1).rolling(window=60).mean()# pandas 0.19
        Df['OD']=Df['Open']-Df['Open'].shift(1)
        Df['OL']=Df['Open']-Df['Close'].shift(1)
        Df['Corr']=Df['Close'] .shift(1).rolling(window=10).corr(Df['S_3'] .shift(1))#pandas 0.19

        ####################### Creation of X and y datasets ######################
        X=Df[['Open','S_3','S_15','S_60','OD','OL','Corr']]# changed
        yU =Df['Std_U']
        yD =Df['Std_D']

        imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
        #############################################################################

        ########################## Centring and Scaling ###########################
        steps = [('imputation', imp),
                     ('scaler',StandardScaler()),
                     ('linear',LinearRegression())]
        #############################################################################

        ############################ Creating a Pipeline ##########################
        pipeline =Pipeline(steps)
        #############################################################################

        ############################# Hyper Parameters ##########################
        parameters = {'linear__fit_intercept':[0,1]}
        #############################################################################


        ############################# Cross Validation ############################
        reg = GridSearchCV(pipeline, parameters,cv=5)
        ############################################################################

        ############################ Test and Train Split ##########################
        t=.8
        split = int(t*len(Df))
        reg.fit(X[:split],yU[:split])
        #############################################################################
        ####################### Data Pre-Processing Completed ###################
        ############################# Regression #################################
        best_fit = reg.best_params_['linear__fit_intercept']
        reg = LinearRegression(fit_intercept =best_fit)
        X=imp.fit_transform(X,yU)
        reg.fit(X[:split],yU[:split])
        yU_predict =reg.predict(X[split:])

        reg = GridSearchCV(pipeline, parameters,cv=5)
        reg.fit(X[:split],yD[:split])
        best_fit = reg.best_params_['linear__fit_intercept']
        reg = LinearRegression(fit_intercept =best_fit)
        X=imp.fit_transform(X,yD)
        reg.fit(X[:split],yD[:split])
        yD_predict =reg.predict(X[split:])
        #############################################################################

        ############################ Prediction #####################################
        Df = Df.assign(Max_U =pd.Series(np.zeros(len(X))).values)
        Df = Df.assign(Max_D =pd.Series(np.zeros(len(X))).values)
        Df['Max_U'][split:]=yU_predict
        Df['Max_D'][split:]=yD_predict
        Df['Max_U'][Df['Max_U']<0]=0
        Df['Max_D'][Df['Max_D']<0]=0
        Df['P_H'] = Df['Open']+Df['Max_U']
        Df['P_L'] = Df['Open']-Df['Max_D']
        #########################################################################

        ######################## Strategy Implementation #######################
        Df = Df.assign(Ret =pd.Series(np.zeros(len(X))).values)

        Df['Ret']=np.log(Df['Close']/Df['Close'].shift(1))

        Df = Df.assign(Ret1 =pd.Series(np.zeros(len(X))).values)
        Df = Df.assign(Signal =pd.Series(np.zeros(len(X))).values)

        Df['Signal'][(Df['High']>Df['P_H']) &(Df['Low']>Df['P_L'])]=-1
        Df['Signal'][(Df['High']<Df['P_H']) &(Df['Low']<Df['P_L'])]=1

        Df['Ret1'][Df['Signal'].shift(1)==1]=Df['Ret']
        Df['Ret1'][Df['Signal'].shift(1)==-1]=-Df['Ret']

        Df = Df.assign(Cu_Ret1 =pd.Series(np.zeros(len(X))).values)
        Df['Cu_Ret1']=np.cumsum(Df['Ret1'][split:])

        Df = Df.assign(Cu_Ret =pd.Series(np.zeros(len(X))).values)
        Df['Cu_Ret']=np.cumsum(Df['Ret'][split:])

        Std =Df['Cu_Ret1'].expanding().std()
        Sharpe = (Df['Cu_Ret1']-Df['Cu_Ret'])/Std
        Sharpe=Sharpe.mean()

        high = Df['High'][-1]
        low = Df['Low'][-1]
        close = Df['Close'][-1]
        pivot = (high + low + close)/3

        R1 = (2 * pivot) - low
        S1 = (2 * pivot) - high
        R2 = (pivot - S1) + R1
        S2= pivot - (R1 - S1)

        Df['daily_ret'] = Df['Close'].pct_change()
        Df['excess_daily_ret'] = Df['daily_ret'] - 0.05/252


        def annualised_sharpe(returns, N=252):

            return np.sqrt(N) * returns.mean() / returns.std()

        def equity_sharpe(a):
            return annualised_sharpe(Df['excess_daily_ret'])

        answers = ['O mercado esta desafiador e o risco esta crescendo, veja se o Sharpe deste ativo é positivo, isto significa que a volatilidade do mesmo é muito boa a partir do indice 1 e representa menor risco no investimento',
                    'O volume negociado neste ativo cresceu muito nos ultimos 30 minutos do pregao, fique atento a reversao caso o ativo atinja o preço de resistencia rapidamente',
                    'Ha um crescente interesse neste ativo no momento, acompanhe os proximos 15 minutos para entrar com mais assertividade, o preço de resistencia indica um risco maior para compra, abaixo deste, o risco deve compensar',]

        answers2 = ['Ha uma tensao aparente e os vendidos comecam a ganhar a guerra dos comprados, nao compre este ativo se o valor de suporte for quebrado, a realizacao de lucros vai se intensificar',
                    'Ha um volume muito crescente de venda do ativo nos ultimos 30 minutos do pregao, fique atento se o Sharpe for inferior a 1, pois devera significar uma intensificacao da venda, em caso contrario compre apenas acima do preco de suporte e abaixo do preco de resistencia',
                    'O mercado esta desafiador, fique atento para comprar o ativo apenas caso o preco de suporte nao seja rompido',]

        answers3 = ['O ativo esta sendo negociado num patamar normal, nao ha indicador que direcione compra ou venda neste momento',
                    'Os indicadores de volume estao divergentes, nao ha uma visibilidade clara sobre posicionamento de curto prazo'
                    'Esteja atento a um aumento do volume para iniciar negociacao neste ativo, neste momento nao ha indicador convincente',]



        if Df['Signal'][-1]== -1:
            xls= ["{0:.2f}".format(R1),"{0:.2f}".format(S1),"{0:.2f}".format(equity_sharpe(df)),'Sell']
        elif Df['Signal'][-1]== 1:
            xls=["{0:.2f}".format(R1),"{0:.2f}".format(S1),"{0:.2f}".format(equity_sharpe(df)), 'Buy']
        else:
            xls=["{0:.2f}".format(R1),"{0:.2f}".format(S1),"{0:.2f}".format(equity_sharpe(df)), 'Neutral']


        if Df['Signal'][-1]== -1:
            talk = random.choice(answers)
        elif Df['Signal'][-1]== 1:
            talk = random.choice(answers2)
        else:
            talk = random.choice(answers3)


        data_barchart = pd.DataFrame(list(xls))
        data_barchart = data_barchart.T
        data_barchart.columns = ['Resistencia','Suporte','Sharpe','Action']
        data_barchart = data_barchart.to_html(index=False,columns=['Resistencia','Suporte','Sharpe','Action'])  # render with dynamic value



        qs2 = Stocks.pdobjects.order_by('-id')[:1].values('email')
        df2 = qs2.to_dataframe()
        df2 = df2['email'].tolist()
            # df = df['Asset'].str[0]
        df2 = df2[0]
        subject, from_email, to = 'Recomendação', 'econobilidade@econobilidade.com', str(df2)
        html_content = render_to_string('blog/name.html', {'data_barchart':data_barchart, 'talk':talk}) # render with dynamic value
        text_content = strip_tags(answers) # Strip the html tag. So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


        return render_to_response('blog/thankyou2.html')

    except Exception:
        return render_to_response('blog/apologies.html')


def migracao(request):
    return render_to_response('blog/migre.html')




from django.core.mail.message import EmailMessage
from .models import IGPM
from django.http import HttpResponseRedirect
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import xmltodict

def XML(request):
    try:
        if request.method == 'POST' and request.FILES['tnt']:
            myfile = request.FILES['tnt']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            with open(filename) as fd:
                doc = xmltodict.parse(fd.read())
            if doc['nfeProc']['NFe']['infNFe']['emit']['CNPJ'] == '33804832000110' and doc['nfeProc']['NFe']['infNFe'] ['ide']['natOp'][0:5] == 'VENDA':
                historico='NF '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' a '+doc['nfeProc']['NFe']['infNFe']['dest']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF'])
                # for index,row in df.iterrows():
                #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'car'
                accounting.credit = 'receita'
                accounting.save()


                historico='ICMS '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' a '+doc['nfeProc']['NFe']['infNFe']['dest']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vICMS'])
                        # for index,row in df.iterrows():
                        #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'desp ICMS'
                accounting.credit = 'ICMS a recolher'
                accounting.save()


                historico='PIS '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' a '+doc['nfeProc']['NFe']['infNFe']['dest']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vPIS'])
                        # for index,row in df.iterrows():
                        #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'desp PIS'
                accounting.credit = 'PIS a recolher'
                accounting.save()


                historico='COFINS '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' a '+doc['nfeProc']['NFe']['infNFe']['dest']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vCOFINS'])
                        # for index,row in df.iterrows():
                        #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'desp COFINS'
                accounting.credit = 'COFINS a recolher'
                accounting.save()


            elif doc['nfeProc']['NFe']['infNFe']['emit']['CNPJ'] == '33804832000110' and doc['nfeProc']['NFe']['infNFe'] ['ide']['natOp'][0:5] != 'VENDA':
                historico='ICMS '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' a '+doc['nfeProc']['NFe']['infNFe']['dest']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vICMS'])
                        # for index,row in df.iterrows():
                        #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'desp ICMS'
                accounting.credit = 'ICMS a recolher'
                accounting.save()


            elif doc['nfeProc']['NFe']['infNFe']['emit']['CNPJ'] != '33804832000110' and doc['nfeProc']['NFe']['infNFe'] ['ide']['natOp'][0:5] == 'VENDA' and doc['nfeProc']['NFe']['infNFe']['dest']['CNPJ'] == '33804832000110':
                historico='Compra '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' de '+doc['nfeProc']['NFe']['infNFe']['emit']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF'])
                        # for index,row in df.iterrows():
                        #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'custo'
                accounting.credit = 'Fornecedores'
                accounting.save()


            elif doc['nfeProc']['NFe']['infNFe']['emit']['CNPJ'] != '33804832000110' and doc['nfeProc']['NFe']['infNFe'] ['ide']['natOp'][0:5] != 'VENDA' and doc['nfeProc']['NFe']['infNFe']['dest']['CNPJ'] == '33804832000110':
                historico='Operacao Fiscal '+doc['nfeProc']['NFe']['infNFe']['ide']['nNF']+' '+doc['nfeProc']['NFe']['infNFe']['ide']['natOp']+' de '+doc['nfeProc']['NFe']['infNFe']['emit']['xNome']
                data = doc['nfeProc']['NFe']['infNFe']['ide']['dhEmi'][0:10]
                valor = float(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF'])
                        # for index,row in df.iterrows():
                        #     if row[0] != 'create_date':
                accounting = Accounting()
                accounting.history = historico
                accounting.date = data
                accounting.amount = valor
                accounting.debit = 'despesa'
                accounting.credit = 'Fornecedores'
                accounting.save()


            elif doc['nfeProc']['NFe']['infNFe']['emit']['CNPJ'] != '33804832000110' and doc['nfeProc']['NFe']['infNFe']['dest']['CNPJ'] != '33804832000110':
                return HttpResponse('NF nao pertence a esta empresa')

            else:
                return HttpResponse('NF parece estar inconsistente, verifique')

            return render_to_response('blog/thankyou2.html')
    except Exception:
        return HttpResponse('NF ja foi importada')

    else:
        return render(request, 'blog/import.html')




def employees_Data(request):
    if request.method == 'POST':
        form = employeesFORM(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('blog/thankyou2.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = employeesFORM()
    return render(request, 'blog/employees.html', {'form': form})




def holerite_Data(request):
    if request.method == 'POST':
        form = holeriteFORM(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('blog/thankyou2.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = holeriteFORM()
    return render(request, 'blog/holerite.html', {'form': form})
