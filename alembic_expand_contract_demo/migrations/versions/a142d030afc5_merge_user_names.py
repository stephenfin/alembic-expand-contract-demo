"""Merge user names

Revision ID: a142d030afc5
Revises: e629a4ea0677
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = 'a142d030afc5'
down_revision = 'e629a4ea0677'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('user_account', 'last_name')
    op.drop_column('user_account', 'first_name')
