#!/bin/bash
cat /dev/urandom | base64 | tr -Cd A-Za-z0-9 | head -c 64; echo

# cat /dev/urandom | base64 | tr -d "a-z0-9-_=+,<.>[{]}/" | head -c 64; echo
