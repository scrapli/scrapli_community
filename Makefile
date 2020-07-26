lint:
	python -m isort -rc -y .
	python -m black .
	python -m pylama .
	python -m pydocstyle .
	python -m mypy --strict scrapli_community/

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
	rm -rf docs/scrapli_community
	python -m pdoc \
	--html \
	--output-dir docs \
	scrapli_community \
	--force
