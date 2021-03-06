"""add subtopic column

Revision ID: 77095fa17d31
Revises: 06d87926c931
Create Date: 2020-05-18 21:19:20.545001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77095fa17d31'
down_revision = '06d87926c931'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('main_topic', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'main_topic')
    # ### end Alembic commands ###
