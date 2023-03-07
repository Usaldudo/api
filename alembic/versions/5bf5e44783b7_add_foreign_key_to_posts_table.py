"""add foreign-key to posts table

Revision ID: 5bf5e44783b7
Revises: 1e67935dddaa
Create Date: 2023-03-06 23:04:06.226617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bf5e44783b7'
down_revision = '1e67935dddaa'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users",local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_table("posts", "owner_id")
