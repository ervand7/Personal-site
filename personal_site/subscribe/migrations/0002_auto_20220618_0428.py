# Generated by Django 3.2 on 2022-06-18 04:28
import os

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [] if os.environ.get('GITLAB_CI_ENABLED') else [
        migrations.RunSQL("""
        CREATE FUNCTION fill_subscription_end() RETURNS trigger AS $fill_subscription_end$
            BEGIN
                NEW.end := current_timestamp + interval '1 year';
                RETURN NEW;
            END;
        $fill_subscription_end$ LANGUAGE plpgsql;
        
        CREATE TRIGGER fill_subscription_end BEFORE INSERT OR UPDATE ON subscribe_subscription
            FOR EACH ROW EXECUTE PROCEDURE fill_subscription_end();
        """)
    ]
