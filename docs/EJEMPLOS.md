# 💡 Ejemplos de Uso

Esta guía proporciona ejemplos prácticos de cómo usar el proyecto SVD Image Compression.

## Tabla de Contenidos
1. [Ejemplo Básico con GUI](#ejemplo-1-uso-básico-con-gui)
2. [Uso Programático](#ejemplo-2-uso-programático)
3. [Análisis de Compresión](#ejemplo-3-análisis-de-compresión)
4. [Comparación de Imágenes](#ejemplo-4-comparación-de-imágenes)
5. [Exportación de Datos](#ejemplo-5-exportación-de-datos)

---

## Ejemplo 1: Uso Básico con GUI

### Inicio Rápido
```bash
# Ejecutar la aplicación
python run.py
```

### Flujo de Trabajo
1. **Cargar una imagen**
   - Clic en "📁 Cargar Imagen"
   - Selecciona una foto (ej: foto.jpg)
   
2. **Ajustar compresión**
   - Mueve el slider a k=50
   - Observa el cambio en tiempo real
   
3. **Analizar resultados**
   - Ratio de compresión: 4.5x
   - Energía retenida: 95.3%
   
4. **Guardar resultado**
   - Clic en "💾 Guardar Imagen Comprimida"
   - Guarda como "foto_comprimida.png"

---

## Ejemplo 2: Uso Programático

### Script Python Básico

```python
import sys
sys.path.insert(0, 'src')

from proyecto_svd.svd_image import SVDImageProcessor
from PIL import Image

# Cargar imagen
processor = SVDImageProcessor('mi_imagen.jpg')

# Calcular SVD
processor.compute_svd()

# Comprimir con k=30
imagen_comprimida = processor.reconstruct_image(k=30)

# Guardar
Image.fromarray(imagen_comprimida).save('resultado.png')

# Obtener estadísticas
ratio = processor.get_compression_ratio(30)
energia = processor.get_energy_retained(30)

print(f"Ratio de compresión: {ratio:.2f}x")
print(f"Energía retenida: {energia:.1f}%")
```

### Procesar Múltiples Imágenes

```python
import os
from proyecto_svd.svd_image import SVDImageProcessor
from PIL import Image

# Directorio con imágenes
input_dir = 'data/imagenes'
output_dir = 'data/comprimidas'
os.makedirs(output_dir, exist_ok=True)

# Nivel de compresión
k = 50

# Procesar todas las imágenes
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f'compressed_{filename}')
        
        print(f"Procesando {filename}...")
        
        processor = SVDImageProcessor(input_path)
        compressed = processor.reconstruct_image(k)
        Image.fromarray(compressed).save(output_path)
        
        print(f"  Ratio: {processor.get_compression_ratio(k):.2f}x")
        print(f"  Energía: {processor.get_energy_retained(k):.1f}%")
```

---

## Ejemplo 3: Análisis de Compresión

### Encontrar el k Óptimo

```python
from proyecto_svd.svd_image import SVDImageProcessor
import matplotlib.pyplot as plt

# Cargar imagen
processor = SVDImageProcessor('foto.jpg')
max_k = processor.get_max_k()

# Probar diferentes valores de k
k_values = range(1, min(max_k, 200), 5)
energias = []
ratios = []

for k in k_values:
    energias.append(processor.get_energy_retained(k))
    ratios.append(processor.get_compression_ratio(k))

# Graficar
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(k_values, energias, 'b-', linewidth=2)
ax1.axhline(y=90, color='r', linestyle='--', label='90% energía')
ax1.set_xlabel('k (valores singulares)')
ax1.set_ylabel('Energía Retenida (%)')
ax1.set_title('Calidad vs k')
ax1.legend()
ax1.grid(True)

ax2.plot(energias, ratios, 'g-', linewidth=2)
ax2.set_xlabel('Energía Retenida (%)')
ax2.set_ylabel('Ratio de Compresión')
ax2.set_title('Trade-off: Calidad vs Compresión')
ax2.grid(True)

plt.tight_layout()
plt.savefig('analisis_compresion.png')
plt.show()

# Encontrar k para 90% de energía
for k, e in zip(k_values, energias):
    if e >= 90:
        print(f"Para 90% energía: k = {k}")
        print(f"Ratio de compresión: {processor.get_compression_ratio(k):.2f}x")
        break
```

---

## Ejemplo 4: Comparación de Imágenes

### Comparar Original vs Comprimidas

```python
from proyecto_svd.svd_image import SVDImageProcessor
import matplotlib.pyplot as plt

processor = SVDImageProcessor('imagen.jpg')

# Diferentes niveles de k
k_levels = [10, 25, 50, 100]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

# Original
axes[0].imshow(processor.image_array)
axes[0].set_title('Original')
axes[0].axis('off')

# Comprimidas
for i, k in enumerate(k_levels, 1):
    compressed = processor.reconstruct_image(k)
    ratio = processor.get_compression_ratio(k)
    energy = processor.get_energy_retained(k)
    
    axes[i].imshow(compressed)
    axes[i].set_title(f'k={k}\n{ratio:.1f}x | {energy:.1f}%')
    axes[i].axis('off')

# Ocultar el último subplot si no se usa
if len(k_levels) < 5:
    axes[5].axis('off')

plt.suptitle('Comparación de Compresión SVD', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('comparacion.png', dpi=150)
plt.show()
```

---

## Ejemplo 5: Exportación de Datos

### Guardar Estadísticas en CSV

```python
import csv
from proyecto_svd.svd_image import SVDImageProcessor

processor = SVDImageProcessor('imagen.jpg')
max_k = processor.get_max_k()

# Generar datos
with open('estadisticas_svd.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['k', 'Ratio_Compresion', 'Energia_Retenida', 'Porcentaje_k'])
    
    for k in range(1, min(max_k, 201), 5):
        ratio = processor.get_compression_ratio(k)
        energia = processor.get_energy_retained(k)
        porcentaje_k = (k / max_k) * 100
        
        writer.writerow([k, f"{ratio:.3f}", f"{energia:.2f}", f"{porcentaje_k:.1f}"])

print("✓ Estadísticas guardadas en estadisticas_svd.csv")
```

### Visualizar Valores Singulares

```python
from proyecto_svd.svd_image import SVDImageProcessor
import matplotlib.pyplot as plt
import numpy as np

processor = SVDImageProcessor('imagen.jpg')
singular_values = processor.get_singular_values()

# Graficar valores singulares por canal
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Valores singulares de cada canal
colors = ['red', 'green', 'blue']
channels = ['Rojo', 'Verde', 'Azul']

for i, (color, channel) in enumerate(zip(colors, channels)):
    ax = axes[i // 2, i % 2]
    ax.plot(singular_values[i], color=color, linewidth=2)
    ax.set_title(f'Canal {channel}')
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor Singular')
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')

# Comparación de todos los canales
ax = axes[1, 1]
for i, (color, channel) in enumerate(zip(colors, channels)):
    ax.plot(singular_values[i], color=color, linewidth=2, label=channel, alpha=0.7)
ax.set_title('Comparación de Canales')
ax.set_xlabel('Índice')
ax.set_ylabel('Valor Singular (log)')
ax.set_yscale('log')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('valores_singulares.png', dpi=150)
plt.show()
```

---

## Ejemplo 6: Procesamiento por Lotes

### Automatizar Compresión

```python
import os
import json
from proyecto_svd.svd_image import SVDImageProcessor
from PIL import Image
from datetime import datetime

def procesar_lote(input_dir, output_dir, k_value=50):
    """
    Procesa todas las imágenes de un directorio.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    resultados = {
        'fecha': datetime.now().isoformat(),
        'k': k_value,
        'imagenes': []
    }
    
    archivos = [f for f in os.listdir(input_dir) 
                if f.endswith(('.jpg', '.png', '.jpeg', '.bmp'))]
    
    print(f"Procesando {len(archivos)} imágenes con k={k_value}...")
    
    for i, filename in enumerate(archivos, 1):
        print(f"[{i}/{len(archivos)}] {filename}...", end=' ')
        
        try:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f'svd_{filename}')
            
            processor = SVDImageProcessor(input_path)
            compressed = processor.reconstruct_image(k_value)
            Image.fromarray(compressed).save(output_path)
            
            resultado = {
                'nombre': filename,
                'dimensiones': processor.image_array.shape[:2],
                'ratio': processor.get_compression_ratio(k_value),
                'energia': processor.get_energy_retained(k_value),
                'max_k': processor.get_max_k()
            }
            
            resultados['imagenes'].append(resultado)
            print(f"✓ ({resultado['ratio']:.2f}x, {resultado['energia']:.1f}%)")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
    
    # Guardar resultados
    with open(os.path.join(output_dir, 'resultados.json'), 'w') as f:
        json.dump(resultados, f, indent=2)
    
    print(f"\n✓ Procesamiento completado. Resultados en {output_dir}/resultados.json")
    return resultados

# Usar
resultados = procesar_lote('data/originales', 'data/comprimidas', k_value=50)
```

---

## Ejemplo 7: Jupyter Notebook

### Análisis Interactivo

```python
# En Jupyter Notebook
import sys
sys.path.insert(0, '../src')

from proyecto_svd.svd_image import SVDImageProcessor
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
from IPython.display import display

processor = SVDImageProcessor('imagen.jpg')

@interact(k=IntSlider(min=1, max=processor.get_max_k(), step=5, value=50))
def mostrar_compresion(k):
    """Widget interactivo para ajustar k."""
    compressed = processor.reconstruct_image(k)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.imshow(processor.image_array)
    ax1.set_title('Original')
    ax1.axis('off')
    
    ax2.imshow(compressed)
    ratio = processor.get_compression_ratio(k)
    energia = processor.get_energy_retained(k)
    ax2.set_title(f'Comprimida (k={k})\n{ratio:.2f}x | {energia:.1f}%')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()
```

---

## Casos de Uso Recomendados

### 1. Fotografías de Paisajes
- **k recomendado**: 80-120
- **Esperado**: Buen balance entre calidad y compresión
- **Ratio típico**: 3-5x

### 2. Logos y Gráficos Simples
- **k recomendado**: 10-30
- **Esperado**: Alta compresión, calidad aceptable
- **Ratio típico**: 8-15x

### 3. Retratos
- **k recomendado**: 100-150
- **Esperado**: Mantiene detalles faciales
- **Ratio típico**: 2-4x

### 4. Imágenes Médicas
- **k recomendado**: 150-200
- **Esperado**: Máxima preservación de detalles
- **Ratio típico**: 1.5-3x

---

## Consejos de Optimización

### Para Mejor Rendimiento
```python
# Usar imágenes más pequeñas
from PIL import Image
img = Image.open('grande.jpg')
img_pequeña = img.resize((800, 600))
img_pequeña.save('pequeña.jpg')

# Procesar
processor = SVDImageProcessor('pequeña.jpg')
```

### Para Mejor Calidad
```python
# Usar k adaptativo basado en energía objetivo
def encontrar_k_optimo(processor, energia_objetivo=95):
    """Encuentra k para alcanzar energía objetivo."""
    max_k = processor.get_max_k()
    
    for k in range(1, max_k + 1):
        if processor.get_energy_retained(k) >= energia_objetivo:
            return k
    
    return max_k

k_optimo = encontrar_k_optimo(processor, 95)
print(f"k óptimo para 95% energía: {k_optimo}")
```

---

¿Tienes más preguntas? Consulta el [README.md](../README.md) o la [teoría de SVD](TEORIA_SVD.md).
