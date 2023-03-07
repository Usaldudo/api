"""add content column to posts table

Revision ID: 3728f9d924d5
Revises: 8774d6333c0b
Create Date: 2023-03-06 18:18:04.447686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3728f9d924d5'
down_revision = '8774d6333c0b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
