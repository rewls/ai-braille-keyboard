#ifndef CALL_PYTHON_H
#define CALL_PYTHON_H

#define NUM_WORD 3
#define MAX_LEN 100

void call_recommend_word(char *phrase, char word_list[][100]);
void call_correct_spelling(char *word, char *corrected_word);

#endif
