from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name='Enquiry',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('name', models.CharField(max_length=160)),
            ('organisation', models.CharField(blank=True, max_length=200)),
            ('email', models.EmailField(max_length=254)),
            ('phone', models.CharField(blank=True, max_length=40)),
            ('topic', models.CharField(blank=True, max_length=180)),
            ('message', models.TextField()),
            ('created_at', models.DateTimeField(auto_now_add=True)),
        ],
        options={'ordering':['-created_at']},
    )]
