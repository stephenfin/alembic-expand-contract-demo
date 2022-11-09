# SPDX-License-Identifier: MIT

import sqlalchemy as sa


def migrate_data():
    engine = sa.create_engine('sqlite:///alembic-expand-contract-demo.db')

    user_account_table = sa.Table(
        'user_account',
        sa.MetaData(),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=30), nullable=True),
        sa.Column('last_name', sa.String(length=30), nullable=True),
        sa.Column('name', sa.String, nullable=True),
    )

    with engine.connect() as conn:
        names = conn.execute(
            sa.select(
                [
                    user_account_table.c.id,
                    user_account_table.c.first_name,
                    user_account_table.c.last_name,
                ]
            )
        ).fetchall()
        for id, first_name, last_name in names:
            conn.execute(
                user_account_table.update()
                .where(user_account_table.c.id == id)
                .values(
                    name=f'{first_name} {last_name}',
                )
            )


if __name__ == '__main__':
    migrate_data()
