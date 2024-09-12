info: 
	@echo "\n=== Available commands ===\n"
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-15s\033[0m %s\n", $$1, $$2}'

init: ## Initialize the project
	@make do-create-venv
	@make do-install-packages

do-create-venv:
	@python3 -m venv .venv

do-install-packages:
	@. .venv/bin/activate; pip install -r requirements.txt

codestyle-check: ## Check all Python scripts code style
	@. .venv/bin/activate; black . --check

codestyle-fix: ## Fix all Python scripts code style
	@. .venv/bin/activate; black .

run: ## Run
	@. .venv/bin/activate; python src/run.py