from django.core.management.base import BaseCommand
from dateutil import parser
from django.utils.timezone import now
import pytz
from datetime import datetime, timezone
from awx.main.models.inventory import HostMetrics
import json


class Command(BaseCommand):

    help = 'This is for offline licensing usage'

    def add_arguments(self, parser):
        parser.add_argument('--since', dest='since', action='store', help='Start date for data')
        parser.add_argument('--until', dest='until', action='store', help='End date for data')
        parser.add_argument('--json', action='store_true', help='Select output as JSON')

    def handle(self, *args, **options):
        opt_since = options.get('since')
        opt_until = options.get('until')

        # user gives no arguments
        if opt_since is None and opt_until is None:
            print("No Arguments received")
            return None

        since = None
        if opt_since:
            since = parser.parse(opt_since)
            if since.tzinfo is None:
                since = since.replace(tzinfo=timezone.utc)

        until = None
        if opt_until:
            until = parser.parse(opt_until)
            if until.tzinfo is None:
                until = until.replace(tzinfo=timezone.utc)

        if (since is None) and (until is not None):
            filter_kwargs = {"last_automation__lte": until}
        elif (since is not None) and (until is None):
            filter_kwargs = {"last_automation__gte": since}
        else:
            filter_kwargs = {"last_automation__gte": since, "last_automation__lte": until}

        result = HostMetrics.objects.filter(**filter_kwargs)

        # if --json flag is set, output the result in json format
        if options['json']:
            list_of_queryset = list(result.values('hostname', 'first_automation', 'last_automation'))
            for item in list_of_queryset:
                item['first_automation'] = item['first_automation'].strftime('%Y-%m-%d')
                item['last_automation'] = item['last_automation'].strftime('%Y-%m-%d')

            json_result = json.dumps(list_of_queryset)
            print(json_result)

        # --json flag is not set, output in plain text
        else:
            print("Total Number of hosts automated : {hosts_automated}".format(hosts_automated=len(result)))
            for item in result:
                print(
                    "Hostname : {hostname} | first_automation : {first_automation} | last_automation : {last_automation}".format(
                        hostname=item.hostname, first_automation=item.first_automation, last_automation=item.last_automation
                    )
                )

        return
