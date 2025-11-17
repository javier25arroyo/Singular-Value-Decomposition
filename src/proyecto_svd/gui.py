"""
Interfaz gráfica para la aplicación de compresión de imágenes con SVD.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

from svd_image import SVDImageProcessor


class SVDImageApp:
    """Aplicación GUI para compresión de imágenes con SVD."""
    
    def __init__(self, root):
        """
        Inicializa la aplicación.
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title("SVD Image Compression - Descomposición en Valores Singulares")
        self.root.geometry("1400x800")
        self.root.configure(bg='#f0f0f0')
        
        self.processor = None
        self.current_image = None
        self.original_photo = None
        self.compressed_photo = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz de usuario."""
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Info.TLabel', font=('Arial', 10), background='#f0f0f0')
        style.configure('Large.TButton', font=('Arial', 12))
        
        # Frame superior - Título y botones
        top_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        top_frame.pack(fill=tk.X, padx=0, pady=0)
        top_frame.pack_propagate(False)
        
        title_label = tk.Label(
            top_frame,
            text="🖼️ Compresión de Imágenes con SVD",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Frame de botones
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=15)
        
        self.load_btn = ttk.Button(
            button_frame,
            text="📁 Cargar Imagen",
            command=self.load_image,
            style='Large.TButton',
            width=20
        )
        self.load_btn.pack(side=tk.LEFT, padx=10)
        
        self.save_btn = ttk.Button(
            button_frame,
            text="💾 Guardar Imagen Comprimida",
            command=self.save_image,
            style='Large.TButton',
            width=25,
            state=tk.DISABLED
        )
        self.save_btn.pack(side=tk.LEFT, padx=10)
        
        self.info_btn = ttk.Button(
            button_frame,
            text="ℹ️ Información SVD",
            command=self.show_info,
            style='Large.TButton',
            width=20
        )
        self.info_btn.pack(side=tk.LEFT, padx=10)
        
        # Frame principal con dos columnas
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Columna izquierda - Imagen original
        left_frame = tk.LabelFrame(
            main_frame,
            text="Imagen Original",
            font=('Arial', 12, 'bold'),
            bg='white',
            padx=10,
            pady=10
        )
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        self.original_canvas = tk.Canvas(left_frame, bg='#ecf0f1', width=400, height=400)
        self.original_canvas.pack(pady=10)
        
        self.original_info_label = ttk.Label(
            left_frame,
            text="Sin imagen cargada",
            style='Info.TLabel'
        )
        self.original_info_label.pack(pady=5)
        
        # Columna derecha - Imagen comprimida
        right_frame = tk.LabelFrame(
            main_frame,
            text="Imagen Comprimida (SVD)",
            font=('Arial', 12, 'bold'),
            bg='white',
            padx=10,
            pady=10
        )
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        self.compressed_canvas = tk.Canvas(right_frame, bg='#ecf0f1', width=400, height=400)
        self.compressed_canvas.pack(pady=10)
        
        self.compressed_info_label = ttk.Label(
            right_frame,
            text="Ajuste el control deslizante",
            style='Info.TLabel'
        )
        self.compressed_info_label.pack(pady=5)
        
        # Frame de control - Slider
        control_frame = tk.LabelFrame(
            self.root,
            text="Control de Compresión",
            font=('Arial', 12, 'bold'),
            bg='white',
            padx=20,
            pady=15
        )
        control_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Slider
        slider_container = tk.Frame(control_frame, bg='white')
        slider_container.pack(fill=tk.X, pady=10)
        
        tk.Label(
            slider_container,
            text="Número de Valores Singulares (k):",
            font=('Arial', 11),
            bg='white'
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.k_var = tk.IntVar(value=50)
        self.k_slider = ttk.Scale(
            slider_container,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.k_var,
            command=self.update_compression,
            length=500
        )
        self.k_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        self.k_slider.config(state=tk.DISABLED)
        
        self.k_value_label = tk.Label(
            slider_container,
            text="50",
            font=('Arial', 11, 'bold'),
            bg='white',
            width=5
        )
        self.k_value_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Información de compresión
        self.stats_label = tk.Label(
            control_frame,
            text="",
            font=('Arial', 10),
            bg='white',
            fg='#2c3e50',
            justify=tk.LEFT
        )
        self.stats_label.pack(pady=10)
    
    def load_image(self):
        """Carga una imagen desde el sistema de archivos."""
        file_path = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[
                ("Imágenes", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        try:
            # Cargar y procesar imagen
            self.processor = SVDImageProcessor(file_path)
            self.processor.compute_svd()
            
            # Mostrar imagen original
            self.display_original_image()
            
            # Configurar slider
            max_k = self.processor.get_max_k()
            self.k_slider.config(to=max_k, state=tk.NORMAL)
            self.k_var.set(min(50, max_k))
            
            # Habilitar botón de guardar
            self.save_btn.config(state=tk.NORMAL)
            
            # Mostrar imagen comprimida inicial
            self.update_compression()
            
            messagebox.showinfo("Éxito", "Imagen cargada correctamente")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen:\n{str(e)}")
    
    def display_original_image(self):
        """Muestra la imagen original en el canvas."""
        img = self.processor.original_image
        img_resized = self.resize_image_for_canvas(img, 400, 400)
        self.original_photo = ImageTk.PhotoImage(img_resized)
        
        self.original_canvas.delete("all")
        self.original_canvas.create_image(200, 200, image=self.original_photo)
        
        # Información
        shape = self.processor.image_array.shape
        if len(shape) == 2:
            info = f"Tamaño: {shape[1]}x{shape[0]} píxeles (Escala de grises)"
        else:
            info = f"Tamaño: {shape[1]}x{shape[0]} píxeles (RGB)"
        
        self.original_info_label.config(text=info)
    
    def update_compression(self, event=None):
        """Actualiza la imagen comprimida según el valor del slider."""
        if self.processor is None:
            return
        
        k = self.k_var.get()
        self.k_value_label.config(text=str(k))
        
        try:
            # Reconstruir imagen
            reconstructed = self.processor.reconstruct_image(k)
            img = Image.fromarray(reconstructed)
            
            # Mostrar imagen comprimida
            img_resized = self.resize_image_for_canvas(img, 400, 400)
            self.compressed_photo = ImageTk.PhotoImage(img_resized)
            
            self.compressed_canvas.delete("all")
            self.compressed_canvas.create_image(200, 200, image=self.compressed_photo)
            
            # Actualizar estadísticas
            compression_ratio = self.processor.get_compression_ratio(k)
            energy_retained = self.processor.get_energy_retained(k)
            
            max_k = self.processor.get_max_k()
            percentage_k = (k / max_k) * 100
            
            stats_text = (
                f"📊 Estadísticas de Compresión:\n"
                f"   • Valores singulares usados: {k} de {max_k} ({percentage_k:.1f}%)\n"
                f"   • Ratio de compresión: {compression_ratio:.2f}x\n"
                f"   • Energía retenida: {energy_retained:.2f}%"
            )
            
            self.stats_label.config(text=stats_text)
            self.compressed_info_label.config(text=f"Comprimida con k={k}")
            
            # Guardar imagen actual para poder salvarla
            self.current_image = img
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al comprimir imagen:\n{str(e)}")
    
    def resize_image_for_canvas(self, img, max_width, max_height):
        """
        Redimensiona una imagen para que quepa en el canvas.
        
        Args:
            img: Imagen PIL
            max_width: Ancho máximo
            max_height: Alto máximo
            
        Returns:
            Imagen redimensionada
        """
        img_width, img_height = img.size
        ratio = min(max_width / img_width, max_height / img_height)
        
        if ratio < 1:
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)
            return img.resize((new_width, new_height), Image.LANCZOS)
        
        return img
    
    def save_image(self):
        """Guarda la imagen comprimida."""
        if self.current_image is None:
            messagebox.showwarning("Advertencia", "No hay imagen comprimida para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar imagen comprimida",
            defaultextension=".png",
            filetypes=[
                ("PNG", "*.png"),
                ("JPEG", "*.jpg"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.current_image.save(file_path)
                messagebox.showinfo("Éxito", f"Imagen guardada en:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la imagen:\n{str(e)}")
    
    def show_info(self):
        """Muestra información sobre SVD."""
        info_window = tk.Toplevel(self.root)
        info_window.title("Información sobre SVD")
        info_window.geometry("700x550")
        info_window.configure(bg='white')
        
        # Frame con scroll
        canvas = tk.Canvas(info_window, bg='white')
        scrollbar = ttk.Scrollbar(info_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Contenido
        title = tk.Label(
            scrollable_frame,
            text="📚 Descomposición en Valores Singulares (SVD)",
            font=('Arial', 16, 'bold'),
            bg='white',
            fg='#2c3e50'
        )
        title.pack(pady=20, padx=20)
        
        info_text = """
