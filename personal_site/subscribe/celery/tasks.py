from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from subscribe.celery.config import app
from subscribe.models import Subscription


@app.task(bind=True)
def send_welcome(task, email, username):
    send_mail(
        subject='Success to subscribe on Ervand Agadzhanyan API newsletter.',
        message=f'Hello, {username}! Now you will receive latest API updates.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


@app.task
def send_daily_newsletter():
    subscriptions = Subscription.objects. \
        filter(daily=True, end__gt=datetime.now()). \
        all()
    emails = [i.user.email for i in subscriptions]
    send_mail(
        subject='Daily news from Ervand Agadzhanyan',
        message=f'I wish you a good day :-)',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails
    )
