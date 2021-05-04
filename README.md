# Web Python Granada 


## ¿Que es esto?

Este es el repositorio con el código fuente de la humilde web de la organización **« Python Granada »** 

El objetivo es que sea un punto de encuentro y un lugar donde compartir las últimas novedades, eventos de interés que se organizan y todos la cosas de la comunidad Python que te puedan interesar para que no te pierdas nada.

Además aquí todo el mundo tiene cabida y tienes tu propio hueco para crear tu post, publicarlo en el blog para que toda la comunidad Python pueda verlo y  fardar cuando hables con tu cuñado. 


## ¿Como puedo ayudar? 

Si te va la marcha y quieres ayudar con este proyecto, ya verás que es bastante fácil hacerlo.

Hemos estructurado el proyecto para separar dos roles diferentes.

### Creador de contenidos o editor

Aquí no necesitas tener grandes conocimientos técnicos, solo necesitamos creatividad.

Todos los contenidos se escriben usando [Markdown](https://markdown.es/) y no tienes que pelearte con HTML ni CSS, solo darle rienda suelta a tu imaginación.


### Web developer

Si tienes conocimientos de maquetación web y un poco de gusto estético, puedes ayudar a mejorar aspectos de diseño o usabilidad de la web.

En principio estamos usando [Bulma Framework](https://bulma.io/), pero siente se puede cambiar a algo más avanzado si merece la pena.


## Al cacharreo

La web es generada usando [Pelican](https://blog.getpelican.com/), que nos ahorra hacer trabajo aburrido, tener que usar copy/paste constantemente y otras muchas magias divertidas con Python que poco a poco irás descubriendo.


### Estructura del proyecto

El proyecto queda estructurado en los siguientes directorios:
Divido los directorios en tres **categorías**.

1. **Infra**, su propósito es preparar el entorno, instalar las dependencias y otras magias.
2. **UI / UX**, contiene el código para darle forma y color a la web, generalmente HTML, CSS.
3. **Content**, contiene artículos y publicaciones en markdown.
4. **Code**, contiene scripts en python para hacer pequeñas magias con Pelican y Python.

Y tendríamos los siguientes directorios: 

- **.github** (infra) Aquí se definen las cosas referentes a la integración continua, (mejor no tocarlo mucho xD)
- **compose** (infra) Aquí se definen los manifiestos Docker, que preparan todo lo necesario para que funcione en tu localhost.
- **content** (content) Aquí se alojan los articulos y publicaciones en formato Markdown.
- **plugins** (code) Plugins de Pelican.
- **themes** (ui/ux) Código HTML y CSS que pone bonita la web.
- **output** (autogenerado) Aquí se guarda el código de la web compilado, se genera automáticamente, por lo tanto **no modifiques manualmente**.


### Localhost

Para arrancar este proyecto en local, independientemente del sistema operativo que uses, necesitas instalar [Docker](https://www.docker.com/get-started) y [docker-compose](https://docs.docker.com/compose/install/).

```sh
docker-compose up --build
```


En el archivo **Makefile** tienes los comandos más usados para gestionar el proyecto en local, ``make``. 


```sh
make up
```

Accede con tu navegador a la url [localhost:8000](http://localhost:8000)


## Tengo algo bueno, vamos a publicar.

Aquí nos gusta mucho el software libre, por tanto todas las contribuciones se gestionan vía Github y usando **Pull Request** una vez se accepte el PR se publica automáticamente mediante nuestro GitHub Action personalizado, [GitHub Pages Pelican Build Action
](https://github.com/PythonGranada/gh-pages-pelican-action) (by fork [nelsonjchen](https://github.com/nelsonjchen/pelican-action-demo))

