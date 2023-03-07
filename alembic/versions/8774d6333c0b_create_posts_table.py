"""create posts table

Revision ID: 8774d6333c0b
Revises: 
Create Date: 2023-03-06 16:06:01.113394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8774d6333c0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
