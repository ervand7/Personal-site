### App, responsible for "Subscribe" rubric on site
local launch: <br>
`$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management`<br>
`$ celery -A subscribe worker --loglevel=INFO`<br>
`$ celery -A subscribe beat --loglevel=DEBUG`