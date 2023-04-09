#Input elements
sku_qty = 1
htprice = 43.15
shipping_charge = 10.40
minimum_order_fee = 20
fulfilment_fee = 12
VAT = 0.2
Amazon_fee = 0.07

#techmargin
tech_margin =  0.2

# Functions to define ingram base price

def fn_htprice_withadditionalcharges(qty,price,shipping,minimumorderfee,fulfilmentfee):
    productprices = 0
    fullprice = qty * price
    if fullprice < 200:
        productprices = (fullprice + shipping + minimumorderfee + fulfilmentfee)
    else:
        productprices = (fullprice + shipping + fulfilment_fee)
    return productprices

def fn_addvat (productprices,vat):
    myvat = round((productprices * vat),2)
    return myvat

def fn_fullprice (productprices,myvat):
    myfullttc = round((productprices + myvat),2)
    return myfullttc


def fn_techmargin(productprices,margin) :
    price_with_margin =  productprices * (1+margin)
    return price_with_margin

def fn_amazonfeee(price_with_margin,amazon_margin):
    amazon_netmargin = round((price_with_margin * amazon_margin),2)
    return amazon_netmargin

def fn_amazon_payout(price_with_margin,amazon_netmargin):
    amazon_payout = round((price_with_margin - amazon_netmargin),2)
    return amazon_payout

def fn_totalsalemargin (amazon_payout,myfullttc):
    techtotalsalemargin = round((amazon_payout - myfullttc),2)
    return techtotalsalemargin


# RESULTS 
# Define Ingram base price
sku_ht_price = fn_htprice_withadditionalcharges(sku_qty,htprice,shipping_charge,minimum_order_fee,fulfilment_fee)
print("ingram ht price including additional fees is :" +  str(sku_ht_price))

myvatamount = fn_addvat(sku_ht_price,VAT)
print("ingram VAT amount is :" + str(myvatamount))

myttcprice = fn_fullprice(sku_ht_price,myvatamount)
print("ingram  ttc amount is : " + str(myttcprice) )

mytechpricewithmargin = fn_techmargin (sku_ht_price,tech_margin)
print("my sale price including " + str(tech_margin * 100) + " % margin is :" + str(mytechpricewithmargin))

mytechvat = fn_addvat(mytechpricewithmargin,VAT)
print("my sale price vat amount will be : " + str(mytechvat))

mytechfullprice =fn_fullprice(mytechpricewithmargin,mytechvat)
print("Tech ttc amount is : " + str(mytechfullprice))

amazon_net_margin = fn_amazonfeee(mytechfullprice,Amazon_fee)
print("amazon fee is : " + str(amazon_net_margin))

amazon_payout = fn_amazon_payout(mytechfullprice,amazon_net_margin)
print("amazon payout will be: " + str(amazon_payout))

Mytechtotalmargin = fn_totalsalemargin(amazon_payout,myttcprice)
print("amazon payout - ingram purchase is = " + str(Mytechtotalmargin))

