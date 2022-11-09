"""Merge user names

Revision ID: 0585005489f0
Revises: 6cb93d555e2b
Create Date: 2022-11-10 17:05:02.774976
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0585005489f0'
down_revision = '6cb93d555e2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # schema migrations - expand
    op.add_column(
        'user_account',
        sa.Column('name', sa.String(), nullable=True),
    )

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

    # schema migrations - contract
    op.drop_column('user_account', 'first_name')
    op.drop_column('user_account', 'last_name')


def downgrade() -> None:
    raise Exception("Irreversible migration")
