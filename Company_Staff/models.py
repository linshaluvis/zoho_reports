#Zoho Final
from django.db import models
from Register_Login.models import *
from django.contrib.auth.models import User
from Register_Login.models import LoginDetails,CompanyDetails
from Register_Login.models import LoginDetails,CompanyDetails,Company_Payment_Term
from datetime import datetime
from datetime import date
from django.utils import timezone

# Create your models here.

#---------------- models for zoho modules--------------------
# TINTO -----ITEM ----START

class Unit(models.Model):
 
    unit_name=models.CharField(max_length=255)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)


class Items(models.Model):
   
    item_type=models.CharField(max_length=255)
    item_name=models.CharField(max_length=255)
   
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    hsn_code=models.IntegerField(null=True,blank=True)
    tax_reference=models.CharField(max_length=255,null=True)
    intrastate_tax=models.IntegerField(null=True,blank=True)
    interstate_tax=models.IntegerField(null=True,blank=True)

    selling_price=models.IntegerField(null=True,blank=True)
    sales_account=models.CharField(max_length=255)
    sales_description=models.CharField(max_length=255)

    purchase_price=models.IntegerField(null=True,blank=True)
    purchase_account=models.CharField(max_length=255)
    purchase_description=models.CharField(max_length=255)
   
    minimum_stock_to_maintain=models.IntegerField(blank=True,null=True)  
    activation_tag=models.CharField(max_length=255,default='active')
    inventory_account=models.CharField(max_length=255,null=True)

    date=models.DateTimeField(auto_now_add=True)                                       

    opening_stock=models.IntegerField(blank=True,null=True,default=0)
    current_stock=models.IntegerField(blank=True,null=True,default=0)
    opening_stock_per_unit=models.IntegerField(blank=True,null=True,)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

    type=models.CharField(max_length=255,blank=True,null=True)

    track_inventory=models.IntegerField(blank=True,null=True)

