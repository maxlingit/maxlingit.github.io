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
	- monthly - is the calendar month
	- calendar week - weekly start on Sunday and end on Saturday
- below is the sketch graph from Scarlett

![[salesDashborad.png]]

# 3. Data Source

- This template is created under GERS old sales data from Feb 2024 - July 2024
- But the new dashboard is going to be based on Netsuite data source

# 4. Metrics
	Note: will use [Netsuite field] name and {GERS Field} Name to distingush the metric from different data source
### 1. Transaction datetime

- Definition 
	- Transaction datetime should be based on BigCommerce Order time
	- these datetime field can be expand into Year, Quarter, Month, Week, Weekday, Day & time
-  Database field
	- ("transaction"."trandate")
	- {SO_WR_DT} Or {FINAL_DT}
### 2. Quantity - Open_Qty

- Definition 
	- The total number of units sold within a specified period
	- net with **cancel order** quantity 
- Metric Interaction with time
	- The datetime the sales order is place and paid for.
- Database field
	- ("transactionLine"."quantity")  - positive value
	- {SO_LN.QTY}
#### 2.1 Open_Qty - Cancel 

- Definition 
	- units sold within a specified period but order was canceled before we ship the item to customers

- Metric Interaction with time
	- it is shown based on the datetime order was placed (not the cancelation time)
#### 2.2 Open_Qty - Sales

- Definition 
	- units sold within a specified period

- Metric Interaction with time
	- it is shown based on the datetime order was placed
### 3. OpenSales -Open_Sales

- Definition 
	- The total dollar amount of sales orders that have been received but not yet fulfilled or completed.
	
- Metric Interaction with time
	- The datetime the sales order is place and paid for.
	
- Database field
	- {SO_LN.QTY * SO_LN.UNIT_PRC}
	- ("transactionLine"."creditforeignamount") OR ("transactionLine"."debitforeignamount")
#### 3.1 Open_Sales - Cancel 

- Definition 
	-  The total dollar amount of sales orders within a specified period but order was canceled before we ship the item to customers

- Metric Interaction with time
	- it is shown based on the datetime order was placed (not the cancelation time)
#### 3.2 Open_Sales - Sales

- Definition 
	-  The total dollar amount of sales orders within a specified period

- Metric Interaction with time
	- it is shown based on the datetime order was placed

### 4. Order Items

In Netsuite each sales order has the following sales item type, this is how it is classified
- Item type
	1. Inventory or kit   - product
	3. Service item        - warranty or membership
	4. Shipping item     - shipping fee

### 5. Inventory category

- Product Group
- Department
- Class
- Collection

# 5. Visualization
    
    - The type of chart or graph used to display the metric on the dashboard (e.g., line chart, bar graph, pie chart).
# 6. Segmentations
    
    - Any segments or filters applied to the metric (e.g., by region, by product line, by customer type).
# 7. **Context/Notes**:

- **Metric Name**:
    
    - **Definition**: A clear and concise definition of the metric.
    - **Purpose**: The reason for tracking this metric and how it aligns with business objectives.
- **Category**:
    
    - The broader category to which this metric belongs (e.g., Sales, Marketing, Customer Support).
- **Calculation/Formula**:
    
    - Detailed explanation of how the metric is calculated, including any necessary formulas.
- **Data Source**:
    
    - The origin of the data used to calculate the metric (e.g., CRM system, Google Analytics, internal database).
- **Frequency**:
    
    - How often the metric is updated (e.g., daily, weekly, monthly).
- **Owner**:
    
    - The individual or team responsible for monitoring and reporting this metric.
- **Target/Goal**:
    
    - The benchmark or target value for the metric. Include short-term and long-term goals if applicable.

    
    - Additional context or notes about the metric, including any assumptions, limitations, or external factors that may impact it.