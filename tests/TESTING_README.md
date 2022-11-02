Pasos para comprobar si todos los tests pasan:
1. Navegar desde el terminal hasta este directorio (carpeta <code>tests</code>).
2. Ejecutar el archivo <code>run_all_tests.py</code>.

En caso de querer ejecutar sólo un archivo de tests, ejecutad en el terminal: 
<br><code>pytest /folder_name/file_name.py</code> 
p.e. <code>pytest /functional/test_session.py</code>

Algunos tests añaden información a la base de datos mediante las comprobaciones de los métodos <code>POST</code>.

Actualmente no hay forma de eliminar esos datos automáticamente. Por ello, hay que ejecutar unos comandos (en un 
terminal independiente desde el **directorio padre** del proyecto) para eliminarlos. 

Si todos los tests pasan, hay que 
eliminar todos los elementos añadidos, si falla algún <code>POST</code> solo hay que eliminar los elementos cuyo 
<code>POST</code> **sí** haya funcionado.

*Podéis hacer <code>Ctrl+C</code> y <code>Ctrl+V</code> de todo el bloque de comandos directamente.

**================== DELETE ALL ADDED ELEMENTS ==================**<br>
<code>flask shell</code><br>
<code>from models.accounts import AccountsModel</code><br>
<code>from models.products import ProductsModel</code><br>
<code>a = AccountsModel.get_by_email('dummy@gmail.com')</code><br>
<code>a.delete_from_db()</code><br>
<code>p = ProductsModel.get_by_id(5)</code><br>
<code>p.delete_from_db()</code><br>
<code>exit()</code>

**================== DELETE ADDED ACCOUNTS ==================**<br>
<code>flask shell</code><br>
<code>from models.accounts import AccountsModel</code><br>
<code>a = AccountsModel.get_by_email('dummy@gmail.com')</code><br>
<code>a.delete_from_db()</code><br>
<code>exit()</code>

**================== DELETE ADDED PRODUCTS ==================**<br>
<code>flask shell</code><br>
<code>from models.products import ProductsModel</code><br>
<code>p = ProductsModel.get_by_id(5)</code><br>
<code>p.delete_from_db()</code><br>
<code>exit()</code>