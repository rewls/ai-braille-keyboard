#ifndef CALL_PYTHON_H
#define CALL_PYTHON_H

#include <wchar.h>

#define NUM_WORD 3
#define MAX_LEN 100

void init_spell_coreprection(void);
int call_recommend_word(wchar_t *phrase, wchar_t word_list[][MAX_LEN]);
int call_correct_spelling(wchar_t *word, wchar_t *corrected_word);

#endif
