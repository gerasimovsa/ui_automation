from base.utils import Utils
from data.data import Person, Date
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
        department=faker_en.job(),
        phone_number=faker_en.msisdn()
    )


def generate_file(cat: str, extension: str) -> str:
    dummy_data = faker_en.word()
    dummy_filename = faker_en.file_name(category=cat, extension=extension)
    path = rf'C:\Users\Sergey_Gerasimov\PycharmProjects\ui_automation\{random.randint(0, 999)}_{dummy_filename}'
    file = open(path, 'w+')
    file.write(dummy_data)
    file.close()
    return path


def generate_path(cat: str, extension: str) -> str:
    dummy_filename = faker_en.file_name(category=cat, extension=extension)
    path = rf'C:\Users\Sergey_Gerasimov\PycharmProjects\ui_automation\{random.randint(0, 999)}_{dummy_filename}'
    return path


def generate_subject() -> str:  # try to implement via the dataclass
    subjects_list = [
        "Hindi",
        "English",
        "Maths",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Commerce",
        "Accounting",
        "Economics",
        "Arts",
        "Social Studies",
        "History",
        "Civics"
    ]
    return subjects_list[random.randint(0, len(subjects_list) - 1)]


def generate_date() -> str:
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=Utils.random_15_minutes_interval_time()
    )
