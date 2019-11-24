.PHONY: test install clean parse release

all: test parse release

parse:
	microkg parse

release:
	microkg release

test:
	pipenv run pytest --black --mypy --color yes

install:
	./install.sh

clean:
	find . | grep -E "(__pycache__|\.mypy_cache|\.pyc|\.pyo$$)" | xargs rm -rf
