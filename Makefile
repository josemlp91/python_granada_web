.DEFAULT_GOAL := help


help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo

clean: ## Clean output
	sudo rm -rf output

up: clean ## Run local pelican server
	docker-compose up --build

restart: clean ## Restart pelican server 
	docker-compose restart pelican-sitebuilder

down: clean ## Stop pelican server
	docker-compose down
