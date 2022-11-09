"""Merge user names (expand)

Revision ID: 9c36df1b3f62
Revises: 6cb93d555e2b
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9c36df1b3f62'
down_revision = '6cb93d555e2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'user_account',
        sa.Column('name', sa.String(), nullable=True),
    )
