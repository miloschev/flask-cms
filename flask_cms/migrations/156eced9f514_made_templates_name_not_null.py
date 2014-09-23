"""made templates.name NOT NULL

Revision ID: 156eced9f514
Revises: 4c0a6bfd982e
Create Date: 2014-07-16 03:26:57.737910

"""

# revision identifiers, used by Alembic.
revision = '156eced9f514'
down_revision = '4c0a6bfd982e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('templates', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('templates', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    ### end Alembic commands ###