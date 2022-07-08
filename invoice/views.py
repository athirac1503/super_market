
from django.shortcuts import render
from datetime import date
import random

from invoice.models import Customer, CustomerReg, Master


# Create your views here.
def customer_home_page(request):
    customer=Customer.objects.all()
    product=Master.objects.all()
    if request.method=='POST':
        current_product=request.session['item_id']
        product=Master.objects.get(id=current_product)
        
        cust_phone=request.POST['number']
        cust_name=request.POST['n_ame']
        pro_name=request.POST['item1']
        qty=request.POST['q_ty']
        pro_unit=request.POST['u_nit']
        customer_no=random.randint(11111,99999)
        c_date=today = date.today()
        customer=Customer(phone=cust_phone,name=cust_name,date=c_date,invoice_no=customer_no,item_name=pro_name,quantity=qty,unit=pro_unit,product_id=product)
        customer.save()
    
    return render(request,'customer/customer_home_page.html',{'customer':customer,'pro':product})

def customer_reg(request):
    # customer_no=random.randint(11111,99999)
    # c_date=today = date.today()
    # if request.method=='POST':
    #     cust_phone=request.POST['number']
    #     cust_name=request.POST['n_ame']
    #     pro_name=request.POST['item']
    #     qty=request.POST['q_ty']
    #     pro_unit=request.POST['u_nit']
    #     customer=CustomerReg(phone=cust_phone,name=cust_name,date=c_date,invoice_no=customer_no,item_name=pro_name,quantity=qty,unit=pro_unit)
    #     request.session['customer_id']=customer.id
    #     customer.save()
    return render(request,'customer/customer_reg.html')

def item_master(request):
        if request.method=='POST':
            i_code=request.POST['code']
            name=request.POST['n_ame']
            item_price=request.POST['p_rice']
            stk=request.POST['stock']
            item=Master(item_code=i_code,item_name=name,price=item_price,stock=stk)
            item.save()
            request.session['item_id']=item.id
        return render(request,'customer/item_master.html')