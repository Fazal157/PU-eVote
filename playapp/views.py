from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import OnlineOrderForm




# ✅ existing shoe list here (don’t delete)
# shoes = [...]

def order_view(request, product_id):
    product = next((s for s in shoes if s["id"] == product_id), None)
    if not product:
        return HttpResponse("❌ Product not found", status=404)
    return render(request, "order_form.html", {"product": product})


# your shoes list remains same here

def order_form(request, shoe_id):
    product = next((s for s in shoes if s["id"] == shoe_id), None)
    if not product:
        return HttpResponse("Product not found.")
    return render(request, "order_form.html", {"product": product})

def submit_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")
        product = request.POST.get("product")
        price = request.POST.get("price")

        # You can save this info to a database later
        return HttpResponse(f"""
        <h2>Order Submitted Successfully!</h2>
        <p>Customer: {name}</p>
        <p>Email: {email}</p>
        <p>Phone: {phone}</p>
        <p>City: {city}</p>
        <p>Product: {product}</p>
        <p>Price: PKR {price}</p>
        <p>Delivery Address: {address}</p>
        """)
    return HttpResponse("Invalid request.")


#  Sample utility function
def calculate():
    return "This is calculate function"

#  List of 30 Nike Shoes
shoes = [
    {"id": 1, "name": "Bata Air Force 1", "price": 15000, "image":"https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco,u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/85321d65-e8b2-4b85-a097-6b8a7cd32345/WMNS+AIR+JORDAN+1+RETRO+HI+OG.png"},
    {"id": 2, "name": "Bata Air Max 90", "price": 16500, "image": "https://www.hopkicks.pk/image/cache/catalog/2024/OCT%2024/ISHOES/P2/47/10-500x500.jpg"},
    {"id": 3, "name": "Bata Air Jordan 1", "price": 20000, "image":"https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/545bfadf-e33a-4877-bfb5-a86dfbd1e2c7/NIKE+AIR+MAX+PLUS+G+NRG.png""jordan1.jpg"},
    {"id": 4, "name": "Bata Dunk Low", "price": 14000, "image": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/98d7df61-df92-4982-958d-eee754acd3d7/NIKE+DUNK+LOW+RETRO+SE.png""dunklow.jpg"},
    {"id": 5, "name": "Bata Blazer Mid", "price": 12000, "image":"https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4480801f-d39b-4b05-a61e-42cdfa2b4eb0/A%27ONE.png""blazer.jpg"},
    {"id": 6, "name": "Bata Pegasus 40", "price": 15500, "image":"https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/4f502640-4972-433d-ac1a-912a88214b85/NIKE+VOMERO+18+GTX.png""pegasus40.jpg"},
    {"id": 7, "name": "Bata ZoomX Vaporfly", "price": 19500, "image": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/ea35ca83-cfdd-4088-b442-977d3069fc3f/AIR+MAX+90+PRM.png""vaporfly.jpg"},
    {"id": 8, "name": "Bata Air Max 97", "price": 18000, "image": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/c786fcae-2410-405f-99c4-0c9b51ba5fc4/NIKE+SHOX+NZ.png""airmax97.jpg"},
    {"id": 9, "name": "Bata Air Max Plus", "price": 17500, "image": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/dcd6af3a-e329-42a2-b4c6-3595d00a0796/NIKE+SHOX+NZ.png""airmaxplus.jpg"},
    {"id": 10, "name": "Bata LeBron 20", "price": 20000, "image":"https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/6087eda1-2dd5-40f7-8f55-462b91524bf9/AIR+JORDAN+5+RETRO+OG.png" "lebron20.jpg"},
    {"id": 11, "name": "Bata Kyrie 7", "price": 17000, "image":"https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/f0fded68-db96-4381-aabd-3b3469511f0f/AIR+MAX+90.png" "kyrie7.jpg"},
    {"id": 12, "name": "Bata KD 15", "price": 18500, "image": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/8b042c57-4beb-4c7a-b0ae-6fdf8cd62495/AIR+MAX+PLUS.png""kd15.jpg"},
    {"id": 13, "name": "Bata Alphafly Next%", "price": 20000, "image":"https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/c5550a8b-7d51-4c78-a534-e8d390726b45/NIKE+GATO.png" "alphafly.jpg"},
    {"id": 14, "name": "Bata Air Max 270", "price": 16000, "image": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/549721bf-bf57-4d6b-bf35-9ddec91c5c3f/NIKE+C1TY+PRM.png" "airmax270.jpg"},
    {"id": 15, "name": "Bata React Infinity Run", "price": 17500, "image":"https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/a88e2bef-3526-4287-b8fc-245126b31838/NIKE+SHOX+TL+PRINT.png" "reactinfinity.jpg"},
    {"id": 16, "name": "Bata Free Run 5.0", "price": 12000, "image":"https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/4ef8a90b-b59d-433a-8a74-737bc5ff5a98/TOTAL+90.png" "freerun.jpg"},
    {"id": 17, "name": "Bata Air Max 720", "price": 19000, "image":"https://speedsports.pk/cdn/shop/files/AURORA_FJ2577-800_PHCFH001-2000.jpg?v=1751357424&width=400" "airmax720.jpg"},
    {"id": 18, "name": "Bata Metcon 8", "price": 15000, "image":"https://www.bata.com.pk/cdn/shop/files/883-4112_1_1_545x545.webp?v=1757075086" "metcon8.jpg"},
    {"id": 19, "name": "Bata SB Dunk High", "price": 14000, "image":"https://www.bata.com.pk/cdn/shop/files/854-4323-_1_545x545.webp?v=1757099322" "sbdunk.jpg"},
    {"id": 20, "name": "Bata Cortez", "price": 11000, "image":"https://www.bata.com.pk/cdn/shop/files/883-4541-_1_545x545.webp?v=1759151384" "cortez.jpg"},
    {"id": 21, "name": "Bata Air Huarache", "price": 14500, "image":"https://www.bata.com.pk/cdn/shop/files/883-4539-_1_545x545.webp?v=1759151309" "huarache.jpg"},
    {"id": 22, "name": "Bata Shox R4", "price": 16000, "image":"https://www.bata.com.pk/cdn/shop/files/883-6111_1_1_545x545.webp?v=1757075269" "shoxr4.jpg"},
    {"id": 23, "name": "Bata Air Max Tailwind", "price": 15000, "image":"https://www.bata.com.pk/cdn/shop/files/840-9079-_1_545x545.webp?v=1757099274" "tailwind.jpg"},
    {"id": 24, "name": "Bata Dunk High Retro", "price": 13500, "image":"https://www.bata.com.pk/cdn/shop/files/864-4952-_1_545x545.webp?v=1757099222" "dunkhigh.jpg"},
    {"id": 25, "name": "Bata Air Zoom Structure", "price": 15500, "image":"https://www.bata.com.pk/cdn/shop/files/861-3527-_1_545x545.jpg?v=1757100475" "zoomstructure.jpg"},
    {"id": 26, "name": "Bata Air Max 95", "price": 17000, "image":"https://www.bata.com.pk/cdn/shop/products/861-4531-_1_545x545.jpg?v=1755753550" "airmax95.jpg"},
    {"id": 27, "name": "Bata Phantom GX", "price": 20000, "image":"https://www.bata.com.pk/cdn/shop/files/883-4540-_1_545x545.webp?v=1759151347" "phantomgx.jpg"},
    {"id": 28, "name": "Bata Tiempo Legend 9", "price": 19000, "image":"https://www.bata.com.pk/cdn/shop/files/871-6882-1_1_545x545.webp?v=1757099165" "tiempo.jpg"},
    {"id": 29, "name": "Bata Mercurial Vapor 15", "price": 20000, "image":"https://www.bata.com.pk/cdn/shop/files/871-6072-_1_545x545.webp?v=1756980906" "mercurial.jpg"},
    {"id": 30, "name": "Bata Air Max Flyknit", "price": 18000, "image":"https://www.bata.com.pk/cdn/shop/files/877-9281-1_545x545.webp?v=1757099671" "flyknit.jpg"},
]

def home(request):
    return render(request, "hello.html", {"shoes": shoes})

# Handle shoe purchase
def buy_shoe(request, shoe_id):
    shoe = next((s for s in shoes if s["id"] == shoe_id), None)
    if shoe:
        return HttpResponse(f"You selected {shoe['name']} for PKR {shoe['price']}")
    return HttpResponse("Shoe not found")



def order_form(request):
    if request.method == "POST":
        context = {
            "order_submitted": True,
            "email": request.POST.get("email"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "address": request.POST.get("address"),
            "city": request.POST.get("city"),
            "postal_code": request.POST.get("postal_code"),
            "phone": request.POST.get("phone"),
        }
        return render(request, "order_form.html", context)
    else:
        return render(request, "order_form.html")




def submit_order(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        product_name = request.POST.get("product_name")
        product_price = request.POST.get("product_price")

        # ✅ After successful submission, show new success page
        return render(request, "order_success.html", {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "city": city,
            "postal_code": postal_code,
            "phone": phone,
            "product_name": product_name,
            "product_price": product_price,
        })

    return HttpResponse("❌ Invalid request method")
