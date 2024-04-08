"""Create Users table

Revision ID: 8c68925930ce
Revises: 
Create Date: 2024-04-03 23:38:10.877484

"""

from typing import Sequence, Union

import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String

from app.models.user import Languages

# revision identifiers, used by Alembic.
revision: str = "8c68925930ce"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("username", sa.String(length=100), nullable=False),
        sa.Column(
            "language",
            sqlalchemy_utils.types.choice.ChoiceType(Languages, impl=String(length=2)),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###