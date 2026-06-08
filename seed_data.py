import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mars_coffee_project.settings')
django.setup()

from cafe.models import Category, Menu

def seed():
    # Categories
    coffee, _ = Category.objects.get_or_create(name='Coffee')
    non_coffee, _ = Category.objects.get_or_create(name='Non-Coffee')
    food, _ = Category.objects.get_or_create(name='Food & Snacks')

    # Menu Items
    Menu.objects.get_or_create(
        name='Mars Espresso',
        category=coffee,
        price=25000,
        description='Double shot of our signature blend beans.',
        is_highlight=True
    )
    Menu.objects.get_or_create(
        name='Creamy Latte',
        category=coffee,
        price=32000,
        description='Smooth espresso with steamed milk and thin foam.',
        is_highlight=True
    )
    Menu.objects.get_or_create(
        name='Matcha Zen',
        category=non_coffee,
        price=35000,
        description='Premium Uji Matcha with fresh milk.',
        is_highlight=True
    )
    Menu.objects.get_or_create(
        name='Chocolate Lava Cake',
        category=food,
        price=38000,
        description='Warm chocolate cake with melting center.',
        is_highlight=False
    )
    Menu.objects.get_or_create(
        name='Truffle Fries',
        category=food,
        price=28000,
        description='Golden fries with truffle oil and parmesan.',
        is_highlight=False
    )

    print("Seed data created successfully.")

if __name__ == '__main__':
    seed()
