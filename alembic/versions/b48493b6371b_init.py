"""init

Revision ID: b48493b6371b
Revises: 
Create Date: 2023-11-19 18:50:39.299059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b48493b6371b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=True, unique=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('notes', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime())
    )

    op.create_table(
        'note',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('body', sa.String, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime())
    )


def downgrade() -> None:
    op.drop_table('note')
    op.drop_table('user')
