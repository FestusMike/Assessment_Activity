import factory
from faker import Faker

from users.models import UserAccount

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccount

    email = factory.LazyAttribute(lambda _: fake.unique.email())
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = factory.Faker("random_int", min=18, max=80)


