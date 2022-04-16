"""Add Confirmation codes table

Revision ID: 2fc7898538a1
Revises: e9c74579db21
Create Date: 2022-03-18 12:47:32.490966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fc7898538a1'
down_revision = 'e9c74579db21'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('confirmation_codes',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('confirmation_code', sa.String(), nullable=False),
                    sa.Column('status', sa.String(1), nullable=False),
                    sa.Column('created_on', sa.DateTime,
                              server_default=sa.text("(now() at time zone 'utc')"), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    pass
