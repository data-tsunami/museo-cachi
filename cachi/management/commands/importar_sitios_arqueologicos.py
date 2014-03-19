# -*- coding: utf-8 -*-
#======================================================================
#    This file is part of "Museo-Cachi".
#
#    Museo-Cachi is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Museo-Cachi is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Museo-Cachi.  If not, see <http://www.gnu.org/licenses/>.
#======================================================================
from __future__ import unicode_literals

import csv
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from cachi.models import Ubicacion, UbicacionGeografica, SitioArqueologico


class Command(BaseCommand):
    args = 'archivo_csv'
    option_list = BaseCommand.option_list + (
        make_option('--ignorar-primer-linea',
            action='store_true',
            dest='ignorar_primer_linea',
            default=False,
            help='Ignora la primer linea del archivo CSV'),
        )

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("Debe especificar el archivo CSV")

        # + Row:
        #     - PAIS
        #     - PROVINCIA
        #     - DEPARTAMENTO
        #     - LOCALIDAD/Municipio
        #     - PARAJE
        #     - NRO - SITIO
        #     - NOMBRE DEL SITIO ARQ
        #
        # + Row:
        #     - Argentina
        #     - Salta
        #     - Cachi
        #     - Cachi
        #     - La Paya
        #     - 1
        #     - Puerta La Paya

        with open(args[0], 'rb') as f:
            reader_csv = csv.reader(f, dialect=csv.excel_tab)
            rows = [row for row in reader_csv]
            if options['ignorar_primer_linea']:
                rows = rows[1:]
            for row in rows:
                print u" + Row:"
                row = [cell.decode('utf-8') for cell in row]
                for cell in row:
                    print u"     - {0}".format(cell)

                pais = row[0].strip().capitalize()
                prov = row[1].strip().capitalize()
                depto = row[2].strip().capitalize()
                loc = row[3].strip().capitalize()
                paraje = row[4].strip().capitalize()
                nomenclatura_sitio = row[5].strip().capitalize()
                nro_sitio = row[6].strip().capitalize()
                nombre_sitio = row[7].strip().capitalize() # puede ser null o vacio

                try:
                    pais = UbicacionGeografica.objects.get(nombre__icontains=pais, padre=None)
                except UbicacionGeografica.DoesNotExist:
                    pais = UbicacionGeografica.objects.create(nombre=pais, nivel=1)

                try:
                    prov = pais.hijos.get(nombre__icontains=prov)
                except UbicacionGeografica.DoesNotExist:
                    prov = UbicacionGeografica.objects.create(nombre=prov, padre=pais, nivel=2)

                try:
                    depto = prov.hijos.get(nombre__icontains=depto)
                except UbicacionGeografica.DoesNotExist:
                    depto = UbicacionGeografica.objects.create(nombre=depto, padre=prov, nivel=3)

                try:
                    loc = depto.hijos.get(nombre__icontains=loc)
                except UbicacionGeografica.DoesNotExist:
                    loc = UbicacionGeografica.objects.create(nombre=loc, padre=depto, nivel=4)

                try:
                    paraje = loc.hijos.get(nombre__icontains=paraje)
                except UbicacionGeografica.DoesNotExist:
                    paraje = UbicacionGeografica.objects.create(nombre=paraje, padre=loc, nivel=5)

                if nombre_sitio:
                    nombre_completo = nomenclatura_sitio + u"-" + nro_sitio + u"-" + nombre_sitio
                else:
                    nombre_completo = nomenclatura_sitio + u"-" + nro_sitio

                try:
                    SitioArqueologico.objects.get(ubicacion_geografica=paraje,
                        nombre=nombre_completo)
                except SitioArqueologico.DoesNotExist:
                    SitioArqueologico.objects.create(ubicacion_geografica=paraje,
                        nombre=nombre_completo)

#            for poll_id in args:
#                try:
#                    poll = Poll.objects.get(pk=int(poll_id))
#                except Poll.DoesNotExist:
#                    raise CommandError('Poll "%s" does not exist' % poll_id)
#
#                poll.opened = False
#                poll.save()
#
#                self.stdout.write('Successfully closed poll "%s"' % poll_id)
