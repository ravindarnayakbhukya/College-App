from django.shortcuts import render

# Create your views here.

def feeCollection(request):
    return render(request,'finance/fee collection.html')

def feeDueReport(request):
    return render(request,'finance/fee due report.html')

def feeCollectionReport(request):
    return render(request,'finance/fee collection report.html')
