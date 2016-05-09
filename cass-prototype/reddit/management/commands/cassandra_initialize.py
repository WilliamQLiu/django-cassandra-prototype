from django.core.management.base import BaseCommand

from cassandra.cluster import Cluster, NoHostAvailable


class Command(BaseCommand):
    #http://datastax.github.io/python-driver/getting_started.html

    def handle(self, *args, **options):
        print "Running Cassandra Initialize"
        cluster = Cluster(['127.0.0.1'])
        try:
            session = cluster.connect()
        except NoHostAvailable:
            print "No Cassandra Host Available: Check Cassandra has started"

        cluster.shutdown()

