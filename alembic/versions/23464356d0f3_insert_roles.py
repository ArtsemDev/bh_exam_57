"""insert roles

Revision ID: 23464356d0f3
Revises: f127e66f699b
Create Date: 2022-08-08 13:13:34.902738

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import create_sync_session, Role


# revision identifiers, used by Alembic.
revision = '23464356d0f3'
down_revision = 'f127e66f699b'
branch_labels = None
depends_on = None

roles = ['user', 'admin', 'support']


@create_sync_session
def upgrade(session: Session = None) -> None:
    for role in roles:
        role = Role(name=role)
        session.add(role)
        try:
            session.commit()
        except IntegrityError:
            pass


@create_sync_session
def downgrade(session: Session = None) -> None:
    for role in roles:
        session.execute(
            sa.delete(Role)
            .where(Role.name == role)
        )
        session.commit()
