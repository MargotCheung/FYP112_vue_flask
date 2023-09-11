"""empty message

Revision ID: 279e61a61e51
Revises: af4c429a195c
Create Date: 2023-09-08 10:02:24.744205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '279e61a61e51'
down_revision = 'af4c429a195c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('index', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('comment_index', sa.Integer(), nullable=True),
    sa.Column('liked_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user_profile.id'], ),
    sa.ForeignKeyConstraint(['comment_index'], ['lesson_response.index'], ),
    sa.PrimaryKeyConstraint('index')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###
