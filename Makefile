.PHONY: test install clean all

all: clean install test

test:
	pipenv run pytest --black --mypy --color yes

install:
	./install.sh

clean:
	find . | grep -E "(__pycache__|\.mypy_cache|\.pyc|\.pyo$$)" | xargs rm -rf
