const { Client } = require('pg');

const client = new Client({
  host: 'localhost', // Cambia si tu servidor no es local
  port: 5432,        // Puerto por defecto de PostgreSQL
  user: 'tu_usuario', // Cambia por tu usuario real
  password: 'tu_contraseña', // Cambia por tu contraseña real
  database: 'tu_base_de_datos' // Cambia por el nombre real de tu base de datos
});

client.connect()
  .then(() => console.log('Conectado a PostgreSQL'))
  .catch(err => {
    console.error('Error de conexión:', err.message);
    console.error('Detalles:', err);
    process.exit(1); // Finaliza el proceso si falla la conexión
  });

module.exports = client;
