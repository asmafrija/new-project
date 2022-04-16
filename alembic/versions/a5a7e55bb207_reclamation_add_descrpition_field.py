"""[Reclamation] add descrpition field

Revision ID: a5a7e55bb207
Revises: 8aecee399bff
Create Date: 2022-04-09 00:11:20.584079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5a7e55bb207'
down_revision = '8aecee399bff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('reclamations', sa.Column('description', sa.String()))
    pass


def downgrade():
    pass
