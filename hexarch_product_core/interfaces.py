from abc import ABC, abstractmethod
from hexarch_product_core.models import CoreProduct

"""INTERFACES DE PRODUCTOS A IMPLEMENTAR POR LOS ADAPTADORES ESPECIFICOS
"""

class IProductAdapter(ABC):
    """Interface de producto abstracto    
    """
    @abstractmethod
    def get_product(self, id_product:int)-> CoreProduct:
        """busca Retorna un objeto producto con el id proporcionado

        Args:
            id_product (int):

        Returns:
            CoreProduct: 
        """
        pass

    @abstractmethod
    def create_product(self, product: CoreProduct) -> CoreProduct:
        """Crea un nuevo producto

        Args:
            product (CoreProduct): 

        Returns:
            CoreProduct: Producto creado con el id informado
        """
        pass

    @abstractmethod
    def send_product(self, product: CoreProduct) -> CoreProduct:
        """Envia una actualizacion de un producto con id

        Args:
            product (CoreProduct): 

        Returns:
            CoreProduct: 
        """
        pass

    @abstractmethod
    def get_or_create_tag_id(self, tag_name) -> int:
        """Envia si la encuentra o crea una tag con el nombre indicado

        Args:
            tag_name (_type_): _description_

        Returns:
            int: _description_
        """
        pass