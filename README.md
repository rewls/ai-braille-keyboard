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
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install pandas numpy symspellpy hangul-utils
```

- 사전데이터 다운로드
  
```
$ wget https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/ko/ko_50k.txt -O ko_50k.txt

``` 주석 처리


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

