# Guía BDD y relaciones & Endpoints
## BDD-relaciones:
### Modelo de accounts.py (models/accounts.py) :

#### Elementos / columnas obligatorios:

- Asumimos que todos los elementos de esta tabla tienen `nullable=False`.
- **Email** es el elemento que servirá de **relacíón / foreign key** con la tabla de products.
- Email y username son únicos para cada usuario
- La variable que encontraremos en accounts.py -> `products = db.relationship('ProductsModel', backref='products', lazy=
  True)` nos servirá para hacer la relación con la tabla de `products` que se encuentra en `models/products.py` y trata
  de los productos que posee un usuario.

| Element   |             Info              |
|-----------|:-----------------------------:|
| **email** | String - primary key - unique |
| username  |        String - unique        |
| password  |            String             |
 
<br>

#### Elementos / columnas opcionales:

- Asumimos que todos los elementos de esta tabla tienen nullable=True

| Element         |    Info     |
|-----------------|:-----------:|
| name            |   String    |
| surname         |   String    |
| birthday        |    Date     |
| profile_picture | String(url) |
 
<br>

#### Elementos de desarroladores:

- En esta tabla tenemos elementos como is_admin (info de si el usuario es admin o no) y token actual del usuario.
- En esta tabla tenemos elementos como confirmed (info de email confirmado o no) y confirmed on (fecha de cuando fue confirmado)

| Element       |                     Info                      |
|---------------|:---------------------------------------------:|
| is_admin      | Int (0->admin, 1->NOT admin) - nullable=False |
| current_token | String - nullable=True - server_default=None  |
| confirmed     |   Boolean - nullable=False - default=False    |
| confirmed_on  |           DateTime - nullable=True            |

<br>

###  Modelo de products.py (models/products.py) :

#### Elementos / columnas obligatorios:

- Asumimos que todos los elementos de esta tabla tienen nullable=False
- `category`, `status` y `condition` son elementos que contienen una lista respectiva a sus diferentes tipos cada uno.
- La variable que encontramos en products.py -> `user_id = db.Column(db.String(50), db.ForeignKey('accounts.email'))` 
  es un elemento o columna más de nuestra tabla products que nos servirá para saber de qué usuario son nuestros
  productos. <br>
  Leemos de la tabla accounts el campo `email`(foreign key)  y lo utilizamos como `user_id` con el propósito qe he
  explicado en el párrafo anterior.

| Element     |                 Info                  |
|-------------|:-------------------------------------:|
| id          |           Int - primary_key           |
| name        |                String                 |
| category    |    Strings list(*`category_list`)     |
| status      |     Strings list(*`status_list`)      |
| condition   |    Strings list(*`condition_list`)    |
| description |                String                 |
| shipment    | Boolean (0-> NO envíos, 1->SÍ envíos) |
| price       |                 Float                 |
| date        |               DateTime                |

<br>

#### Elementos / columnas opcionales:

- Si no hay url para la imagen del producto se pondrá un placeholder por defecto.

| Element |                          Info                           |
|---------|:-------------------------------------------------------:|
| image   | String(url) - server_default='product_placeholder.png'  |

<br>

###  Modelo de favourites.py (models/favourites.py):

#### Elementos / columnas obligatorios:

- Asumimos que todos los elementos de esta tabla tienen nullable=False
- La variable que encontramos en favourites.py -> `user_id = db.Column(db.String(50), db.ForeignKey('accounts.email'))`
  y `product_id = db.Column(db.Integer, db.ForeignKey('products.id'))` es un elemento o columna más de nuestra 
  tabla favourites que nos servirá para saber de qué usuario son nuestros productos. <br>

| Element     |                 Info                  |
|-------------|:-------------------------------------:|
| id          |           Int - primary_key           |
| user_id     |                String                 |
| product_id  |                 Int                   |
| user        |             AccountsModel             |
| product     |             ProductsModel             |

<br>

###  Modelo de orders.py (models/orders.py):

#### Elementos / columnas obligatorios:

- Asumimos que todos los elementos de esta tabla tienen nullable=False
- La tabla contiene la información necesaría para hacer una transacción.

| Element                |                 Info                  |
|------------------------|:-------------------------------------:|
| id                     |           Int - primary_key           |
| buyer_id               |                  Int                  |
| seller_id              |                  Int                  |
| product_id             |                  Int                  |
| credit_card            |           Int(Número largo)           |
| cvc                    |                  Int                  |
| cc_expiration_date     |        DateTime(validez tarjeta)      |
| cc_owner               |          String(Dueño tarjeta)        |
| date                   |         DateTime(Fecha de compra)     |
<br>

## API Endpoints:

### Accounts
`Accounts, /API/account/<'string:email'>'` <br>

- Se encarga de gestionar el registro.

`Validate, /API/validation/'string:validation_token''` <br>

- Se encarga de comprobar si la nueva cuenta registrada está verificada para confirmar el registro y permitir al usuario
  iniciar sesión.

`Profile, /API/profile/'string:email'`

- Se encarga de actualizar el perfil correctamente.

### Products
`Product, '/API/product/'string:id'''`

- Se encarga de devolver toda la información de un producto.

`ProductsList, '/API/products')`

- Se encarga de devolver una lista con todos los productos de nuestra BDD.

`AddProduct, '/API/catalog/add/'string:email''`

- Se encarga de añadir un producto a nuestra BDD.

### Filtering
`Filter, '/API/filter'`

- Se encarga de devolver los productos con el filtro seleccionado.

`FilterCategory, '/API/filter/'string:category''`

- Se encarga de devolver los productos filtrados por categoría.

### Session
`Login, '/API/login'`

- Se encarga de comprobar que los campos introducidos en el login son correctos y devuelve un token de autenticacón con
  un tiempo de expiración de 10 minutos.

`Logout, '/API/logout/'string:email''`

- Se encarga de cerrar la sesión del usuario controlando la autenticidad de la cuenta mediante el token del usuario.


### Favourites

`/API/favourites`, `/API/favourites/<string:email>`

- Se encarga de añadir productos a la lista de favoritos, eliminar de la lista de favoritos y devolver todos
  los productos añadido a la lista de favoritos para un usuario en concreto.

### Orders
`/API/order/add/<string:email>`

- Marca un producto como vendido y también genera una transacción con la información de compra

### Purchases

`/API/order/purchases/<string:email>`

- Devueve el listado de todas las compras del usuario (más recientes primero)

### Sales

`/API/order/sales/<string:email>`

- Devuelve el listado de todas las ventas del usuario (más recientes primero)