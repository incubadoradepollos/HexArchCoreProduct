class ProductCreateException(Exception):
    def __init__(self, error_code, message="Error en la aplicación"):
        self.error_code = error_code
        super().__init__(f"[Error {error_code}] {message}")
