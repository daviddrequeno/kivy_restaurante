from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import json


class PantallaInicio(Screen):    
    def __init__(self, nombre_restaurante, **kwargs):
        super().__init__(**kwargs)
        self.name = 'inicio'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        titulo = Label(
            text=f'[b]{nombre_restaurante}[/b]',
            markup=True,
            font_size='40sp',
            size_hint=(1, 0.3),
            color=(0.2, 0.6, 0.86, 1)
        )
        
        subtitulo = Label(
            text='Bienvenido a nuestro restaurante',
            font_size='20sp',
            size_hint=(1, 0.2),
            color=(0.4, 0.4, 0.4, 1)
        )
        
        # boton para ver menú
        btn_ver_menu = Button(
            text='Ver Menú',
            font_size='24sp',
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 0.86, 1),
            background_normal=''
        )
        btn_ver_menu.bind(on_press=self.ir_a_categorias)
        
        espacio = Label(size_hint=(1, 0.3))
        
        layout.add_widget(titulo)
        layout.add_widget(subtitulo)
        layout.add_widget(btn_ver_menu)
        layout.add_widget(espacio)
        
        self.add_widget(layout)
    
    def ir_a_categorias(self, instance):
        self.manager.current = 'categorias'


class PantallaCategorias(Screen):    
    def __init__(self, categorias, **kwargs):
        super().__init__(**kwargs)
        self.name = 'categorias'
        self.categorias = categorias
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        titulo = Label(
            text='[b]Categorías[/b]',
            markup=True,
            font_size='32sp',
            size_hint=(1, 0.15),
            color=(0.2, 0.6, 0.86, 1)
        )
        
        scroll = ScrollView(size_hint=(1, 0.75))
        
        grid = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None,
            padding=10
        )
        grid.bind(minimum_height=grid.setter('height'))
        
        # crear botón para cada categoría
        for categoria in categorias:
            btn = Button(
                text=categoria['nombre'],
                font_size='22sp',
                size_hint_y=None,
                height=80,
                background_color=(0.3, 0.7, 0.9, 1),
                background_normal=''
            )
            btn.bind(on_press=lambda x, cat=categoria: self.ir_a_productos(cat))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        
        # boton de regreso
        btn_volver = Button(
            text='Volver',
            font_size='18sp',
            size_hint=(1, 0.1),
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        btn_volver.bind(on_press=self.volver_inicio)
        
        layout.add_widget(titulo)
        layout.add_widget(scroll)
        layout.add_widget(btn_volver)
        
        self.add_widget(layout)
    
    def ir_a_productos(self, categoria):
        pantalla_productos = self.manager.get_screen('productos')
        pantalla_productos.cargar_categoria(categoria)
        self.manager.current = 'productos'
    
    def volver_inicio(self, instance):
        self.manager.current = 'inicio'


class PantallaProductos(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'productos'
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.titulo = Label(
            text='',
            markup=True,
            font_size='32sp',
            size_hint=(1, 0.15),
            color=(0.2, 0.6, 0.86, 1)
        )
        
        self.scroll = ScrollView(size_hint=(1, 0.75))
        
        self.grid = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None,
            padding=10
        )
        self.grid.bind(minimum_height=self.grid.setter('height'))
        
        self.scroll.add_widget(self.grid)
        
        btn_volver = Button(
            text='Volver a Categorías',
            font_size='18sp',
            size_hint=(1, 0.1),
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        btn_volver.bind(on_press=self.volver_categorias)
        
        self.layout.add_widget(self.titulo)
        self.layout.add_widget(self.scroll)
        self.layout.add_widget(btn_volver)
        
        self.add_widget(self.layout)
    
    def cargar_categoria(self, categoria):
        self.titulo.text = f'[b]{categoria["nombre"]}[/b]'
        
        self.grid.clear_widgets()
        
        for producto in categoria['productos']:
            producto_layout = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=100,
                padding=10,
                spacing=10
            )
            
            contenedor = BoxLayout(
                orientation='horizontal',
                padding=15,
                spacing=15
            )
            
            nombre = Label(
                text=producto['nombre'],
                font_size='20sp',
                size_hint_x=0.7,
                halign='left',
                valign='middle',
                color=(0.2, 0.2, 0.2, 1)
            )
            nombre.bind(size=nombre.setter('text_size'))
            
            precio = Label(
                text=f'${producto["precio"]:.2f}',
                font_size='22sp',
                size_hint_x=0.3,
                halign='right',
                valign='middle',
                color=(0.2, 0.6, 0.2, 1),
                bold=True
            )
            precio.bind(size=precio.setter('text_size'))
            
            contenedor.add_widget(nombre)
            contenedor.add_widget(precio)
            
            # crear efecto de tarjeta
            from kivy.graphics import Color, RoundedRectangle
            with contenedor.canvas.before:
                Color(0.95, 0.95, 0.95, 1)
                contenedor.rect = RoundedRectangle(
                    pos=contenedor.pos,
                    size=contenedor.size,
                    radius=[10]
                )
            
            def actualizar_rect(instance, value):
                instance.rect.pos = instance.pos
                instance.rect.size = instance.size
            
            contenedor.bind(pos=actualizar_rect, size=actualizar_rect)
            
            producto_layout.add_widget(contenedor)
            self.grid.add_widget(producto_layout)
    
    def volver_categorias(self, instance):
        self.manager.current = 'categorias'


class MenuRestauranteApp(App):
    
    def build(self):
        """Construir la aplicación"""
        Window.size = (400, 600)
        Window.clearcolor = (1, 1, 1, 1)
        
        # cargar datos del menú desde JSON
        try:
            with open('menu_data.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
        except FileNotFoundError:
            print("Error: No se encontró el archivo menu_data.json")
            return Label(text='Error: Archivo de menú no encontrado')
        
        sm = ScreenManager()
        
        pantalla_inicio = PantallaInicio(datos['restaurante'])
        pantalla_categorias = PantallaCategorias(datos['categorias'])
        pantalla_productos = PantallaProductos()
        
        sm.add_widget(pantalla_inicio)
        sm.add_widget(pantalla_categorias)
        sm.add_widget(pantalla_productos)
        
        sm.current = 'inicio'
        
        return sm


if __name__ == '__main__':
    MenuRestauranteApp().run()