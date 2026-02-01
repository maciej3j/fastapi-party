import datetime
from typing import Callable
from fastapi.testclient import TestClient
from sqlmodel import Session


def test_party_list_page_returns_list_of_future_parties(
        session: Session, client = TestClient, create_party: Callable[..., Party]
):
    today = datetime.date.today()
    valid_party = create_party(
        session=session, party_date=today + datetime.timedelta(days=1), venue="Venue 1"
    )
    create_party(session=session, party_date=today - datetime.timedelta(days=10), venue="Venue 2")
