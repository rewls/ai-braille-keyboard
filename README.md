# AI 휴대용 점자 키보드

## Requirement

### 단어 추천

```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ export GOOGLE_API_KEY=<google-api-key>
$ python -m pip install langchain langchain-chroma langchain-google-genai \
    langchainhub pillow
```

### 오타 교정

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

### HID Gadget 설정

- `/boot/firmware/config.txt`:

    ```
    ...
    [all]
    dtoverlay=dwc2,dr_mode=peripheral
    ```

```sh
$ sudo cp usb_hid_gadget.service /etc/systemd/system
$ sudo systemctl start usb_hid_gadget
$ sudo systemctl enable usb_hid_gadget
```

### 음성출력
- `/boot/firmware/config.txt`:

    ```
    ...
    [all]
    #dtparam=i2s=on
    dtoverlay=hifiberry-dac
    dtoverlay=i2s-mmap
    ```

- `/etc/asound.conf`:

    ```
    ...
    [all]
    pcm.hifiberry {
        type hw card 0
    }

    pcm.!default {
        type plug
    slave.pcm "dmixer"
    }

    pcm.dmixer {
        type dmix
        ipc_key 1024
        slave {
            pcm "hifiberry"
            channels 2
        }
    }
    ```

