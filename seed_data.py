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

    # Menu Items - Coffee
    Menu.objects.get_or_create(
        name='Mars Latte Art',
        category=coffee,
        price=25000,
        description='Diracik dengan ketelitian, dituangkan dengan rasa. Setiap cangkir menghadirkan kehangatan yang tak sekadar dinikmati.',
        is_highlight=True
    )
    Menu.objects.get_or_create(
        name='Frozen Caramel Vanilla',
        category=coffee,
        price=32000,
        description='Dinginnya memikat, manisnya elegan. Nikmati momen sederhana dengan rasa istimewa dari Frozen Caramel Vanilla.',
        is_highlight=True
    )

    # Menu Items - Non-Coffee
    Menu.objects.get_or_create(
        name='Pink Candy',
        category=non_coffee,
        price=35000,
        description='Elegan dalam rasa, lembut dalam setiap lapisan. Memberikan kenyamanan yang membuat hari terasa lebih istimewa.',
        is_highlight=True
    )
    Menu.objects.get_or_create(
        name='mojito green apple',
        category=non_coffee,
        price=34000,
        description='Sip slow, feel fresh. Let the chill run through your day, one sip at a time.',
        is_highlight=False
    )
    Menu.objects.get_or_create(
        name='Teh Telang Sereh',
        category=non_coffee,
        price=10000,
        description='Minuman herbal kaya manfaat yang memadukan bunga telang dengan sereh aroma wangi dan efek relaksasi.',
        is_highlight=False
    )

    # Menu Items - Food
    Menu.objects.get_or_create(
        name='Chicken Ramen',
        category=food,
        price=38000,
        description='Ramen ayam dengan kuah kaldu gurih, mi kenyal, dan topping telur serta sayuran segar.',
        is_highlight=False
    )
    Menu.objects.get_or_create(
        name='Rawon Sapi',
        category=food,
        price=28000,
        description='Daging sapi empuk dengan kuah hitam kluwek khas Jawa Timur yang kaya rempah.',
        is_highlight=False
    )
    Menu.objects.get_or_create(
        name='Nasi Iga Sambal Ijo',
        category=food,
        price=68000,
        description='Nasi Hangat dengan Perpaduan Iga yang Di Siram Dengan Sambal Cabai Hijau Yang menyegarkan.',
        is_highlight=True
    )

    print("Seed data updated successfully with items from screenshot.")

if __name__ == '__main__':
    seed()
