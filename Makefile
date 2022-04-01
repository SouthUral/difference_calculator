enter-point:
	poetry run enter-point

publish:
	poetry publish --dry-run

build:
	poetry build

install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff -h

flake:
	poetry run flake8 general_code

test:
	poetry run pytest

test1:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json