"""Merge user names (contract)

Revision ID: e629a4ea0677
Revises: c9afc30a70ee
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = 'e629a4ea0677'
down_revision = 'c9afc30a70ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # schema migrations - contract
    op.drop_column('user_account', 'first_name')
    op.drop_column('user_account', 'last_name')
