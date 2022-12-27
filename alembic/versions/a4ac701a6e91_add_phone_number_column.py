"""add phone_number column

Revision ID: a4ac701a6e91
Revises: e19283638a82
Create Date: 2022-12-27 09:51:53.680554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4ac701a6e91'
down_revision = 'e19283638a82'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
