# Mini Home Information Display

A small desktop home information display designed around a Raspberry Pi zero and a [Pimoroni Inky wHat](https://shop.pimoroni.com/products/inky-what?variant=21214020436051).

## Setup

- Flash the pi with Raspbian Bookworm
- Install ssh key ```ssh-copy-id -i ~/.ssh/id_rsa <IP_ADDRESS>```, if not done by flasher
- SSH into pi
- Do update / upgrade
- Clone repo
- Set up venv ```python3 -m venv .venv```
- Activate venv ```source .venv/bin/activate```
