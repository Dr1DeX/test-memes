from app.infrastructure.database import Base

from sqlalchemy.orm import Mapped, mapped_column


class Posts(Base):
    __tablename__ = 'Posts'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
