def process_order(customer_name,product_name, price,quantity , country_code,discount_code):
    if customer_name:
        if product_name:
            if country_code=="FR": shipping_cost=10 
            elif country_code=="DE": shipping_cost=15
            elif country_code=="US": shipping_cost=20
            else: shipping_cost=30 
            if discount_code=="DISCOUNT10": discount=0.10 
            else: discount=0 
            total_price=(price*quantity)*(1-discount)+shipping_cost
            if total_price>100: status="VIP"
            else: status="STANDARD"
            return {"customer_name":customer_name,"product_name":product_name,"total_price":total_price,"status":status}
        else: raise ValueError("Customer name and product name must be provided")
