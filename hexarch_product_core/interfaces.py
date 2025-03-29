from abc import ABC, abstractmethod
from hexarch_product_core.models import CoreProduct


class IProductAdapter(ABC):
    @abstractmethod
    def get_product(self, id_product:int)-> CoreProduct:
        pass

    @abstractmethod
    def create_product(self, product: CoreProduct) -> CoreProduct:
        pass

    @abstractmethod
    def send_product(self, product: CoreProduct) -> CoreProduct:
        pass

    @abstractmethod
    def get_or_create_tag_id(self, tag_name) -> int:
        pass