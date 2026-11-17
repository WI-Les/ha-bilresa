# BILRESA for Home Assistant

Control lights, media players and other Home Assistant devices with IKEA BILRESA
Matter remotes. Configure channels and gestures in the Home Assistant interface.

Maintained by **Les.**, based on the work of [Vituhlos and contributors](https://github.com/Vituhlos/ha-ikea-bilresa). This independent community project is not affiliated with or endorsed by IKEA.

See the [changelog](CHANGELOG.md) for changes relative to the upstream release.

## Features

- Discover supported BILRESA wheels and buttons through Matter.
- Bind rotation and gestures to Home Assistant entities and actions.
- Configure brightness, colour, media volume and other supported controls.
- Use an optional follower light with a configurable brightness offset. It is
  adjusted only when already on.
- Manage bindings from the integration panel; no household-specific settings
  are included.

## Requirements

- Home Assistant 2026.8 or newer, with Matter integration and Matter Server.
- A supported BILRESA device commissioned over Matter/Thread.

## Installation

This is a pre-release. Back up your Home Assistant configuration first and
keep existing controls available until the replacement has been tested.

1. Copy the complete `custom_components/ikea_bilresa` directory, including
   `brand`, to your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. In **Settings → Devices & services**, add **IKEA BILRESA** and connect it
   to the Matter Server.
4. Open the BILRESA panel and configure a channel's target, mode and actions.
5. Test each channel before disabling its previous automation. Ensure only one
   controller owns a given gesture during migration.

For follower lights, do not select a follower contained in the primary group
and avoid circular mappings. Devices without transition support may change
brightness in visible steps.

## Testing and compatibility

See [project status](PROJECT_STATUS.md) and the [hardware validation plan](docs/HARDWARE-VALIDATION.md)
for current coverage and limitations. Automated tests run on the Home Assistant
versions defined in the workflows; hardware, Matter networks and Zigbee2MQTT
groups can behave differently.

Run `node --test tests/panel_frontend.test.mjs tests/iconset_frontend.test.mjs`
for frontend tests. Install `requirements-test.txt` and run `python -m pytest`
for Home Assistant tests. Protocol-only tests can be run with
`python tools/test_pure.py` after installing pytest and pytest-asyncio.

## Credits and license

The upstream MIT license and copyright are retained in [LICENSE](LICENSE).
See [third-party notices](THIRD_PARTY_NOTICES.md) for source attribution.
