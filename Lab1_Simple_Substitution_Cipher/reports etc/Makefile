FILTERS += -F pandoc-crossref
PDF_ENGINE += --pdf-engine=xelatex --pdf-engine-opt=--shell-escape
OPTIONS += --number-sections
PDF_BIB_OPTIONS = --biblatex
BIB_OPTIONS = --citeproc

build:
	-pandoc "report.md" $(FILTERS) $(OPTIONS) $(BIB_OPTIONS) -o "report.docx"
	-pandoc "report.md" $(FILTERS) $(PDF_ENGINE) $(PDF_OPTIONS) $(BIB_OPTIONS) $(FORMAT_OPTIONS) $(OPTIONS) -o "report.pdf"
	-pandoc "presentation.md" -F pandoc-crossref --pdf-engine=lualatex --number-sections -t beamer --slide-level=2 -o "presentation.pdf"