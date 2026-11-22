# Project status

BILRESA.MasterControl 0.2.0-rc.2 extends the existing runtime; it retains the
`ikea_bilresa` domain, connection and entity identifiers. New hold lifecycle and
linked-profile tests cover the software behaviour. Physical acceptance of all
new migrated gestures must be confirmed on the target installation.

The README, Quick Start and full manual describe the current candidate, including
press response, bounded hold sequences, release actions, observe-only migration
and linked profiles. Seven browser screenshots show the production panel with
synthetic data; see [screenshot provenance](docs/SCREENSHOTS.md). They do not
establish physical hardware response. The source candidate is distinct from
published Marketplace/HACS releases.

The [upstream comparison](docs/UPSTREAM-COMPARISON.md) records the original
project's retained capabilities and this fork's additions. The editor, release
validation and summaries have focused regression coverage. The physical
MasterControl gesture acceptance run remains pending.


This is an independent integration maintained by Les., based on the MIT-licensed
Vituhlos integration at commit `67639e18d6d8595e87a31993802ae76745915a97`.

Version 0.1.0 is the first stable release and uses the same integration code
as 0.1.0-rc.2. Automated integration and frontend tests cover the software
behaviour. The 0.1.0-rc.2 pilot confirmed that a BILRESA scroll wheel dimmed a
three-light Zigbee2MQTT group in both directions on Home Assistant 2026.11.2. A separate
Chrome test confirmed manual installation, setup recovery and panel loading
on Home Assistant 2026.11.1 with a simulated Matter device.

On a fresh Home Assistant 2026.11.1 instance, Chrome installed 0.1.0
through Marketplace with the pre-release setting off. The installed
integration files matched the release tag. The configuration flow finished,
the panel loaded at desktop and phone widths, and Home Assistant served both
bundled icons. The test used simulated GitHub approval and Matter remotes.

On the pilot installation, a physical press and release started and stopped
a configured colour automation. The automation trace recorded seven light
commands without errors. A separate BILRESA panel test verified that a media
player reported a three-percentage-point decrease and returned to its initial
volume after the opposite simulated rotation.

Device and network behaviour can differ. The pilot covers one Zigbee2MQTT
group and does not establish compatibility across all devices and networks.
See the [hardware validation plan](docs/HARDWARE-VALIDATION.md).
