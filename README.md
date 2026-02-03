# Menú de Restaurante - Aplicación Kivy

Una aplicación interactiva de menú de restaurante desarrollada con Python y Kivy que permite visualizar categorías de productos, sus precios y navegar de forma intuitiva entre las diferentes secciones.

---

## ¿Qué hace esta aplicación?

Esta aplicación muestra el menú de un restaurante de forma digital e interactiva. Permite:

- **Ver el nombre del restaurante** en una pantalla de bienvenida  
- **Explorar categorías** de productos (Comidas, Bebidas, Postres, etc.)  
- **Consultar productos** con sus nombres y precios  
- **Navegar fácilmente** entre pantallas con botones intuitivos  
- **Interfaz responsive** que se adapta a diferentes tamaños de pantalla  

### Características principales:

- **3 pantallas navegables:**
  1. Pantalla de inicio con bienvenida
  2. Pantalla de categorías
  3. Pantalla de productos por categoría

- **Datos configurables:** El menú se carga desde un archivo JSON, fácil de modificar sin tocar el código

- **Interfaz moderna:** Diseño limpio y profesional con colores atractivos

- **Sin funciones de compra:** Esta app solo muestra información (no incluye carrito, pagos, ni sistema de pedidos)

---

## ¿Cómo ejecutar la aplicación?

### Opción 1: Ejecutar como Script Python 

#### Requisitos previos:
- Python 3.7 o superior instalado
- Kivy instalado

#### Paso 1: Instalar Python

**Windows:**
1. Descarga Python desde: https://www.python.org/downloads/
2. Durante la instalación, marca "Add Python to PATH"
3. Completa la instalación

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

#### Paso 2: Instalar Kivy

**Windows/macOS/Linux:**
```bash
pip install kivy
```

O si usas Python 3:
```bash
pip3 install kivy
```

#### Paso 3: Ejecutar la aplicación

1. Descarga todos los archivos del proyecto
2. Asegúrate de tener estos archivos en la misma carpeta:
   - `main.py`
   - `menu_data.json`

3. Abre una terminal/CMD en la carpeta del proyecto

4. Ejecuta:
```bash
python main.py
```

O en sistemas con Python 3:
```bash
python3 main.py
```

¡La aplicación debería iniciarse automáticamente! 

---

### Opción 2: Ejecutar como Ejecutable 

Si tienes el archivo ejecutable generado:

**Windows:**
1. Doble clic en `MenuRestaurante.exe`
2. ¡Listo!

**Linux/macOS:**
1. Abre terminal en la carpeta del ejecutable
2. Ejecuta:
```bash
./MenuRestaurante
```
---

## Generar Ejecutable

Para crear un archivo ejecutable (.exe en Windows):

### Método Rápido:

**Windows:**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "menu_data.json;." --name "MenuRestaurante" main.py
```

**Linux/macOS:**
```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed --add-data "menu_data.json:." --name "MenuRestaurante" main.py
```

El ejecutable estará en la carpeta `dist/`
