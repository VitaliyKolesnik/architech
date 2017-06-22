.PHONY: run clean doc pep8 pyflakes cover

run:
	touch test.py
	echo "import main\n\nmain.start(\".config\", \"db.txt\")\n" > test.py
	python test.py

clean:
	rm -vf *.pyc
	rm -rvf documentation/*.html
	rm -rvf htmlcov
	rm -rvf.coverage

doc:
	pydoc -w ./
	mv *.html	documentation/

pep8:
	pep8 serialize.py serialize.py model.py view.py controller.py main.py tests.py

pyflakes:
	pyflakes serialize.py model.py view.py controller.py main.py tests.py

cover:
	coverage run mtests.py
	coverage html
	google-chrome htmlcov/index.html
