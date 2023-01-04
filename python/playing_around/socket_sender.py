from os import scandir
from os.path import join
import socket
from time import sleep


BASE_DIR = '/dev/shm/pulse_temp/'


def sock_send_pulses():
    while True:
        sleep(1)
        for filename in scandir(BASE_DIR):
            with open (join(filename), 'r') as pulse_file:
                pulse =a



