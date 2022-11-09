"""Initial models

Revision ID: 6cb93d555e2b
Revises:
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6cb93d555e2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user_account',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=30), nullable=True),
        sa.Column('last_name', sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'address',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email_address', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user_account.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
