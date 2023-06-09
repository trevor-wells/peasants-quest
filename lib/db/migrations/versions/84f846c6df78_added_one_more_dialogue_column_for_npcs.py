"""added one more dialogue column for npcs

Revision ID: 84f846c6df78
Revises: e837c481cf60
Create Date: 2023-05-18 11:50:08.309414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84f846c6df78'
down_revision = 'e837c481cf60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('npcs', sa.Column('dialogue5', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('npcs', 'dialogue5')
    # ### end Alembic commands ###
