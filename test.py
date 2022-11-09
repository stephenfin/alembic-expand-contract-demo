# SPDX-License-Identifier: MIT

import csv
import os

import sqlalchemy as sa
from sqlalchemy import orm

from alembic_expand_contract_demo import models

USERS = os.path.join('data', 'users.csv')
ADDRESSES = os.path.join('data', 'addresses.csv')


def main():
    engine = sa.create_engine('sqlite:///alembic-expand-contract-demo.db')

    with open(USERS) as users_fh, open(ADDRESSES) as addresses_fh:
        user_data = csv.reader(users_fh)
        address_data = csv.reader(addresses_fh)

        with orm.Session(engine) as session:
            session.execute(
                sa.insert(models.User),
                [
                    {'first_name': user[0], 'last_name': user[1]}
                    for user in user_data
                ],
            )
            session.commit()

            session.execute(
                sa.insert(models.Address),
                [
                    {'email_address': address[0], 'user_id': address[1]}
                    for address in address_data
                ],
            )
            session.commit()


if __name__ == '__main__':
    main()
