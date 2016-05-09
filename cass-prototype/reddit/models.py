import uuid
from cassandra.cqlengine import columns, models


class Blog(models.Model):
    blog_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    created_at = columns.DateTime()
    user = columns.Text(index=True)
    description = columns.Text(required=False)
