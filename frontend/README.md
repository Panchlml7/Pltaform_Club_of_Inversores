# Frontend Club de Inversores

Este frontend está basado en React y Tailwind CSS.

## Instalación

1. Abre una terminal en la carpeta `frontend`.
2. Ejecuta:
   ```powershell
   npx create-react-app .
   npm install tailwindcss
   npx tailwindcss init
   ```
3. Configura Tailwind en `src/index.css`:
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```
4. Inicia el frontend:
   ```powershell
   npm start
   ```

## Estructura sugerida
- `src/pages/Login.js` (login de usuario)
- `src/pages/Dashboard.js` (dashboard inversionista)
- `src/pages/AdminPanel.js` (panel administrador)
