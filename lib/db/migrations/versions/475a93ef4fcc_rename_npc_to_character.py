"""rename npc to character

Revision ID: 475a93ef4fcc
Revises: 84f846c6df78
Create Date: 2023-05-18 14:51:15.848080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475a93ef4fcc'
down_revision = '84f846c6df78'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('dialogue1', sa.String(), nullable=True),
    sa.Column('dialogue2', sa.String(), nullable=True),
    sa.Column('dialogue3', sa.String(), nullable=True),
    sa.Column('dialogue4', sa.String(), nullable=True),
    sa.Column('dialogue5', sa.String(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('alive', sa.Boolean(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name=op.f('fk_characters_location_id_locations')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('npcs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('npcs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('dialogue1', sa.VARCHAR(), nullable=True),
    sa.Column('dialogue2', sa.VARCHAR(), nullable=True),
    sa.Column('dialogue3', sa.VARCHAR(), nullable=True),
    sa.Column('dialogue4', sa.VARCHAR(), nullable=True),
    sa.Column('alive', sa.BOOLEAN(), nullable=True),
    sa.Column('location_id', sa.INTEGER(), nullable=True),
    sa.Column('completed', sa.BOOLEAN(), nullable=True),
    sa.Column('dialogue5', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name='fk_npcs_location_id_locations'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('characters')
    # ### end Alembic commands ###
