"""Add is_main column to promotion_images

Revision ID: 8b2ad962e3ee
Revises: c4e547fea349
Create Date: 2025-02-26 18:47:33.363311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b2ad962e3ee'
down_revision = 'c4e547fea349'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('branches', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'cities', ['city_id'], ['id'])
        batch_op.create_foreign_key(None, 'countries', ['country_id'], ['id'])

    with op.batch_alter_table('promotion_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_main', sa.Boolean(), nullable=True))

    with op.batch_alter_table('tourist_points', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'countries', ['country_id'], ['id'])
        batch_op.create_foreign_key(None, 'cities', ['city_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tourist_points', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('promotion_images', schema=None) as batch_op:
        batch_op.drop_column('is_main')

    with op.batch_alter_table('branches', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
