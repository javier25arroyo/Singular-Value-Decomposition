"""
Paquete proyecto_svd para compresión de imágenes usando SVD.
"""

from .svd_image import SVDImageProcessor
from .gui import SVDImageApp, main

__all__ = ["SVDImageProcessor", "SVDImageApp", "main"]
