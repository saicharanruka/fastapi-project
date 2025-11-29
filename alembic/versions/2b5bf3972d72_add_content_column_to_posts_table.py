"""add content column to posts table

Revision ID: 2b5bf3972d72
Revises: cf8f46882bdd
Create Date: 2025-11-29 12:46:08.537571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b5bf3972d72'
down_revision: Union[str, Sequence[str], None] = 'cf8f46882bdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
