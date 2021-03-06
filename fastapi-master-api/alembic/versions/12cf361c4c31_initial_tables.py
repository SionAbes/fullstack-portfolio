"""Initial tables

Revision ID: 12cf361c4c31
Revises: 
Create Date: 2021-12-23 11:52:22.814141

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "12cf361c4c31"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("last_login", sa.DateTime(timezone=True), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("first_name", sa.String(length=150), nullable=False),
        sa.Column("last_name", sa.String(length=150), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###
