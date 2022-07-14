#!/bin/sh

#intofiywait - watch for file modification
while inotifywait -e modify /var/log/secure; do
  journalctl _SYSTEMD_UNIT=sshd.service | egrep -o "sshd\[[0-9]*\]: (Failure|Accepted|Invalid)" | wc -l > inotres.txt
done