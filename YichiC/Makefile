# Makefile for Assignment 1
INFILE = b.c
OUTEXE = b.exe
CRESULT = input.txt
PYPROCESS = process.py
OUTRESULT = output.txt


# non dependency commands for this Makefile
.PHONY: run_python


build:
	gcc ${INFILE} -o ${OUTEXE}

run_python:
	./${OUTEXE} > ${CRESULT}
	python ${PYPROCESS}

clean:
	rm -f ${OUTEXE}
	rm -f ${CRESULT}
	rm -f ${OUTRESULT}

test:
	./test.sh