.PHONy: lint

requirements:
	@echo "Installing poetry to global python interpreter..."
	@curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
	@echo "poetry successfully installed."

shell:
	@poetry shell

app:
	@poetry run python -m main.py

containers:
	@docker-compose up -d

deps:
	@poetry install

lint:
	@poetry run python -m black .

check:
	@poetry run python -m mypy .
