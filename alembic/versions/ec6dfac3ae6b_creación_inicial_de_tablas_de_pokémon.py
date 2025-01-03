"""Creación inicial de tablas de Pokémon

Revision ID: ec6dfac3ae6b
Revises: 
Create Date: 2024-11-12 18:07:40.555073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec6dfac3ae6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_abilities_id'), 'abilities', ['id'], unique=False)
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pokemon_id'), 'pokemon', ['id'], unique=False)
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_id'), 'type', ['id'], unique=False)
    op.create_table('weakness',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weakness_id'), 'weakness', ['id'], unique=False)
    op.create_table('pokemon_type',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], ),
    sa.PrimaryKeyConstraint('pokemon_id', 'type_id')
    )
    op.create_table('pokemon_weakness',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('weakness_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['weakness_id'], ['weakness.id'], ),
    sa.PrimaryKeyConstraint('pokemon_id', 'weakness_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon_weakness')
    op.drop_table('pokemon_type')
    op.drop_index(op.f('ix_weakness_id'), table_name='weakness')
    op.drop_table('weakness')
    op.drop_index(op.f('ix_type_id'), table_name='type')
    op.drop_table('type')
    op.drop_index(op.f('ix_pokemon_id'), table_name='pokemon')
    op.drop_table('pokemon')
    op.drop_index(op.f('ix_abilities_id'), table_name='abilities')
    op.drop_table('abilities')
    # ### end Alembic commands ###
