# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError


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

        with open(args[0], 'rb') as f:
            reader_csv = csv.reader(f, dialect=csv.excel_tab)
            rows = [row for row in reader_csv]
            if options['ignorar_primer_linea']:
                rows = rows[1:]
            for row in rows:
                print u" + Row:"
                for cell in row:
                    print u"     - {0}".format(cell.decode('utf-8'))

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
