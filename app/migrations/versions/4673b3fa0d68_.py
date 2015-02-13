"""Add geom field to zones to hold regions.

Revision ID: 4673b3fa0d68
Revises: 4ef20b76cab1
Create Date: 2015-02-11 21:12:26.578588

"""

# revision identifiers, used by Alembic.
revision = '4673b3fa0d68'
down_revision = '4ef20b76cab1'

from alembic import op
import sqlalchemy as sa
import geoalchemy2 as geo


def upgrade():
    op.add_column('zones', sa.Column('geog', geo.Geography(geometry_type='MULTIPOLYGON', srid=4326)))


def downgrade():
    op.drop_column('zones', 'geog')
