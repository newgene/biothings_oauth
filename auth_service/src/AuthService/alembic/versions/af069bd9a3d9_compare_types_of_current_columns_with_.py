"""Compare types of current columns with updates

Revision ID: af069bd9a3d9
Revises: 2af962ae9684
Create Date: 2021-02-18 06:28:18.681427+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af069bd9a3d9'
down_revision = '2af962ae9684'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'identity_provider_user_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('users', 'identity_provider_user_id',
               existing_type=sa.String(length=255),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
