"""update table books

Revision ID: adecc0907956
Revises: ee57f9d6e930
Create Date: 2023-11-12 15:53:29.396386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adecc0907956'
down_revision: Union[str, None] = 'ee57f9d6e930'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author', sa.VARCHAR(), nullable=False))
    op.add_column('books', sa.Column('description', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'description')
    op.drop_column('books', 'author')
    # ### end Alembic commands ###
