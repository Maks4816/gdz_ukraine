"""add specification column

Revision ID: 67170eb02e22
Revises: f66ad1856095
Create Date: 2020-05-11 14:21:35.259733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67170eb02e22'
down_revision = 'f66ad1856095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('specification', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'specification')
    # ### end Alembic commands ###