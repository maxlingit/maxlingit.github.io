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


## Meeting Note
1. test if sales order has disable avalara how it will affect the invoice.  
2. 其中如果碰到需要某些货品是免税，avalara自动设置时收税，则需要一些设置
	1. 到customer页面 ==>Financial 
	2. if we map customer to "tax item" != avatax, it will only map tax by sku tax code in the portal.
3. 店铺信用抵扣 大部分是0 税率，但是某些州是有税的。会造成tax different
4. To answer your recent question the reason this transaction was not exempt from tax is because the tax code NT is not allowed and disabled if you an SST Member.

	Ref Link. [https://knowledge.avalara.com/bundle/mws1662464730314_mws1662464730314/page/zfs1665053707514.html](https://knowledge.avalara.com/bundle/mws1662464730314_mws1662464730314/page/zfs1665053707514.html "https://knowledge.avalara.com/bundle/mws1662464730314_mws1662464730314/page/zfs1665053707514.html")
	
	**Solution**: Use SST Approved Non-taxable transaction TaxCode ON030000