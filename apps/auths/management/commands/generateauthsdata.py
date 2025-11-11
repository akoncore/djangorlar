from random import choice,choices,randint
from typing import Any

#django modules
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from apps.auths.models import CustomUser


class Command(BaseCommand):
    
    EMAIL_DOMAINS = (
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "aol.com",
        "msn.com",
        "comcast.net",
        "live.com",
        "rediffmail.com",
        "outlook.com",
        "icloud.com",
    )
    CITY =(
        "Almaty",
        "Nur-Sultan",
        "Shymkent",
        "Karaganda",
        "Aktobe",
        "Taraz",
    )
    DEPARTAMENTS =(
        "HR",
        "Sales",
        "IT",
        "Marketing",
    )
    ROLES =(
        "admin",
        "manager",
        "employee",       
    )
    COUNTRY =(
        "Kazakhstan",
        "USA",
        "Russia",
        "Germany",
        "France",
    )
    
    
    def __generate_users(self,user_count:int = 2000)->None:
        USER_PASSWORD = make_password(password="12345")
        created_users:list[CustomUser] = []
        users_before: int=CustomUser.objects.count()
        
        i:int
        for i in range(user_count):
            first_name:str = f"FirstName{i+1}"
            last_name:str = f"LastName{i+1}"
            full_name:str = f"{first_name} {last_name}"
            email:str = f"user{i+1}@{choice(self.EMAIL_DOMAINS)}"
            city:str = choice(self.CITY)
            country:str = choice(self.COUNTRY)
            department:str = choice(self.DEPARTAMENTS)
            role:str = choice(self.ROLES)
            birth_date:datetime = datetime(
                year=randint(1970,2005),
                month=randint(1,12),
                day=randint(1,28)
            )
            salary:float = float(randint(50000,200000))
            is_active:bool = True
            is_staff:bool = role in ['admin','manager']
            is_superuser:bool = role == 'admin'
            date_joined:datetime = datetime.now()
            created_users.append(
                CustomUser(
                    email = email,
                    first_name=first_name,
                    full_name=full_name,
                    last_name=last_name,
                    city=city,
                    country=country,
                    department=department,
                    role=role,
                    salary=salary,
                    birth_date=birth_date,
                    password = USER_PASSWORD,
                    is_active=is_active,
                    is_staff=is_staff,
                    is_superuser=is_superuser,
                    date_joined=date_joined
                )
            )
        CustomUser.objects.bulk_create(created_users,ignore_conflicts=True)
        users_after: int=CustomUser.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {users_after - users_before} users."
            )
        )
    def handle(self, *args:tuple[Any,...], **kwargs:dict[str,Any])->None:
        start_time: datetime = datetime.now()
        self.__generate_users(user_count = 2000)
        self.stdout.write(
            self.style.SUCCESS(
                f"User data generation completed in {datetime.now() - start_time}."
            )
        )