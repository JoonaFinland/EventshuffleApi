"""dates array

Revision ID: 0054928b890b
Revises: 75e7fb0095aa
Create Date: 2023-12-01 00:37:58.922290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0054928b890b'
down_revision: Union[str, None] = '75e7fb0095aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add a new column
    op.add_column('votes', sa.Column('date_new', sa.ARRAY(sa.String())))

    # Copy data from old column to new column
    op.execute('UPDATE votes SET date_new = ARRAY[date]')

    # Drop the old column
    op.drop_column('votes', 'date')

    # Rename the new column to the original name
    op.alter_column('votes', 'date_new', new_column_name='date')


def downgrade() -> None:
    # In case of a downgrade, reverse the process
    op.add_column('votes', sa.Column('date_new', sa.DATE()))
    op.execute('UPDATE votes SET date = date_new')
    op.drop_column('votes', 'date_new')
