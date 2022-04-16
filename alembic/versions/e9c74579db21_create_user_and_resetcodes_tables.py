"""Create User and ResetCodes Tables

Revision ID: e9c74579db21
Revises: 
Create Date: 2022-03-12 16:52:00.492217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c74579db21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
                    sa.Column('is_confirmed', sa.Boolean(), nullable=False, server_default='false'),
                    sa.Column('creation_date', sa.DateTime,
                              server_default=sa.text("(now() at time zone 'utc')"), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )

    op.create_table('reset_codes',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('reset_code', sa.String(), nullable=False),
                    sa.Column('status', sa.String(1), nullable=False),
                    sa.Column('expired_in', sa.DateTime,
                              server_default=sa.text("(now() at time zone 'utc')"), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade():
    pass
