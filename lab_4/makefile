.PHONY: run clean doc pep8 pyflakes cover

run:
	touch test.py
	echo "import main\n\nmain.start()\n" > test.py
	python test.py
	rm -rf test.py

clean:
	rm -vf *.pyc
	rm -rvf documentation/*.html
	rm -rvf htmlcov
	rm -rvf .coverage

doc:
	pydoc -w ./
	mv *.html	documentation/

pep8:
	pep8 model.py

pyflakes:
	pyflakes model.py

cover:
	coverage run tests.py
	coverage html
	google-chrome htmlcov/index.html
