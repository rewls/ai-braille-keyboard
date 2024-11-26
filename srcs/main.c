#include <wiringPi.h>
#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <fcntl.h>
#include "braille.h"
#include "call-python.h"
#include "report.h"
#include "jamo.h"

#define NUM_INPUTS 3
#define NUM_OUTPUTS 4
#define NUM_KEYS 9
#define REC_INPUT_SW 7
#define REC_OUTPUT_SW 1

wchar_t buf[1000] = L"";
wchar_t word[1000] = L"";

// 입력 핀 및 출력 핀 정의
int input_pins[NUM_INPUTS] = {0, 2, 3};       // input 1, input 2, input 3 (WiringPi 기준)
int output_pins[NUM_OUTPUTS] = {4, 5, 10, 11}; // output 1, output 2, output 3, output 4 (WiringPi 기준)

// 각 키의 상태를 저장하는 배열 (KEY1 ~ KEY9)
bool key_states[NUM_KEYS] = {false, false, false, false, false, false, false, false, false};  

void send_corrected_word(int fd)
{
    char corrected_word[MAX_LEN];
    wchar_t wch_word_list[MAX_LEN];
    wchar_t jamo_word[MAX_LEN*3];

    call_correct_spelling(word, corrected_word);
    printf("corrected word : %s\n", corrected_word);

    int len = ch2wch(corrected_word, wch_word_list);
    jamo(wch_word_list, jamo_word);
    for(int i=0; i<wcslen(word)+1; i++)
    {
        remove_letter(fd);
    }
    
    for(int i=0; i<wcslen(jamo_word); i++)
    {
        write_kor(fd, jamo_word[i]);
    }
    write_space(fd);
}

void send_rec_word(int fd)
{
    char word_list[NUM_WORD][MAX_LEN] = {"안녕하세요", "안녕하니", "안녕하지"};
    wchar_t wch_word_list[MAX_LEN];
    wchar_t jamo_word[MAX_LEN*3];

    /*
    call_recommend_word(buf, word_list);
    for (int i = 0; i < NUM_WORD; i++)
        printf("%s\n", word_list[i]);
    */
    int select = -1;
    while(select == -1)
    {
        digitalWrite(input_pins[0], HIGH);
        digitalWrite(input_pins[1], LOW);
        digitalWrite(input_pins[2], LOW);

        if(digitalRead(output_pins[0]))
            select = 0;
        else if(digitalRead(output_pins[1]))
            select = 1;
        else if(digitalRead(output_pins[2]))
            select = 2;  
        
        usleep(100 * 10);
    }
    digitalWrite(input_pins[0], LOW);

    int len = ch2wch(word_list[select], wch_word_list);
    jamo(wch_word_list, jamo_word);
    write_space(fd);
    for(int i=0; i<wcslen(word)+1; i++)
    {
        remove_letter(fd);
    }
    
    for(int i=0; i<wcslen(jamo_word); i++)
    {
        write_kor(fd, jamo_word[i]);
    }

    memcpy(word, wch_word_list, sizeof(wchar_t)*(wcslen(wch_word_list)+1));
    word_cnt = wcslen(word) - 1;
}
// 특정 입력/출력 핀 조합에 따라 key_states 배열의 해당 키 상태를 토글하는 함수
void toggleKey(int fd, int input_idx, int output_idx) {
    int key_index = -1;

    // 입력/출력 핀 조합에 따라 key_index 설정
    if (input_idx == 0 && output_idx == 0) key_index = 0;  // KEY 1
    else if (input_idx == 0 && output_idx == 1) key_index = 1;  // KEY 2
    else if (input_idx == 0 && output_idx == 2) key_index = 2;  // KEY 3
    else if (input_idx == 1 && output_idx == 0) key_index = 3;  // KEY 4
    else if (input_idx == 1 && output_idx == 1) key_index = 4;  // KEY 5
    else if (input_idx == 1 && output_idx == 2) key_index = 5;  // KEY 6
    else if (input_idx == 2 && output_idx == 3) key_index = 6;  // KEY 7
    else if (input_idx == 0 && output_idx == 3) key_index = 7;  // KEY 8
    else if (input_idx == 1 && output_idx == 3) key_index = 8;  // KEY 9
    
    if (key_index != -1) {
        key_states[key_index] = !key_states[key_index];
        printf("키 %d 상태가 변경되었습니다: ", key_index + 1);
        for (int i = 0; i < NUM_KEYS; i++) {
            printf("%d ", key_states[i]);
        }
        printf("\n");

        if(key_index == 8)
        {
            int braille = 0;
            for (int i = 0; i < 6; i++)
            {
                braille += (int)key_states[i] * pow(2, i);
            }
            printf("braille : %d\n", braille);
            b2k(fd, braille, buf, word);
            for (int i = 0; i < 6; i++)
            {
                key_states[i] = false;
            }
            if (braille == 0) 
            {
                send_corrected_word(fd);
		    }
        }
        if(key_index == 7)
        {
            write_enter(fd);
            /*
            */
        }
        if(key_index == 6)
        {
            remove_letter(fd);
        }
    }
}

void setup() {
    for (int i = 0; i < NUM_INPUTS; i++) {
        pinMode(input_pins[i], OUTPUT);
        digitalWrite(input_pins[i], LOW);
    }

    for (int j = 0; j < NUM_OUTPUTS; j++) {
        pinMode(output_pins[j], INPUT);
        pullUpDnControl(output_pins[j], PUD_DOWN);  // 풀다운 저항 설정
    }

    pinMode(REC_INPUT_SW, OUTPUT);
    digitalWrite(REC_INPUT_SW, HIGH);

    pinMode(REC_OUTPUT_SW, INPUT);
    pullUpDnControl(REC_OUTPUT_SW, PUD_DOWN);
}


void scanKeys(int fd) {
    for (int i = 0; i < NUM_INPUTS; i++) {
        for (int k = 0; k < NUM_INPUTS; k++) {
            digitalWrite(input_pins[k], (k == i) ? HIGH : LOW);
        }
        usleep(100);  

        for (int j = 0; j < NUM_OUTPUTS; j++) {
            if (digitalRead(output_pins[j]) == HIGH) {  
                toggleKey(fd, i, j);  
                usleep(100 * 2000);  
            }
        }
        if(digitalRead(REC_OUTPUT_SW) == HIGH)
        {
            send_rec_word(fd);
            usleep(100 * 2000);
        }
    }
}

int main() {
    if (wiringPiSetup() == -1) {
        printf("wiringPi 초기화 실패!\n");
        return 1;
    }

    setup(); 

    printf("점자 키보드 입력 상태 확인을 시작합니다...\n");

    char* filename;
	int fd;
	filename = "/dev/hidg0";
	if((fd = open(filename,O_RDWR, 0666)) == -1)
	{
		perror(filename);
		return 1;
	}

    printf("준비완료...\n");
    while (1) {
        scanKeys(fd); 
    }

    return 0;
}