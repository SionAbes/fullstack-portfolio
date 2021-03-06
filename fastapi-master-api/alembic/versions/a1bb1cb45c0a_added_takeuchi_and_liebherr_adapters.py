"""added takeuchi and liebherr adapters

Revision ID: a1bb1cb45c0a
Revises: c9f78a7d00ab
Create Date: 2022-01-31 23:39:40.540879

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a1bb1cb45c0a"
down_revision = "c9f78a7d00ab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "adapter_liebherr_lidat",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("password", sa.Text(), nullable=False),
        sa.Column("username", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adapters.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "adapter_takeuchi_tfm",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token_url", sa.Text(), nullable=False),
        sa.Column("client_id", sa.Text(), nullable=False),
        sa.Column("client_secret", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adapters.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("adapter_takeuchi_tfm")
    op.drop_table("adapter_liebherr_lidat")
    # ### end Alembic commands ###
