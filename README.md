# Cómo ejecutar el backend

1. Abrir terminal dentro de la carpeta backend
2. Crear entorno virtual con ```python -m venv venv```
3. Activar entorno virtual con ```./venv/Scripts/activate``` (windows)
4. Instalar dependencias con el comando ```pip install -r requirements.txt```
5. Ejecutar api con ```uvicorn api:app --reload```

Luego de la instalación, solo se deben realizar los pasos 1, 3 y 5.

# Cómo ejecutar el frontend
Para los pasos a continuación se debe tener instalado Node

1. Abrir terminal dentro de la carpeta frontend
2. Instalar dependencias con ```npm install```
3. Ejecutar frontend con ```npm run dev```
4. Ingresar a la URL que dice la consola, en mi caso: http://localhost:5173/

Luego de la instalación, solo se deben ejecutar los pasos 1, 3 y 4

# Posibles errores

## Frontend no puede acceder al backend
Esto puede deberse a que el backend quedó levantado en un puerto distinto al definido en el código: http://localhost:8000/simular

Lo que se debe hacer es levantar el backend en el puerto 8000, o en su defecto modificar la línea que realiza la petición 
(useManageData.jsx, la función llamada 'simular'):

```javascript
const response = await fetch('http://localhost:8000/simular', request)
```
