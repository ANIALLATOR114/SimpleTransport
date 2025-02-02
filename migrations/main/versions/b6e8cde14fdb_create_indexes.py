"""Create indexes

Revision ID: b6e8cde14fdb
Revises:
Create Date: 2023-11-09 23:55:03.391726

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b6e8cde14fdb"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_calendar_date_service_id"), "calendar_date", ["service_id"], unique=False)
    op.create_index(op.f("ix_route_agency_id"), "route", ["agency_id"], unique=False)
    op.create_index(op.f("ix_route_long_name"), "route", ["long_name"], unique=False)
    op.create_index(op.f("ix_route_short_name"), "route", ["short_name"], unique=False)
    op.create_index(op.f("ix_stop_time_stop_id"), "stop_time", ["stop_id"], unique=False)
    op.create_index(op.f("ix_stop_time_trip_id"), "stop_time", ["trip_id"], unique=False)
    op.create_index(op.f("ix_trip_route_id"), "trip", ["route_id"], unique=False)
    op.create_index(op.f("ix_trip_service_id"), "trip", ["service_id"], unique=False)
    op.create_index(op.f("ix_trip_shape_id"), "trip", ["shape_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_trip_shape_id"), table_name="trip")
    op.drop_index(op.f("ix_trip_service_id"), table_name="trip")
    op.drop_index(op.f("ix_trip_route_id"), table_name="trip")
    op.drop_index(op.f("ix_stop_time_trip_id"), table_name="stop_time")
    op.drop_index(op.f("ix_stop_time_stop_id"), table_name="stop_time")
    op.drop_index(op.f("ix_route_short_name"), table_name="route")
    op.drop_index(op.f("ix_route_long_name"), table_name="route")
    op.drop_index(op.f("ix_route_agency_id"), table_name="route")
    op.drop_index(op.f("ix_calendar_date_service_id"), table_name="calendar_date")
    # ### end Alembic commands ###
