# MODELOS DE PRODUCTO
from pydantic import BaseModel
from typing import List, Optional

"""CORE PRODUCT MODEL
"""
class CoreProduct(BaseModel):
    
    id: Optional[int] = None
    """ID unico del producto
    """
    name: Optional[str] = None
    """Nombre del producto en su idioma original.
    """
    images_base64 : Optional[list[str]] = []                
    """IMAGENES EN BASE 68
    """
    # PRECIOS Y COSTOS
    price: Optional[float] = None                           
    """precio de venta
    """
    price_cost : Optional[float] = None
    """costo del producto    
    """
    tax_id: Optional[float] = None
    """id de taxa
    """
    
    """CODIGOS
    """    

    default_code : Optional[str] = None
    """codigo interno
    """
    barcode: Optional[str] = None
    """codigo de barras
    """

    """DESCRIPCIONES
    """    
    
    ecommerce_description : Optional[str] = None
    """descripcion para el ecomerce
    """
    store_description  : Optional[str] = None
    """descripcion del almacen
    """
    ia_descripcion : Optional[str] = None
    """tanscripciones de la ia
    """

    """CLASIFICACION
    """
    categories : Optional[list[str]] = []
    """CATEGORIAS
    """
    tags : Optional[list[str]] = []
    """TAGS DEL PRODUCTOS
    """
