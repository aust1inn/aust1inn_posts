"""Initial Migration

Revision ID: 8cc6ae2cd5cd
Revises: 7852a6ecd881
Create Date: 2022-05-14 14:21:20.513116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cc6ae2cd5cd'
down_revision = '7852a6ecd881'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=60), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###