import factory
from faker import Factory as FakerFactory
from Study_Swamp_API.models import *

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    first_name = factory.LazyAttribute(lambda x: faker.name())
    last_name = factory.LazyAttribute(lambda x: faker.name())
    username = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())
    is_active = True
    is_superuser = False

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted or "password"
        self.set_password(password)
        if create:
            self.save()
