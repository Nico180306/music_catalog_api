# 1. Definir la imagen base
FROM python:3.12-slim

# 2. Configurar variables de entorno de Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Establecer el directorio de trabajo
WORKDIR /app

# 4. Copiar e instalar dependencias primero
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código del proyecto
COPY . /app/

# 6. Exponer el puerto de comunicación
EXPOSE 8000

# 7. Definir el comando de arranque
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]