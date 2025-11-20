# Crear clase Producto con los mismos atributos de la tabla producto, código(solo get), todos los demás atributos con get y set.

class Producto:
    def __init__(self, codigo:int, descripcion:str, stock:int, ubicacion:str):
        self._codigo = codigo # solo get
        self._descripcion = descripcion # get y set 
        self._stock = stock # get y set
        self._ubicacion = ubicacion # get y set

# ------ getters -------
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def stock(self):
        return self._stock
    
    @property
    def ubicacion(self):
        return self._ubicacion


# ------ setters -------
    @descripcion.setter
    def descripcion(self): # incompleto
        pass

    @stock.setter
    def stock(self):
        pass

    @ubicacion.setter
    def ubicacion(self):
        pass


