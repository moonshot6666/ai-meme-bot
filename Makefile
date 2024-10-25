# Define the Python interpreter
PYTHON = python3

# Define the main Python script
MAIN = main.py

# Default target: run the main Python script
run:
	$(PYTHON) $(MAIN)

# Clean target: remove all .txt files
clean:
	rm -f output.txt

# Phony targets to avoid filename conflicts
.PHONY: run clean