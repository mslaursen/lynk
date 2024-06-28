
run:  ## Run server
	python src/__main__.py

lint:  ## Run linter
	poetry run ruff check . --fix
	poetry run mypy .

up:  ## Start services
	docker-compose up -d

down:  ## Stop services
	docker-compose down