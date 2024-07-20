from app.posts.infrastructure.database import Base

from sqlalchemy.orm import Mapped, mapped_column


class Posts(Base):
    __tablename__ = 'Posts'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    text: Mapped[str] = mapped_column(nullable=False, index=True)
