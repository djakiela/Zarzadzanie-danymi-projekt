"""Add password_hash to User

Revision ID: 4f1d5c0a01bc
Revises: 280c009dd656
Create Date: 2024-06-09 22:24:29.050770

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4f1d5c0a01bc'
down_revision = '280c009dd656'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ride', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DATE(),
               type_=sa.String(length=10),
               existing_nullable=False)
        batch_op.alter_column('time',
               existing_type=postgresql.TIME(),
               type_=sa.String(length=5),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=False))
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.drop_index('ix_user_email')
        batch_op.drop_index('ix_user_username')
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('ix_user_username', ['username'], unique=True)
        batch_op.create_index('ix_user_email', ['email'], unique=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
        batch_op.drop_column('password_hash')

    with op.batch_alter_table('ride', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=sa.String(length=5),
               type_=postgresql.TIME(),
               existing_nullable=False)
        batch_op.alter_column('date',
               existing_type=sa.String(length=10),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###