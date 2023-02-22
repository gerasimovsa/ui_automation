from data.data import Person
from faker import Faker
import random

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(18, 100),
        salary=random.randint(5000, 20000),
        department=faker_en.job()
    )
