
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
            custemail = customer.customer_email
            custfname = customer.first_name
            custlname = customer.last_name
            custphno = customer.customer_mobile

            invoices = invoice.objects.filter(customer=customer, status='Saved')
            recurring_invoices = RecurringInvoice.objects.filter(customer=customer, status='Saved')
            credit_notes = Credit_Note.objects.filter(customer=customer, status='Saved')
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
            

            customers_data.append({
                'name': customerName, 
                'custemail':custemail,
                'custfname': custfname,
                'custlname': custlname,
                'custphno': custphno,               
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
            'cemail':None, 
            'cfname':'on', 
            'clname':'on', 
            'cphno':None

             }
        
        return render(request, 'zohomodules/Reports/customerbalances.html', context)
    else:
        return redirect('/')
    

def CustomizecustomerBalances(request):
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
        allmodules= ZohoModules.objects.get(company = cmp)
        cust = Customer.objects.filter(company=cmp)

        customers_data = []
        total_balance1 = 0
        invoice_balance1 = 0
        recurring_invoice_balance1 = 0
        available_credits1 = 0
        invoice_balance=0
        total_invoice_balance1 = 0
        totCust = 0
        recurring_invoice_balance = 0
        total_invoice_balance = 0
        available_credits = 0
        total_balance=0

        # Get the start date from POST data with a default value of None
     
        if 'from_date' in request.POST:
            start_date_str = request.POST['from_date']
        else:
            start_date_str = None
        if 'to_date' in request.POST:
            end_date_str = request.POST['to_date']
        else:
            end_date_str = None
        
        

        if 'include_invoice' in request.POST:
            invoice_c = request.POST['include_invoice']
        else:
            invoice_c = ''

        if 'include_cnote' in request.POST:
            cnote_c = request.POST['include_cnote']
        else:
            cnote_c = ''

        if 'transactions' in request.POST:
            name = request.POST['transactions']
        else:
            name = None
       # Handling 'cust_email_show' checkbox
        if 'cust_email_show' in request.POST:
            cemail = request.POST['cust_email_show']
        else:
            cemail = None

        # Handling 'cust_fname_show' checkbox
        if 'cust_fname_show' in request.POST:
            cfname = request.POST['cust_fname_show']
        else:
            cfname = None

        # Handling 'cust_lname_show' checkbox
        if 'cust_lname_show' in request.POST:
            clname = request.POST['cust_lname_show']
        else:
            clname = None

        # Handling 'cust_phone_show' checkbox
        if 'cust_phone_show' in request.POST:
            cphno = request.POST['cust_phone_show']
        else:
            cphno = None

        # Convert start_date and end_date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

        if name == 'all':
            for customer in cust:
                customerName = customer.first_name + " " + customer.last_name
                custemail = customer.customer_email
                custfname = customer.first_name
                custlname = customer.last_name
                custphno = customer.customer_mobile
                invoices = invoice.objects.filter(customer=customer, status='Saved')
                recurring_invoices = RecurringInvoice.objects.filter(customer=customer, status='Saved')
                credit_notes = Credit_Note.objects.filter(customer=customer, status='Saved')

                # Filter invoices based on start_date and end_date if provided
                if start_date and end_date:
                    invoices = invoices.filter(date__range=[start_date, end_date])
                    recurring_invoices = recurring_invoices.filter(start_date__range=[start_date, end_date])
                    credit_notes = credit_notes.filter(credit_note_date__range=[start_date, end_date])


                # Calculate invoice balance only if 'invoice_c_present' is true
                if invoice_c:
                    invoice_balance = sum(float(inv.balance) for inv in invoices)
                    
                    recurring_invoice_balance = sum(float(rec_inv.balance) for rec_inv in recurring_invoices)
                    total_invoice_balance = invoice_balance + recurring_invoice_balance
                    available_credits = 0 
                    total_balance = total_invoice_balance - available_credits

                if cnote_c:
                    available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                    invoice_balance = 0  # Set invoice balance to 0
                    recurring_invoice_balance = 0
                    total_invoice_balance = 0
                    total_balance = total_invoice_balance - available_credits

                if  invoice_c and cnote_c:
                    invoice_balance = sum(float(inv.balance) for inv in invoices)
                    
                    recurring_invoice_balance = sum(float(rec_inv.balance) for rec_inv in recurring_invoices)
                    available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                    total_invoice_balance = invoice_balance + recurring_invoice_balance
                    total_balance = total_invoice_balance - available_credits

                    # Update the total balance
                total_balance1 += total_balance
                totCust = len(cust)
                invoice_balance1 += invoice_balance
                recurring_invoice_balance1 += recurring_invoice_balance
                available_credits1 += available_credits
                total_invoice_balance1 += total_invoice_balance

                

                customers_data.append({
                        'name': customerName,
                        'custemail':custemail,
                        'custfname': custfname,
                        'custlname': custlname,
                        'custphno': custphno,
                        'invoice_balance': total_invoice_balance,
                        'available_credits': available_credits,
                        'total_balance': total_balance,
                    })

        else:
            for customer in cust:
                customerName = customer.first_name + " " + customer.last_name
                custemail = customer.customer_email
                custfname = customer.first_name
                custlname = customer.last_name
                custphno = customer.customer_mobile

                # Check if the name matches the filter, if provided
                if name and name != customerName:
                    continue


                # Initialize total balance outside the loop
                for customer in cust:
                    customerName = customer.first_name + " " + customer.last_name
                    custemail = customer.customer_email
                    custfname = customer.first_name
                    custlname = customer.last_name
                    custphno = customer.customer_mobile

                    # Check if the name matches the filter, if provided
                    if name and name != customerName:
                        continue

                    invoices = invoice.objects.filter(customer=customer, status='Saved')
                    recurring_invoices = RecurringInvoice.objects.filter(customer=customer, status='Saved')
                    credit_notes = Credit_Note.objects.filter(customer=customer, status='Saved')

                    # Filter invoices based on start_date and end_date if provided
                    if start_date and end_date:
                        invoices = invoices.filter(date__range=[start_date, end_date])
                        recurring_invoices = recurring_invoices.filter(start_date__range=[start_date, end_date])
                        credit_notes = credit_notes.filter(credit_note_date__range=[start_date, end_date])

                    # Calculate invoice balance only if 'bills' is true
                    if invoice_c:
                        invoice_balance = sum(float(inv.balance) for inv in invoices)
                        recurring_invoice_balance = sum(float(rec_inv.balance) for rec_inv in recurring_invoices)
                        total_invoice_balance = invoice_balance + recurring_invoice_balance
                        available_credits = 0  # Set credit note balance to 0
                    if cnote_c:
                        available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                        invoice_balance = 0  # Set invoice balance to 0
                        recurring_invoice_balance = 0
                        total_invoice_balance = 0
                    if cnote_c and invoice_c:
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
                    total_invoice_balance1 += total_invoice_balance

                    customers_data.append({
                        'name': customerName,
                        'custemail':custemail,
                        'custfname': custfname,
                        'custlname': custlname,
                        'custphno': custphno,
                        'invoice_balance': total_invoice_balance,
                        'available_credits': available_credits,
                        'total_balance': total_balance,
                    })

        context = {
            'cust':cust,
            'customers': customers_data,
            'total_balance1': total_balance1,
            'cmp': cmp,
            'allmodules': allmodules,
            'details':dash_details,
            'log_details':log_details , 

            'totalCustomers': totCust,
            'totalInvoice': invoice_balance1,
            'totalRecInvoice': recurring_invoice_balance1,
            'totalCreditNote': available_credits1,
            'invoice_balance': total_invoice_balance,
            'available_credits': available_credits,
            'total_invoice_balance': total_invoice_balance1,
            'start_date': start_date_str,  # Pass start_date to the template
            'end_date': end_date_str,  # Pass end_date to the template
            'name': name,  # Pass name to the template
            'invoice_c_present': bool(invoice_c),
            'cnote_c_present': bool(cnote_c),
             'cemail':cemail, 'cfname':cfname, 'clname':clname, 'cphno':cphno
        }

        return render(request,'zohomodules/Reports/customerbalances.html', context)
    else:
        return redirect('/')
        

def sharecustomerBalances(request):
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

        if request.method == 'POST':
            emails_string = request.POST['email_ids']

            # Split the string by commas and remove any leading or trailing whitespace
            emails_list = [email.strip() for email in emails_string.split(',')]
            email_message = request.POST['email_message']        
            startDate = request.POST['start']
            endDate = request.POST['end']
            if startDate == "":
                startDate = None
            if endDate == "":
                endDate = None
            cust = Customer.objects.filter(company=cmp) 

            customers_data = []
            total_balance1 = 0 
            invoice_balance1=0
            recurring_invoice_balance1=0
            available_credits1=0
            total_invoice_balance1=0

            # Initialize total balance outside the loop
            for customer in cust:
                customerName = customer.first_name +" "+customer.last_name
                customerName = customer.first_name +" "+customer.last_name
                custemail = customer.customer_email
                custfname = customer.first_name
                custlname = customer.last_name
                custphno = customer.customer_mobile

                invoices = invoice.objects.filter(customer=customer, status='Saved')
                recurring_invoices = RecurringInvoice.objects.filter(customer=customer, status='Saved')
                credit_notes = Credit_Note.objects.filter(customer=customer, status='Saved')
                        
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



                customers_data.append({
                    'name': customerName,  
                    'custemail':custemail,
                    'custfname': custfname,
                    'custlname': custlname,
                    'custphno': custphno,              
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
                    'cemail':None, 
                    'cfname':'on', 
                    'clname':'on', 
                    'cphno':None
                }
        

            template_path = 'zohomodules/Reports/sharecustomerBalancesPDF.html'
            template = get_template(template_path)
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            pdf = result.getvalue()

            filename = f'customerBalances'
            subject = f"customerBalances"
            email = EmailMsg(
                subject,
                f"Hi,\nPlease find the attached customerBalances Reports for\n{email_message}\n\n--\nRegards,\n{cmp.company_name}\n{cmp.address}\n{cmp.state} - {cmp.country}\n{cmp.contact}",
                from_email=settings.EMAIL_HOST_USER,
                to=emails_list
            )
            email.attach(filename, pdf, "application/pdf")
            email.send(fail_silently=False)

            messages.success(request, 'customerBalances Reports has been shared via email successfully..!')
            return redirect(customerBalances)

    

def vendorBalances(request):
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
    
    
        
        cust = Vendor.objects.filter(company=cmp)
        
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
            custemail = customer.vendor_email
            custfname = customer.first_name
            custlname = customer.last_name
            custphno = customer.mobile

            invoices = Bill.objects.filter(Vendor=customer, Status='Saved')
            recurring_invoices = Recurring_bills.objects.filter(vendor_details=customer, status='save')
            credit_notes = debitnote.objects.filter(vendor=customer, status='Saved')
            invoice_balance = sum(float(inv.Balance) for inv in invoices)
            recurring_invoice_balance = sum(float(rec_inv.bal) for rec_inv in recurring_invoices)
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
            

            customers_data.append({
                'name': customerName, 
                'custemail':custemail,
                'custfname': custfname,
                'custlname': custlname,
                'custphno': custphno,               
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
            'cemail':None, 
            'cfname':'on', 
            'clname':'on', 
            'cphno':None

            }
        
        return render(request, 'zohomodules/Reports/vendorBalances.html', context)
    else:
        return redirect('/')
    

def CustomizevendorBalances(request):
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
        allmodules= ZohoModules.objects.get(company = cmp)
        cust = Vendor.objects.filter(company=cmp)

        customers_data = []
        total_balance1 = 0
        invoice_balance1 = 0
        recurring_invoice_balance1 = 0
        available_credits1 = 0
        invoice_balance=0
        total_invoice_balance1 = 0
        totCust = 0
        recurring_invoice_balance = 0
        total_invoice_balance = 0
        available_credits = 0
        total_balance=0

        # Get the start date from POST data with a default value of None
     
        if 'from_date' in request.POST:
            start_date_str = request.POST['from_date']
        else:
            start_date_str = None
        if 'to_date' in request.POST:
            end_date_str = request.POST['to_date']
        else:
            end_date_str = None
        
        

        if 'include_invoice' in request.POST:
            invoice_c = request.POST['include_invoice']
        else:
            invoice_c = ''

        if 'include_cnote' in request.POST:
            cnote_c = request.POST['include_cnote']
        else:
            cnote_c = ''

        if 'transactions' in request.POST:
            name = request.POST['transactions']
        else:
            name = None
       # Handling 'cust_email_show' checkbox
        if 'cust_email_show' in request.POST:
            cemail = request.POST['cust_email_show']
        else:
            cemail = None

        # Handling 'cust_fname_show' checkbox
        if 'cust_fname_show' in request.POST:
            cfname = request.POST['cust_fname_show']
        else:
            cfname = None

        # Handling 'cust_lname_show' checkbox
        if 'cust_lname_show' in request.POST:
            clname = request.POST['cust_lname_show']
        else:
            clname = None

        # Handling 'cust_phone_show' checkbox
        if 'cust_phone_show' in request.POST:
            cphno = request.POST['cust_phone_show']
        else:
            cphno = None

        # Convert start_date and end_date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

        if name == 'all':
            for customer in cust:
                customerName = customer.first_name + " " + customer.last_name
                custemail = customer.vendor_email
                custfname = customer.first_name
                custlname = customer.last_name
                custphno = customer.mobile
                invoices = Bill.objects.filter(Vendor=customer, Status='Saved')
                recurring_invoices = Recurring_bills.objects.filter(vendor_details=customer, status='save')
                credit_notes = debitnote.objects.filter(vendor=customer, status='Saved')

                # Filter invoices based on start_date and end_date if provided
                if start_date and end_date:
                    invoices = invoices.filter(Bill_Date__range=[start_date, end_date])
                    recurring_invoices = recurring_invoices.filter(rec_bill_date__range=[start_date, end_date])
                    credit_notes = credit_notes.filter(debitnote_date__range=[start_date, end_date])


                # Calculate invoice balance only if 'invoice_c_present' is true
                if invoice_c:
                    invoice_balance = sum(float(inv.Balance) for inv in invoices)
                    
                    recurring_invoice_balance = sum(float(rec_inv.bal) for rec_inv in recurring_invoices)
                    total_invoice_balance = invoice_balance + recurring_invoice_balance
                    available_credits = 0 
                    total_balance = total_invoice_balance - available_credits

                if cnote_c:
                    available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                    invoice_balance = 0  # Set invoice balance to 0
                    recurring_invoice_balance = 0
                    total_invoice_balance = 0
                    total_balance = total_invoice_balance - available_credits

                if  invoice_c and cnote_c:
                    invoice_balance = sum(float(inv.Balance) for inv in invoices)
                    
                    recurring_invoice_balance = sum(float(rec_inv.bal) for rec_inv in recurring_invoices)
                    available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                    total_invoice_balance = invoice_balance + recurring_invoice_balance
                    total_balance = total_invoice_balance - available_credits

                    # Update the total balance
                total_balance1 += total_balance
                totCust = len(cust)
                invoice_balance1 += invoice_balance
                recurring_invoice_balance1 += recurring_invoice_balance
                available_credits1 += available_credits
                total_invoice_balance1 += total_invoice_balance

                

                customers_data.append({
                        'name': customerName,
                        'custemail':custemail,
                        'custfname': custfname,
                        'custlname': custlname,
                        'custphno': custphno,
                        'invoice_balance': total_invoice_balance,
                        'available_credits': available_credits,
                        'total_balance': total_balance,
                    })

        else:
            for customer in cust:
                customerName = customer.first_name + " " + customer.last_name
                custemail = customer.vendor_email
                custfname = customer.first_name
                custlname = customer.last_name
                custphno = customer.mobile

                # Check if the name matches the filter, if provided
                if name and name != customerName:
                    continue


                # Initialize total balance outside the loop
                for customer in cust:
                    customerName = customer.first_name + " " + customer.last_name
                    custemail = customer.vendor_email
                    custfname = customer.first_name
                    custlname = customer.last_name
                    custphno = customer.mobile

                    # Check if the name matches the filter, if provided
                    if name and name != customerName:
                        continue

                    invoices = Bill.objects.filter(Vendor=customer, Status='Saved')
                    recurring_invoices = Recurring_bills.objects.filter(vendor_details=customer, status='save')
                    credit_notes = debitnote.objects.filter(vendor=customer, status='Saved')

                    # Filter invoices based on start_date and end_date if provided
                    if start_date and end_date:
                        invoices = invoices.filter(Bill_Date__range=[start_date, end_date])
                        recurring_invoices = recurring_invoices.filter(rec_bill_date__range=[start_date, end_date])
                        credit_notes = credit_notes.filter(debitnote_date__range=[start_date, end_date])
                    # Calculate invoice balance only if 'bills' is true
                    if invoice_c:
                        invoice_balance = sum(float(inv.Balance) for inv in invoices)
                        recurring_invoice_balance = sum(float(rec_inv.bal) for rec_inv in recurring_invoices)
                        total_invoice_balance = invoice_balance + recurring_invoice_balance
                        available_credits = 0  # Set credit note balance to 0
                    if cnote_c:
                        available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                        invoice_balance = 0  # Set invoice balance to 0
                        recurring_invoice_balance = 0
                        total_invoice_balance = 0
                    if cnote_c and invoice_c:
                        invoice_balance = sum(float(inv.Balance) for inv in invoices)
                        recurring_invoice_balance = sum(float(rec_inv.bal) for rec_inv in recurring_invoices)
                        total_invoice_balance = invoice_balance + recurring_invoice_balance
                        available_credits = sum(float(credit_note.balance) for credit_note in credit_notes)
                        
                    total_balance = total_invoice_balance - available_credits
                    # Update the total balance
                    total_balance1 += total_balance
                    totCust = len(cust)
                    invoice_balance1 += invoice_balance
                    recurring_invoice_balance1 += recurring_invoice_balance
                    available_credits1 += available_credits
                    total_invoice_balance1 += total_invoice_balance

                    customers_data.append({
                        'name': customerName,
                        'custemail':custemail,
                        'custfname': custfname,
                        'custlname': custlname,
                        'custphno': custphno,
                        'invoice_balance': total_invoice_balance,
                        'available_credits': available_credits,
                        'total_balance': total_balance,
                    })

        context = {
            'cust':cust,
            'customers': customers_data,
            'total_balance1': total_balance1,
            'cmp': cmp,
            'allmodules': allmodules,
            'details':dash_details,
            'log_details':log_details , 

            'totalCustomers': totCust,
            'totalInvoice': invoice_balance1,
            'totalRecInvoice': recurring_invoice_balance1,
            'totalCreditNote': available_credits1,
            'invoice_balance': total_invoice_balance,
            'available_credits': available_credits,
            'total_invoice_balance': total_invoice_balance1,
            'start_date': start_date_str,  # Pass start_date to the template
            'end_date': end_date_str,  # Pass end_date to the template
            'name': name,  # Pass name to the template
            'invoice_c_present': bool(invoice_c),
            'cnote_c_present': bool(cnote_c),
             'cemail':cemail, 'cfname':cfname, 'clname':clname, 'cphno':cphno
        }

        return render(request,'zohomodules/Reports/vendorBalances.html', context)
    else:
        return redirect('/')
        

def sharevendorBalances(request):
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
    
    
        
        cust = Vendor.objects.filter(company=cmp) 

        if request.method == 'POST':
            emails_string = request.POST['email_ids']

            # Split the string by commas and remove any leading or trailing whitespace
            emails_list = [email.strip() for email in emails_string.split(',')]
            email_message = request.POST['email_message']        
            startDate = request.POST['start']
            endDate = request.POST['end']
            if startDate == "":
                startDate = None
            if endDate == "":
                endDate = None
            cust = Vendor.objects.filter(company=cmp) 

            customers_data = []
            total_balance1 = 0 
            invoice_balance1=0
            recurring_invoice_balance1=0
            available_credits1=0
            total_invoice_balance1=0

            # Initialize total balance outside the loop
            for customer in cust:
                customerName = customer.first_name +" "+customer.last_name
                custemail = customer.vendor_email
                custfname = customer.first_name
                custlname = customer.last_name
                custphno = customer.mobile

                invoices = Bill.objects.filter(Vendor=customer, Status='Saved')
                recurring_invoices = Recurring_bills.objects.filter(vendor_details=customer, status='save')
                credit_notes = debitnote.objects.filter(vendor=customer, status='Saved')
                        
                invoice_balance = sum(float(inv.Balance) for inv in invoices)
                recurring_invoice_balance = sum(float(rec_inv.bal) for rec_inv in recurring_invoices)
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



                customers_data.append({
                    'name': customerName,  
                    'custemail':custemail,
                    'custfname': custfname,
                    'custlname': custlname,
                    'custphno': custphno,              
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
                    'cemail':None, 
                    'cfname':'on', 
                    'clname':'on', 
                    'cphno':None
                }
        

            template_path = 'zohomodules/Reports/vendorbalancepdf.html'
            template = get_template(template_path)
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            pdf = result.getvalue()

            filename = f'vendorbalance'
            subject = f"vendorbalance"
            email = EmailMsg(
                subject,
                f"Hi,\nPlease find the attached vendor balance Reports for\n{email_message}\n\n--\nRegards,\n{cmp.company_name}\n{cmp.address}\n{cmp.state} - {cmp.country}\n{cmp.contact}",
                from_email=settings.EMAIL_HOST_USER,
                to=emails_list
            )
            email.attach(filename, pdf, "application/pdf")
            email.send(fail_silently=False)

            messages.success(request, 'vendor balance Reports has been shared via email successfully..!')
            return redirect(vendorBalances)
            
            
