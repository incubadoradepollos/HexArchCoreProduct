from setuptools import setup, find_packages

setup(
    name="hexarch_product_core",
    version="0.1.1",
    packages=find_packages(),
    author="Jose Manuel Herrera",
    author_email="incubadoradepollos@gmail.com",
    description="Productos abstractos para utilizar con adaptadores de ecommerce",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/mi-paquete",
    install_requires=[
        "hexarch_core @ git+https://github.com/incubadoradepollos/HexArchCore.git"
        # Lista de dependencias, ej:
        # "requests>=2.25.1",
    ],
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.4",
)