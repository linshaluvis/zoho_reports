
def Salesbycustomer(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        log_details= LoginDetails.objects.get(id=log_id)
        if log_details.user_type == 'Company':
            cmp = CompanyDetails.objects.get(login_details = log_details)
            dash_details = CompanyDetails.objects.get(login_details=log_details)
        else:
            cmp = StaffDetails.objects.get(login_details = log_details).company
            dash_details = StaffDetails.objects.get(login_details=log_details)

        # rec = RecurringInvoice.objects.filter(company = cmp)
        allmodules= ZohoModules.objects.get(company = cmp)
        reportData = []
        totInv = 0
        totRecInv = 0
        totCrdNote = 0
        subTot = 0
        subTotWOCrd = 0
        totjour =0

        cust = Customer.objects.filter(company=cmp)
        
        for c in cust:
            customerName = c.first_name +" "+c.last_name
            count = 0
            sales = 0

            inv = invoice.objects.filter(customer=c, status = 'Saved')
            recInv = RecurringInvoice.objects.filter(customer=c, status = 'Saved')
            crd = Credit_Note.objects.filter(customer=c, status = 'Saved')
        
            

            for i in inv:
                sales += float(i.grand_total)
                totInv += float(i.grand_total)
                subTot += float(i.sub_total)
                subTotWOCrd += float(i.sub_total)

            for r in recInv:
                sales += float(r.grandtotal)
                totRecInv += float(r.grandtotal)
                subTot += float(r.subtotal)
                subTotWOCrd += float(r.subtotal)

            for n in crd:
                sales -= float(n.grand_total)
                totCrdNote += float(n.grand_total)
                subTot -= float(n.sub_total)
            
           

            count = len(inv) + len(recInv) + len(crd)

            details = {
                'name': customerName,
                'count':count,
                'sales':sales
            }

            reportData.append(details)

        totCust = len(cust)
        totSale = totInv + totRecInv - totCrdNote 
        totSaleWOCrdNote = totInv + totRecInv 

        context = {
            'allmodules':allmodules, 'details':dash_details,'log_details':log_details , 'cmp':cmp,'reportData':reportData,
            'totalCustomers':totCust, 'totalInvoice':totInv, 'totalRecInvoice':totRecInv, 'totalCreditNote': totCrdNote,
            'subtotal':subTot, 'subtotalWOCredit':subTotWOCrd, 'totalSale':totSale, 'totalSaleWOCredit':totSaleWOCrdNote,
            'startDate':None, 'endDate':None
        }
        
        
        return render(request, 'zohomodules/Reports/sales_by_customer.html', context)
    else:
        return redirect('/')
        