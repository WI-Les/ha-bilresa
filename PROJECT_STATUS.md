# Project status

This is an independent integration maintained by Les., based on the MIT-licensed
Vituhlos integration at commit `67639e18d6d8595e87a31993802ae76745915a97`.

Version 0.1.0 is the first stable release and uses the same integration code
as 0.1.0-rc.2. Automated integration and frontend tests cover the software
behaviour. The 0.1.0-rc.2 pilot confirmed that a BILRESA scroll wheel dimmed a
three-light Zigbee2MQTT group in both directions on Home Assistant 2026.11.2. A separate
Chrome test confirmed manual installation, setup recovery and panel loading
on Home Assistant 2026.11.1 with a simulated Matter device.

On the pilot installation, a physical press and release started and stopped
a configured colour automation. The automation trace recorded seven light
commands without errors. A separate BILRESA panel test verified that a media
player reported a three-percentage-point decrease and returned to its initial
volume after the opposite simulated rotation.

Device and network behaviour can differ. The pilot covers one Zigbee2MQTT
group and does not establish compatibility across all devices and networks.
See the [hardware validation plan](docs/HARDWARE-VALIDATION.md).
