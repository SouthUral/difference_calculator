enter-point:
	poetry run enter-point

publish:
	poetry publish --dry-run

build:
	poetry build

install:
	python3 -m pip install --user dist/*.whl