#include "jamo.h"

#define HANGUL_START 0xAC00
#define HANGUL_END 0xD7A3
unsigned int ch2wch(char *input, wchar_t* output) 
{
	size_t len = mbstowcs(NULL, input, 0) + 1;
	mbstowcs(output, input, len);

	return len - 1;
}

void jamo(wchar_t* wstr, wchar_t* output)
{
	int index = 0;
	for(int i=0; i<wcslen(wstr); i++)
	{
		wchar_t ch = wstr[i]; 

        // 한글 범위 체크
        if (ch >= HANGUL_START && ch <= HANGUL_END) 
		{
            wchar_t offset = ch - HANGUL_START;

            int cho_idx = offset / (21 * 28);
            int jung_idx = (offset % (21 * 28)) / 28;
            int jong_idx = offset % 28;

            // 분해된 자모 추가
            output[index++] = cho_idx + 0x1100;
            output[index++] = jung_idx + 0x1161;
            if (jong_idx != 0) {  // 종성이 있으면 추가
                output[index++] = jong_idx + 0x11a7;
            }
        } 
		else 
		{
            output[index++] = ch;  // 한글이 아니면 그대로 추가
    	}
    	output[index] = L'\0'; // null-terminat
	}
}

int main() {
    setlocale(LC_ALL, "");

    char *input = "안녕 하세요";
    wchar_t wstr[50];
    wchar_t output[150];   // 분해된 자모를 저장할 배열

    size_t len = ch2wch(input, wstr);
    jamo(wstr, output);

    wprintf(L"wchar 변환 : %ls\n", wstr);
    wprintf(L"자모 분해: %S\n", output);    // 결과: ㅇㅏㄴㄴㅕㅇ

    wprintf(L"%lc\n", wstr[0]);
    wprintf(L"%lc\n", output[0]);

    return 0;
}
