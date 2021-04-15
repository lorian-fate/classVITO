https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json

TIA Covid-19
NOMENCLATURA EN INGLÉS
##Recopilación

1._Crear un json con todos los datos obtenidos en la response, de este punto en adelante, solo se consultará nuestro json
    #*Este dataset funciona de la siguiente manera, cada día que pasa se agregan todos los municipios con su nuevo valor acumulativo.
    #*Por ende, no se reescriben, se agregan (append) todos los municipios cada vez


2._Sin contar la reescrituras, cuántos municipios hay en total? O lo que es lo mismo, cuántos diccionarios se agregan cada día?
3._Obtener la TIA inicial
4._Obtener la TIA final

5._Crea una lista con valores de 1 a n siendo 1 la primer fecha y n la última
    #*Esta lista representará el eje x

6._Crea una lista con la TIA diaria de la comunidad (Cada valor será la sumatoria de todos los municipios)
    #*Esta lista representará el eje y

===================================================================================================================================================
OOP
1._Crea en un fichero aparte, un objeto llamado statistics
2._Tendrá los siguiente atributos: x (list), y (list)
3._Propiedades: n, media de x, media de y, varianza de x, varianza de y, sumatoria xy, sumatoria x^2, sumatoria y^2, sumatoria x^2y^2, covarianza,b b0
4._Métodos: coeficiente pearson, y


En conjunto
1._Cuál es el coeficiente de pearson?
2._Cuál es el valor de la covarianza
3._b
4._b0
5._Pasando 10 días, cuál será el valor de la TIA de la comunidad?
6._Cuál era el valor de Pearson durante el confinamiento

Gráficas
1._Representar los últimos 20 días en una gráfica