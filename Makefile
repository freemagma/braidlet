.PHONY: clean all

EXECUTABLES = poetry
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

FLASK_ENV := development
all: library/dist
	FLASK_ENV=$(FLASK_ENV) FLASK_APP=flaskapp python -m flask run

clean:
	rm -rf library/dist
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

LIBRARY_FILES := $(shell find library/math-braid -type f)
library/dist: $(LIBRARY_FILES) library/poetry.lock library/pyproject.toml
	cd library && rm -rf dist && poetry build -f wheel
	cd library/dist && pip wheel --no-binary :all: math_braid-*.whl
	cd flaskapp && pip uninstall -y math-braid && pip install -r requirements.txt