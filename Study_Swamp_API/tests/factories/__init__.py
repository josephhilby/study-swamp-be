import datetime
import factory
import random
from faker import Faker
from Study_Swamp_API.models import *
from django.utils import timezone

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.user_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    is_active = True
    is_superuser = False

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted or "password"
        self.set_password(password)
        if create:
            self.save()


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    building = factory.LazyAttribute(lambda x: faker.company()[:50])
    room = factory.LazyAttribute(lambda x: faker.bothify('Room ###'))
    latitude = factory.LazyAttribute(lambda x: faker.latitude())
    longitude = factory.LazyAttribute(lambda x: faker.longitude())


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.LazyAttribute(lambda x: faker.catch_phrase()[:50])
    department = factory.LazyAttribute(lambda x: random.choice(['MAS','CEN','COP']))
    class_number = factory.LazyAttribute(lambda x: faker.random_int(1000, 5999))


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Member

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
    creator = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=25))
    editor = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=50))


class MeetingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meeting

    group = factory.SubFactory(GroupFactory)
    location = factory.SubFactory(LocationFactory)
    name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5)[:50])
    start_time = factory.LazyAttribute(
        lambda x: timezone.make_aware(faker.date_time_this_month())
    )
    end_time = factory.LazyAttribute(
        lambda x: x.start_time + datetime.timedelta(hours=1)
    )


class AttendeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendee

    user = factory.SubFactory(UserFactory)
    meeting = factory.SubFactory(MeetingFactory)
    rsvp_type = factory.LazyAttribute(lambda x: random.choice([0,1,2]))
    checked_in = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=50))
    creator = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=25))
    editor = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=50))


class AwardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Award

    user = factory.SubFactory(UserFactory)
    badge_type = factory.LazyAttribute(lambda x: random.choice([0, 1, 2, 3, 4, 5]))


class MeetingCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MeetingComment

    user = factory.SubFactory(UserFactory)
    meeting = factory.SubFactory(MeetingFactory)
    text = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))


class GroupCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupComment

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
    text = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))
