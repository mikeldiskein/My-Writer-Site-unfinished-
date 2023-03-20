"""init

Revision ID: b760176e79b2
Revises: 
Create Date: 2023-03-20 15:56:41.819917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b760176e79b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('avg_rating', sa.Float(), nullable=True))
    op.drop_constraint('books_author_id_fkey', 'books', type_='foreignkey')
    op.create_foreign_key(None, 'books', 'authors', ['author_id'], ['id'])
    op.add_column('comments', sa.Column('author', sa.String(), nullable=True))
    op.drop_constraint('comments_author_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_book_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'books', ['book_id'], ['id'])
    op.drop_column('comments', 'author_id')
    op.drop_constraint('downloads_book_id_fkey', 'downloads', type_='foreignkey')
    op.create_foreign_key(None, 'downloads', 'books', ['book_id'], ['id'])
    op.drop_column('downloads', 'ip_address')
    op.add_column('ratings', sa.Column('comment', sa.Text(), nullable=True))
    op.add_column('ratings', sa.Column('avg_rating', sa.Float(), nullable=True))
    op.drop_constraint('ratings_book_id_fkey', 'ratings', type_='foreignkey')
    op.drop_constraint('ratings_user_id_fkey', 'ratings', type_='foreignkey')
    op.create_foreign_key(None, 'ratings', 'users', ['user_id'], ['id'])
    op.drop_column('ratings', 'book_id')
    op.add_column('users', sa.Column('comments_by_user', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'comments_by_user')
    op.add_column('ratings', sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'ratings', type_='foreignkey')
    op.create_foreign_key('ratings_user_id_fkey', 'ratings', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('ratings_book_id_fkey', 'ratings', 'books', ['book_id'], ['id'], ondelete='CASCADE')
    op.drop_column('ratings', 'avg_rating')
    op.drop_column('ratings', 'comment')
    op.add_column('downloads', sa.Column('ip_address', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'downloads', type_='foreignkey')
    op.create_foreign_key('downloads_book_id_fkey', 'downloads', 'books', ['book_id'], ['id'], ondelete='CASCADE')
    op.add_column('comments', sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_book_id_fkey', 'comments', 'books', ['book_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('comments_author_id_fkey', 'comments', 'users', ['author_id'], ['id'], ondelete='CASCADE')
    op.drop_column('comments', 'author')
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.create_foreign_key('books_author_id_fkey', 'books', 'authors', ['author_id'], ['id'], ondelete='CASCADE')
    op.drop_column('books', 'avg_rating')
    # ### end Alembic commands ###
