# Release candidate 0.1.0-rc.2

## Highlights

- Reject follower configurations whose reported light groups overlap, with a
  clear message in both setup interfaces. Recheck membership before dispatch.
- Cancel stale follower-group work when another binding changes a group member.
- Avoid guessing a media player's volume when its reported level is missing,
  invalid or outside its supported range.
- Add installation, migration, rollback and target compatibility guidance.

Based on Vituhlos/ha-ikea-bilresa v0.7.0-rc.7; retain the original MIT notice
and contributor attribution. The original Matter event engine, dimming logic
and panel remain upstream work.

## Release checks

- Review the public branch and its history for private data and credentials.
- Run the full Home Assistant matrix, protocol and frontend suites, Hassfest,
  and HACS validation against the exact release candidate. HACS validation for
  a private development repository is skipped by design.
- Confirm both icon files are included, installation instructions match the
  actual release, and the manifest, tag and release metadata agree.
- Record tested device classes and disclose remaining hardware and browser gaps.
- Keep the existing public release available until the new candidate is ready;
  do not replace or move an existing tag.

## Validation

- A physical BILRESA scroll wheel on Home Assistant 2026.11.2 controlled a
  native three-light Zigbee2MQTT group. All three lights reported the same
  settled brightness after changes in both directions. The tester confirmed
  that the lamps dimmed together without visible jumps.
- On an isolated Home Assistant 2026.11.1 installation, Chrome completed the
  setup flow after recovering from a Matter connection error. The panel loaded
  at desktop and phone widths, and Home Assistant served both bundled icons.
  The Matter device in that browser test was simulated.
- The hardware pilot covered one group. Other devices and network
  configurations may behave differently.
