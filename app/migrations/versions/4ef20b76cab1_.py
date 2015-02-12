"""Enable PostGIS

Revision ID: 4ef20b76cab1
Revises: 55004b0f00d6
Create Date: 2015-02-11 20:49:42.303864

"""

# revision identifiers, used by Alembic.
revision = '4ef20b76cab1'
down_revision = '55004b0f00d6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis_topology;")

def downgrade():
    op.execute("DROP EXTENSION IF EXISTS postgis_topology;")
    op.execute("DROP EXTENSION IF EXISTS postgis;")
