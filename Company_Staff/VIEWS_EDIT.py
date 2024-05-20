def customerBalances(request):
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
    
    
        
        cust = Customer.objects.filter(company=cmp)
        print(cust)
        
        customers_data = []
        total_balance1 = 0 
        invoice_balance1=0
        recurring_invoice_balance1=0
        available_credits1=0
        recurring_invoice_balance=0
        available_credits=0
        total_invoice_balance1=0
        total_invoice_balance=0

        totCust = 0

        # Initialize total balance outside the loop
        for customer in cust:
            customerName = customer.first_name +" "+customer.last_name
            print(customerName)

            invoices = invoice.objects.filter(customer=customer, status='Saved')
            print(invoices)
            recurring_invoices = RecurringInvoice.objects.filter(customer=customer, status='Saved')
            print(recurring_invoices)
            credit_notes = Credit_Note.objects.filter(customer=customer, status='Saved')
            print(credit_notes)
            invoice_balance = sum(float(inv.balance) for inv in invoices)
            recurring_invoice_balance = sum(float(rec_inv.balance) for rec_inv in recurring_invoices)
            total_invoice_balance = invoice_balance + recurring_invoice_balance
            
            available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
            
            total_balance = total_invoice_balance - available_credits
            
            # Update the total balance
            total_balance1 += total_balance
            totCust = len(cust)
            invoice_balance1 += invoice_balance
            recurring_invoice_balance1 += recurring_invoice_balance
            available_credits1 += available_credits
            total_invoice_balance1+=total_invoice_balance
            print(total_invoice_balance)
            print(total_balance)
            
            



            customers_data.append({
                'name': customerName,                
                'invoice_balance': total_invoice_balance,
                'available_credits': available_credits,
                'total_balance': total_balance,
            })
        
            context = {
            'cust':cust,
            'customers': customers_data,
            'total_balance1': total_balance1,
            'allmodules':allmodules,
            'details':dash_details,
            'log_details':log_details , 
            'cmp':cmp,
             'totalCustomers':totCust,
             'totalInvoice':invoice_balance1,
             'totalRecInvoice':recurring_invoice_balance1, 
             'totalCreditNote': available_credits1,
             'invoice_balance':total_invoice_balance,
            'available_credits': available_credits,
            'total_invoice_balance':total_invoice_balance1,
            'invoice_c_present': True,
            'cnote_c_present': True,

             }
        
        return render(request, 'zohomodules/Reports/customerbalances.html', context)
    else:
        return redirect('/')
    

