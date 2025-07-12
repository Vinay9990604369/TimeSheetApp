from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_default_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('core', 'UserProfile')
    
    # Create admin user if not exists
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'password': make_password('adminpass123'),  # Change password here
            'is_staff': True,
            'is_superuser': True,
        }
    )
    if created:
        UserProfile.objects.create(user=admin_user, role='admin')

    # Create consultant user if not exists
    consultant_user, created = User.objects.get_or_create(
        username='consultant',
        defaults={
            'email': 'consultant@example.com',
            'password': make_password('consultantpass123'),  # Change password here
            'is_staff': False,
            'is_superuser': False,
        }
    )
    if created:
        UserProfile.objects.create(user=consultant_user, role='consultant')

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),  # replace with your last migration file
        ('auth', '0012_alter_user_first_name_max_length'),  # or appropriate auth migration dependency
    ]

    operations = [
        migrations.RunPython(create_default_users),
    ]
