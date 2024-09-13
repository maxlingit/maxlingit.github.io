---
title: China-Accounting-Note
date: 2024-05-29
categories:
  - 步骤
tags:
  - F
  - JIE
  - 财务部
layout: post
---
## Accounting


## Invoicing

- Confirm only hit the Sales Revenue when items has been shipped out
- If customer payment that is not shipped, they manually prepare Journal Entry to hit the customer deposit account.
- If shipped item got return, they will prepare "customer refund" step
- If non-shipped item returned, they  they manually prepare Journal Entry 

## Revenue Recognition

- Sales Revenue are booked only when shipped.
- Shipping Revenue was booked to shipping expense intentionally- because they say someone say they should do it 

## Payment

- all inventory vendor is using AP Accrual
- All logistic vendor is using AP Accrual
- All other vender is Journal entry to hit the "other payable account" -manually accrual
- when making a payment, they hit the bank and "other payable account" using journal entry
- They reject to go through normal AP process for other vendors. need CFO approval 
## Vendor

- They are not sure if they can add vendor and use netsuite to enter bill. 
- because it require a person to "enter bill" --> "make payment"
- I suggest US AP person will enter bill and China team will make payment (for accounting process)

## Customer Deposit

- they have been putting everything into a customer deposit account. All the bank, receivable, payable should be correct, but they flow any unreconciled item to customer deposit account
- And they say they have excel can track the balance.
## Sales Tax

- not matched on invoice, total invoice is wrong.
- but there is a memo in NS will show the sales tax amount.
- they manually calculate sales tax and Journal entry once a month.
- returned item tax was not calculated properly
- The reason the sales tax is wrong is because when IT import the sales order from BigCommerce, the bigcommerce only show tax and shipment in one line instead of item level (I am working with IT)
- Another issue is Netsuite has a tax function, IT can't import the tax amount directly into netsuite. Netsuite  sales tax field only allow their own calculation. For example, we can only input sales amount and customer address, Nesuite will compute sales tax for you. But bigcommerce is the one handle the sales tax calculate and push into ERP. Netsuite always shows the tax differences in the sales order compare to real sales order.

