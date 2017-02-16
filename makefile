main:
	@echo 'sorry, beware: this takes a while to run :/'
	python main.py
	convert img.ppm img.png
	@echo 'you can open img.png!'

clean:
	rm *.pyc *.ppm *.png

all: clean main