from django.core.management.base import BaseCommand
from dateutil import parser
from django.utils.timezone import now


class Command(BaseCommand):

    help = 'This is for offline licensing usage'

    def add_arguments(self, parser):
        parser.add_argument('--since', dest='since', action='store', help='Start date for data')
        parser.add_argument('--until', dest='until', action='store', help='End date for data')

    def handle(self, *args, **options):

        opt_since = options.get('since')
        opt_until = options.get('until')

        if opt_since:
            since = parser.parse(opt_since)
            self.stdout.write(self.style.SUCCESS(since))
        else:
            since = None
        if opt_until:
            until = parser.parse(opt_until)
            self.stdout.write(self.style.SUCCESS(until))
        else:
            until = now()
            self.stdout.write(self.style.SUCCESS(until))

        self.stdout.write(self.style.SUCCESS("at this point , we have stored the 'since' and 'until' time stamp in two different variable"))

        # go into DB and extract the host names and filter by 'since' and 'until' keyword
