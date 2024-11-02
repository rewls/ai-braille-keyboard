#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "call-python.h"

void call_recommend_word(char *phrase, char word_list[][100])
{
	int fildes[2];
	pipe(fildes);

	if (!Py_IsInitialized())
		Py_Initialize();

	switch (fork()) {
	case -1:
		break;
	case 0:
		char script[MAX_LEN];
		close(fildes[0]);
		dup2(fildes[1], STDOUT_FILENO);
		PyRun_SimpleString("import word_recommendation as wr");
		sprintf(script, "print(','.join(wr.recommend_word('%s')))",
				phrase);
		PyRun_SimpleString(script);
		close(fildes[1]);
		exit(EXIT_SUCCESS);
	}

	int nbytes, j;
	char buf[MAX_LEN], *str1, *token, *saveptr1;

	close(fildes[1]);
	nbytes = read(fildes[0], buf, MAX_LEN);
	buf[nbytes] = '\0';

	for (j = 0, str1 = buf; ; j++, str1 = NULL) {
		token = strtok_r(str1, ",", &saveptr1);
		if (token == NULL)
			break;
		strcpy(word_list[j], token);
	}
	close(fildes[0]);

	if (Py_IsInitialized())
		Py_FinalizeEx();
}

void call_correct_spelling(char *word, char *corrected_word)
{
	int fildes[2];
	pipe(fildes);

	if (!Py_IsInitialized())
		Py_Initialize();

	switch (fork()) {
	case -1:
		break;
	case 0:
		char script[MAX_LEN];
		close(fildes[0]);
		dup2(fildes[1], STDOUT_FILENO);
		PyRun_SimpleString("import spell_correction as sc");
		sprintf(script, "print(sc.correct_spelling('%s')))", word);
		PyRun_SimpleString(script);
		close(fildes[1]);
		exit(EXIT_SUCCESS);
	}

	int nbytes;
	char buf[MAX_LEN];

	close(fildes[1]);
	nbytes = read(fildes[0], buf, MAX_LEN);
	buf[nbytes] = '\0';
	strcpy(corrected_word, buf);
	close(fildes[0]);

	if (Py_IsInitialized())
		Py_FinalizeEx();
}
