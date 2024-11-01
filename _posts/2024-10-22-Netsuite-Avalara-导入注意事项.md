---
title: Netsuite Avalara 导入注意事项
date: 2024-10-22
categories:
  - 周报
tags:
  - F
  - JIE
  - 财务部
layout: post
---
## Netsuite Avalara 从Bigcommerce API 导入注意事项



1. 订单主行上的location，需要设置为 ZG-LA-DcSelf-New
	- 如图 ![[Pasted image 20241022150346.png]]
1. 导入的客户里的 Financial ->税务信息  需要勾选taxable，tax item选择AVATAX
	- 如图 ![[Pasted image 20241022150546.png]]
3. 订单的Shipping address一定要对应BigCommerce的shipping address，有时客户的地址和实际发货地址不一样，会导致计算错误
4. 客户使用店铺积分抵扣： 注意按照我们测试的设置 ，税后抵扣
5. 销售订单行上的每个ITEM上面挂的tax code是AVATAX 
	- 如图![[Pasted image 20241022151826.png]]
6. Shipping下面挂的tax code 也是AVATAX
	- ![[Pasted image 20241022151907.png]]