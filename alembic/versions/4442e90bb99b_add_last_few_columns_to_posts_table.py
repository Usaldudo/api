"""add last few columns to posts table

Revision ID: 4442e90bb99b
Revises: 5bf5e44783b7
Create Date: 2023-03-06 23:10:02.816027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4442e90bb99b'
down_revision = '5bf5e44783b7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE "),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),)


def downgrade():
    op.delete_column("posts", "published")
    op.delete_column("posts", "created_at")
