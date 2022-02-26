# Generated by Django 4.0.2 on 2022-02-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('stripe_price_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='stripecustomer',
            old_name='stripeCustomerId',
            new_name='stripe_customer_id',
        ),
        migrations.RenameField(
            model_name='stripecustomer',
            old_name='stripeSubscriptionId',
            new_name='stripe_subscription_id',
        ),
    ]