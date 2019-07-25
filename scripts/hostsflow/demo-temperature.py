#!/usr/bin/env python

import json
import socket

tempC = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
msg = {
  "rtmetric": {
    "datasource": "sensors",
    "tempC": { "type": "gaugeFloat", "value": tempC }
  }
}
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(json.dumps(msg),("127.0.0.1",36343))
