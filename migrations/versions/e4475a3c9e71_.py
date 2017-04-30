"""empty message

Revision ID: e4475a3c9e71
Revises: 122acf4ca311
Create Date: 2016-03-30 15:42:02.962616

"""

# revision identifiers, used by Alembic.
revision = 'e4475a3c9e71'
down_revision = '122acf4ca311'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wishes', 'status')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wishes', sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    ### end Alembic commands ###