import factory
from faker import Faker
from app.posts.models import Posts

faker = Faker()


class FakePostsFactory(factory.Factory):
    class Meta:
        model = Posts

    id: int = factory.LazyFunction(lambda: faker.random_int())
    text: str = factory.LazyFunction(lambda: faker.text())
    image_url: str = factory.LazyFunction(lambda: faker.image_url())

    def __repr__(self):
        return f'Post({self.id}, text={self.text}, image_url={self.image_url})'
