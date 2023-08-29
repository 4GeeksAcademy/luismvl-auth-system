"""empty message

Revision ID: 6045ee99da6e
Revises: 3d904a858f95
Create Date: 2023-08-28 23:51:44.349691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6045ee99da6e'
down_revision = '3d904a858f95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
