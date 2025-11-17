# 📐 Teoría de SVD (Descomposición en Valores Singulares)

## ¿Qué es SVD?

La **Descomposición en Valores Singulares** (SVD por sus siglas en inglés: Singular Value Decomposition) es una de las factorizaciones de matrices más importantes en álgebra lineal.

Para cualquier matriz **A** de dimensiones m×n, SVD la descompone en tres matrices:

```
A = U × Σ × V^T
```

Donde:
- **U** es una matriz ortogonal m×m (vectores singulares izquierdos)
- **Σ** es una matriz diagonal m×n con valores singulares no negativos
- **V^T** es la transpuesta de una matriz ortogonal n×n (vectores singulares derechos)

## Propiedades Matemáticas

### 1. Valores Singulares
Los valores singulares σ₁, σ₂, ..., σᵣ en la diagonal de Σ están ordenados:
```
σ₁ ≥ σ₂ ≥ ... ≥ σᵣ ≥ 0
```

donde r es el rango de la matriz A.

### 2. Matrices Ortogonales
Las matrices U y V son ortogonales, lo que significa:
```
U^T × U = I
V^T × V = I
```

### 3. Relación con Autovalores
Los valores singulares de A son las raíces cuadradas de los autovalores de A^T×A (o A×A^T):
```
σᵢ = √λᵢ
```

## Aplicación en Compresión de Imágenes

### Paso 1: Representación Matricial
Una imagen digital se puede representar como una matriz:
- **Escala de grises**: Matriz m×n donde cada elemento es la intensidad del píxel
- **Color (RGB)**: Tres matrices m×n, una por cada canal de color

### Paso 2: Descomposición
Para cada canal de color:
```
Canal_Rojo = U_R × Σ_R × V_R^T
```

### Paso 3: Aproximación de Rango Bajo
En lugar de usar todos los valores singulares, usamos solo los k más grandes:

```
A_k = U[:, 1:k] × Σ[1:k, 1:k] × V^T[1:k, :]
```

### Paso 4: Reconstrucción
La imagen comprimida se obtiene recombinando los k componentes principales.

## ¿Por Qué Funciona?

### Teorema de Eckart-Young
SVD proporciona la **mejor aproximación** de rango k a una matriz en el sentido de:
- Norma de Frobenius
- Norma espectral

Esto significa que A_k minimiza el error:
```
||A - A_k|| = mínimo
```

### Interpretación Geométrica
Los valores singulares representan la "importancia" de cada componente:
- **Valores grandes**: Características principales de la imagen
- **Valores pequeños**: Detalles finos y ruido

Al mantener solo los k valores más grandes, preservamos las características más importantes.

## Análisis de Compresión

### Tamaño Original
Para una imagen m×n con c canales:
```
Tamaño_original = m × n × c
```

### Tamaño Comprimido
Con k valores singulares por canal:
```
Tamaño_comprimido = k × (m + n + 1) × c
```

Esto incluye:
- k columnas de U (m elementos cada una)
- k valores singulares
- k filas de V^T (n elementos cada una)

### Ratio de Compresión
```
Ratio = Tamaño_original / Tamaño_comprimido
      = (m × n × c) / (k × (m + n + 1) × c)
      = (m × n) / (k × (m + n + 1))
```

### Energía Retenida
El porcentaje de información preservada:
```
Energía = (Σᵢ₌₁ᵏ σᵢ²) / (Σᵢ₌₁ʳ σᵢ²) × 100%
```

## Ejemplos Numéricos

### Ejemplo 1: Matriz Simple
```python
A = [[3, 1, 1],
     [-1, 3, 1]]

U, Σ, V^T = SVD(A)

U ≈ [[-0.71, -0.71],
     [-0.71,  0.71]]

Σ ≈ [3.74, 0]
    [0,    2.83]

V^T ≈ [[-0.34, -0.91, -0.24],
       [-0.91,  0.26,  0.33]]
```

### Ejemplo 2: Compresión de Imagen 100×100

**Sin compresión (k=100):**
- Tamaño: 100 × 100 × 3 = 30,000 valores
- Energía: 100%
- Calidad: Perfecta

**Compresión alta (k=10):**
- Tamaño: 10 × (100 + 100 + 1) × 3 = 6,030 valores
- Ratio: 4.98x
- Energía: ~85%
- Calidad: Buena, detalles borrosos

**Compresión media (k=50):**
- Tamaño: 50 × (100 + 100 + 1) × 3 = 30,150 valores
- Ratio: 0.99x (no hay compresión efectiva)
- Energía: ~99%
- Calidad: Excelente

## Ventajas y Desventajas

### ✅ Ventajas
1. **Óptima**: Mejor aproximación posible para un rango dado
2. **Controlable**: Ajuste fino entre compresión y calidad
3. **Interpretable**: Los componentes tienen significado matemático
4. **Estable**: Numéricamente robusta
5. **Versátil**: Aplicable a cualquier matriz

### ❌ Desventajas
1. **Costo computacional**: O(min(m²n, mn²)) para calcular SVD completo
2. **No específica para imágenes**: Métodos como JPEG son más eficientes
3. **Pérdida de información**: Compresión con pérdida
4. **Almacenamiento de U y V**: Requiere guardar matrices adicionales

## Comparación con Otros Métodos

| Método | Ratio típico | Calidad | Velocidad | Estándar |
|--------|-------------|---------|-----------|----------|
| **SVD** | 2-10x | Buena | Media | No |
| **JPEG** | 10-100x | Variable | Rápida | Sí |
| **PNG** | 2-3x | Perfecta | Rápida | Sí |
| **WebP** | 20-30x | Buena | Rápida | Sí |

## Aplicaciones Adicionales de SVD

Además de compresión de imágenes, SVD se usa en:

1. **Sistemas de recomendación**: Netflix, Amazon
2. **Procesamiento de lenguaje natural**: LSA (Latent Semantic Analysis)
3. **Reducción de dimensionalidad**: PCA está relacionado con SVD
4. **Eliminación de ruido**: Filtrado de señales
5. **Análisis de datos**: Identificación de patrones
6. **Visión por computadora**: Reconocimiento facial
7. **Álgebra lineal numérica**: Solución de sistemas

## Implementación Eficiente

### Algoritmos Comunes
1. **SVD completo**: Método de Golub-Kahan
2. **SVD truncado**: Algoritmo de Lanczos
3. **Randomized SVD**: Para matrices grandes

### En Python
```python
import numpy as np

# SVD completo
U, s, VT = np.linalg.svd(A, full_matrices=False)

# SVD truncado (más rápido para k pequeño)
from scipy.sparse.linalg import svds
U, s, VT = svds(A, k=50)
```

## Referencias

1. Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations*. Johns Hopkins University Press.
2. Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.
3. Strang, G. (2016). *Introduction to Linear Algebra*. Wellesley-Cambridge Press.
4. Eckart, C., & Young, G. (1936). "The approximation of one matrix by another of lower rank". *Psychometrika*.

## Ejercicios Propuestos

1. **Básico**: Calcula manualmente SVD de la matriz [[1, 2], [2, 1]]
2. **Intermedio**: Implementa compresión SVD sin librerías (solo operaciones básicas)
3. **Avanzado**: Compara SVD con PCA para reducción de dimensionalidad
4. **Aplicado**: Usa SVD para eliminar ruido de una imagen

---

*Esta documentación forma parte del proyecto SVD Image Compression para el curso de Álgebra Lineal.*
