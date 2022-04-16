"""Create Reclamations table

Revision ID: 8aecee399bff
Revises: 2fc7898538a1
Create Date: 2022-03-19 17:11:52.954004

"""
from alembic import op
import sqlalchemy as sa

from app.models.Enums.reclamationStatus import ReclamationStatus


# revision identifiers, used by Alembic.
revision = '8aecee399bff'
down_revision = '2fc7898538a1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('reclamations',
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('longitude', sa.Float(), nullable=False),
                sa.Column('latitude', sa.Float(), nullable=False),
                sa.Column('photo_url', sa.String(), nullable=False),
                sa.Column('reclamation_status', sa.Enum(ReclamationStatus), nullable=False, server_default=ReclamationStatus.pending),
                sa.Column('creation_date', sa.DateTime,
                server_default=sa.text("(now() at time zone 'utc')"), nullable=False),
                sa.Column('owner_id', sa.Integer(), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.ForeignKeyConstraint(['owner_id'], ['users.id'], )
            )
    pass


def downgrade():
    pass
