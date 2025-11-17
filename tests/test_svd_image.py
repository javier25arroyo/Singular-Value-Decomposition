"""
Tests para el módulo svd_image.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import numpy as np
from PIL import Image
import tempfile
import pytest
from proyecto_svd.svd_image import SVDImageProcessor


def create_test_image(width=100, height=100, channels=3):
    """Crea una imagen de prueba."""
    if channels == 3:
        img_array = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
    else:
        img_array = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    return Image.fromarray(img_array)


def test_load_rgb_image():
    """Test cargar imagen RGB."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(50, 50, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        
        assert processor.image_array is not None
        assert processor.image_array.shape == (50, 50, 3)
        assert processor.original_image is not None
        
        os.unlink(f.name)


def test_load_grayscale_image():
    """Test cargar imagen en escala de grises."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(50, 50, 1)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        
        assert processor.image_array is not None
        assert len(processor.image_array.shape) in [2, 3]  # Puede ser 2D o 3D con 1 canal
        
        os.unlink(f.name)


def test_compute_svd():
    """Test cálculo de SVD."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(50, 50, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        U_channels, s_channels, VT_channels = processor.compute_svd()
        
        # Verificar que se calculó SVD para cada canal
        assert len(U_channels) == 3
        assert len(s_channels) == 3
        assert len(VT_channels) == 3
        
        # Verificar dimensiones
        for i in range(3):
            assert U_channels[i].shape[0] == 50
            assert VT_channels[i].shape[1] == 50
            assert len(s_channels[i]) == min(50, 50)
        
        os.unlink(f.name)


def test_reconstruct_image():
    """Test reconstrucción de imagen."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(50, 50, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        original = processor.image_array.copy()
        
        # Reconstruir con todos los valores singulares
        max_k = processor.get_max_k()
        reconstructed = processor.reconstruct_image(max_k)
        
        # La reconstrucción completa debe ser casi igual a la original
        assert reconstructed.shape == original.shape
        assert np.allclose(reconstructed, original, atol=1)
        
        os.unlink(f.name)


def test_compression_ratio():
    """Test cálculo de ratio de compresión."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(100, 100, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        
        # Con k pequeño, ratio debe ser alto
        ratio_small = processor.get_compression_ratio(10)
        # Con k grande, ratio debe ser bajo
        ratio_large = processor.get_compression_ratio(50)
        
        assert ratio_small > ratio_large
        assert ratio_small > 1
        
        os.unlink(f.name)


def test_energy_retained():
    """Test cálculo de energía retenida."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(50, 50, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        
        # Con k=1, energía debe ser baja
        energy_low = processor.get_energy_retained(1)
        # Con k=max, energía debe ser 100%
        max_k = processor.get_max_k()
        energy_max = processor.get_energy_retained(max_k)
        
        assert 0 <= energy_low <= 100
        assert 95 <= energy_max <= 100  # Casi 100% con todos los valores
        assert energy_low < energy_max
        
        os.unlink(f.name)


def test_get_max_k():
    """Test obtener número máximo de valores singulares."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(80, 60, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        max_k = processor.get_max_k()
        
        # max_k debe ser el mínimo entre ancho y alto
        assert max_k == min(80, 60)
        
        os.unlink(f.name)


def test_reconstruction_with_small_k():
    """Test reconstrucción con k pequeño."""
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img = create_test_image(50, 50, 3)
        img.save(f.name)
        
        processor = SVDImageProcessor(f.name)
        
        # Reconstruir con k=5
        reconstructed = processor.reconstruct_image(5)
        
        assert reconstructed.shape == processor.image_array.shape
        assert reconstructed.dtype == np.uint8
        assert np.all(reconstructed >= 0) and np.all(reconstructed <= 255)
        
        os.unlink(f.name)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
