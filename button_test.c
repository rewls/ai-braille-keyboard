#include <wiringPi.h>
#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>  // system() 호출에 필요

#define NUM_INPUTS 3
#define NUM_OUTPUTS 4
#define NUM_KEYS 9

// 입력 핀 및 출력 핀 정의
int input_pins[NUM_INPUTS] = {0, 2, 3};       // input 1, input 2, input 3 (WiringPi 기준)
int output_pins[NUM_OUTPUTS] = {4, 5, 6, 25}; // output 1, output 2, output 3, output 4 (WiringPi 기준)

// 각 키의 상태를 저장하는 배열 (KEY1 ~ KEY9)
bool key_states[NUM_KEYS] = {false, false, false, false, false, false, false, false, false};

// 음성 출력 함수
void playAudio(const char* text) {
    char command[256];
    snprintf(command, sizeof(command), "espeak -v ko \"%s\" --stdout | sox -t wav - -r 48000 -c 2 -t wav - gain -n bass +3 treble +6 | aplay -D hw:0,0", text);
    system(command);
}

void toggleKey(int input_idx, int output_idx) {
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

        // 현재 상태를 출력
        printf("키 %d 상태가 변경되었습니다: ", key_index + 1);
        for (int i = 0; i < NUM_KEYS; i++) {
            printf("%d ", key_states[i]);
        }
        printf("\n");

        // 상태에 따른 음성 메시지
        char audio_msg[32];
        if (key_index < 6) {
            // 1~6번 키
            if (key_states[key_index]) {
                snprintf(audio_msg, sizeof(audio_msg), "%d", key_index + 1); 
            } else {
                snprintf(audio_msg, sizeof(audio_msg), "%d 취소", key_index + 1);
            }
        } else {
            // 7~9번 키
            const char* key_names[] = {"send", "enter", "delete"};
            if (key_states[key_index]) {
                snprintf(audio_msg, sizeof(audio_msg), "%s", key_names[key_index - 6]); 
            } else {
                snprintf(audio_msg, sizeof(audio_msg), "%s 취소", key_names[key_index - 6]); 
            }
        }

        playAudio(audio_msg); 
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
}

void scanKeys() {
    for (int i = 0; i < NUM_INPUTS; i++) {
        // 모든 입력 핀 LOW로 초기화
        for (int k = 0; k < NUM_INPUTS; k++) {
            digitalWrite(input_pins[k], (k == i) ? HIGH : LOW);
        }
        usleep(100); // 신호 안정화를 위한 대기

        for (int j = 0; j < NUM_OUTPUTS; j++) {
            if (digitalRead(output_pins[j]) == HIGH) {  // 출력 핀이 HIGH로 변하면 해당 키 감지
                toggleKey(i, j);  // 상태 변경 및 음성 출력
                usleep(100 * 1000); // 중복 감지를 방지하기 위한 대기
            }
        }
    }
}

int main() {
    if (wiringPiSetup() == -1) {
        printf("wiringPi 초기화 실패!\n");
        return 1;
    }

    setup(); // 핀 설정

    printf("점자 키보드 입력 상태 확인을 시작합니다...\n");

    while (1) {
        scanKeys(); // 키 스캔 루프
    }

    return 0;
}
