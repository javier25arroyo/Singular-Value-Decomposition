"""
Módulo para aplicar SVD (Singular Value Decomposition) a imágenes.
Permite comprimir imágenes manteniendo solo los valores singulares más importantes.
"""

import numpy as np
from PIL import Image
from typing import Tuple, List


class SVDImageProcessor:
    """Clase para procesar imágenes con SVD."""
    
    def __init__(self, image_path: str = None):
        """
        Inicializa el procesador de imágenes.
        
        Args:
            image_path: Ruta de la imagen a procesar
        """
        self.image_path = image_path
        self.original_image = None
        self.image_array = None
        self.svd_components = None
        
        if image_path:
            self.load_image(image_path)
    
    def load_image(self, image_path: str) -> None:
        """
        Carga una imagen desde un archivo.
        
        Args:
            image_path: Ruta de la imagen
        """
        self.image_path = image_path
        self.original_image = Image.open(image_path)
        self.image_array = np.array(self.original_image)
    
    def compute_svd(self) -> Tuple[List, List, List]:
        """
        Calcula la descomposición SVD para cada canal de color.
        
        Returns:
            Tupla con listas de U, S, VT para cada canal
        """
        if self.image_array is None:
            raise ValueError("No hay imagen cargada. Use load_image() primero.")
        
        # Si la imagen es en escala de grises
        if len(self.image_array.shape) == 2:
            U, s, VT = np.linalg.svd(self.image_array, full_matrices=False)
            self.svd_components = ([U], [s], [VT])
        else:
            # Imagen RGB
            U_channels = []
            s_channels = []
            VT_channels = []
            
            for i in range(self.image_array.shape[2]):
                U, s, VT = np.linalg.svd(self.image_array[:, :, i], full_matrices=False)
                U_channels.append(U)
                s_channels.append(s)
                VT_channels.append(VT)
            
            self.svd_components = (U_channels, s_channels, VT_channels)
        
        return self.svd_components
    
    def reconstruct_image(self, k: int) -> np.ndarray:
        """
        Reconstruye la imagen usando solo los primeros k valores singulares.
        
        Args:
            k: Número de valores singulares a usar
            
        Returns:
            Array NumPy con la imagen reconstruida
        """
        if self.svd_components is None:
            self.compute_svd()
        
        U_channels, s_channels, VT_channels = self.svd_components
        
        if len(U_channels) == 1:
            # Imagen en escala de grises
            U, s, VT = U_channels[0], s_channels[0], VT_channels[0]
            k = min(k, len(s))
            reconstructed = U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]
            reconstructed = np.clip(reconstructed, 0, 255).astype(np.uint8)
        else:
            # Imagen RGB
            reconstructed = np.zeros_like(self.image_array)
            for i in range(len(U_channels)):
                U, s, VT = U_channels[i], s_channels[i], VT_channels[i]
                k_channel = min(k, len(s))
                channel_reconstructed = U[:, :k_channel] @ np.diag(s[:k_channel]) @ VT[:k_channel, :]
                reconstructed[:, :, i] = np.clip(channel_reconstructed, 0, 255)
            
            reconstructed = reconstructed.astype(np.uint8)
        
        return reconstructed
    
    def get_compression_ratio(self, k: int) -> float:
        """
        Calcula el ratio de compresión.
        
        Args:
            k: Número de valores singulares usados
            
        Returns:
            Ratio de compresión (original/comprimido)
        """
        if self.image_array is None:
            return 0.0
        
        if len(self.image_array.shape) == 2:
            m, n = self.image_array.shape
            original_size = m * n
            compressed_size = k * (m + n + 1)
            channels = 1
        else:
            m, n, channels = self.image_array.shape
            original_size = m * n * channels
            compressed_size = channels * k * (m + n + 1)
        
        return original_size / compressed_size
    
    def get_energy_retained(self, k: int) -> float:
        """
        Calcula el porcentaje de energía retenida con k valores singulares.
        
        Args:
            k: Número de valores singulares usados
            
        Returns:
            Porcentaje de energía retenida (0-100)
        """
        if self.svd_components is None:
            self.compute_svd()
        
        _, s_channels, _ = self.svd_components
        
        total_energy = 0
        retained_energy = 0
        
        for s in s_channels:
            k_actual = min(k, len(s))
            total_energy += np.sum(s ** 2)
            retained_energy += np.sum(s[:k_actual] ** 2)
        
        return (retained_energy / total_energy) * 100 if total_energy > 0 else 0
    
    def get_singular_values(self) -> List[np.ndarray]:
        """
        Obtiene los valores singulares de cada canal.
        
        Returns:
            Lista de arrays con valores singulares
        """
        if self.svd_components is None:
            self.compute_svd()
        
        return self.svd_components[1]
    
    def get_max_k(self) -> int:
        """
        Obtiene el número máximo de valores singulares.
        
        Returns:
            Número máximo de componentes
        """
        if self.svd_components is None:
            self.compute_svd()
        
        _, s_channels, _ = self.svd_components
        return min(len(s) for s in s_channels)
