from setuptools import setup, find_packages

setup(
    name="mi_paquete",
    version="0.1",
    packages=find_packages(),
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Descripción breve de tu paquete",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/mi-paquete",
    install_requires=[
        # Lista de dependencias, ej:
        # "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)