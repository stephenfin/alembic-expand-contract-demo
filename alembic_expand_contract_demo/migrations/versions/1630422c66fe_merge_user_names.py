"""Merge user names

Revision ID: 1630422c66fe
Revises: 9c36df1b3f62
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1630422c66fe'
down_revision = '9c36df1b3f62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'user_account', sa.Column('name', sa.String(), nullable=True)
    )
