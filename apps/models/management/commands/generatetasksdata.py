
from typing import Any
from random import choices, choice
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import QuerySet

from apps.models.models import Restaurant

class Command(BaseCommand):
    help = "Generate tasks data for testing purposes"
    
    EMAIL_DOMAINS = (
        "gmali.com",
        "mail.ru",
    )
    SOME_WORDS = (
        "lorem",
        "ipsum",
        "dolor",
        "sit",
        "amet",
        "consectetur",
        "adipiscing",
        "elit",
        "sed",
        "do",
        "eiusmod",
        "tempor",
        "incididunt",
        "ut",
        "labore",
        "et",
        "dolore",
        "magna",
        "aliqua",
    )
     
    def __generate_users(self,user_count:int = 20)->None:
        USER_PASSWORD = make_password(password="12345")
        created_users:list[User] = []
        users_before: int=User.objects.count()
        
        i:int
        for i in range(user_count):
            username:str = f"user{i+1}"
            email:str = f"user{i+1}@{choice(self.EMAIL_DOMAINS)}"
            created_users.append(
                User(
                    username = username,
                    email = email,
                    password = USER_PASSWORD
                )
            )
        User.objects.bulk_create(created_users,ignore_conflicts=True)
        users_after: int=User.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {users_after - users_before} users."
            )
        )
        
    def __generate_restaurant(self,rest_count:int = 20)->None:
        create_rest:list[Restaurant] = []
        rest_before: int = Restaurant.objects.count()
        
        i:int
        for i in range(rest_count):
            name = " ".join(choices(self.SOME_WORDS,k=7)).capitalize()
            description = " ".join(choices(self.SOME_WORDS,k=15)).capitalize()
            create_rest.append(
                Restaurant(
                    name = name,
                    description = description
                )
            )
        Restaurant.objects.bulk_create(create_rest,ignore_conflicts=True)
        rest_after: int = Restaurant.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f"Created{rest_after - rest_before} restaurant"
            )
        )


    def handle(self, *args: tuple[Any, ...], **kwargs: dict[str, Any])->None:
        start_time: datetime = datetime.now()
        
        self.__generate_users(user_count = 20)
        self.__generate_restaurant(rest_count=20)
        
        self.stdout.write(
                "The whole process to generate data took: {} seconds".format(
                    (datetime.now() - start_time).total_seconds()
                )
            )