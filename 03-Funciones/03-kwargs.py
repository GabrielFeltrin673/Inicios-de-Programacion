def get_product(**datos):
    print(datos["name"], datos["price"])

get_product(id="id", name="Producto 1", price=100, stock=1)