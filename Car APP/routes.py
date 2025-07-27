routes.py
@main.route('/')
def index():
    cars= [
        {"make:"Wolkswagen", "model":"Gol", "year":2020, "price":20000},
        {"make":"Chevrolet", "model":"Onix", "year":2019, "price":18000},
        {"make":"Fiat", "model":"Argo", "year":2018, "price":15000},
        {"make":"Ford", "model":"KA", "year":2021, "price":22000},
    ]
    return render_template("car_sales.html", cars=cars)