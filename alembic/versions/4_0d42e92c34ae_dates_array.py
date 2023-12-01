"""dates array

Revision ID: 0d42e92c34ae
Revises: 0054928b890b
Create Date: 2023-12-01 00:43:40.339061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d42e92c34ae'
down_revision: Union[str, None] = '0054928b890b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Convert existing data to ARRAY(String)
    op.execute('ALTER TABLE events ALTER COLUMN possible_dates TYPE VARCHAR[] USING ARRAY[possible_dates]::VARCHAR[]')
    # Now change the column type
    op.alter_column('events', 'possible_dates', existing_type=sa.String(), type_=sa.ARRAY(sa.String()))

def downgrade():
    op.alter_column('events', 'possible_dates', existing_type=sa.ARRAY(sa.String()), type_=sa.String(), using='possible_dates::varchar')
