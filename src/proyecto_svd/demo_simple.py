"""
Demo simple de SVD sin GUI - para verificar que todo funciona.
"""

import numpy as np
from PIL import Image
import os


def demo_svd_basico():
    """Demostración básica de SVD con una matriz pequeña."""
    print("=" * 60)
    print("DEMO 1: SVD con una Matriz Simple")
    print("=" * 60)
    
    # Crear una matriz de ejemplo
    A = np.array([[3, 1, 1],
                  [-1, 3, 1]], dtype=float)
    
    print("\nMatriz original A:")
    print(A)
    print(f"Dimensiones: {A.shape}")
    
    # Calcular SVD
    U, s, VT = np.linalg.svd(A, full_matrices=False)
    
    print("\n--- Descomposición SVD: A = U × Σ × V^T ---")
    
    print("\nMatriz U (vectores singulares izquierdos):")
    print(U)
    print(f"Dimensiones: {U.shape}")
    
    print("\nValores singulares (Σ):")
    print(s)
    print(f"Dimensiones: {s.shape}")
    
    print("\nMatriz V^T (vectores singulares derechos transpuestos):")
    print(VT)
    print(f"Dimensiones: {VT.shape}")
    
    # Reconstruir la matriz
    Sigma = np.diag(s)
    A_reconstructed = U @ Sigma @ VT
    
    print("\nMatriz reconstruida (U × Σ × V^T):")
    print(A_reconstructed)
    
    print("\nError de reconstrucción (debe ser casi cero):")
    error = np.max(np.abs(A - A_reconstructed))
    print(f"{error:.10f}")
    
    print("\n✓ Demo 1 completado exitosamente!\n")


def demo_imagen_sintetica():
    """Demostración con una imagen sintética."""
    print("=" * 60)
    print("DEMO 2: SVD con Imagen Sintética")
    print("=" * 60)
    
    # Crear una imagen de gradiente simple
    print("\nCreando imagen de prueba (gradiente)...")
    width, height = 100, 100
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            image_array[i, j] = [i * 255 // height, j * 255 // width, 128]
    
    print(f"Imagen creada: {width}x{height} píxeles, 3 canales (RGB)")
    print(f"Tamaño del array: {image_array.shape}")
    
    # Aplicar SVD a cada canal
    print("\nAplicando SVD a cada canal de color...")
    
    for channel_idx, channel_name in enumerate(['Rojo', 'Verde', 'Azul']):
        channel_data = image_array[:, :, channel_idx]
        U, s, VT = np.linalg.svd(channel_data, full_matrices=False)
        
        print(f"\nCanal {channel_name}:")
        print(f"  - Valores singulares: {len(s)}")
        print(f"  - Top 5 valores: {s[:5]}")
        print(f"  - Suma de valores: {np.sum(s):.2f}")
    
    # Comprimir con diferentes valores de k
    print("\n" + "-" * 60)
    print("Probando compresión con diferentes valores de k:")
    print("-" * 60)
    
    k_values = [5, 10, 25, 50]
    
    for k in k_values:
        # Calcular energía retenida
        total_energy = 0
        retained_energy = 0
        
        for channel_idx in range(3):
            channel_data = image_array[:, :, channel_idx]
            U, s, VT = np.linalg.svd(channel_data, full_matrices=False)
            
            total_energy += np.sum(s ** 2)
            retained_energy += np.sum(s[:k] ** 2)
        
        energy_percent = (retained_energy / total_energy) * 100
        
        # Calcular ratio de compresión
        original_size = height * width * 3
        compressed_size = 3 * k * (height + width + 1)
        compression_ratio = original_size / compressed_size
        
        print(f"\nk = {k:3d}:")
        print(f"  - Energía retenida: {energy_percent:6.2f}%")
        print(f"  - Ratio compresión: {compression_ratio:6.2f}x")
        print(f"  - Tamaño reducido: {(1 - 1/compression_ratio) * 100:5.1f}%")
    
    print("\n✓ Demo 2 completado exitosamente!\n")


def demo_guardado_imagen():
    """Demo de guardado de imagen procesada."""
    print("=" * 60)
    print("DEMO 3: Crear y Guardar Imagen de Ejemplo")
    print("=" * 60)
    
    # Crear directorio data si no existe
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Crear una imagen de ejemplo más interesante
    print("\nCreando imagen de ejemplo con patrón de círculos...")
    width, height = 200, 200
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    center_x, center_y = width // 2, height // 2
    
    for i in range(height):
        for j in range(width):
            dist = np.sqrt((i - center_y)**2 + (j - center_x)**2)
            
            # Patrón de círculos concéntricos
            value = int(128 + 127 * np.sin(dist / 10))
            image_array[i, j] = [value, 255 - value, 128]
    
    # Guardar imagen
    img = Image.fromarray(image_array)
    output_path = os.path.join(data_dir, 'ejemplo_demo.png')
    img.save(output_path)
    
    print(f"✓ Imagen guardada en: {output_path}")
    print(f"  Dimensiones: {width}x{height} píxeles")
    print(f"  Formato: PNG")
    
    print("\n✓ Demo 3 completado exitosamente!")
    print("\nPuedes usar esta imagen para probar la aplicación GUI.\n")


def main():
    """Ejecuta todos los demos."""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "  DEMOS DE SVD - Descomposición en Valores Singulares  ".center(58) + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    print("\n")
    
    try:
        # Demo 1: SVD básico
        demo_svd_basico()
        
        input("Presiona ENTER para continuar con el Demo 2...")
        print("\n")
        
        # Demo 2: SVD con imagen
        demo_imagen_sintetica()
        
        input("Presiona ENTER para continuar con el Demo 3...")
        print("\n")
        
        # Demo 3: Guardar imagen
        demo_guardado_imagen()
        
        print("\n" + "=" * 60)
        print("¡TODOS LOS DEMOS COMPLETADOS EXITOSAMENTE!")
        print("=" * 60)
        print("\nAhora puedes ejecutar la aplicación GUI con:")
        print("  python run.py")
        print("\nO desde el directorio src/proyecto_svd:")
        print("  python gui.py")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nVerifica que todas las dependencias estén instaladas:")
        print("  pip install -r requirements.txt")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
