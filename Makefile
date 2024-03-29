.PHONy: lint


setup:
	 python3.9 -m venv env
	 env/bin/python3.9 -m pip install --upgrade pip
	 env/bin/pip3.9 install -r requirements.txt


clean_env:
	rm -r env

shell:
	@poetry shell

app:
	uvicorn application:application --reload

containers:
	@docker-compose up -d

test:
	pytest tests

clean:
	@echo "Cleaning pycache files..."
	@rm -rf __pycache__
