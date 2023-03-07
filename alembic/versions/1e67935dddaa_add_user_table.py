"""add user table

Revision ID: 1e67935dddaa
Revises: 3728f9d924d5
Create Date: 2023-03-06 19:29:14.437422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e67935dddaa'
down_revision = '3728f9d924d5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )


def downgrade():
    op.drop_table("users")
