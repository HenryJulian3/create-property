# create-property

Este proyecto es una utilidad para crear propiedades en objetos de JavaScript de manera segura y eficiente, incluso cuando las propiedades están profundamente anidadas.

## 🚀 Características

- Crea propiedades en objetos anidados utilizando una cadena de ruta.
- Si alguna de las propiedades intermedias no existe, las crea automáticamente.
- Devuelve `true` si la propiedad se creó o actualizó con éxito.
- Devuelve `false` si el argumento proporcionado no es un objeto.

## 📦 Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/HenryJulian3/create-property.git
   cd create-property
   ```

2. Instala las dependencias:

   ```sh
   npm install
   ```

## 🛠 Uso

1. Importa la función en tu proyecto:

   ```javascript
   const createProperty = require('create-property');
   ```

2. Utiliza la función para crear una propiedad anidada:

   ```javascript
   const obj = {};

   const result = createProperty('n.p.m', obj, true);
   console.log(result); // true
   console.log(obj.n.p.m); // true
   ```

## 📋 Notas

- Si la propiedad ya existe, su valor será actualizado.
- Si el argumento proporcionado no es un objeto, la función devolverá `false`.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.
