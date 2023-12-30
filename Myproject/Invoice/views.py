from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Model_Invoice, Model_Invoice_Detail
from Invoice.urls import *
from .forms import *

# Create your views here.

def get_data(request): 
    if request.method == "POST":
        invoice_form = InvoiceForm(request.POST)
        invoice_detail_form = InvoiceDetailForm(request.POST)
        if invoice_form.is_valid() and invoice_detail_form.is_valid():
            invoice = invoice_form.save()
            invoice_detail = invoice_detail_form.save(commit=False)
            invoice_detail.invoice = invoice
            invoice_detail.save()
            messages.success(request,"Thank you")
            return redirect('invoice')
        else:
            messages.error(request,"Please fill the required fields!")
    else:
        invoice_form = InvoiceForm()
        invoice_detail_form = InvoiceDetailForm()
    data = Model_Invoice_Detail.objects.all()
    return render(request, "invoice.html", {'invoice': invoice_form, 'invoiceDetail':invoice_detail_form, 'data':data})



def update(request,id):
    mid = Model_Invoice_Detail.objects.get(pk=id)
    if request.method=="POST":
        idf = InvoiceDetailForm(request.POST,request.FILES,instance=mid)
        if idf.is_valid():
            var_description = idf.cleaned_data['description']
            var_quantity = idf.cleaned_data['quantity']
            var_unitprice = idf.cleaned_data['unitprice']
            var_price = idf.cleaned_data['price']
            print(var_description,var_quantity,var_unitprice,var_price)
            idf.save()
            messages.success(request,"Update successfully")
            return redirect('invoice')
        else:
            print("Form not valid.")
            messages.error(request,"Something went wrong!!!")
    else:
        idf = InvoiceDetailForm(instance=mid)
    template = "update.html"
    return render(request, template, {'form':idf, 'key':mid})

def remove(request,id):
    data = Model_Invoice_Detail.objects.get(pk=id)
    data.delete()
    messages.success(request,"Data deleted successfully")
    return redirect('invoice')