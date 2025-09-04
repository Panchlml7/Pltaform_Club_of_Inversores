# Pltaform Club of Inversores

Este proyecto es una plataforma web para gestión de inversiones, pensada para personas y empresas. Incluye páginas para login, portafolio, historial, ganancias y dinero invertido, con diseño responsivo y moderno.

## ¿Cómo funciona la página?

- **Frontend:** HTML, CSS y JavaScript puro, organizado en carpetas `/css` y `/js`.
- **Páginas:**
  - `index.html`: Página principal.
  - `other_pag/`: Contiene las páginas secundarias (`login.html`, `dinero.html`, `ganancias.html`, `historial.html`).
- **Estilos:** Todos los estilos están en `/css`.
- **Scripts:** Todos los scripts están en `/js`.
- **Navegación:** Menú superior para PC/tablet y menú inferior para móvil.
- **Login:** Permite elegir entre persona o empresa, con email y contraseña.

## ¿Cómo ver la página?

1. Sube el proyecto a GitHub y activa GitHub Pages desde la rama `main` y carpeta raíz (`/`).
2. Accede a la URL que te da GitHub Pages para ver la web.

## ¿Cómo conectar con pgAdmin y una base de datos?

1. Instala **pgAdmin** y **PostgreSQL** en tu máquina.
2. Crea una base de datos y usuario en pgAdmin.
3. En el backend (por ejemplo, usando Python y Flask), conecta a la base de datos PostgreSQL usando la librería `psycopg2` o `SQLAlchemy`.
4. Expón una API REST para que el frontend pueda consultar y enviar datos.
5. Modifica el frontend para consumir la API y mostrar datos reales.

### Ejemplo de conexión en Python (Flask):
```python
import psycopg2
conn = psycopg2.connect(
    dbname='tu_db', user='tu_usuario', password='tu_pass', host='localhost', port='5432'
)
```

## Próximos pasos
- Integrar backend con Flask o FastAPI.
- Conectar frontend con la API.
- Guardar y mostrar datos reales de inversiones, usuarios y movimientos.
- Mejorar seguridad y validaciones.

---

¿Dudas? Puedes contactarme por GitHub o correo.
