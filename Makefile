# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: upd - docker-compose up -d
upd:
	docker-compose up -d

# target: test - run test in docker container
test:
	docker exec -it web pytest personal_site/auth_djoser/tests personal_site/auth_JWT/tests personal_site/core/tests

# target: down - docker-compose down
down:
	docker-compose down

# target: install - pip install -U -r requirements.txt
install:
	pip install -U -r requirements.txt
