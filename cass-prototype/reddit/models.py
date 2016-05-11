"""
In a real app, we should probably split all these models into separate apps.
Since this is a prototype, we have it all here to more easily understand

Resource: https://datastax.github.io/python-driver/cqlengine/models.html

"""

import uuid
from cassandra.cqlengine import columns, models, usertype, ValidationError


class Address(usertype.UserType):
    """ Custom field: Address """
    street = columns.Text(required=True)
    zipcode = columns.Integer()

    def validate(self):
        super(Address, self).validate()
        if len(self.zipcode) < 4:
            raise ValidationError("This Zip Code seems too short")


class User(models.Model):
    """ A User """
    user_id = columns.UUID(primary_key=True)
    first_name = columns.Text()
    last_name = columns.Text()
    addr = columns.UserDefinedType(Address)
    todo_list = columns.List(columns.Text)
    favorite_restaurant = columns.Map(columns.Text, columns.Text)
    favorite_numbers = columns.Set(columns.Integer)


class Blog(models.Model):
    """ General Info about a Blog (aka a Subreddit) """
    blog_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    created_at = columns.DateTime()
    user = columns.Text(index=True)
    description = columns.Text(required=False)


class Post(models.Model):
    """ A Post inside a Blog/Subreddit """
    post_id = columns.TimeUUID(primary_key=True)
    blog_id = columns.UUID()
    created_at = columns.DateTime()
    post_title = columns.Text()
    content = columns.Text()
    tags = columns.Set(columns.Text)
    flagged = columns.Boolean(default=False)


class PostVote(models.Model):
    """
    Cassandra requires counters in a separate table (unless the counter is
    part of the primary key definition, which in this case it isn't)
    """
    post_id = columns.TimeUUID(primary_key=True, default=uuid.uuid4)
    upvotes = columns.Counter()
    downvotes = columns.Counter()


class Category(models.Model):
    name = columns.Text(primary_key=True)
    blog_id = columns.UUID(primary_key=True)
    post_id = columns.TimeUUID(primary_key=True)
    post_title = columns.Text()