¿Qué es SVD?

La Descomposición en Valores Singulares (SVD) es una técnica fundamental del 
álgebra lineal que descompone una matriz A en tres matrices:

    A = U × Σ × V^T

Donde:
  • U: Matriz ortogonal (vectores singulares izquierdos)
  • Σ: Matriz diagonal con valores singulares (ordenados de mayor a menor)
  • V^T: Matriz ortogonal transpuesta (vectores singulares derechos)

Aplicación en Compresión de Imágenes:

1. Cada canal de color se trata como una matriz
2. Se calcula la SVD de cada matriz
3. Se mantienen solo los k valores singulares más grandes
4. Se reconstruye la imagen usando estos k componentes

Ventajas:
  ✓ Compresión con pérdida controlada
  ✓ Mantiene las características más importantes de la imagen
  ✓ Permite ajustar el balance entre calidad y tamaño

Interpretación de los valores:
  • k pequeño: Mayor compresión, menor calidad
  • k grande: Menor compresión, mayor calidad
  • Ratio de compresión: Cuántas veces es más pequeña la representación
  • Energía retenida: Porcentaje de información preservada

Uso de la aplicación:
  1. Carga una imagen con el botón "Cargar Imagen"
  2. Ajusta el slider para cambiar k (número de valores singulares)
  3. Observa cómo cambia la calidad y compresión
  4. Guarda la imagen comprimida si lo deseas
        """
        
        text_label = tk.Label(
            scrollable_frame,
            text=info_text,
            font=('Arial', 10),
            bg='white',
            fg='#34495e',
            justify=tk.LEFT,
            padx=30
        )
        text_label.pack(pady=10)
        
        close_btn = ttk.Button(
            scrollable_frame,
            text="Cerrar",
            command=info_window.destroy
        )
        close_btn.pack(pady=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def main():
    """Función principal para ejecutar la aplicación."""
    root = tk.Tk()
    app = SVDImageApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
