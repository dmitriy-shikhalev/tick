from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass
from sqlalchemy.orm import relationship

from .status import Status


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


class Input(Base):
    __tablename__ = "input"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    key: Mapped[str] = mapped_column()
    value: Mapped[str] = mapped_column()
    request_id: Mapped[int] = mapped_column(ForeignKey("request.id"), nullable=True)
    request: Mapped["Request"] = relationship(back_populates="inputs")


class Output(Base):
    __tablename__ = "output"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    key: Mapped[str] = mapped_column()
    value: Mapped[str] = mapped_column()
    request_id: Mapped[int] = mapped_column(ForeignKey("request.id"), nullable=True)
    request: Mapped["Request"] = relationship(back_populates="outputs")


class Request(Base):
    __tablename__ = "request"

    id: Mapped[int] = mapped_column(primary_key=True)
    inputs: Mapped[list[Input]] = relationship(back_populates="request")
    outputs: Mapped[list[Output]] = relationship(back_populates="request")
    status: Mapped[Status] = mapped_column(default=Status.PENDING)