class Item_Transaction_History(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    items=models.ForeignKey(Items,on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    action=models.CharField(max_length=255,default='Created')

class Items_comments(models.Model):                                              
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    Items=models.ForeignKey(Items,on_delete=models.CASCADE)
    comments = models.CharField(max_length=255,null=True,blank=True)


# TINTO -----ITEM ----END
    
# TINTO -----CHART OF ACCOUNNTS ----START
    
class Chart_of_Accounts(models.Model):
  
    account_type = models.CharField(max_length=255,null=True,blank=True)
    account_name = models.CharField(max_length=255,null=True,blank=True)

    account_description = models.CharField(max_length=255,null=True,blank=True)

    account_number = models.CharField(max_length=255,null=True,blank=True)
    
    account_code = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True,default='Active')
    Create_status = models.CharField(max_length=255,null=True,blank=True,default='added')
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    sub_account = models.CharField(max_length=255,null=True,blank=True)
    parent_account = models.CharField(max_length=255,null=True,blank=True)

class Chart_of_Accounts_History(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    chart_of_accounts=models.ForeignKey(Chart_of_Accounts,on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    action=models.CharField(max_length=255,default='Created')

class chart_of_accounts_comments(models.Model):                                         
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    chart_of_accounts=models.ForeignKey(Chart_of_Accounts,on_delete=models.CASCADE)
    comments = models.CharField(max_length=255,null=True,blank=True)
    
# TINTO -----CHART OF ACCOUNNTS ----END


#--------------------------GEORGE MATHEW____________
class payroll_employee(models.Model):
    title = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    alias = models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="image/", null=True)
    joindate=models.DateField(null=True)
    salary_type = models.CharField(max_length=100, default='Fixed',null=True)
    salary = models.IntegerField(null=True,blank=True)
    emp_number = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    dob=models.DateField(null=True)
    age = models.PositiveIntegerField(default=0)
    blood = models.CharField(max_length=10,null=True)
    parent = models.CharField(max_length=100,null=True)
    spouse_name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=250,null=True)
    permanent_address = models.CharField(max_length=250,null=True)
    Phone = models.BigIntegerField(null=True)
    emergency_phone = models.BigIntegerField(null=True ,blank=True,default=1)
    email = models.EmailField(max_length=255,null=True)
    Income_tax_no = models.CharField(max_length=255,null=True)
    Aadhar = models.CharField(max_length=250,default='',null=True)
    UAN = models.CharField(max_length=255,null=True)
    PFN = models.CharField(max_length=255,null=True)
    PRAN = models.CharField(max_length=255,null=True)
    status=models.CharField(max_length=200,default='Active',null=True)
    isTDS=models.CharField(max_length=200,null=True)
    TDS_percentage = models.IntegerField(null=True,default=0)
    salaryrange = models.CharField(max_length=10, choices=[('1-10', '1-10'), ('10-15', '10-15'), ('15-31', '15-31')], default='1-10',null=True)
    amountperhr = models.IntegerField(default=0,blank=True,null=True)
    workhr = models.IntegerField(default=0,blank=True,null=True)
    uploaded_file=models.FileField(upload_to="images/",null=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    acc_no = models.CharField(null=True,max_length=255)  
    IFSC = models.CharField(max_length=100,null=True)
    bank_name = models.CharField(max_length=100,null=True)
    branch = models.CharField(max_length=100,null=True)
    transaction_type = models.CharField(max_length=100,null=True)
    
class employee_history(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
    Date=models.DateField(null=True,auto_now=True)
    Action=models.CharField(null=True,max_length=255)
    
class Bloodgroup(models.Model):
    Blood_group=models.CharField(max_length=255,null=True)
    
class comment(models.Model):
    comment=models.CharField(null=True,max_length=255)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
#------------------------------------------------------------------end-------------------------------------------------------


class payroll_employee_comment(models.Model):
    comment=models.CharField(null=True,max_length=255)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
    
    
#----------------- Banking -----------------------------#

class Banking(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    bnk_name = models.CharField(max_length=220,default='', null=True, blank=True)
    bnk_branch = models.CharField(max_length=220,default='', null=True, blank=True)
    bnk_acno = models.CharField(max_length=220,default='', null=True, blank=True)
    bnk_ifsc = models.CharField(max_length=220,default='', null=True, blank=True)
    BAL_TYPE = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    bnk_bal_type = models.CharField(max_length=220,choices=BAL_TYPE, default='Debit')
    bnk_opnbal =models.FloatField(null=True, blank=True)
    bnk_bal =models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    document=models.FileField(upload_to='bank/',null=True,blank=True)
    status= models.TextField(default='Active')

 
class BankTransaction(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    banking = models.ForeignKey(Banking,on_delete=models.CASCADE)
    trans_cur_amount = models.FloatField(null=True, blank=True)
    trans_amount = models.FloatField(null=True, blank=True)
    trans_adj_amount = models.FloatField(null=True, blank=True)
    trans_adj_date = models.DateField(null=True, blank=True)

    TRANS_TYPE = [
        ('Opening Balance', 'Opening Balance'),
        ('Bank to Bank', 'Bank to Bank'),
        ('Bank to Cash', 'Bank to Cash'),
        ('Cash to Bank', 'Cash to Bank'),
        ('Bank Adjustment', 'Bank Adjustment'),
    ]
    trans_type = models.CharField(max_length=220,choices=TRANS_TYPE)

    ADJ_TYPE = [
        ('', ''),
        ('Balance Increase', 'Balance Increase'),
        ('Balance Decrease', 'Balance Decrease'),
    ]
    trans_adj_type = models.CharField(max_length=220,choices=ADJ_TYPE)
    trans_desc = models.CharField(max_length=220,null=True,blank=True)
    bank_to_bank_no = models.PositiveIntegerField(null=True,blank=True)


class BankingHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    banking = models.ForeignKey(Banking,on_delete=models.CASCADE)
    hist_adj_amount = models.FloatField(null=True, blank=True)
    hist_adj_date = models.DateField(auto_now_add=True, null=True, blank=True)
    ACTION_TYPE = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    hist_action = models.CharField(max_length=220,choices=ACTION_TYPE)

class BankTransactionHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    transaction = models.ForeignKey(BankTransaction,on_delete=models.CASCADE,null=True,blank=True)
    hist_cur_amount = models.FloatField(null=True, blank=True)
    hist_amount = models.FloatField(null=True, blank=True)
    hist_adj_amount = models.FloatField(null=True, blank=True)
    hist_adj_date = models.DateField(auto_now_add=True, null=True, blank=True)
    ACTION_TYPE = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    hist_action = models.CharField(max_length=220,choices=ACTION_TYPE)
    
    
#----------------------------------------------------------akshay--start--------------------------------------------------------


#------------------- PRICE LIST MODULE ------------

class PriceList(models.Model):
    
    name = models.CharField(max_length=255, null=True)
    type_choices = [
        ('Sales', 'Sales'),('Purchase', 'Purchase'),]
    type = models.CharField(max_length=10, choices=type_choices, null=True)
    item_rate_choices = [('Percentage', 'Percentage'),('Each Item', 'Each Item'),]
    item_rate_type = models.CharField(max_length=15, choices=item_rate_choices, null=True)
    description = models.TextField(null=True)
    percentage_type_choices = [('Markup', 'Markup'),('Markdown', 'Markdown'),]
    percentage_type = models.CharField(max_length=10, choices=percentage_type_choices, null=True, blank=True)
    percentage_value = models.IntegerField(null=True, blank=True)
    round_off_choices = [
        ('Never Mind', 'Never Mind'),
        ('Nearest Whole Number', 'Nearest Whole Number'),
        ('0.99', '0.99'),
        ('0.50', '0.50'),
        ('0.49', '0.49'),
    ]
    round_off = models.CharField(max_length=20, choices=round_off_choices, null=True)
    currency_choices = [('Indian Rupee', 'Indian Rupee')]
    currency = models.CharField(max_length=20, choices=currency_choices, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    STATUS_CHOICES = [('Active', 'Active'),('Inactive', 'Inactive'),]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    attachment = models.FileField(upload_to='price_list_attachment/', null=True, blank=True)

    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)

class PriceListItem(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)  
    standard_rate = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    custom_rate = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

class PriceListTransactionHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,null=True)
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
        ]
    action = models.CharField(max_length=10, choices=action_choices,null=True)

class PriceListComment(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateField(auto_now_add=True)

#----------------------------------------------------------akshay--end--------------------------------------------------------

#-----------------Arya E.R----------------------------------------

class Vendor(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    vendor_display_name = models.CharField(max_length=255,null=True,blank=True)
    vendor_email = models.EmailField()
    mobile = models.CharField(max_length=15,default='')
    phone = models.CharField(max_length=15,default='')
    company_name = models.CharField(max_length=255,null=True,blank=True)
    skype_name_number = models.CharField(max_length=255,null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    department = models.CharField(max_length=255,null=True,blank=True)
    website = models.URLField(blank=True, null=True,default='')
    gst_treatment = models.CharField(max_length=255,null=True,blank=True)
    gst_number = models.CharField(max_length=20,null=True,blank=True)
    pan_number = models.CharField(max_length=20,null=True,blank=True)
    currency = models.CharField(max_length=255,null=True,blank=True)
    opening_balance_type = models.CharField(max_length=255,null=True,blank=True)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    source_of_supply = models.CharField(max_length=255,null=True,blank=True)
    payment_term = models.ForeignKey(Company_Payment_Term, on_delete=models.SET_NULL,null=True,blank=True)
    billing_attention = models.CharField(max_length=255,null=True,blank=True)
    billing_address = models.TextField(null=True,blank=True)
    billing_city = models.CharField(max_length=255,null=True,blank=True)
    billing_state = models.CharField(max_length=255,null=True,blank=True)
    billing_country = models.CharField(max_length=255,null=True,blank=True)
    billing_pin_code = models.CharField(max_length=10,null=True,blank=True)
    billing_phone = models.CharField(max_length=15,null=True,blank=True)
    billing_fax = models.CharField(max_length=15,null=True,blank=True)
    shipping_attention = models.CharField(max_length=255,null=True,blank=True)
    shipping_address = models.TextField(null=True,blank=True)
    shipping_city = models.CharField(max_length=255,null=True,blank=True)
    shipping_state = models.CharField(max_length=255,null=True,blank=True)
    shipping_country = models.CharField(max_length=255,null=True,blank=True)
    shipping_pin_code = models.CharField(max_length=10,null=True,blank=True)
    shipping_phone = models.CharField(max_length=15,null=True,blank=True)
    shipping_fax = models.CharField(max_length=15,null=True,blank=True)
    remarks = models.TextField(null=True,blank=True)
    vendor_status = models.CharField(max_length=10,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VendorContactPerson(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    work_phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    skype_name_number = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VendorHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.vendor} - {self.action}"
    
class Vendor_remarks_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    remarks=models.CharField(max_length=500)

class Vendor_comments_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length=500)

class Vendor_mail_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    mail_from=models.TextField(max_length=300)
    mail_to=models.TextField(max_length=300)
    subject=models.TextField(max_length=250)
    content=models.TextField(max_length=900)
    mail_date=models.DateTimeField(auto_now_add=True)

class Vendor_doc_upload_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')

#--------------------------------------end-----------------------------------------------------------

class Holiday(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    holiday_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    company=models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True,blank=True)
    
class CompanyRepeatEvery(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    repeat_every =models.CharField(max_length=100,null=True,blank=True,default='')
    repeat_type =models.CharField(max_length=100,null=True,blank=True,default='')
    duration =models.IntegerField(null=True,default=0)
    days =models.IntegerField(null=True,default=0)
    
    
#---------------- Zoho Final Attendance - Meenu Shaju - Start--------------------

class Attendance(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
    holiday=models.ForeignKey(Holiday,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    status=models.CharField(max_length=255,null=True)
    reason=models.CharField(max_length=255,null=True)

    
class Attendance_History(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    attendance=models.ForeignKey(Attendance,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    action=models.CharField(max_length=100,null=True)

class Attendance_comment(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
    comment = models.TextField(null=True) 
    month = models.IntegerField(null=True)  
    year = models.IntegerField(null=True)  

#---------------- Zoho Final Attendance - Meenu Shaju - End--------------------


# ------------------------------- GOKUL KRISHNA UR -----------------------------------------

class SalaryDetails(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
    attendance=models.ForeignKey(Attendance,on_delete=models.CASCADE,null=True)
    holiday=models.IntegerField(default=0,blank=True,null=True)
    salary_date =models.DateField(null=True)
    casual_leave = models.IntegerField(default=0,blank=True,null=True)
    month =  models.CharField(max_length=100,null=True)
    year = models.IntegerField(default=0,blank=True,null=True)
    basic_salary = models.IntegerField(default=0,blank=True,null=True)
    conveyance_allowance = models.IntegerField(default=0,blank=True,null=True)
    hra = models.IntegerField(default=0,blank=True,null=True)
    other_allowance = models.IntegerField(default=0,blank=True,null=True)
    total_working_days = models.IntegerField(default=0,blank=True,null=True)
    other_cuttings = models.IntegerField(default=0,blank=True,null=True)
    add_bonus = models.IntegerField(default=0,blank=True,null=True)
    salary = models.FloatField(default=0,blank=True,null=True)
    description = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True,default='Active')
    DraftorSave = models.CharField(max_length=100,null=True)
    total_amount= models.FloatField(default=0,blank=True,null=True)
    

class CommentSalaryDetails(models.Model):
    employee=models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=100,null=True)
    salary_details = models.ForeignKey(SalaryDetails,on_delete=models.CASCADE,null=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    

class HistorySalaryDetails(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    salary_details = models.ForeignKey(SalaryDetails,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True,auto_now=True)
    action=models.CharField(max_length=100,null=True)

# ------------------------------- GOKUL KRISHNA UR -----------------------------------------

#---------------------EMPLOYEE_LOAN------------------------------------------#by haripriya

class LoanDuration(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    day = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=50, choices=(
        ('Months', 'Months'),
        ('Month', 'Month'),
        ('Years', 'Years'),
        ('Year', 'Year'),
    ))

class EmployeeLoan(models.Model):
    Employee = models.ForeignKey(payroll_employee,on_delete=models.CASCADE,null=True,blank=True)
    
    Loandate = models.DateField(null=True)
    LoanAmount =  models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=255, blank=True)
    Expiry_date = models.DateField(null=True)
    payment_method = models.CharField(max_length=220,null=True,blank=True)
    cheque_number = models.CharField(max_length=220,null=True,blank=True)
    upi_id =models.CharField(max_length=220,null=True,blank=True)
    bank_acc_number =models.CharField(max_length=220,null=True,blank=True)
    Monthly_payment_type =models.CharField(max_length=220,null=True,blank=True)
    MonthlyCut_percentage = models.IntegerField(null=True,blank=True)
    MonthlyCut_Amount =models.IntegerField(null=True,blank=True)
    note = models.CharField(max_length=220,null=True,blank=True)
    file = models.FileField(upload_to="images/",null=True)
    status =models.CharField(max_length=200,null=True,blank=True,default='')
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    balance=models.IntegerField(null=True,blank=True)
    active = models.BooleanField(default=True)
    emp_name= models.CharField(max_length=220,null=True,blank=True)
    emp_no= models.IntegerField(null=True,blank=True)
    join_date = models.DateField(null=True)
    salary = models.IntegerField(null=True,blank=True)
    email= models.EmailField(max_length=255,null=True)
 

class Employeeloan_history(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    employeeloan =models.ForeignKey(EmployeeLoan,on_delete=models.CASCADE,null=True,blank=True)
    
    Date = models.DateField(null=True,auto_now=True)
    action = models.CharField(max_length=220,null=True,blank=True)

class employeeloan_comments(models.Model):                                         
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    employee=models.ForeignKey(EmployeeLoan,on_delete=models.CASCADE)
    comments = models.CharField(max_length=255,null=True,blank=True)

class EmployeeLoanRepayment(models.Model):
    employee = models.ForeignKey(payroll_employee, on_delete=models.CASCADE, null=True)
    principal_amount = models.IntegerField(null=True)
    interest_amonut = models.IntegerField(null=True)
    payment_date = models.DateField(null=True)
    payment_method = models.CharField(max_length=255,null=True)
    cheque_id=models.CharField(null=True,blank=True,max_length=255)
    upi_id=models.CharField(null=True,blank=True,max_length=255)
    bank_id=models.CharField(null=True,blank=True,max_length=255)
    total_payment = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    particular = models.CharField(max_length=255,null=True)
    emp = models.ForeignKey(EmployeeLoan, on_delete=models.CASCADE, null=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

#..........................Employeeloan end...........................#

class Customer(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    company_payment_terms = models.ForeignKey(Company_Payment_Term,on_delete=models.CASCADE,null=True,blank=True)

    customer_type = models.CharField(max_length=220,null=True,blank=True)
    title = models.CharField(max_length=220,null=True,blank=True)
    first_name = models.CharField(max_length=220,null=True,blank=True)
    last_name = models.CharField(max_length=220,null=True,blank=True)
    customer_display_name = models.CharField(max_length=220,null=True,blank=True)
    company_name = models.CharField(max_length=220,null=True,blank=True)
    customer_email = models.EmailField(max_length=255,null=True)
    customer_phone = models.CharField(max_length=220,null=True,blank=True)
    customer_mobile = models.CharField(max_length=220,null=True,blank=True)

    skype = models.CharField(max_length=220,null=True,blank=True)
    designation = models.CharField(max_length=220,null=True,blank=True)
    department = models.CharField(max_length=220,null=True,blank=True)
    website = models.CharField(max_length=220,null=True,blank=True)
    GST_treatement = models.CharField(max_length=220,null=True,blank=True)
    GST_number = models.CharField(max_length=220,null=True,blank=True)
    PAN_number = models.CharField(max_length=220,null=True,blank=True)
    place_of_supply = models.CharField(max_length=220,null=True,blank=True)
    tax_preference = models.CharField(max_length=220,null=True,blank=True)

    currency = models.CharField(max_length=220,null=True,blank=True)
    opening_balance_type = models.CharField(max_length=220,null=True,blank=True)
    opening_balance = models.FloatField(null=True, blank=True,default=0.00)
    credit_limit = models.FloatField(null=True, blank=True)
    price_list = models.CharField(max_length=220,null=True,blank=True)
    portal_language = models.CharField(max_length=220,null=True,blank=True)

    facebook = models.CharField(max_length=220,null=True,blank=True)
    twitter = models.CharField(max_length=220,null=True,blank=True)
    current_balance = models.FloatField(null=True, blank=True,default=0.00)

    billing_attention = models.CharField(max_length=220,null=True,blank=True)
    billing_address = models.CharField(max_length=220,null=True,blank=True)
    billing_city = models.CharField(max_length=220,null=True,blank=True)
    billing_state = models.CharField(max_length=220,null=True,blank=True)
    billing_country = models.CharField(max_length=220,null=True,blank=True)
    billing_pincode = models.CharField(max_length=220,null=True,blank=True)
    billing_mobile = models.CharField(max_length=220,null=True,blank=True)
    billing_fax = models.CharField(max_length=220,null=True,blank=True)

    shipping_attention = models.CharField(max_length=220,null=True,blank=True)
    shipping_address = models.CharField(max_length=220,null=True,blank=True)
    shipping_city = models.CharField(max_length=220,null=True,blank=True)
    shipping_state = models.CharField(max_length=220,null=True,blank=True)
    shipping_country = models.CharField(max_length=220,null=True,blank=True)
    shipping_pincode = models.CharField(max_length=220,null=True,blank=True)
    shipping_mobile = models.CharField(max_length=220,null=True,blank=True)
    shipping_fax = models.CharField(max_length=220,null=True,blank=True)

    remarks = models.CharField(max_length=220,null=True,blank=True)
    customer_status = models.CharField(max_length=220,null=True,blank=True)


class Customer_remarks_table(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    remarks=models.CharField(max_length=500)   

class Customer_comments_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length=500)  

class Customer_doc_upload_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')
    
class CustomerContactPersons(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)

    title = models.CharField(max_length=220,null=True,blank=True)
    first_name = models.CharField(max_length=220,null=True,blank=True)
    last_name = models.CharField(max_length=220,null=True,blank=True)
    email = models.EmailField(max_length=220,null=True,blank=True)
    work_phone = models.CharField(max_length=220,null=True,blank=True)
    mobile = models.CharField(max_length=220,null=True,blank=True)
    skype = models.CharField(max_length=220,null=True,blank=True)
    designation = models.CharField(max_length=220,null=True,blank=True)
    department = models.CharField(max_length=220,null=True,blank=True)


class CustomerHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)

    action = models.CharField(max_length=220,null=True,blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    
class BankAccount(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    bank=models.ForeignKey(Banking, on_delete=models.CASCADE,null=True,blank=True)
    customer_name = models.CharField(max_length=220,null=True)
    alias = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=100,null=True)
    account_type = models.CharField(max_length=100,null=True)
    bankname=models.CharField(max_length=100,null=True)
    account_number = models.CharField(max_length=15,null=True)
    ifsc_code = models.CharField(max_length=100,null=True)
    swift_code = models.CharField(max_length=100,null=True)
    branch_name = models.CharField(max_length=100,null=True)
    cheque_book_range = models.CharField(max_length=100,null=True)
    enable_cheque_printing = models.CharField(max_length=100,null=True)
    cheque_printing_configuration = models.CharField(max_length=100,null=True)
    mailing_name = models.CharField(max_length=100,null=True)
    address = models.TextField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    pin = models.CharField(max_length=100,null=True)
    pan_number = models.CharField(max_length=100,null=True)
    registration_type = models.CharField(max_length=100,null=True)
    gst_num = models.CharField(max_length=100,null=True)
    alter_gst_details = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now_add=True, null=True)
    amount_type = models.CharField(max_length=100,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    status=models.CharField(max_length=10,default='Active',null=True)
    
    
class BankAccountHistory(models.Model):
    company=models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    logindetails= models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    bank_holder=models.ForeignKey(BankAccount, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    action = models.CharField(max_length=100,null=True)
    
class Loan_Term(models.Model):
    duration= models.IntegerField(null=True,blank=True)
    term = models.CharField(max_length=255,null=True,blank=True)
    days = models.IntegerField(null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    
    
class loan_account(models.Model):
    bank_holder=models.ForeignKey(BankAccount,on_delete=models.CASCADE,null=True)
    logindetails = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    loan_term = models.ForeignKey(Loan_Term, on_delete=models.CASCADE,null=True,blank=True)
  
    account_number = models.CharField(max_length=15,null=True)
    loan_amount=models.IntegerField()
    balance=models.IntegerField(default=0,null=True)
    lender_bank=models.CharField(max_length=255)
    loan_date = models.DateField()
    payment_method=models.CharField(max_length=255)
    upi_id=models.CharField(max_length=255,default='', null=True, blank=True)
    cheque=models.CharField(max_length=255,default='', null=True, blank=True)
    payment_accountnumber=models.CharField(max_length=255,default='', null=True, blank=True)
    processing_method=models.CharField(max_length=255)
    processing_upi=models.CharField(max_length=255,default='', null=True, blank=True)
    processing_cheque=models.CharField(max_length=255,default='', null=True, blank=True)
    processing_acc=models.CharField(max_length=255,default='', null=True, blank=True)
    processing_fee=models.IntegerField(default='', null=True, blank=True)
    term=models.CharField(max_length=15,default='', null=True, blank=True)
    interest=models.IntegerField(default='', null=True, blank=True)
    description=models.CharField(max_length=255,default='', null=True, blank=True)
    status= models.TextField(default='Active')
    
    
class LoanRepayemnt(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    loan=models.ForeignKey(loan_account, on_delete=models.CASCADE,null=True,blank=True)
    principal_amount=models.IntegerField(null=True,blank=True)
    interest_amount=models.IntegerField(null=True,blank=True)
    payment_method=models.CharField(max_length=255)
    upi_id=models.CharField(max_length=255,default=None, null=True, blank=True)
    cheque=models.CharField(max_length=255,default=None, null=True, blank=True)
    account_number=models.CharField(max_length=255,default=None, null=True, blank=True)
    payment_date=models.DateField(default=date.today)
    total_amount=models.IntegerField(null=True,blank=True)
    balance=models.IntegerField(default=0) 
    type=models.CharField(max_length=255,null=True)
    
class LoanAccountHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    loan=models.ForeignKey(loan_account,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(default=date.today)
    action=models.CharField(max_length=255)
    
    
class LoanRepaymentHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    repayment=models.ForeignKey(LoanRepayemnt,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(default=date.today)
    action=models.CharField(max_length=255)
    
    
class Comments(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    loan=models.ForeignKey(loan_account,on_delete=models.CASCADE,null=True,blank=True)
    comment=models.CharField(max_length=255)
    
    
class Godown(models.Model):
    date = models.DateField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.CharField(max_length = 250)
    stock_in_hand = models.IntegerField()
    godown_name = models.CharField(max_length = 250)
    godown_address = models.CharField(max_length = 300)
    stock_keeping = models.IntegerField()
    distance = models.IntegerField()
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=200, default = 'Active', null=True)
    action = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='file/', null=True, blank=True)


class GodownHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField()
    action = models.CharField(max_length = 250)

class GodownComments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length = 250)
    
class Holiday_history(models.Model):
    company=models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    
class Comment_holiday(models.Model):
    holiday_details = models.ForeignKey(Holiday, on_delete = models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    company=models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True,blank=True)
    
    
class JournalRecievedIdModel(models.Model):
    user = models.CharField(max_length=200,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, null=True, blank=True)
    pattern = models.CharField(max_length=255,null=True)
    ref_number = models.CharField(max_length=255,null=True)
    jn_rec_number = models.CharField(max_length=255,null=True) 

      
class Journal(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('save', 'Save'),
    )
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, null=True, blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True,auto_now_add=True)
    journal_no = models.CharField(max_length=255,null=True)  
    reference_no = models.IntegerField(null=True)
    notes = models.TextField(blank=True,null=True)
    currency = models.CharField(max_length=255,null=True)
    journal_type = models.CharField(max_length=255,null=True)
    attachment = models.FileField(upload_to='journal_attachments/', blank=True,null=True)
    total_debit = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    debit_difference = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    credit_difference = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, null=True, blank=True)
     
    def __str__(self):
        return self.journal_no
    
    def getNumFieldName(self):
        return 'journal_no'
    
class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    login = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, null=True, blank=True)
    account = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    contact = models.CharField(max_length=200,null=True)
    debits = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    credits = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    
class JournalTransactionHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, null=True, blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
    ]
    action = models.CharField(max_length=10, choices=action_choices, null=True)

class JournalComment(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, null=True, blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateField(auto_now_add=True)  
    
    
#-----------------invoice -----------------------------#
class invoice(models.Model):
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    payment_terms = models.ForeignKey(Company_Payment_Term,on_delete=models.CASCADE,null=True,blank=True)

    customer_email=models.EmailField(max_length=220,null=True,blank=True)
    customer_billingaddress=models.CharField(max_length=220,null=True,blank=True)
    customer_GSTtype=models.CharField(max_length=220,null=True,blank=True)
    customer_GSTnumber=models.CharField(max_length=220,null=True,blank=True)
    customer_place_of_supply=models.CharField(max_length=220,null=True,blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True) 
    expiration_date = models.DateField(auto_now_add=True, null=True, blank=True) 
    reference_number=models.IntegerField(blank=True,null=True,)
    invoice_number=models.CharField(max_length=220,null=True,blank=True) 
    payment_method=models.CharField(max_length=220,null=True,blank=True) 
    cheque_number=models.CharField(max_length=220,null=True,blank=True) 
    UPI_number=models.CharField(max_length=220,null=True,blank=True) 
    bank_account_number=models.CharField(max_length=220,null=True,blank=True) 
    description=models.CharField(max_length=220,null=True,blank=True) 
    terms_and_condition=models.CharField(max_length=220,null=True,blank=True) 
    document=models.FileField(upload_to="images/",null=True)
    sub_total=models.FloatField(default=0.0, null=True, blank=True)
    CGST=models.FloatField(default=0.0, null=True, blank=True)
    SGST=models.FloatField(default=0.0, null=True, blank=True)
    IGST = models.FloatField(default=0.0, null=True, blank=True)
    price_list_applied = models.BooleanField(null=True, default=False)
    price_list = models.ForeignKey(PriceList, on_delete = models.SET_NULL,null=True)


    tax_amount=models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge=models.FloatField(default=0.0, null=True, blank=True)
    adjustment=models.FloatField(default=0.0, null=True, blank=True)
    grand_total=models.FloatField(default=0.0, null=True, blank=True)
    advanced_paid=models.FloatField(default=0.0, null=True, blank=True)
    balance=models.FloatField(default=0.0, null=True, blank=True)
    status=models.CharField(max_length=220,null=True,blank=True)

    def getNumFieldName(self):
        return 'invoice_number'  

class invoiceHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    invoice = models.ForeignKey(invoice,on_delete=models.CASCADE,null=True,blank=True)

    action = models.CharField(max_length=220,null=True,blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True) 
    
class invoiceReference(models.Model):
    reference_number = models.CharField(max_length=220,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    staff = models.ForeignKey(StaffDetails,on_delete=models.CASCADE,null=True,blank=True)


class invoiceitems(models.Model):
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails = models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    Items = models.ForeignKey(Items,on_delete=models.CASCADE)
    invoice = models.ForeignKey(invoice,on_delete=models.CASCADE,null=True,blank=True)

    hsn = models.CharField(max_length=220,null=True,blank=True)
    quantity=models.IntegerField(blank=True,null=True,default=0)
    price=models.FloatField(default=0.0, null=True, blank=True)
    tax_rate=models.FloatField(default=0.0, null=True, blank=True)
    discount=models.FloatField(default=0.0, null=True, blank=True)
    total=models.FloatField(default=0.0, null=True, blank=True)

class invoicecomments(models.Model):
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    invoice = models.ForeignKey(invoice,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

#End
class EmployeeLoanRepaymentHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    repayment=models.ForeignKey(EmployeeLoanRepayment,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(default=date.today)
    action=models.CharField(max_length=255)
    
    
# < ------------- Shemeem -------- > Recurring Invoice < ------------------------------- >
    
class RecurringInvoice(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    entry_type = models.CharField(max_length=20, null=True, blank=True)
    profile_name = models.CharField(max_length=100, null=True, blank=True)
    reference_no = models.BigIntegerField(null=True, blank=True)
    rec_invoice_no = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    salesOrder_no = models.CharField(max_length=100, null=True, blank=True)
    repeat_every = models.ForeignKey(CompanyRepeatEvery, on_delete=models.CASCADE,null=True)
    payment_terms = models.ForeignKey(Company_Payment_Term, on_delete=models.CASCADE,null=True)
    price_list_applied = models.BooleanField(null=True, default=False)
    price_list = models.ForeignKey(PriceList, on_delete = models.SET_NULL,null=True)
    payment_method = models.CharField(max_length=20, null=True,blank=True)
    cheque_number = models.CharField(max_length=100, null=True, blank=True)
    upi_number = models.CharField(max_length=100, null=True, blank=True)
    bank_account_number = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)
    document=models.FileField(upload_to="images/",null=True)
    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    advance_paid = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Saved', 'Saved'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def getNumFieldName(self):
        return 'rec_invoice_no'


class RecurringInvoiceHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    recurring_invoice = models.ForeignKey(RecurringInvoice, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    action = models.CharField(max_length=20, null=True)


class Reccurring_Invoice_item(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    reccuring_invoice=models.ForeignKey(RecurringInvoice,on_delete=models.CASCADE,null=True,blank=True)
    
    item=models.ForeignKey(Items, on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)
    price=  models.FloatField(default=0.0, null=True, blank=True)
    tax_rate= models.FloatField(default=0.0, null=True, blank=True)
    discount= models.FloatField(default=0.0, null=True, blank=True)
    total =  models.FloatField(default=0.0, null=True, blank=True)


class Reccurring_Invoice_Reference(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    reference_number = models.BigIntegerField(null=True, blank=True)

class Recurring_Invoice_Comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True)
    recurring_invoice = models.ForeignKey(RecurringInvoice,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

# < -------------------- > Recurring Invoice - End < ------------------------------- >

#------------Retainer_invoice---------------
class RetainerInvoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    logindetails = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    customer_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    customer_name1=models.CharField(max_length=100,null=True,blank=True)
    customer_mailid = models.CharField(max_length=100,null=True,blank=True)
    customer_placesupply=models.CharField(max_length=100,null=True,blank=True)
    retainer_invoice_number=models.CharField(max_length=255)
    refrences=models.CharField(max_length=255)
    retainer_invoice_date=models.DateField()
    advance=models.IntegerField(null=True)
    total_amount=models.CharField(max_length=100)
    customer_notes=models.TextField()
    terms_and_conditions=models.TextField()
    is_draft=models.BooleanField(default=True)
    is_sent=models.BooleanField(default=False)
    balance=models.CharField(max_length=100,null=True,blank=True)
    created_by = models.ForeignKey(LoginDetails, on_delete=models.SET_NULL, related_name='retainer_created', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(LoginDetails, on_delete=models.SET_NULL, related_name='retainer_modified', null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    adjustment = models.IntegerField(null=True, blank=True)
    paid = models.IntegerField(null=True, blank=True)

    def getNumFieldName(self):
        return 'retainer_invoice_number'
        
        
#-------Delivery Challan ------------------------------------

class Delivery_challan(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    place_of_supply = models.CharField(max_length=200,null=True)
    challan_date=  models.DateField(auto_now_add=True, null=True)
    reference_number = models.IntegerField(null=True)  
    challan_number = models.CharField(max_length=200,null=True)
    challan_type = models.CharField(max_length=200,null=True)
    description = models.TextField(max_length=200,null=True)
    terms_condition = models.CharField(max_length=200,null=True)
    document=models.FileField(upload_to="documents/",null=True)
    sub_total = models.FloatField(default=0.0, null=True, blank=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    grand_total = models.FloatField(default=0.0, null=True, blank=True)
    advance = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)
    status = models.CharField(max_length=50,null=True)
    invoice_convert = models.ForeignKey(invoice, on_delete=models.CASCADE,null=True,blank=True)
    rec_invoice_convert = models.ForeignKey(RecurringInvoice, on_delete=models.CASCADE,null=True,blank=True)


    def getNumFieldName(self):
        return 'challan_number'
        
class Delivery_challan_item(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    delivery_challan=models.ForeignKey(Delivery_challan, on_delete=models.CASCADE,null=True,blank=True)
    item=models.ForeignKey(Items, on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)
    price=  models.FloatField(default=0.0, null=True, blank=True)
    tax_rate= models.IntegerField(null=True, blank=True)
    discount= models.FloatField(default=0.0, null=True, blank=True)
    total =  models.FloatField(default=0.0, null=True, blank=True)



class Delivery_challan_reference(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    
    reference_number = models.IntegerField(max_length=200,null=True)

class Delivery_challan_history(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    delivery_challan=models.ForeignKey(Delivery_challan, on_delete=models.CASCADE,null=True,blank=True)
    date=  models.DateField(auto_now_add=True, null=True)
   
    action = models.CharField(max_length=200,null=True)

class Delivery_challan_comment(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    delivery_challan=models.ForeignKey(Delivery_challan, on_delete=models.CASCADE,null=True,blank=True)
    date=  models.DateField(auto_now_add=True, null=True)
    comment = models.TextField(null=True)  
    action = models.CharField(max_length=200,null=True)
    
#End
#------------Bill---------------
class Bill(models.Model):
    Vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)
    Bill_Number = models.CharField(max_length=220,null=True,blank=True)
    Reference_Number = models.IntegerField(null=True)
    Purchase_Order_Number = models.CharField(max_length=220,null=True,blank=True)
    Bill_Date = models.DateField(null=True)
    pattern = models.CharField(max_length=255,null=True)

    Company_Payment_Terms = models.ForeignKey(Company_Payment_Term,on_delete=models.CASCADE,null=True,blank=True)
    Due_Date = models.DateField(null=True)
    Payment_Method = models.CharField(max_length=220,null=True,blank=True)
    Cheque_Number = models.CharField(max_length=220,null=True,blank=True)
    UPI_Id = models.CharField(max_length=220,null=True,blank=True)
    Bank_Account = models.CharField(max_length=220,null=True,blank=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    Description = models.CharField(max_length=220,null=True,blank=True)
    Document = models.FileField(upload_to='doc/')
    Sub_Total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    CGST = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    SGST = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    IGST = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Tax_Amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Shipping_Charge =models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Adjustment_Number = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Grand_Total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Advance_amount_Paid = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,null=True,blank=True)
    Status = models.CharField(max_length=220,null=True,blank=True)
    Login_Details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    Action = models.CharField(max_length=220,null=True,blank=True)
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
    ]
    debitNoteaction = models.CharField(max_length=10, choices=action_choices, default='Created')

    def getNumFieldName(self):
        return 'Bill_Number'

class BillItems(models.Model):
    item_id = models.ForeignKey(Items,on_delete=models.CASCADE,null=True,blank=True)
    item_name = models.CharField(max_length=255,null=True)
    item_hsn = models.IntegerField(null=True,blank=True)
    total_qty = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    qty = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    bal_qty = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    price = models.PositiveBigIntegerField(null=True,blank=True)
    taxGST = models.CharField(max_length=255,null=True,blank=True)
    taxIGST = models.CharField(max_length=255,null=True,blank=True)
    discount = models.PositiveBigIntegerField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    Bills = models.ForeignKey(Bill,on_delete=models.CASCADE,null=True)
    Login_Details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    
class Bill_History(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    bills = models.ForeignKey(Bill, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
    ]
    action = models.CharField(max_length=10, choices=action_choices, null=True)

class Bill_Reference(models.Model):
    Reference_Number = models.IntegerField(null=True)
    Company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    Login_Details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    Bill = models.ForeignKey(Bill,on_delete=models.CASCADE,null=True,blank=True)
#End              
        
#------------Sales Order---------------
class SaleOrder(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null=True)
    customer_email = models.EmailField()
    customer_billing_address = models.CharField(max_length=255)
    customer_gst_type = models.CharField(max_length=255)
    customer_gst_number = models.CharField(max_length=255)
    customer_place_of_supply = models.CharField(max_length=255)
    sales_order_date = models.DateField()
    payment_terms = models.ForeignKey(Company_Payment_Term, on_delete=models.CASCADE,blank=True, null=True)
    expiration_date = models.DateField()
    reference_number = models.CharField(max_length=255)
    sales_order_number = models.CharField(max_length=255)
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('UPI', 'UPI'),
        ('Bank', 'Bank'),
    ]
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    
    cheque_number = models.CharField(max_length=255, blank=True, null=True)
    upi_number = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=255, blank=True, null=True)
    
    
    description = models.CharField(max_length=255)
    terms_and_condition = models.TextField()
    document = models.FileField(upload_to='documents/',blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    adjustment = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    advanced_paid = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    Save='Save'
    Draft='Draft'
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Save', 'Save'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft') 
    convert_to_invoice=models.ForeignKey(invoice,on_delete=models.CASCADE,null=True,blank=True)
    convert_to_recurringinvoice=models.ForeignKey(RecurringInvoice,on_delete=models.CASCADE,null=True,blank=True)
    
    def getNumFieldName(self):
        return 'sales_order_number'   

class SalesOrderItems(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True, null=True)
    hsn = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, blank=True, null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    
    
class SalesOrderReference(models.Model):
    reference_number = models.BigIntegerField(null=True, blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, blank=True, null=True)
    
class SalesOrderHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    current_date = models.DateField()
    action = models.CharField(max_length=255)
    
class Salesorder_comments_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, blank=True, null=True)
    comment=models.TextField(max_length=500)
    
class Salesorder_doc_upload_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    sales_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, blank=True, null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')         
#End

# --------------------------------------   ashikhvu   (start)   -----------------------------------------------

class RecurringRepeatEvery(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    repeat_duration = models.IntegerField(blank=True,null=True,default=0)
    repeat_type = models.CharField(max_length=255,null=True,blank=True)

class RecurringCreditPeriod(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    credit_name = models.CharField(max_length=255,blank=True,null=True)
    days = models.IntegerField(null=True,blank=True)

class Recurring_bills(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    
    vendor_details = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)
    vend_name = models.CharField(max_length=255)
    vend_mail = models.EmailField(null=True,blank=True)
    vend_gst_treat = models.CharField(max_length=255,null=True,blank=True)
    vend_gst_no = models.CharField(max_length=220,null=True,blank=True)
    vend_source_of_supply = models.CharField(max_length=220,null=True,blank=True)
    vend_billing_address = models.TextField(null=True,blank=True)

    recc_bill_no= models.CharField(max_length=255)
    recc_ref_no = models.IntegerField(blank=True,null=True)
    profile_name = models.CharField(max_length=255,blank=True,null=True)
    purchase_order_no = models.CharField(max_length=255,null=True,blank=True)
    repeat_every_id = models.ForeignKey(RecurringRepeatEvery,on_delete=models.CASCADE,null=True,blank=True)
    repeat_every_duration = models.IntegerField(blank=True,null=True)
    repeat_every_type = models.CharField(max_length=255,null=True,blank=True)

    rec_bill_date= models.DateTimeField(null=True,blank=True)
    expiry_date = models.DateTimeField(null=True,blank=True)
    credit_period = models.CharField(max_length=255,null=True,blank=True)
    credit_period_id = models.ForeignKey(RecurringCreditPeriod,on_delete=models.CASCADE,null=True,blank=True)
    credit_period_termname = models.CharField(max_length=255,blank=True,null=True)
    credit_period_days = models.IntegerField(blank=True,null=True)

    customer_details = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    cust_name = models.CharField(max_length=255,null=True)
    cust_mail = models.EmailField(null=True,blank=True)
    cust_gst_treat = models.CharField(max_length=255,null=True,blank=True)
    cust_gst_no = models.CharField(max_length=220,null=True,blank=True)
    cust_place_of_supply = models.CharField(max_length=220,null=True,blank=True)
    cust_billing_address = models.TextField(null=True,blank=True)
    
    payment_type = models.CharField(max_length=255,null=True,blank=True)
    cheque_no = models.CharField(max_length=255,null=True,blank=True)
    upi_id = models.CharField(max_length=255,null=True,blank=True)
    bank_id = models.ForeignKey(Banking,on_delete=models.CASCADE,null=True,blank=True)
    bank_name = models.CharField(max_length=255,null=True,blank=True)
    bank_acc_no = models.CharField(max_length=255,null=True,blank=True)

    price_list = models.ForeignKey(PriceList,on_delete=models.CASCADE,null=True,blank=True)
    price_list_name = models.CharField(max_length=255,null=True,blank=True)

    sub_total = models.FloatField(null=True,blank=True)
    igst = models.FloatField(null=True,blank=True)
    cgst = models.FloatField(null=True,blank=True)
    sgst = models.FloatField(null=True,blank=True)
    tax_amount = models.FloatField(null=True,blank=True)
    shipping_charge = models.FloatField(null=True,blank=True)
    adjustment = models.FloatField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    paid = models.FloatField(null=True,blank=True)
    bal = models.FloatField(null=True,blank=True)
    status_type = [
        ('save','save'),
        ('draft','draft')
    ]
    status = models.CharField(max_length=255,null=True,choices=status_type)
    note = models.TextField(null=True,blank=True)
    document=models.FileField(upload_to='docs/',null=True,blank=True)
    template1_doc = models.FileField(null=True,blank=True,upload_to='docs/')
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
    ]
    debitNoteaction = models.CharField(max_length=10, choices=action_choices, default='Created')

class recurr_comments(models.Model):
    recurr = models.ForeignKey(Recurring_bills,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.TextField(null=True,blank=True)

class RecurringRecievedId(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    pattern = models.CharField(max_length=255,null=True)
    recc_rec_number = models.CharField(max_length=255,null=True)
    ref_number = models.CharField(max_length=255,null=True)
    
class RecurrItemsList(models.Model):
    item_id = models.ForeignKey(Items,on_delete=models.CASCADE,null=True,blank=True)
    item_name = models.CharField(max_length=255)
    item_hsn = models.IntegerField(null=True,blank=True)
    total_qty = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    qty = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    bal_qty = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    price = models.PositiveBigIntegerField(null=True,blank=True)
    taxGST = models.CharField(max_length=255,null=True,blank=True)
    taxIGST = models.CharField(max_length=255,null=True,blank=True)
    discount = models.PositiveBigIntegerField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    recurr_bill_id = models.ForeignKey(Recurring_bills,on_delete=models.CASCADE,null=True,blank=True)

class Recurr_history(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    Recurr = models.ForeignKey(Recurring_bills, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
    ]
    action = models.CharField(max_length=10, choices=action_choices, null=True)

# --------------------------------------   ashikhvu   (end)   -----------------------------------------------

# credit note start - harikrishnan -------------------

class Credit_Note(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null=True)
    customer_email = models.EmailField()
    customer_billing_address = models.CharField(max_length=255)
    customer_gst_type = models.CharField(max_length=255)
    customer_gst_number = models.CharField(max_length=255)
    customer_place_of_supply = models.CharField(max_length=255)
    credit_note_date = models.DateField()
    invoice = models.ForeignKey(invoice, on_delete=models.CASCADE,blank=True, null=True)
    recurring_invoice = models.ForeignKey(RecurringInvoice, on_delete=models.CASCADE,blank=True, null=True)
    invoice_type = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    reference_number = models.IntegerField()
    credit_note_number = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    cheque_number = models.CharField(max_length=255)
    upi_number = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    terms_and_condition = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/')
    sub_total = models.FloatField()
    cgst = models.FloatField()
    sgst = models.FloatField()
    taxAmount_igst = models.FloatField()
    shipping_charge = models.FloatField()
    adjustment = models.FloatField()
    grand_total = models.FloatField()
    advance_paid = models.FloatField()
    balance = models.FloatField()
    status = models.CharField(max_length=255)
    
    def getNumFieldName(self):
        return 'invoice_number'

class Credit_Note_Items(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    hsn = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    tax_rate = models.IntegerField()
    discount = models.FloatField()
    total = models.FloatField()
    credit_note = models.ForeignKey(Credit_Note, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)

class Credit_Note_Reference(models.Model):
    reference_number = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)

class Credit_Note_History(models.Model):
    reference_number = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    credit_note = models.ForeignKey(Credit_Note, on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=255)

class Credit_Note_Comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    credit_note = models.ForeignKey(Credit_Note, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    
# credit note end - harikrishnan ------------------------------

class Recurring_Expense(models.Model):
    EXPENSE_TYPES = [
        ('goods', 'Goods'),
        ('services', 'Services'),
    ]

    profile_name = models.CharField(max_length=255)
    exp_date =models.DateField(auto_now_add=True, null=True, blank=True)
    expense_type = models.CharField(max_length=50,choices=EXPENSE_TYPES)
    Expense_account= models.CharField(max_length=255, blank=True, null=True)
    hsn = models.CharField(max_length=255, blank=True, null=True)
    sac = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_Method = models.CharField(max_length=10,null=True)
    cheque_id = models.CharField(max_length=50, blank=True, null=True)
    upi_number = models.CharField(max_length=50, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
   

   
   
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    vendor_name= models.CharField(max_length=255, blank=True, null=True)
    vendor_mail=models.CharField(max_length=100,null=True,blank=True)
    vendor_address = models.CharField(max_length=255, blank=True,null=True)
    vendor_gst_type = models.CharField(max_length=255, blank=True,null=True)
    vendor_gst = models.CharField(max_length=255, blank=True,null=True)
    Vendor_Sourceofsupply=models.CharField(max_length=255, blank=True,null=True)

    refrenceid=models.IntegerField(blank=True,null=True)
    Expense_Number=models.CharField(max_length=255,default='',null=True)
    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    customer_name= models.CharField(max_length=255, blank=True, null=True)
    customeremail=models.CharField(max_length=100,null=True,blank=True)
    cust_gsttype= models.CharField(max_length=255, blank=True,null=True)
    cust_gst_no= models.CharField(max_length=255, blank=True,null=True)
    cust_address= models.CharField(max_length=255, blank=True,null=True)
    cust_placeofsupply=models.CharField(max_length=255, blank=True,null=True)
    
    gst_treatment=models.CharField(max_length=255, blank=True,null=True)
    
    status = models.TextField(default='Active')
  
    activation_tag = models.CharField(max_length=255,default='')
   
    document = models.FileField(upload_to='uploads/', null=True, blank=True)
    notes = models.CharField(max_length=255, blank=True,null=True)
    repeatEvery=models.CharField(max_length=255, blank=True,null=True)
    chart_of_accounts = models.ForeignKey(Chart_of_Accounts, null=True, blank=True, on_delete=models.SET_NULL)

    repeat =models.ForeignKey(CompanyRepeatEvery,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)

    def _str_(self):
        return self.profile_namee

class recurring_expense_History(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    expense=models.ForeignKey(Recurring_Expense,on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    action=models.CharField(max_length=255,default='Created')


class recurring_expense_Reference(models.Model):
    reference_number = models.CharField(max_length=220,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True,blank=True)

class Recurring_Expense_comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    expense = models.ForeignKey(Recurring_Expense,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

# < -------------------- > Stock Adjustment - Start < ------------------------------- >

class StockAdjustment(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    MODE_CHOICES = [
        ('Quantity', 'Quantity'),
        ('Value', 'Value'),
    ]
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='Draft')
    ref_no = models.CharField(max_length=255)
    adj_date = models.DateField(null=True)
    account = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length = 200, blank=True, null=True)
    desc = models.CharField(max_length = 200, blank=True, null=True)
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Save', 'Save'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft')
    file = models.FileField(upload_to="images/",null=True)

class StockAdjustmentItem(models.Model):
    stock_adj = models.ForeignKey(StockAdjustment, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    current_val = models.CharField(max_length = 200, blank=True, null=True)
    changed_val = models.CharField(max_length = 200, blank=True, null=True)
    adjusted_val = models.CharField(max_length = 200, blank=True, null=True)

class StockAdjustmentRefNo(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    logindetails = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True)
    ref_no = models.CharField(max_length=100, default=0, null=True)

class StockAdjustmentReason(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    reason = models.CharField(max_length = 200, blank=True, null=True)

class StockAdjustmentHistory(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    stock_adj = models.ForeignKey(StockAdjustment, on_delete=models.CASCADE)
    ACTION_CHOICES = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, blank=True, null=True)

class StockAdjustmentComment(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    stock_adj = models.ForeignKey(StockAdjustment, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 200, blank=True, null=True)

# < -------------------- > Stock Adjustment - End < ------------------------------- >
#Debit note
class debitnote(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)

    
    profile_name = models.CharField(max_length=100, null=True, blank=True)

    vendor_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    bill_type = models.CharField(max_length=20, null=True, blank=True)
    reference_no = models.BigIntegerField(null=True, blank=True)
    bill_no = models.CharField(max_length=100)
    debitnote_date = models.DateField(null=True, blank=True)
    debitnote_no = models.CharField(max_length=100, null=True, blank=True)
    
    price_list_applied = models.BooleanField(null=True, default=False)
    price_list = models.ForeignKey(PriceList, on_delete = models.SET_NULL,null=True)
    payment_method = models.CharField(max_length=20, null=True,blank=True)
    cheque_number = models.CharField(max_length=100, null=True, blank=True)
    upi_number = models.CharField(max_length=100, null=True, blank=True)
    bank_account_number = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)
    document=models.FileField(upload_to="images/",null=True)
    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    advance_paid = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Saved', 'Saved'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
class debitnote_History(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    debit_note = models.ForeignKey(debitnote, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    action = models.CharField(max_length=20, null=True)


class debitnote_item(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    debit_note=models.ForeignKey(debitnote,on_delete=models.CASCADE,null=True,blank=True)
    
    item=models.ForeignKey(Items, on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)
    price=  models.FloatField(default=0.0, null=True, blank=True)
    tax_rate= models.FloatField(default=0.0, null=True, blank=True)
    discount= models.FloatField(default=0.0, null=True, blank=True)
    total =  models.FloatField(default=0.0, null=True, blank=True)


class debitnote_Reference(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    reference_number = models.BigIntegerField(null=True, blank=True)

class debitnote_Comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True)
    debit_note=models.ForeignKey(debitnote,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
#End

class Retaineritems(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    logindetails = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    retainer=models.ForeignKey(RetainerInvoice, on_delete=models.CASCADE)
    description=models.TextField()
    amount=models.CharField(max_length=100)
    itemname=models.CharField(max_length=100,null=True)
    hsn=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)
    item=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)
    def getNumFieldName(self):
        return 'retainer_invoice_number'

class retInvoiceReference(models.Model):
    reference = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    logindetails = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    
class retainer_payment_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    retainer=models.ForeignKey(RetainerInvoice,on_delete=models.CASCADE,null=True,blank=True)
    payment_opt=models.CharField(max_length=100,null=True,blank=True)
    acc_no=models.CharField(max_length=100,null=True,blank=True)
    upi_id=models.CharField(max_length=100,null=True,blank=True)
    cheque_no=models.CharField(max_length=100,null=True,blank=True)
    bank = models.ForeignKey(Banking,on_delete=models.SET_NULL,null=True,blank=True)

class RetainerInvoiceComment(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    retainer_invoice = models.ForeignKey(RetainerInvoice, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.company} on Retainer Invoice #{self.retainer_invoice.id}"

class RetainerInvoiceHistory(models.Model):
    retainer_invoice = models.ForeignKey('RetainerInvoice', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100, default='')  # Provide a default value here
    # Add any other fields as needed
    
# < -------------------- > Eway Bills < ------------------------------- >
class EwayBill(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True)
    document_type = models.CharField(max_length=100, null=True, blank=True)
    transaction_sub_type = models.CharField(max_length=100, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    eway_billing_address = models.CharField(max_length=100, null=True, blank=True)
    eway_bill_number = models.CharField(max_length=100, null=True, blank=True)
    hsn = models.CharField(max_length=100, null=True, blank=True)
    sac = models.CharField(max_length=100, null=True, blank=True)
    reference_no = models.BigIntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    transaction_type = models.CharField(max_length=100, null=True, blank=True)
    transportation = models.CharField(max_length=100, null=True, blank=True)
    kilometers = models.CharField(max_length=100, null=True, blank=True)
    vehicle_number = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    document=models.FileField(upload_to="images/",null=True)
    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    
    STATUS_CHOICES = [
        ('Saved', 'Saved'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Eway_bill_item(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    EwayBill = models.ForeignKey(EwayBill,on_delete=models.CASCADE,null=True,blank=True)
    item=models.ForeignKey(Items, on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)
    price=  models.FloatField(default=0.0, null=True, blank=True)
    tax_rate= models.FloatField(default=0.0, null=True, blank=True)
    discount= models.FloatField(default=0.0, null=True, blank=True)
    total =  models.FloatField(default=0.0, null=True, blank=True)

class Eway_bill_Reference(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    reference_number = models.BigIntegerField(null=True, blank=True)

class EwayBillHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    EwayBill = models.ForeignKey(EwayBill, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    action = models.CharField(max_length=20, null=True)

class Eway_Bill_Comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True)
    eway_bill = models.ForeignKey(EwayBill,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
class Transportation(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    transportation = models.CharField(max_length=500,null=True,blank=True)
    
#End
#Cash in hand
class CashInHand(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    adjustment_coices = (
        ('Reduce Cash','Reduce Cash'),
        ('Add Cash','Add Cash')
    )
    adjustment = models.CharField(max_length=50,choices=adjustment_coices)
    amount = models.BigIntegerField(default=0)
    date = models.DateTimeField()
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.adjustment

class CashInHandHistory(models.Model):
    user = models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    action_choices = (
        ('Created','Created'),
        ('Edited','Edited')
    )
    cih = models.ForeignKey(CashInHand,on_delete=models.CASCADE,null=True,blank=True)
    action = models.CharField(max_length=50,choices=action_choices)
    
class Payment_recieved(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    customer_email=models.EmailField(max_length=220,null=True,blank=True)
    customer_billingaddress=models.CharField(max_length=220,null=True,blank=True)
    customer_GSTtype=models.CharField(max_length=220,null=True,blank=True)
    customer_GSTnumber=models.CharField(max_length=220,null=True,blank=True)
    customer_place_of_supply=models.CharField(max_length=220,null=True,blank=True)
    payment_date = models.DateField(null=True)
    reference_number=models.IntegerField(blank=True,null=True,)
    payment_method = models.CharField(max_length=100,null=True,blank=True)
    payment_number=models.CharField(max_length=100,null=True,blank=True)
    cheque_number = models.CharField(max_length=220,null=True,blank=True)
    upi_id =models.CharField(max_length=220,null=True,blank=True)
    bank_account_number = models.CharField(max_length=255, blank=True, null=True)
    amount_to_apply = models.FloatField(default=0.0, null=True, blank=True)
    amount_to_credit = models.FloatField(default=0.0, null=True, blank=True)
    total_payment = models.FloatField(default=0.0, null=True, blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)  
    payment_number=models.CharField(max_length=100,null=True,blank=True)


class Payment_details(models.Model): 
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    payment_recieved=models.ForeignKey(Payment_recieved,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    payment=models.IntegerField(blank=True,null=True,)
    invoice_amount =models.IntegerField(blank=True,null=True,)
    invoice_number=models.CharField(max_length=220,null=True,blank=True)
    invoice_type=models.CharField(max_length=220,null=True,blank=True)
    Due_Date = models.DateField(null=True)
    Date=models.DateField(null=True)  

class Payment_reference(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=220,null=True,blank=True)

class payment_history(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    payment_recieved=models.ForeignKey(Payment_recieved,on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    action_choices = [
        ('Created', 'Created'), 
        ('Edited', 'Edited')
        ]
    action = models.CharField(max_length=10, choices=action_choices,null=True)

class Payment_Comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True)
    payment_recieved = models.ForeignKey(Payment_recieved,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
class Expense(models.Model):
    #company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField()
    account = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=100, null=True)
    hsn_code = models.CharField(max_length=100, blank=True, null=True)
    sac_code = models.CharField(max_length=100, blank=True, null=True)
    expense_number = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100,null=True)
    vendor_email = models.EmailField()
    vendor_gstin = models.CharField(max_length=100)
    vendor_gst_type = models.CharField(max_length=100)
    vendor_source_of_supply = models.CharField(max_length=100,null=True)
    vendor_billing_address = models.TextField(null=True)
    customer_name = models.CharField(max_length=100, null=True)
    customer_email = models.EmailField(null=True)
    customer_gstin = models.CharField(max_length=100, null=True)
    customer_gst_type = models.CharField(max_length=100, null=True)
    customer_price_of_supply = models.CharField(max_length=100, null=True)
    customer_billing_address = models.TextField(null=True)
    note = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    status = models.CharField(max_length=20, null=True)


##########Payment made############
class payment_made(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)
    vendor_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    source_of_supply = models.CharField(max_length=100, null=True, blank=True)
    reference_no = models.BigIntegerField(null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_no = models.CharField(max_length=100, null=True, blank=True)
    cheque_number = models.CharField(max_length=100, null=True, blank=True)
    upi_number = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    document=models.FileField(upload_to="images/",null=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Saved', 'Saved'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class payment_made_bills(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    payment_made = models.ForeignKey(payment_made, on_delete=models.CASCADE,null=True)
    bill_type = models.CharField(max_length=100, null=True, blank=True)
    bill_number=models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now_add=True)
    amount_due= models.FloatField(default=0.0, null=True, blank=True)
    payment= models.FloatField(default=0.0, null=True, blank=True)


class payment_made_Reference(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    reference_number = models.BigIntegerField(null=True, blank=True)

class payment_made_Comments(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True)
    payment_made=models.ForeignKey(payment_made,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

class payment_made_History(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    payment_made=models.ForeignKey(payment_made,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    action = models.CharField(max_length=20, null=True)

class Estimate(models.Model):
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True) 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    customer_email = models.EmailField(max_length=220,null=True,blank=True)
    customer_bill_address = models.CharField(max_length=255)
    customer_gst_treatment = models.CharField(max_length=255)
    customer_gst_number = models.CharField(max_length=255)
    customer_place_of_supply = models.CharField(max_length=255)
    estimate_date = models.DateField()
    payment_term = models.ForeignKey(Company_Payment_Term,on_delete=models.CASCADE)
    expiration_date = models.DateField()
    reference_number = models.IntegerField()
    estimate_number = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    terms_and_condition = models.CharField(max_length=255)
    document = models.FileField()
    sub_total = models.FloatField()
    cgst = models.FloatField()
    sgst = models.FloatField()
    tax_amount_igst = models.FloatField()
    shipping_charge = models.FloatField()
    adjustment = models.FloatField()
    grand_total = models.FloatField()

    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Saved', 'Saved'),
    ]
    status = models.CharField(max_length=255,  choices=STATUS_CHOICES)
    converted_to_invoice = models.ForeignKey(invoice,on_delete=models.CASCADE,null=True)
    converted_to_recurring_invoice = models.ForeignKey(RecurringInvoice,on_delete=models.CASCADE,null=True)
    converted_to_sales_order = models.ForeignKey(SaleOrder,on_delete=models.CASCADE,null=True)

    def getNumFieldName(self):
        return 'estimate_number'


class EstimateItems(models.Model):
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    hsn = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    tax_rate = models.FloatField()
    discount = models.FloatField()
    total = models.FloatField()
    estimate = models.ForeignKey(Estimate,on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)

class EstimateReference(models.Model):
    reference_number = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

class EstimateHistory(models.Model):
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    estimate = models.ForeignKey(Estimate,on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=255)

class EstimateComment(models.Model):
    estimate = models.ForeignKey(Estimate,on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details = models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

class PurchaseOrder(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,blank=True, null=True) 
    vendor_email = models.EmailField()
    vendor_billing_address = models.CharField(max_length=255)
    vendor_gst_type = models.CharField(max_length=255)
    vendor_gst_number = models.CharField(max_length=255)
    vendor_place_of_supply = models.CharField(max_length=255)
    #CUSTOMER
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    customer_email = models.EmailField(null=True)
    customer_billing_address = models.CharField(max_length=255,null=True)
    customer_gst_type = models.CharField(max_length=50,null=True)
    customer_gst_number = models.CharField(max_length=20,null=True)
    customer_place_of_supply = models.CharField(max_length=100,null=True)

    org_name = models.CharField(max_length=255,null=True)
    org_gst_number = models.CharField(max_length=20,null=True)
    org_email = models.EmailField(null=True)
    org_address = models.CharField(max_length=255,null=True)
    org_street = models.CharField(max_length=255,null=True)
    org_city = models.CharField(max_length=100,null=True)
    org_state = models.CharField(max_length=100,null=True)

    
    purchase_order_date = models.DateField()
    payment_terms = models.ForeignKey(Company_Payment_Term, on_delete=models.CASCADE,blank=True, null=True)
    expiration_date = models.DateField()
    reference_number = models.CharField(max_length=255)
    
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('UPI', 'UPI'),
        ('Bank', 'Bank'),
    ]
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    
    cheque_number = models.CharField(max_length=255, blank=True, null=True)
    upi_number = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=255, blank=True, null=True)
    sales_order_number = models.CharField(max_length=100,null=True)
    
    
    description = models.CharField(max_length=255)
    terms_and_condition = models.TextField()
    document = models.FileField(upload_to='documents/',blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    adjustment = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    advanced_paid = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    Save='Save'
    Draft='Draft'
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Save', 'Save'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft') 
    
    
class PurchaseOrderItems(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True, null=True)
    hsn = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=True, null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    
class PurchaseOrderReference(models.Model):
    reference_number = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)

class PurchaseOrderHistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, blank=True, null=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, blank=True, null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    current_date = models.DateField()
    action = models.CharField(max_length=255)
    
class Purchaseorder_comments_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=True, null=True)
    comment=models.TextField(max_length=500)
    
class purchaseorder_doc_upload_table(models.Model):
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, blank=True, null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')    
#End