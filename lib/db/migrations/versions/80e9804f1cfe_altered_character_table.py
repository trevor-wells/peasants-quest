"""altered character table

Revision ID: 80e9804f1cfe
Revises: 1fec25e79abc
Create Date: 2023-05-19 12:50:47.019826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80e9804f1cfe'
down_revision = '1fec25e79abc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'description')
    # ### end Alembic commands ###