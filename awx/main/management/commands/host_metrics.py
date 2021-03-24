from django.core.management.base import BaseCommand
from dateutil import parser
from django.utils.timezone import now
import pytz
from datetime import datetime, timezone
from awx.main.models.inventory import HostMetrics
import sdb


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
            since = since.replace(tzinfo=timezone.utc)
        else:
            since = None
        if opt_until:
            until = parser.parse(opt_until)
            until = until.replace(tzinfo=timezone.utc)
        else:
            until = now()

        # a sample query and result , probably need to add a filter for until as well
        result = HostMetrics.objects.filter(last_automation__lte=since)
        print(result)
