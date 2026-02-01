from datetime import date, time
from decimal import Decimal
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel, Column, String, Text


class PartyBase(SQLModel):
    party_date: date
    party_time: time
    invitation: str = Field(sa_column=Column(Text), min_length=10)
    venue: str = Field(sa_column=Column(String(100)))


class Party(PartyBase, table=True):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True)
    gifts: list["Gift"] = Relationship(back_populates="party")
    guests: list["Guest"] = Relationship(back_populates="party")


class PartyForm(PartyBase):
    pass


class GiftBase(SQLModel):
    gift_name: str = Field(sa_column=Column(String(100)))
    price: Decimal = Field(decimal_places=2, ge=0)
    link: str | None
    party_id: UUID = Field(default=None, foreign_key="party.uuid")


class Gift(GiftBase, table=True):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True)
    party: Party = Relationship(back_populates="gifts")


class GiftForm(GiftBase):
    pass


class GuestBase(SQLModel):
    name: str = Field(sa_column=Column(String(100)))
    attending: bool = False
    party_id: UUID = Field(default=None, foreign_key="party.uuid")


class Guest(GuestBase, table=True):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True)
    party: Party = Relationship(back_populates="guests")


class GuestForm(GuestBase):
    pass
