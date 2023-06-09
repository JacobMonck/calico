"""make thread created_at nullable

Revision ID: 83f1945c25f2
Revises: 21dbb05d8941
Create Date: 2023-04-11 20:47:54.634101

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "83f1945c25f2"
down_revision = "21dbb05d8941"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "threads", "created_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "threads", "created_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    # ### end Alembic commands ###
