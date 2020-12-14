from pydantic import BaseModel

class registro(BaseModel):
    id_r: int
    valor: int 
    tipo_registro: str
    clase_registro: str
    fecha: str
    nota: str

registros = {
    1: registro(id_r=1, valor=50000, tipo_registro="Gasto", clase_registro="Comida", fecha="22-11-2020", nota="Comida restaurante"),
    2: registro(id_r=2, valor=90000, tipo_registro="Gasto", clase_registro="Entretenimiento", fecha="23-11-2020", nota="Salida a la playa")    
}

def consultar_registro():
    lista_registros= []

    for e in registros:
        lista_registros.append(registros[e])
    return lista_registros

def crear_registro(registro: registro ):
    if registro.id_r in registros:
        return False
    else:
        registros[registro.id_r] = registro
        return True