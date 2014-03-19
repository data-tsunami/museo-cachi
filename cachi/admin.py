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

from cachi import models
from django.contrib import admin


admin.site.register(models.PiezaConjunto)
admin.site.register(models.Fragmento)
admin.site.register(models.FichaTecnica)
admin.site.register(models.Adjunto)
admin.site.register(models.TipoAdquisicion)
admin.site.register(models.TipoCondicionHallazgo)
admin.site.register(models.Naturaleza)
admin.site.register(models.Persona)
admin.site.register(models.Ubicacion)
admin.site.register(models.InformeCampo)
admin.site.register(models.UbicacionGeografica)
admin.site.register(models.Procedencia)
admin.site.register(models.SitioArqueologico)
admin.site.register(models.FichaRelevamientoSitio)
admin.site.register(models.Modificacion)
