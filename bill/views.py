from django.shortcuts import render
import random
from datetime import date


from bill.models import Vendor
from invoice.models import Customer, Master

# Create your views here.
def vendor_home_page(request):
    customer=Customer.objects.all()
    product=Master.objects.all()
    v_billno=random.randint(11111,99999)
    v_date=today = date.today()
    if request.method=='POST':
        v_name=request.POST['n_ame']
        bill=Vendor(name=v_name,date=v_date,bill_no=v_billno)
        bill.save()
    vendor=Vendor.objects.all()
    return render(request,'billapp/vendor_home_page.html',{'customer':customer,'pro':product,'ven':vendor})

