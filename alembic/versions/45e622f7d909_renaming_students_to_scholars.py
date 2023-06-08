"""Renaming students to scholars

Revision ID: 45e622f7d909
Revises: 
Create Date: 2023-06-08 08:37:09.190651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e622f7d909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
