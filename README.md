# Mini Home Information Display

A small desktop home information display designed around a Raspberry Pi zero and a [Pimoroni Inky wHat](https://shop.pimoroni.com/products/inky-what?variant=21214020436051).

## Setup

- Set up raspberry pi
  - Flash the pi with Raspbian Bookworm
  - Install ssh key ```ssh-copy-id -i ~/.ssh/id_rsa <IP_ADDRESS>```, if not done by flasher
  - SSH into pi
  - Do update / upgrade
- Set up this repo
  - Clone repo
  - Set up venv ```python3 -m venv .venv```
  - Activate venv ```source .venv/bin/activate```
- Clone inky installer
  - ```git clone https://github.com/pimoroni/inky```
  - ```cd inky```
  - ```install.sh```
- Install things that the inky installer misses
  - ```sudo apt install libopenjp2-7 libopenjp2-7-dev libopenjp2-tools```
  - ```sudo apt install libopenblas-dev```
