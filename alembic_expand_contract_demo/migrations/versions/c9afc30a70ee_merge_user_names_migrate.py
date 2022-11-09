"""Merge user names (migrate)

Revision ID: c9afc30a70ee
Revises: 9c36df1b3f62
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c9afc30a70ee'
down_revision = '9c36df1b3f62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # data migrations
    bind = op.get_bind()

    user_account_table = sa.Table(
        'user_account',
        sa.MetaData(),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=30), nullable=True),
        sa.Column('last_name', sa.String(length=30), nullable=True),
        sa.Column('name', sa.String, nullable=True),
    )

    names = bind.execute(
        sa.select(
            [
                user_account_table.c.id,
                user_account_table.c.first_name,
                user_account_table.c.last_name,
            ]
        )
    ).fetchall()
    for id, first_name, last_name in names:
        bind.execute(
            user_account_table.update()
            .where(user_account_table.c.id == id)
            .values(
                name=f'{first_name} {last_name}',
            )
        )
