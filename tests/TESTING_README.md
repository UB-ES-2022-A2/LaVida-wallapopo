<h1>Guía de testing</h1>
<h3>Backend</h3>
Pasos para comprobar si todos los tests pasan:

1. Ejecutar el <code>app.run()</code> (sólo requerido si se ejecutarán tests funcionales).
2. Navegar desde el terminal hasta este directorio (carpeta <code>tests</code>).
3. Ejecutar el archivo <code>run_all_tests.py</code>.

(O simplemnete haced click derecho en una de las carpetas <code>tests</code>/<code>functional</code>/<code>unit</code> 
y seleccionad <code>Run 'pytest in <name_folder>'</code>).

En caso de querer ejecutar sólo un archivo de tests, ejecutad en el terminal: 
<br><code>pytest /folder_name/file_name.py</code> 
p.e. <code>pytest /functional/test_session.py</code>