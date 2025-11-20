class Producto:
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - ${self.precio} - Stock: {self.stock}"
