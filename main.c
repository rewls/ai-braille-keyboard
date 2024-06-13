#include <stdio.h>
#include <wiringPi.h>
#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "library/braille.h"
#include "library/call-python.h"

#define SW1 8
#define SW2 9
#define SW3 12
#define SW4 0
#define SW5 2
#define SW6 22
#define sw_send 23
#define RECOMMEND 16
#define debounce_time 200

int list[6] = { 0, };
void callback_func1(void);
void callback_func2(void);

volatile int lastInterruptTime = 0;
static wchar_t buf[1000] = L"";
static wchar_t word[1000] = L"";

void callback_func1(void)
{
	int i = 0;
	int pin = 0;

	int interruptTime = millis();

	if (interruptTime - lastInterruptTime > debounce_time)
	{
		lastInterruptTime = interruptTime;
		if (digitalRead(SW1) == 0) pin = 0;
		else if (digitalRead(SW2) == 0) pin = 1;
		else if (digitalRead(SW3) == 0) pin = 2;
		else if (digitalRead(SW4) == 0) pin = 3;
		else if (digitalRead(SW5) == 0) pin = 4;
		else if (digitalRead(SW6) == 0) pin = 5;

		list[pin] = !(list[pin]);
		printf("button pressed : { ");
		for (i = 0; i < 6; i++)
		{
			printf("%d ", list[i]);
		}
		printf("}\n");
		delay(100);
	}
}

void callback_func2(void)
{
	int interruptTime = millis();
	int braille = 0;
	int i = 0;

	if (interruptTime - lastInterruptTime > debounce_time)
	{
		lastInterruptTime = interruptTime;

		for (i = 0; i < 6; i++)
		{
			braille += list[i] * pow(2, i);
		}
		printf("send word : %d\n", braille);
		b2k(braille,buf,word);

		for (i = 0; i < 6; i++)
		{
			list[i] = 0;
		}
		if (braille == 0) {
			char corrected_word[MAX_LEN];
			call_correct_spelling(word, corrected_word);
			printf("correct word : %s\n", corrected_word);
		}

		delay(200);
	}
}

void callback_recommend_word(void)
{
	int interruptTime = millis();
	if (interruptTime - lastInterruptTime > debounce_time) {
		char word_list[NUM_WORD][MAX_LEN];
		call_recommend_word(buf, word_list);
		for (int i = 0; i < NUM_WORD; i++)
			printf("%s\n", word_list[i]);
		delay(100);
	}
}

int main(void)
{
	if (wiringPiSetup() == -1)
	{
		printf("failed\n");
		return 1;
	}

	setenv("PYTHONPATH", "library", 1);

	pinMode(SW1, INPUT);
	pinMode(SW2, INPUT);
	pinMode(SW3, INPUT);
	pinMode(SW4, INPUT);
	pinMode(SW5, INPUT);
	pinMode(SW6, INPUT);
	pinMode(sw_send, INPUT);


	wiringPiISR(SW1, INT_EDGE_FALLING, &callback_func1);
	wiringPiISR(SW2, INT_EDGE_FALLING, &callback_func1);
	wiringPiISR(SW3, INT_EDGE_FALLING, &callback_func1);
	wiringPiISR(SW4, INT_EDGE_FALLING, &callback_func1);
	wiringPiISR(SW5, INT_EDGE_FALLING, &callback_func1);
	wiringPiISR(SW6, INT_EDGE_FALLING, &callback_func1);
	wiringPiISR(sw_send, INT_EDGE_FALLING, &callback_func2);
	wiringPiISR(RECOMMEND, INT_EDGE_FALLING, &callback_recommend_word);

	while (1)
		delay(200);

	return 0;
}
