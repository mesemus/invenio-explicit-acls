#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""PropertyValueACL."""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
from invenio_explicit_acls.acls.propertyvalue_acls import MatchOperation

revision = '21ab0d49a6ca'
down_revision = 'e1f135387190'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('explicit_acls_propertyvalueacl',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('property_name', sa.String(length=64), nullable=True),
    sa.Column('property_value', sa.String(length=128), nullable=True),
    sa.Column('match_operation', sqlalchemy_utils.types.choice.ChoiceType(MatchOperation, impl=sa.String(length=10)), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['explicit_acls_acl.id'], name=op.f('fk_explicit_acls_propertyvalueacl_id_explicit_acls_acl')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_explicit_acls_propertyvalueacl'))
    )
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('explicit_acls_propertyvalueacl')
    # ### end Alembic commands ###
