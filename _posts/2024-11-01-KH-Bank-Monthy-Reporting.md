---
layout: post
categories:
  - Procedures
title: KH Bank Monthly Reporting
date: 2024-11-01
tags:
  - 财务部
  - JIE
---
# Overview

## 1. Account Receivable Aging
### Step 1: Source:  A/R Aging Summary(Customer & AIO) W/AIO Filter
- **Note : Aging Option ==> {Aging based on : Transaction Date,
						 Ages as of : *Reporting end date*}** 

### Step 2: Export to Excel

### Step 3: Pivot table

- Rows : AIO Account
- Values: Aging date from 90 to current
- Calculated Field: <30  = current + 30
- sort by :Total column

### Step 4: Adjust the detail
- All the Customer:公司间客户 need to assign a AIO Account as the receivable Platform
- Move around some over 90 days intercompany to 30-60 (because it is not real over 90 days, just internal accounting issue)
- For Hulala home or any intercompany receivable has large AR balance, we will let the Receivable Flow Through to Karat Home 
	- For example: Amazon owes hulala Home, hulala home owes karat home. -> we will put amazon's receivable on Karat Home AR aging report
- Make sure the detail total match with original total

### Step 5: Copy prior month format

The prior month format has the following thing need attention
1. Make sure the title shows correct period
2. Platform name is sorted by large to small of the total column
3. The grand total need to double check to match the original AR summary

### Step 6: Save to a PDF file

- save the Account Receivable Aging report to a PDF name ：AR Aging Summary - (period end)




## 2. Inventory Valuation summary

### Step 1: Source:  存货簿报告（按仓库）
- Note : remove all filter. Should match Balance Sheet 

### Step 2: Export to Excel
- save to .xlsm or .xlsx format to keep all format

### Step 3: Pivot table

- Rows : 地点
- Values: 期末现有库存量  &  期末现有库存值
- sort by : 期末现有库存值

### Step 4: Copy prior month format

The prior month format has the following thing need attention
1. Make sure the title shows correct period
2. Location name is sorted by large to small of the total column
3. The grand total need to double check to match the original AR Inventory valuation summary
### Step 5: Save to a PDF file

- save the Inventory valuation report to a PDF name ：Inventory Report - (period end)

## 3. Borrowing base certificate

There are 4 major worksheet we need to work on
- Borrowing Base Main page
- Ineligible Calculation workpaper
- NJ Lease Schedule
- Houston Lease Schedule
#### Borrowing Base Main page

This is the front page of the borrow base, and it is the summary of everything

There are 2 major sections
###### Eligible Account Receivable

- GROSS BOOK VALUE OF ACCOUNTS  -> This need to input
- Accounts past 90 days past invoice date  -> will flow from the worksheet
- Concentration rule (25%) (Wayfair 40%)  -> will flow from the worksheet
- Cross-aged (90 days) / Taint rule (25%)  -> will flow from the worksheet
- Accounts due from affiliates -> will need to fix this in the future

###### Eligible Inventory

- TOTAL INVENTORY     -> will flow from the worksheet
- Slow moving, obsolete, unsalable or unfit for further processing  -> relative fix amount, inventory impairment on the book
- In transit or located outside of the U.S. -> will flow from the worksheet
###### Rent reserve to be deducted

- This is due to we don't have landlord's waiver, use one month rent as reserve.

#### Ineligible AR Calculation worksheet

- 90 days +  over due. -> this is the total of AR amount over 90 days
- Taint rule (25%)   -> this is the amount <90 days overdue, but the customer has 25% over 90 day. will make entire account receivable ineligible
- Concentration Limits   ->  customer AR balance that is over 25% will deem to be ineligible. But bank gives us 40% for wayfair.

#### Ineligible Inventory Calculation worksheet

- Total inventory
- minus: the inventory in our warehouse, Houston, NJ, DFW
- equal: Ineligible Inventory

