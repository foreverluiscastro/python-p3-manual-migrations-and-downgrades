"""Renaming enrolled_date column to start_date

Revision ID: c1c936c797a9
Revises: 791279dd0760
Create Date: 2023-02-09 14:38:21.671362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1c936c797a9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    op.alter_column('students', 'enrolled_date', new_column_name='start_date')


def downgrade() -> None:
    pass
    op.alter_column('students', 'start_date', new_column_name='enrolled_date')