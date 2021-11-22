#!/bin/sh
docker run -d --privileged -v /dev/i2c-1:/dev/i2c-1 -v /dev/spidev0.0:/dev/spidev0.0 --restart always --name $(basename "$PWD") $USER/$(basename "$PWD"):latest
