"""empty message

Revision ID: 1da9b8577dab
Revises: 277adea76bdf
Create Date: 2022-05-20 00:44:48.078029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1da9b8577dab'
down_revision = '277adea76bdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=30), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('date_of_comment', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('comments')
    # ### end Alembic commands ###
