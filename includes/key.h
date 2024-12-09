#ifndef KEY_H
#define KEY_H

#define NUM_COL 3
#define NUM_ROW 4

enum key_func {
	DOT1, DOT2, DOT3, DOT4, DOT5, DOT6, 
	DELETE, ENTER, SEND
};

int pin_init(const int *row, const int *col);
enum key_func scan_key(const int *row, const int *col);

#endif
