"""first migration

Revision ID: f13f8ad416ef
Revises: 
Create Date: 2023-05-17 11:37:28.787120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f13f8ad416ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('look', sa.String(), nullable=True),
    sa.Column('up', sa.String(), nullable=True),
    sa.Column('down', sa.String(), nullable=True),
    sa.Column('left', sa.String(), nullable=True),
    sa.Column('right', sa.String(), nullable=True),
    sa.Column('outside', sa.String(), nullable=True),
    sa.Column('inside', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name=op.f('fk_items_location_id_locations')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('dead', sa.Boolean(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name=op.f('fk_players_location_id_locations')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_player_items_item_id_items')),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], name=op.f('fk_player_items_player_id_players')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_items')
    op.drop_table('players')
    op.drop_table('items')
    op.drop_table('locations')
    # ### end Alembic commands ###
