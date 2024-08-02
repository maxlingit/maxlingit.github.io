---
layout: post
categories:
  - Procedures
title: ZGallerie Sales DashboardReport
date: 2024-08-01
tags:
  - 财务部
  - JIE
  - F
---
# 1. Project Overview

This dashboard project is requested by Scarlett & Jie to make a dashboard template for IT department to make a sales dashboard for ZG management team to see the sales data and to make sure they can achieve objective
# 2. Project Goals & Objectives

- This dashboard is used by Sobia for finance department and Kelly for planning.
- They need to see sales data for different categories
	- **Open Order**  - When customer order online and make payment.
	- **Shipped Order**  - When ZG ship the product and fulfill the sales order
	- **Unship Order** - amount of order remain open (this data is going change all the time, we may on a separate dashboard)
	
- For each sales data it may have sub-category like sales item type
	- Product Sales
	- Membership Sales
	- Warranty Sales
		- product warrant
		- shipping warranty
	- Shipping fee 


- For each sales category, it will have 2 different situation. refund or cancel order
	- Open Order （order placed online and paid）
		- All paid sales order 
		- And order cancelation before is was shipped
		
	- Shipped Order
		- All the order fulfilled.
		- **Return**: Customer received the product and want to return the product

- Time metrics : we will follow the sales calendar week and monthly timeframe to expand the data
	- monthly - is the retail 4-4-5 calendrer
	- calendar week - weekly start on Sunday and end on Saturday
	- 1st fiscal week start from February 4
	- Month is fiscal calendrer.
![[Pasted image 20240802155123.png]]
- below is the sketch graph from Scarlett

![[salesDashborad.png]]

# 3. Data Source

- This template is created under GERS old sales data from Feb 2024 - July 2024
- But the new dashboard is going to be based on Netsuite data source

# 4. Metrics

### 1. Transaction datetime

- Definition 
	- Transaction datetime should be based on BigCommerce Order time
	- these datetime field can be expand into Year, Quarter, Month, Week, Weekday, Day & time
-  Database field
### 2. Quantity - Open_Qty

- Definition 
	- The total number of units sold within a specified period
	- net with **cancel order** quantity 
- Metric Interaction with time
	- The datetime the sales order is place and paid for.
#### 2.1 Open_Qty - Cancel 

- Definition 
	- units sold within a specified period but order was canceled before we ship the item to customers

- Metric Interaction with time
	- it is shown based on the datetime order was **canceled**
#### 2.2 Open_Qty - Sales

- Definition 
	- units sold within a specified period

- Metric Interaction with time
	- it is shown based on the datetime order was placed
### 3. OpenSales - Open_Sales

- Definition 
	- The total dollar amount of sales orders that have been received but not yet fulfilled or completed.
	
- Metric Interaction with time
	- The datetime the sales order is place and paid for.
	
#### 3.1 Open_Sales - Cancel 

- Definition 
	-  The total dollar amount of sales orders within a specified period but order was canceled before we ship the item to customers

- Metric Interaction with time
	- it is shown based on the datetime order was **canceled**
#### 3.2 Open_Sales - Sales

- Definition 
	-  The total dollar amount of sales orders within a specified period

- Metric Interaction with time
	- it is shown based on the datetime order was placed
### 4.SO_DeliveryIncome

- Definition 
	- The total dollar amount of shipping fee collected when sales orders that have been received but not yet fulfilled or completed.
	
- Metric Interaction with time
	- The datetime the sales order is place and paid for.
#### 4.1 SO_DeliveryIncome - Cancel 

- Definition 
	-  The total dollar amount of shipping fee collected on sales orders within a specified period but order was canceled before we ship the item to customers

- Metric Interaction with time
	- it is shown based on the datetime order was **canceled**
#### 4.2 SO_DeliveryIncome - Sales

- Definition 
	-  The total dollar amount of shipping fee collected on sales orders within a specified period

- Metric Interaction with time
	- it is shown based on the datetime order was placed
	
### 5. SO_WK_vs_WK_Variance

- Definition 
	- The percentage change in the dollar amount of **Net** sales orders + shipping fee(#pending) (net with cancelation)from one week compare to previous week
	- This column doesn't separately calculate the %change in cancelled order, only net sales+ shipping fee
	
### 6. SO_Mtd_vs_Mtd variance

- Definition 
	- The percentage change in the dollar amount of **Net** sales orders + shipping fee(#pending)  (net with cancelation) from one **Month** compare to previous week
	- This column doesn't separately calculate the %change in cancelled order, only net sales+ shipping fee


### 7 Quantity - Shippied_Qty

- Definition 
	- The total number of units fulfilled a specified period
	- net with **cancel order** quantity 
	
- Metric Interaction with time
	- The datetime the order is fulfilled and shipped.
	
- Database field

#### 7.1 Shippied_Qty - Return 

- Definition 
	- units **sold and fulfilled** within a specified period but order was return by customer

- Metric Interaction with time
	- it is shown based on the datetime order is **returned**
#### 7.2 Shippied_Qty - Sales

- Definition 
	- units **fulfilled** within a specified period

- Metric Interaction with time
	- it is shown based on the datetime the order is **fulfilled**
### 8. Shipped Sales - Shipped_Sales

- Definition 
	- The total dollar amount of sales orders that have been fulfilled or completed.
	
- Metric Interaction with time
	- The datetime the sales order order is fulfilled and shipped.
	
#### 8.1 Shipped_Sales - Returned 

- Definition 
	-  The total dollar amount of fulfilled sales orders within a specified period but order was returned 

- Metric Interaction with time
	- it is shown based on the datetime order was  **returned**
#### 8.2 Shipped_Sales - Sales

- Definition 
	-  The total dollar amount of sales orders was **fulfilled** within a specified period

- Metric Interaction with time
	- it is shown based on the datetime order was **fulfilled**

### 9. DeliveryIncome
### 9. WK_vs_WK_Variance

- Definition 
	- The percentage change in the dollar amount of **Net** Fulfilled sales orders + shipping fee (net with cancelation) from one week compare to previous week
	- This column doesn't separately calculate the %change in cancelled order, only net sales+ shipping fee
	
### 10. Mtd_vs_Mtd_variance

- Definition 
	- The percentage change in the dollar amount of **Net** sales orders + shipping fee (net with cancelation) from one **Month** compare to previous week
	- This column doesn't separately calculate the %change in cancelled order, only net sales+ shipping fee

### 11. Order Items

In Netsuite each sales order has the following sales item type, this is how it is classified
- Item type
	1. Inventory or kit   - product
	3. Service item        - warranty or membership
	4. Shipping item     - shipping fee

### 11. Segmentations

We need to add a **filter** to enable user to select the follow segmentation to see the metrics

- Product Group
- Department
- Class
- Collection

**We need to be able to pull multiple segmentation in the same BI report.** 