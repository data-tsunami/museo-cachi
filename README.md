# Museo Arqueologico "Pio Pablo Diaz"
### Cachi - Salta - Argentina

![Museo Arqueologico Pio Pablo Diaz](https://raw.github.com/data-tsunami/museo-cachi/master/doc/Museo-Arqueologico-Pio-Pablo-Diaz-Cachi.png)

# Modelo de datos

![Modelo de datos](https://github.com/data-tsunami/museo-cachi/raw/master/doc/modelos.png)

# Datos iniciales

Para cargar fixtures:

    $ python manage.py loaddata fixtures.json

Para cargar ubicaciones geograficas y sitios arqueologicos:

    $ python manage.py importar_sitios_arqueologicos --ignorar-primer-linea Ubicacion-Geografica-y-sitios-S-SAL-CAC.csv

Para generar fixture:

    $ python manage.py dumpdata --indent=2 cachi.naturaleza cachi.tipoadquisicion cachi.tipocondicionhallazgo cachi.ubicacion > fixtures.json

# Licencia - GPLv3

    Museo-Cachi is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Museo-Cachi is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Museo-Cachi.  If not, see <http://www.gnu.org/licenses/>.
