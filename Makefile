lint:
	poetry run flake8 gendiff

install:
	poetry install

gendiff:
	poetry run gendiff
	
test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-force-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl