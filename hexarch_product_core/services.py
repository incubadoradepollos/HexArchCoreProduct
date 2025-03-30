# SERVICES
from hexarch_product_core.interfaces import IProductAdapter
from hexarch_product_core.models import CoreProduct
from hexarch_core.adapters.openia import OpenIAAdapter


class ProductsService():

    def __init__(self, product_adapter : IProductAdapter, open_ia_adapter: OpenIAAdapter ):
        self.product_adapter = product_adapter    
        self.open_ia_adapter = open_ia_adapter    

    def save_product(self, product: CoreProduct) -> CoreProduct:
        if product.id:
            return self.product_adapter.send_product(product)
        else :
            return self.product_adapter.create_product(product)
        

    def get_product(self, id_product:int)-> CoreProduct:
        return self.product_adapter.get_product(id_product)
        
    def get_product_from_image_ia(self, image_base_64, prompt_identify, prompt_clasify):
        
        response_ia = self.open_ia_adapter.get_image_chat("gpt-4o",
                                                    image_base64=image_base_64,
                                                    prompt=prompt_identify)
        
        clasify = f"""Identifica el producto con la descripcion que te paso dame un json con los campos Nombre, Año en formato string, Formato, Descripcion de 255 caracteres en formato colocial, Precio en decimal y sin simbolo de moneda si no sabemos precio son 5 y tags que se describen a continuacion: 
                    {prompt_clasify}"""
        print(response_ia)
        response_json = self.open_ia_adapter.get_text_chat_context_json("gpt-3.5-turbo",clasify, response_ia)
        print(response_json)
        
        product = CoreProduct(    
            name=response_json["Nombre"],
            images_base64=[image_base_64],
            price=response_json["Precio"],
            price_cost=0.5,
            tax_id=0,
            default_code="PYCP"  , 
            barcode="00000000000000",
            ecommerce_description=response_json["Descripcion"],
            store_description="DESCRIPCION DEL ALMACENA",
            ia_descripcion="DESCRIPCION DE LA IA",
            categories=["3","1"],
            # tags=response_json["tags"]
            ) 
                
        return product
        pass