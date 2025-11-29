"""create posts table

Revision ID: cf8f46882bdd
Revises: 
Create Date: 2025-11-28 21:07:52.546763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf8f46882bdd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts', sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
