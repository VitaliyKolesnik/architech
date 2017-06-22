.PHONY: run clean doc doctests

run:
	touch test.py
	echo "import Main\n\nMain.start(\".config\", \"db.txt\")\n" > test.py
	python test.py
	rm -rf test.py

clean:
	rm -rvf *.pyc documentation/*.html

doc:
	pydoc -w ./
	mv *.html	documentation/

doctests:
	python Editor.py -v
	python In_out.py -v

pep8:
	pep8 serialize.py tests.py

pyflakes:
	pyflakes serialize.py

cover:
	coverage run tests.py
	coverage html
	google-chrome htmlcov/index.html
