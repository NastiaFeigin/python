"""First migration

Revision ID: 72a6c1dc4fa3
Revises: 
Create Date: 2023-06-29 10:34:00.340685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a6c1dc4fa3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('info', sa.String(length=300), nullable=False),
    sa.Column('address', sa.String(length=99), nullable=False),
    sa.Column('price_level', sa.String(length=30), nullable=False),
    sa.Column('kitchen_type', sa.String(length=99), nullable=False),
    sa.Column('happy_hour', sa.String(length=99), nullable=False),
    sa.Column('style', sa.String(length=99), nullable=False),
    sa.Column('opening_hours', sa.String(length=300), nullable=False),
    sa.Column('site', sa.String(length=300), nullable=False),
    sa.Column('wolt_review', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('restaurants')
    # ### end Alembic commands ###
