# AI 휴대용 점자 키보드

## Requirement

### 단어 추천

```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ export GOOGLE_API_KEY=<google-api-key>
$ python -m pip install google-generativeai
```

## 오타 교정

```shell
$ python -m pip install pandas hangul-utils
```

- 자모 분해를 위한 hangul_utils 설치 시 오류 발생
- 수동 설치 : https://pypi.org/project/hangul-utils/#description

change setup.py - install_requires 함수 일부 주석 처리
```
 install_requires=[
        "tqdm",
        "six",
        #"jpype1;python_version<='2.7'",
        "jpype1>=1.2.0",
        #"jpype1-py3;python_version>='3.5'",
        #"mecab-python==0.996-ko-0.9.2",
        "map-async>=1.2.3"
    ]
```
