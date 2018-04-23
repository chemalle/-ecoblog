from django.contrib import admin

# Register your models here.
from blog.models import (Post, Comment, Document, Balance_Sheet, Question, Choice,
                        Accounting, Site, MyPlan, ECD01, Prediction,Dolar, IGPM,Selic, Stocks, employees, holerite)



class SiteAdmin(admin.ModelAdmin):
    list_display =["__str__","site"]
    list_filter = ["site"]
    class Meta:
        model = Site
        fields = ("site")

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Document)
admin.site.register(Balance_Sheet)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Accounting)
admin.site.register(Site)
admin.site.register(MyPlan)
admin.site.register(ECD01)
admin.site.register(Prediction)
admin.site.register(Dolar)
admin.site.register(IGPM)
admin.site.register(Selic)
admin.site.register(Stocks)
admin.site.register(employees)
admin.site.register(holerite)
