"""create column content

Revision ID: 3e51772cde73
Revises: 46b32c27a5aa
Create Date: 2022-12-26 21:14:40.103379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e51772cde73'
down_revision = '46b32c27a5aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
