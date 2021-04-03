lint:
	python -m isort .
	python -m black .
	python -m pylama .
	python -m pydocstyle .
	python -m mypy scrapli_community/ --strict

test:
	python -m pytest \
	tests/

cov:
	python -m pytest \
	--cov=scrapli_community \
	--cov-report html \
	--cov-report term \
	tests/

.PHONY: docs
docs:
	python docs/generate/generate_docs.py

deploy_docs:
	mkdocs gh-deploy
