"""added a machines table for aemp

Revision ID: 823a2ed817ac
Revises: a1bb1cb45c0a
Create Date: 2022-03-19 11:30:57.952137

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "823a2ed817ac"
down_revision = "a1bb1cb45c0a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "machines",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("unit_installed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("oem_name", sa.Text(), nullable=False),
        sa.Column("model", sa.Text(), nullable=True),
        sa.Column("make", sa.Text(), nullable=True),
        sa.Column("equipment_id", sa.Text(), nullable=True),
        sa.Column("serial_number", sa.Text(), nullable=True),
        sa.Column("pin", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], initially="DEFERRED", deferrable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_machines_user_id"), "machines", ["user_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_machines_user_id"), table_name="machines")
    op.drop_table("machines")
    # ### end Alembic commands ###
