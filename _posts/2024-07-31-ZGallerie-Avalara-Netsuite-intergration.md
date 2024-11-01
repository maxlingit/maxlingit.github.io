---
layout: post
categories:
  - Procedures
title: ZGallerie Avalara Netsuite Intergration
date: 2024-08-01
tags:
  - 财务部
  - JIE
  - F
---
- according to Jeremy it is not available between avalara bigcommerce connect and avalara netsuite connector.![[Pasted image 20240809125637.png]]
- so we have to figure out why netsuite have a different calculation result from bigcommerce



测试订单：

Avalara: 
	Document code:  cogc1vyegn_1011439_de69e1
Netsuite:  SOZG031007

# Pending Items
1. Location must be in DC address
2. Latitude and log 
3. Inventory location can be anything
4. Customer Shipping address must match bigCommerce 
5. Shipping state name must match