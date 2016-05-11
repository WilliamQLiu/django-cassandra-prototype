"""
Examples of using the API from datastax to query Cassandra
https://datastax.github.io/python-driver/api/index.html
"""

import pprint
import uuid

from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import setup
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.functions import MinTimeUUID, MaxTimeUUID
#from cassandra.metadata import KeyspaceMetadata, TableMetadata
from datetime import datetime

from models import Blog, Post

pp = pprint.PrettyPrinter(indent=4)


class CassObj(object):
    def __init__(self):
        self.cluster, self.session = self.connect_cluster()
        self.connection = self.connect_cqlengine()

    def connect_cluster(self, ip=['localhost']):
        """
        Connect to a cluster and create a session to explore the cluster
        looking at keyspaces, token_map, and tables
        """
        cluster = Cluster(ip)
        session = cluster.connect()
        return (cluster, session)

    def connect_cqlengine(self):
        """
        Setup a cqlengine connection so we can do queries like query_blogs
        """
        setup(['localhost'], 'cassdb')

    def get_cluster_metadata(self):
        """ Example of how to get metadata about the Cluster """
        pp.pprint("Cluster Name is: " + self.cluster.metadata.cluster_name)  # 'Test Cluster'
        pp.pprint(self.session.hosts)  # [<Host: 127.0.0.1 datacenter1>]
        pp.pprint(self.cluster.metadata.keyspaces)  # { 'cassdb': ...,
        #pp.pprint(self.cluster.metadata.token_map.token_to_host_owner)  # <Murmur3Token: -6809172061991742977>: <Host: 127.0.0.1 datacenter1>

    def get_keyspace_metadata(self):
        """ Example of how to get metadata about specific Keyspaces """
        my_keyspace = self.cluster.metadata.keyspaces['cassdb']
        pp.pprint("Keyspace name is: " + my_keyspace.name)  # 'cassdb'
        pp.pprint(my_keyspace.tables)  # { 'blog': ...,
        pp.pprint(my_keyspace.user_types)  # { 'address': ...
        pp.pprint(my_keyspace.indexes)  # { 'blog_user_idx': ...
        pp.pprint(my_keyspace.views)

    def get_table_metadata(self):
        """ Example of how to get metadata about Tables in a specific Keyspace """
        my_keyspace = self.cluster.metadata.keyspaces['cassdb']
        my_table = my_keyspace.tables['blog']
        pp.pprint(my_table)
        pp.pprint(my_table.columns)  # { 'blog_id': }

    def query_blogs(self):
        """ Examples of some simple querying """
        print "Queryset for All Blogs"
        for blog in Blog.objects.all():
            print(blog)

        print "Queryset to Filter Blogs with user: Will"
        queryset_will = Blog.objects.filter(user='will')
        for blog in queryset_will:
            print(blog)

    def create_posts(self):
        sync_table(Post)
        self.post1 = Post.create(
            post_id=uuid.uuid1(),
            blog_id='fdd0ba00-13b2-11e6-88a9-0002a5d5c51c',
            created_at=datetime.now(),
            post_title='I did it!',
            content='Stuff goes in here'
        )
        self.post2 = Post.create(
            post_id=uuid.uuid1(),
            blog_id='fdd0ba00-13b2-11e6-88a9-0002a5d5c51c',
            created_at=datetime.now(),
            post_title='You did it!',
            content='More stuff goes in here'
        )

    def query_posts(self):
        """ Examples of some slightly more advanced querying """
        min_time = datetime(2016, 1, 1)
        max_time = datetime(2017, 1, 1)

        queryset_filter = Post.objects.filter(
            post_id__gt=MinTimeUUID(min_time),
            post_id__lt=MaxTimeUUID(max_time))
        for post in queryset_filter:
            print(post)


if __name__ == '__main__':

    cass1 = CassObj()
    # cass1.get_cluster_metadata()
    # cass1.get_keyspace_metadata()
    # cass1.get_table_metadata()
    #cass1.query_blogs()
    cass1.create_posts()
    #cass1.query_posts()  # Not working
