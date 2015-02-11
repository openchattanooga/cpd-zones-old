"""Add officers table.

Revision ID: 11a746893a56
Revises: None
Create Date: 2015-02-11 18:49:51.382847

"""

# revision identifiers, used by Alembic.
revision = '11a746893a56'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'officers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(200), nullable=False),
        sa.Column('email', sa.Unicode(200), nullable=False),
        sa.Column('phone', sa.Unicode(200), nullable=False),
        sa.Column('title', sa.Unicode(200), nullable=False),
    )


def downgrade():
    op.drop_table('officers')
