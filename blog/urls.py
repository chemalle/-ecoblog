from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/$',views.PostListView.as_view(),name='about'),
    url(r'^$',views.AboutView.as_view(),name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^document/$', views.model_form_upload, name='form_upload'),#foi apenas um teste que virou a url 2018
    url(r'^2018/$', views.model_form_upload, name='form_upload'),#algoritmo de conversao xls
    url(r'^Demonstrativos/$', views.Statements_Upload, name='statements'),# algoritmo que gera o balanço
    url(r'^download/$', views.excel_download, name='excel'),# isto realiza o download
    url(r'^modelos/$', views.download, name='modelo'),#esta é apenas a interface para o download
    url(r'^var/$', views.index, name='index'),
    url(r'^convert/$', views.get_data, name='teste'),
    url(r'^import/', views.import_data, name="import"),
    url(r'^accounting/', views.import_Accounting, name="accountant"),
    url(r'^handson_view/', views.handson_table, name="handson_view"),
    url(r'^handson_view_accounting/', views.handson_table_accounting, name="handson_view_accounting"),
    url(r'^Accounting_query/$', views.Statements_Upload_Accounting, name='statements_query'),
    url(r'^Area_Cliente/$', views.User, name='customers_site'),
    url(r'^email_marketplace/$', views.email_marketplace, name='email_marketplace'),
    url(r'^email/$',views.email,name='email'),
    url(r'^thanks/$',views.thanks,name='thanks'),
    url(r'^myplan/$',views.plan_form,name='myplan'),
    url(r'^myplanmail/$',views.plan_form_mail,name='myplanmail'),
    url(r'^myplanBusiness/$',views.plan_form_mail_Business,name='Business'),
    url(r'^myplanCorporate/$',views.plan_form_mail_Corporate,name='Corporate'),
    url(r'^cadastro/$',views.cadastro,name='CADASTRO'),
    url(r'^ECD/$',views.ECD,name='ECD'),
    url(r'^download_CSV/$', views.download_CSV, name='CSV'),
    url(r'^prediction/$', views.Prediction_Data, name='prediction'),
    url(r'^dolar/$', views.data, name='dolar'),
    url(r'^IGPM/$', views.data_IGPM, name='IGPM'),
    url(r'^Selic/$', views.data_Selic, name='Selic'),
    url(r'^forecast/$', views.forecast, name='forecast'),
    url(r'^stocks/$', views.Stocks_Data, name='stocks'),
    url(r'^recommendation/$', views.recommendation, name='recommendation'),
    url(r'^migre/$', views.migracao, name='migrar'),
    url(r'^xml/$', views.XML, name='xml'),
    url(r'^employees/$', views.employees_Data, name='employees'),
    url(r'^holerite/$', views.holerite_Data, name='holerite'),

]
