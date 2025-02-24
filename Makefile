PYTHON = 3.12

all: build


install: build
	( \
		uv pip install --upgrade -e . \
	)


build: 
	( \
		uv run hatch build -t wheel \
	)

.PHONY: clean clean_build tests deps install build docs grammar
