"""Modify DB to have regions that belong to a zone.

Revision ID: 3972e8a70667
Revises: 4673b3fa0d68
Create Date: 2015-02-12 19:00:21.009736

"""

# revision identifiers, used by Alembic.
revision = '3972e8a70667'
down_revision = '4673b3fa0d68'

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    op.create_table('regions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('geog', geoalchemy2.types.Geography(geometry_type='POLYGON', srid=4326), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['zone_id'], ['zones.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('zones', 'geog')


def downgrade():
    op.add_column('zones', sa.Column('geog', geoalchemy2.types.Geography(geometry_type=u'MULTIPOLYGON', srid=4326), autoincrement=False, nullable=True))
    op.drop_table('regions')
