"""Add zones table

Revision ID: 55004b0f00d6
Revises: 11a746893a56
Create Date: 2015-02-11 19:25:19.261785

"""

# revision identifiers, used by Alembic.
revision = '55004b0f00d6'
down_revision = '11a746893a56'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('zones',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.Unicode(length=200), autoincrement=False, nullable=False),
    )


def downgrade():
    op.drop_table('zones')
