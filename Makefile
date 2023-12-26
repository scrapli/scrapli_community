lint:
	python -m isort .
	python -m black .
	python -m pylama .
	python -m pydocstyle .
	python -m mypy --strict scrapli_community/

darglint:
	find scrapli_community -type f \( -iname "*.py"\ ) | xargs darglint -x

test:
	python -m pytest \
	tests/

cov:
	python -m pytest \
	--cov=scrapli_community \
	--cov-report html \
	--cov-report term \
	tests/

test_unit:
	python -m pytest \
	tests/unit/

cov_unit:
	python -m pytest \
	--cov=scrapli_community \
	--cov-report html \
	--cov-report term \
	tests/unit/

.PHONY: docs
docs:
	python docs/generate.py

test_docs:
	mkdocs build --clean --strict
	htmltest -c docs/htmltest.yml -s
	rm -rf tmp

deploy_docs:
	mkdocs gh-deploy
