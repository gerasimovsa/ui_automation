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


def generate_text_file() -> str:
    dummy_data = faker_en.word()
    dummy_filename = faker_en.file_name(category='text', extension='txt')
    path = rf'C:\Users\Sergey_Gerasimov\PycharmProjects\ui_automation\{random.randint(0, 999)}_{dummy_filename}'
    file = open(path, 'w+')
    file.write(dummy_data)
    file.close()
    return path


def generate_path(cat: str, extension: str) -> str:
    dummy_filename = faker_en.file_name(category=cat, extension=extension)
    path = rf'C:\Users\Sergey_Gerasimov\PycharmProjects\ui_automation\{random.randint(0, 999)}_{dummy_filename}'
    return path
