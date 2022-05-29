"""Added Departments

Revision ID: 2cb802a768fd
Revises: 619b93b8cead
Create Date: 2022-05-29 16:10:01.262376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cb802a768fd'
down_revision = '619b93b8cead'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    departments_table = op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
    op.bulk_insert(departments_table,
    [
        {'id':1, 'name':'Web'},
        {'id':2, 'name':'Data Analytics'},
        {'id':3, 'name':'AI'},
        {'id':4, 'name':'Cloud DevOps'}

    ])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('departments')
    # ### end Alembic commands ###
