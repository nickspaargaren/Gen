info: 
	@echo "\n=== Available commands ===\n"
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-15s\033[0m %s\n", $$1, $$2}'

init: ## Initialize the project
	@make do-install-packages

do-install-packages:
	@poetry install

codestyle-check: ## Check all Python scripts code style
	@poetry run black . --check

codestyle-fix: ## Fix all Python scripts code style
	@poetry run black .

run: ## Run
	@poetry run python src/run.py