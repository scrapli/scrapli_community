lint:
	python -m isort scrapli_community/
	python -m isort tests/
	python -m black scrapli_community/
	python -m black tests/
	python -m pylama scrapli_community/
	python -m pydocstyle scrapli_community/
	python -m mypy scrapli_community/

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