def Fin_customize_aging_summary(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id = s_id)
            cmp = com
        else:
            com = Fin_Staff_Details.objects.get(Login_Id = s_id)
            cmp = com.company_id
        
        allmodules = Fin_Modules_List.objects.get(company_id = cmp,status = 'New')

        startDate = request.GET['from_date']
        endDate = request.GET['to_date']
        if startDate == "":
            startDate = None
        if endDate == "":
            endDate = None

        aging_by = request.GET.get('aging_by')
        if aging_by == '' or aging_by == None:
            aging_by = 'inv_due_date'

        age_interval = int(request.GET['age_interval'])

        if age_interval == 0:
            age_interval = 4

        try:
            day_interval = int(request.GET['day_interval'])
        except:
            day_interval = 15

        try:
            show_by = request.GET['show_by']
        except:
            show_by = 'inv_amt'

        if 'cust_email_show' in request.GET:
            cemail = request.GET['cust_email_show']
        else:
            cemail = None

        if 'cust_fname_show' in request.GET:
            cfname = request.GET['cust_fname_show']
        else:
            cfname = None

        if 'cust_lname_show' in request.GET:
            clname = request.GET['cust_lname_show']
        else:
            clname = None

        if 'cust_phone_show' in request.GET:
            cphno = request.GET['cust_phone_show']
        else:
            cphno = None

        first_interval = 1
        last_interval = day_interval
        interval_data = []
        day_count = []
        for i in range(age_interval):
            if i == age_interval -1 :
                interval_data.append(f'> {first_interval - 1} Days')
            else:
                interval_data.append(f'{first_interval} - {last_interval} Days')
            first_interval = last_interval + 1
            last_interval += day_interval
            day_count.append(first_interval)
        
        cust = Fin_Customers.objects.filter(Company = cmp)
        reportData = []
        total_matrix = []
        total_matrix += [0] * age_interval
        total_current = 0
        final_balance = 0
        cust_no = 0

        for c in cust:
            current = 0
            custemail = c.email
            custfname = c.first_name
            custlname = c.last_name
            custphno = c.mobile
            day_matrix = []
            day_matrix += [0] * age_interval
            if startDate and endDate:
                if aging_by == 'inv_due_date':
                    invo = Fin_Invoice.objects.filter(Customer=c, duedate__range = [startDate, endDate], status = 'Saved')
                    rinvo = Fin_Recurring_Invoice.objects.filter(Customer=c, end_date__range = [startDate, endDate], status = 'Saved')
                else:
                    invo = Fin_Invoice.objects.filter(Customer=c, invoice_date__range = [startDate, endDate], status = 'Saved')
                    rinvo = Fin_Recurring_Invoice.objects.filter(Customer=c, start_date__range = [startDate, endDate], status = 'Saved')
            else:
                invo = Fin_Invoice.objects.filter(Customer=c, status = 'Saved')
                rinvo = Fin_Recurring_Invoice.objects.filter(Customer=c, status = 'Saved')
            for i in invo:
                if float(i.balance) > 0: 
                    if aging_by == 'inv_due_date':
                        days = int((i.duedate - date.today()).days)
                        if days <= 0:
                            days = days*-1
                            if days == 0:
                                if show_by == 'inv_amt':
                                    current += float(i.balance)
                                else:
                                    current += 1
                            else:
                                for index in range(age_interval):
                                    if days < day_count[index]:
                                        if show_by == 'inv_amt':
                                            day_matrix[index] += i.balance
                                        else:
                                            day_matrix[index] += 1
                                        break
                                else:
                                    if show_by == 'inv_amt':
                                        day_matrix[-1] += i.balance
                                    else:
                                        day_matrix[-1] += 1

                    elif aging_by == 'inv_date':
                        if int((i.duedate - date.today()).days) >= 0:
                            days = int((date.today() - i.invoice_date).days)
                            if days <= 0:
                                days = days*-1
                            if days == 0:
                                if show_by == 'inv_amt':
                                    current += float(i.balance)
                                else:
                                    current += 1
                            else:
                                for index in range(age_interval):
                                    if days < day_count[index]:
                                        if show_by == 'inv_amt':
                                            day_matrix[index] += i.balance
                                        else:
                                            day_matrix[index] += 1
                                        break
                                else:
                                    if show_by == 'inv_amt':
                                        day_matrix[-1] += i.balance
                                    else:
                                        day_matrix[-1] += 1

            for i in rinvo:
                if float(i.balance) > 0: 
                    if aging_by == 'inv_due_date':
                        days = int((i.end_date - date.today()).days)
                        if days <= 0:
                            days = days*-1
                            if days == 0:
                                if show_by == 'inv_amt':
                                    current += float(i.balance)
                                else:
                                    current += 1
                            else:
                                for index in range(age_interval):
                                    if days < day_count[index]:
                                        if show_by == 'inv_amt':
                                            day_matrix[index] += i.balance
                                        else:
                                            day_matrix[index] += 1
                                        break
                                else:
                                    if show_by == 'inv_amt':
                                        day_matrix[-1] += i.balance
                                    else:
                                        day_matrix[-1] += 1

                    elif aging_by == 'inv_date':
                        if int((i.end_date - date.today()).days) >= 0:
                            days = int((i.start_date - date.today()).days)
                            if days <= 0:
                                days = days*-1
                            if days == 0:
                                if show_by == 'inv_amt':
                                    current += float(i.balance)
                                else:
                                    current += 1
                            else:
                                for index in range(age_interval):
                                    if days < day_count[index]:
                                        if show_by == 'inv_amt':
                                            day_matrix[index] += i.balance
                                        else:
                                            day_matrix[index] += 1
                                        break
                                else:
                                    if show_by == 'inv_amt':
                                        day_matrix[-1] += i.balance
                                    else:
                                        day_matrix[-1] += 1

            total_balance = current + sum(day_matrix)
            final_balance += total_balance
            total_current += current
            total_matrix = [x + y for x, y in zip(total_matrix, day_matrix)]

            if total_balance != 0:
                details = {
                    'custemail':custemail,
                    'custfname': custfname,
                    'custlname': custlname,
                    'custphno': custphno,
                    'current': current,
                    'day_matrix': day_matrix,
                    'total_balance':total_balance
                }
                reportData.append(details)
                cust_no += 1

        context = {
            'allmodules':allmodules, 'com':com, 'cmp':cmp, 'interval_data':interval_data, 'reportData':reportData, 'cust_no':cust_no, 'total_current':total_current,
            'final_balance':final_balance, 'total_matrix':total_matrix, 'startDate': startDate, 'endDate':endDate, 'aging_by':aging_by, 'age_interval':age_interval, 
            'day_interval':day_interval, 'show_by':show_by, 'cemail':cemail, 'cfname':cfname, 'clname':clname, 'cphno':cphno
        }