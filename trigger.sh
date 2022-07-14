#!/bin/sh

#intofiywait - watch for file modification
while inotifywait -e modify /var/log/secure; do
  /send_data.sh
done