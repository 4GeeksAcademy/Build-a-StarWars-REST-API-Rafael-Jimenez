"""empty message

Revision ID: 193fe7863f29
Revises: 687b17275ed1
Create Date: 2023-07-25 09:40:27.642771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '193fe7863f29'
down_revision = '687b17275ed1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('People',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('FavPeople',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['people_id'], ['People.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('FavPlanet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPlanet', sa.Integer(), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idPlanet'], ['Planet.id'], ),
    sa.ForeignKeyConstraint(['idUser'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('FavPlanet')
    op.drop_table('FavPeople')
    op.drop_table('User')
    op.drop_table('Planet')
    op.drop_table('People')
    # ### end Alembic commands ###
