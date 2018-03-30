RESOURCE_DIR := GUI/Resource
COMPILED_DIR := GUI/UI

UI_FILES := main.ui
COMPILED_UI = $(UI_FILES:%.ui=$(COMPILED_DIR)/ui_%.py)

PYUIC := pyuic5

run:
	python3 main.py

ui: $(COMPILED_UI)

$(COMPILED_DIR)/ui_%.py: $(RESOURCE_DIR)/%.ui
	$(PYUIC) $< -o $@ 
