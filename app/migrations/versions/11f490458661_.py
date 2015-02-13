"""Create association object/table for zones and officers.

Revision ID: 11f490458661
Revises: 3972e8a70667
Create Date: 2015-02-12 20:39:06.473168

"""

# revision identifiers, used by Alembic.
revision = '11f490458661'
down_revision = '3972e8a70667'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('zone_assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('officer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['officer_id'], ['officers.id'], ),
    sa.ForeignKeyConstraint(['zone_id'], ['zones.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('zone_assignments')
