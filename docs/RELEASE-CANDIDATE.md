# Next release candidate

Draft for a future public pre-release; no release is created by this document.

## Proposed highlights

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
  Physical Zigbee2MQTT group testing and an authenticated browser installation
  have not yet been established by the automated tests.
- Keep the existing public release available until the new candidate is ready;
  do not replace or move an existing tag.
