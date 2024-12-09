#include "key.h"

#include <unistd.h>

#include <wiringPi.h>

// WirintPi number
const int col[NUM_COL] = {0, 2, 3};
const int row[NUM_ROW] = {4, 5, 6, 7};
const int sw_rec = 25;

int pin_init(void)
{
	int i;

	if (wiringPiSetup() == -1)
		return 1;
	for (i = 0; i < NUM_COL; i++) {
		pinMode(col[i], OUTPUT);
		digitalWrite(col[i], LOW);
	}
	for (i = 0; i < NUM_ROW; i++) {
		pinMode(row[i], INPUT);
		pullUpDnControl(row[i], PUD_DOWN);
	}
	pinMode(sw_rec, INPUT);
	pullUpDnControl(sw_rec, PUD_DOWN);
	return 0;
}

static int get_key(int r, int c)
{
	if (c == 0 && r == 0)
		return DOT1;
	if (c == 0 && r == 1)
		return DOT2;
	if (c == 0 && r == 2)
		return DOT3;
	if (c == 0 && r == 3)
		return DELETE;
	if (c == 1 && r == 0)
		return DOT4;
	if (c == 1 && r == 1)
		return DOT5;
	if (c == 1 && r == 2)
		return DOT6;
	if (c == 1 && r == 3)
		return ENTER;
	if (c == 2 && r == 3)
		return SEND;
	return -1;
}

enum key_func scan_key(void)
{
	while (1) {
		for (int i = 0; i < NUM_COL; i++) {
			digitalWrite(col[i], HIGH);
			for (int j = 0; j < NUM_ROW; j++) {
				if (digitalRead(row[j]) == HIGH) {
					digitalWrite(col[i], LOW);
					usleep(200 * 1000);
					return get_key(j, i);
				}
			}
			digitalWrite(col[i], LOW);
			if (digitalRead(sw_rec) == HIGH)
				return REC;
		}
	}
}
