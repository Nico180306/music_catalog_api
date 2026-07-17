# Music Catalog API

API REST desarrollada con **Django** y **Django REST Framework**, para el manejo de un catálogo de **Artistas** y **Álbumes** (relación uno a muchos). Protegida mediante **OAuth 2.0** usando `django-oauth-toolkit`.

Este backend expone únicamente endpoints JSON — no renderiza vistas HTML. El consumo está pensado para el frontend en React del proyecto: [`music_catalog_client`](#).

---

## 🛠️ Tecnologías

- Python 3.12
- Django 6
- Django REST Framework
- django-oauth-toolkit (OAuth 2.0)
- django-cors-headers
- SQLite (desarrollo)

---

## 📋 Requisitos previos

- Python 3.12 o superior instalado ([python.org](https://www.python.org/downloads/) — evitar la versión de Microsoft Store)
- Git
- Node.js (solo si vas a correr también el frontend, no es necesario para el backend)

---

## 🚀 Instalación paso a paso (desde cero)

### 1. Clonar el repositorio

```bash
git clone https://github.com/Nico180306/music_catalog_api.git
cd music_catalog_api
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Sabrás que está activo porque el prompt de la terminal mostrará `(venv)` al inicio.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. (Opcional) Crear un superusuario para acceder al admin de Django

```bash
python manage.py createsuperuser
```

### 6. Levantar el servidor

```bash
python manage.py runserver
```

El servidor quedará disponible en `http://127.0.0.1:8000/`.

---

## 🔐 Autenticación OAuth 2.0

Todos los endpoints bajo `/api/` requieren un token de acceso válido.

### 1. Registrar una aplicación OAuth2

Ingresa al panel de administración (`http://127.0.0.1:8000/admin/`) con el superusuario creado antes, y en **Django OAuth Toolkit → Applications**, crea una nueva aplicación:

- **Client type:** Confidential
- **Authorization grant type:** Resource owner password-based

Guarda el `Client ID` y `Client Secret` generados — se usan para obtener el token.

### 2. Obtener un token de acceso

```
POST /o/token/
Content-Type: application/x-www-form-urlencoded

grant_type=password
username=<usuario>
password=<contraseña>
client_id=<client_id>
client_secret=<client_secret>
```

Respuesta esperada:

```json
{
  "access_token": "xxxxxxxx",
  "expires_in": 36000,
  "token_type": "Bearer",
  "refresh_token": "xxxxxxxx",
  "scope": "read write"
}
```

### 3. Usar el token en las peticiones protegidas

```
GET /api/artistas/
Authorization: Bearer <access_token>
```

---

## 📡 Endpoints principales

| Método | Endpoint | Descripción | Auth requerida |
|---|---|---|---|
| POST | `/o/token/` | Obtener token OAuth2 | No |
| GET | `/api/artistas/` | Listar artistas | Sí |
| POST | `/api/artistas/` | Crear artista | Sí |
| GET | `/api/artistas/{id}/` | Detalle de un artista | Sí |
| PUT/PATCH | `/api/artistas/{id}/` | Editar artista | Sí |
| DELETE | `/api/artistas/{id}/` | Eliminar artista | Sí |
| GET | `/api/albumes/` | Listar álbumes | Sí |
| POST | `/api/albumes/` | Crear álbum | Sí |
| GET | `/api/albumes/{id}/` | Detalle de un álbum | Sí |
| PUT/PATCH | `/api/albumes/{id}/` | Editar álbum | Sí |
| DELETE | `/api/albumes/{id}/` | Eliminar álbum | Sí |

Todas las respuestas están en formato **JSON** — la interfaz navegable de DRF está deshabilitada intencionalmente.

---

## 📦 Colección de Postman

En la carpeta [`/postman`](./postman) se encuentra la colección exportada con variables de entorno (`base_url`, `client_id`, `client_secret`, `access_token`) para probar todos los endpoints, incluido el flujo completo de obtención de token.

---

## 📁 Estructura del proyecto

```
music_catalog_api/
├── catalog/
│   ├── models.py        # Modelos Artist y Album
│   ├── serializers.py
│   ├── views.py          # ViewSets
│   ├── urls.py
│   └── migrations/
├── music_api/
│   ├── settings.py       # Config general, OAuth2, CORS, DRF
│   └── urls.py
├── postman/               # Colección exportada de Postman
├── requirements.txt
├── manage.py
└── README.md
```

---

## 👥 Equipo

- **Nicolás Santillán** — Configuración base del proyecto, CORS, OAuth 2.0, relación 1:N en rutas.
- **Jaime Jiménez** — Modelos, serializers y viewsets de Artista y Álbum, documentación.

---

## ⚠️ Notas de desarrollo

- El proyecto usa `JSONRenderer` como único renderer configurado — no se puede acceder a la interfaz navegable de DRF desde el navegador; usar Postman o el frontend para probar operaciones distintas a `GET`.
- Variables sensibles (`SECRET_KEY`, credenciales de OAuth2) deben moverse a variables de entorno antes de cualquier despliegue a producción — actualmente están en `settings.py` solo para fines de desarrollo académico.
