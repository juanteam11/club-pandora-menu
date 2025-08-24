# 🎭 Club Secret - Menú Digital con Código QR

Una solución completa para mostrar el menú de bebidas del Club Secret mediante códigos QR que los clientes pueden escanear desde sus mesas.

## 📱 ¿Qué incluye este proyecto?

- **Menú Digital Interactivo**: Página web responsive con el listado completo de bebidas
- **Generador de Códigos QR**: Herramientas para crear QR codes que dirijan al menú
- **Diseño Profesional**: Tema visual elegante apropiado para un club nocturno
- **Compatible con Móviles**: Optimizado para verse perfectamente en smartphones

## 🚀 Archivos del Proyecto

```
club-secret-menu/
├── index.html          # Página principal del menú
├── css/
│   └── styles.css      # Estilos del menú (tema club nocturno)
├── js/
│   └── menu.js         # Funcionalidades interactivas
├── qr-generator.html   # Generador de QR en el navegador
├── generate_qr.py      # Script Python para generar QR
└── README.md           # Este archivo de instrucciones
```

## 🎯 Uso Rápido

### Opción 1: Generador Web (Recomendado)
1. Abre `qr-generator.html` en tu navegador
2. Deja la URL vacía para usar el archivo local o introduce tu URL web
3. Haz clic en "Generar Código QR"
4. Descarga la imagen del QR
5. ¡Imprime y coloca en las mesas!

### Opción 2: Script Python
```bash
# Instalar dependencias
pip install qrcode[pil] pillow

# Generar QR con URL personalizada
python generate_qr.py "https://tu-servidor.com/menu"

# O generar QR para uso local
python generate_qr.py
```

## 🌐 Configuración para Servidor Web

Si quieres alojar el menú en un servidor web:

1. Sube todos los archivos a tu servidor web
2. Asegúrate de que `index.html` sea accesible
3. Usa la URL completa al generar el QR
4. Ejemplo: `https://clubsecret.com/menu/`

## 📋 Menú Actual

El menú incluye las siguientes categorías:

- **Cocktails Premium** (Secret Manhattan, Mystique Martini, etc.)
- **Cocktails Signature** (Club Secret Especial, Midnight Kiss, etc.)
- **Shots Premium** (Tequila Don Julio, Whiskey Jack Daniel's, etc.)
- **Cervezas** (Corona, Heineken, Stella Artois, etc.)
- **Vinos** (Malbec, Sauvignon Blanc, Prosecco, etc.)
- **Sin Alcohol** (Virgin Mojito, jugos naturales, etc.)

## ✏️ Personalización

### Modificar Bebidas
Edita el archivo `index.html` en las secciones `<div class="drink-item">` para:
- Cambiar nombres de bebidas
- Actualizar descripciones
- Modificar precios
- Agregar/quitar categorías

### Cambiar Colores y Estilo
Modifica el archivo `css/styles.css` para:
- Cambiar la paleta de colores
- Ajustar tipografías
- Modificar efectos visuales
- Adaptar el responsive design

### Información del Club
En `index.html`, actualiza la sección `<footer>` con:
- Dirección real del club
- Número de teléfono para reservas
- Redes sociales

## 📱 Cómo Usar los QR Codes

1. **Impresión**: Imprime los códigos QR en tamaño mínimo 5x5 cm
2. **Ubicación**: Coloca en cada mesa o en lugares visibles
3. **Material**: Usa material resistente (plastificado recomendado)
4. **Instrucciones**: Agrega texto "Escanea para ver nuestro menú"

## 🎨 Características del Diseño

- **Tema Nocturno**: Colores dorados y púrpuras elegantes
- **Efectos Visuales**: Animaciones suaves y efectos hover
- **Responsive**: Se adapta perfectamente a cualquier tamaño de pantalla
- **Fuentes Web**: Tipografías elegantes de Google Fonts
- **Interactividad**: Elementos con efectos al hacer clic

## 🔧 Resolución de Problemas

### El QR no funciona
- Verifica que la URL sea correcta y accesible
- Para uso local, asegúrate de que todos los archivos estén en la misma carpeta
- Prueba el QR con diferentes apps de escaneo

### El menú no se ve bien en móvil
- Verifica que el archivo `css/styles.css` esté cargando correctamente
- Asegúrate de tener conexión a internet para las fuentes de Google

### Problemas con el script Python
```bash
# Instalar dependencias en macOS/Linux
pip3 install qrcode[pil] pillow

# En Windows
pip install qrcode[pil] pillow
```

## 📞 Soporte

Para personalización adicional o soporte técnico, contacta al desarrollador con los detalles específicos de tu implementación.

---

### 🌟 ¡Disfruta tu menú digital!

Este sistema te permitirá ofrecer una experiencia moderna y elegante a los clientes de Club Secret, facilitando el acceso al menú de bebidas de forma rápida y sin contacto.
