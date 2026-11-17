# Changelog

## 0.1.0-rc.1

This independent pre-release builds on
[Vituhlos/ha-ikea-bilresa v0.7.0-rc.7](https://github.com/Vituhlos/ha-ikea-bilresa/releases/tag/v0.7.0-rc.7).
It retains the upstream Matter gesture engine, dimming and binding interface.

Changes relative to that baseline:

- Add an optional follower light to brightness bindings, with an adjustable
  offset and minimum. The follower is adjusted only while already on.
- Add follower settings to the Home Assistant configuration flow and panel.
  Skip a follower command when the primary service call fails, and discard
  superseded follower updates.
- Reject invalid Matter multipress counts above 255 for wheel and button
  events, including when the device does not advertise a maximum.
- Add local integration icons, installation and migration guidance, and a
  hardware validation plan.
- Expand automated coverage for gesture counts, follower behaviour and
  simulated sequences. Run Home Assistant, frontend, protocol, Hassfest and
  HACS validation in GitHub Actions.

The upstream release already included the Matter event-loop improvements and
smooth dimming behaviour; these are inherited rather than new in this project.
The pre-release has been piloted with physical remotes and lights, but other
hardware combinations and Zigbee2MQTT groups still need physical validation.
