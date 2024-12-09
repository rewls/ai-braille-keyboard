#ifndef KEY_H
#define KEY_H

#define NUM_COL 3
#define NUM_ROW 4

enum key_func {
	DOT1, DOT2, DOT3, DOT4, DOT5, DOT6, 
	DELETE, ENTER, SEND, REC
};

int pin_init(void);
enum key_func scan_key(void);

#endif
