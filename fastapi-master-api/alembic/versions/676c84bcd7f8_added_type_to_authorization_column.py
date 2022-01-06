"""added type to authorization column

Revision ID: 676c84bcd7f8
Revises: a6a21dfb20ab
Create Date: 2022-01-06 11:57:16.164723

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "676c84bcd7f8"
down_revision = "a6a21dfb20ab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "adapters", sa.Column("authorization_type", sa.Text(), nullable=False)
    )
    op.drop_column("adapters", "authorization")
    op.add_column(
        "authorization_bearer_token",
        sa.Column("bearer_token", sa.Text(), nullable=False),
    )
    op.drop_column("authorization_bearer_token", "token")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "authorization_bearer_token",
        sa.Column("token", sa.TEXT(), autoincrement=False, nullable=False),
    )
    op.drop_column("authorization_bearer_token", "bearer_token")
    op.add_column(
        "adapters",
        sa.Column("authorization", sa.TEXT(), autoincrement=False, nullable=False),
    )
    op.drop_column("adapters", "authorization_type")
    # ### end Alembic commands ###