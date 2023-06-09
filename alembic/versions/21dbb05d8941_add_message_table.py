"""add message table

Revision ID: 21dbb05d8941
Revises: 57ad979c6250
Create Date: 2023-04-11 19:14:06.029116

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "21dbb05d8941"
down_revision = "57ad979c6250"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "messages",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=False),
        sa.Column("author", sa.BigInteger(), nullable=True),
        sa.Column("channel", sa.BigInteger(), nullable=True),
        sa.Column("thread", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author"], ["users.id"], name="fk_messages_users_id_author"
        ),
        sa.ForeignKeyConstraint(
            ["channel"], ["channels.id"], name="fk_messages_channels_id_channel"
        ),
        sa.ForeignKeyConstraint(
            ["thread"], ["threads.id"], name="fk_messages_threads_id_thread"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("messages")
    # ### end Alembic commands ###
