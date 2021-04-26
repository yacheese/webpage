"""add language to posts

Revision ID: 75feabe2b995
Revises: 57af3ce77539
Create Date: 2021-04-20 19:47:45.630374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75feabe2b995'
down_revision = '57af3ce77539'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###