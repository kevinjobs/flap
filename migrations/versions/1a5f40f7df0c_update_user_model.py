"""update User Model

Revision ID: 1a5f40f7df0c
Revises: 
Create Date: 2023-01-19 15:56:01.535326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a5f40f7df0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_users_name'), ['name'])
        batch_op.create_unique_constraint(batch_op.f('uq_users_uid'), ['uid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_users_uid'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_users_name'), type_='unique')

    # ### end Alembic commands ###
