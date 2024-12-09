#include "call-python.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wchar.h>

#include <Python.h>

void init_spell_coreprection(void)
{
	system("python -c \"import spell_suggestion as ss; ss.init()\"");
}

int call_recommend_word(wchar_t *phrase, wchar_t word_list[][MAX_LEN])
{
	char command[MAX_LEN];
	FILE *fp;

	snprintf(command, sizeof(command),
			"python -c \"import word_recommendation as wr;"
			"print(','.join(wr.recommend_word('%S')))\"",
			phrase);
	fp = popen(command, "r");
	if (!fp) {
		pclose(fp);
		perror(__func__);
		return 1;
	}
	fscanf(fp, "%l[^,],", word_list[0]);
	fscanf(fp, "%l[^,],", word_list[1]);
	fscanf(fp, "%l[^\n]", word_list[2]);
	pclose(fp);
	return 0;
}

int call_correct_spelling(wchar_t *word, wchar_t *corrected_word)
{
	char command[MAX_LEN];
	FILE *fp;

	snprintf(command, sizeof(command),
			"python -c \"import spell_suggestion as ss;"
			"print(ss.correct_spelling('%S'))\"",
			word);

	fp = popen(command, "r");
	if (!fp) {
		perror("popen");
		return 1;
	}
	fscanf(fp, "%S", corrected_word);
	pclose(fp);
	return 0;
}
