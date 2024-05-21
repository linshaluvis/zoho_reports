        # -------------------------------customer and vendor balances--------------------------------

    
     path('customerBalances',views.customerBalances,name='customerBalances'),
    path('CustomizecustomerBalances',views.CustomizecustomerBalances,name='CustomizecustomerBalances'),
    path('sharecustomerBalances',views.sharecustomerBalances,name='sharecustomerBalances'),

    path('vendorBalances',views.vendorBalances,name='vendorBalances'),
    path('CustomizevendorBalances',views.CustomizevendorBalances,name='CustomizevendorBalances'),
    path('sharevendorBalances',views.sharevendorBalances,name='sharevendorBalances'),