"""add channel table

Revision ID: 33acd613eb6a
Revises: 1ba4762cd490
Create Date: 2023-04-11 19:11:13.332660

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "33acd613eb6a"
down_revision = "1ba4762cd490"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "channels",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("staff", sa.Boolean(), nullable=False),
        sa.Column("category", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category"], ["categories.id"], name="fk_channels_categories_id_category"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("channels")
    # ### end Alembic commands ###
