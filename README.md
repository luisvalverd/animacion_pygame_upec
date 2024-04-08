
# UPEC Animacion por los 18 años

Este es un proyecto en python el cual se realiza una 
animacion sobre los 18 años de la UPEC.

Este proyecto utiliza la libreria de `pygame`

## dependencies

las dependencias del proyecto son las siguientes

| Dependencies  | Version |
|---------------|---------|
|Python         | 3.12.x |
|Pygame         | 2.5.x  |


## install dependencies

```bash
pip install 
```

## Run Animation

```bash
python game.py
```

### fireworks
los fuegos artificiales se dividen en 3 clases
una clase de cola una de particulas y los fuegos artificiales

En la clase de fuegos artificiales tenemos:
```python
class Firework:
  def __init__(self):
    self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    self.colors = (
      (randint(0, 255), randint(0, 255), randint(0, 255)),
      (randint(0, 255), randint(0, 255), randint(0, 255)),
      (randint(0, 255), randint(0, 255), randint(0, 255))
    )
    self.firework = ParticleRule(randint(0, WIN_WIDTH), WIN_HEIGHT, True, self.colors)
    self.exploded = False
    self.particles = []
    self.min_max_particles = VECTOR(100, 200)

```
aqui inicializamos todo lo de la clase como colores de los fuegos artificiales las particulase y un vector donde tenemos un minimo y maximo de particulas.

```python
self.exploded = False
```
El `self.exploded` nos ayuda a verificar si nuestro fuegoa artificial ya ha explotado o aun no

```python
  def explode(self):
    amount = randint(int(self.min_max_particles.x), int(self.min_max_particles.y))
    for _ in range(amount):
      self.particles.append(ParticleRule(self.firework.pos.x, self.firework.pos.y, False, self.colors))
```
esta funcion genera una cantidad de particulas en la explocion de un firework y lo añade a la `lista` de `particles`

La funcion `remove` de la clase `Firework` elimina el fuego artificial como sus particulas

#### controller
El controllador `FireworkAnimation` es el encargado de maneja el tiempo de espera de esta animacion como su duracion y si esta animacion ya paso su timepo se detiene.

Para el uso de esta clase se necesita: `List[Fireworks]`, `transition_speed`, `screen`

para el manejo de la animacion tenemos los metodos `waitingAnimation()` que maneja la espera de los tiempos y `updatePositionFirework()` que maneja la posicion de los fuegos artificiales y actualiza la pantalla

#### Reglas de negocio
para la creacion de la clase de `FireworkAnimation` es necesario usar la funcion de la regla de negocio `createFireworkAnimation(fireworks, waiting_time, screen)` y retorna `FireworkAnimation`


>la clase `FirworkAnimation` hereda de la clase `HandlerAnimation` para el manejo de la animacion

### Particle

En la clase de la `Particle` tenemos necesario la posicion en `x` y `y` un `firework` y la lista de colores

aqui ve manejara el radio de explocion, la vida del fuego artificial, la cola, con su posicion previa una aceleracion y si es remove, 

### SpriteGroup
esta clase nos ayuda a manejar los diferentes grupos de sprites necesarios el agregar un sprite a un grupo mostrarlos por pantalla o limpiar el contenido

En las reglas de negocio de los sprites group
tenemos el creador de un grupo y su asignador
para el asignador tenemos que dar el grupo al cual se va a asignar el sprite y el sprite que se le quiere asignar


## Config
para configurar que musica va sonar o las imagenes o tiempos o la gravedad solo es necesario configurar el archivo `config.py`

la imagen de fondo solo hay que modificar
```python
BG_BUILDING = "img/{image_name}"
```

para la configuracion del sonido
```python 
BG_MUSIC = "sounds/{music}"
```

