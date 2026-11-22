# Changelog

## 0.2.0 — BILRESA.MasterControl

- Publish MasterControl through the stable release channel, retaining the
  integration runtime from 0.2.0-rc.3.
- Rename the banner to BILRESA.MasterControl while preserving its visual style.
- Add clickable Quick Start, Full Manual and Installation Guide buttons and
  remove Changelog from the README's primary navigation.
- Update installation and user documentation for the stable release.
- Retain all existing pairings, bindings, entity IDs and rollback paths.

Physical acceptance of all MasterControl gestures remains pending; automated
software checks and synthetic screenshots do not establish physical behaviour.

## 0.2.0-rc.3

- Restore the original README banner and official Open in Marketplace badge.
- Use the existing three-dot channel symbols in the overview and Live test,
  with matching upper/lower symbols for dual-button remotes.
- Keep localized channel/button tooltips and accessible marker names.
- Refresh all seven documentation screenshots and installation/version guidance
  for the public MasterControl release candidate.
- Retain the existing gesture behaviour, bindings, entity IDs and recovery path.

## 0.2.0-rc.2

- Fix the binding editor's undefined shared-profile variable.
- Label Buttons only correctly and avoid reporting brightness for its rotation.
- Expose optional release actions with every hold choice and include them in
  wheel/button summaries, including combined stop-and-run behaviour.
- Reject invalid fallback JSON and incomplete release action rows before saving.
- Use the MasterControl panel title and rewrite README, Quick Start and manual
  with current examples, migration details and seven synthetic browser captures.
- Document the upstream capability comparison and release/source distinction.

## 0.2.0-rc.1 — BILRESA.MasterControl

- Keep scrolling and all button gestures in the existing integration.
- Add optional stop-on-release action sequences, a configurable 1–300 second hold limit (default 60), and release actions.
- Prevent delayed hold validation from starting a run after release.
- Add linked profiles for existing wheel channel bindings, preserving individual device identities.
- Add observe-only button actions and action validation without execution for staged migrations.
- Ignore duplicate Matter events without replaying button actions.


## 0.1.0

- Publish the first stable release with the same integration code as
  `0.1.0-rc.2`.
- Make the stable version available through the normal Marketplace installation
  path.
- Update the illustrated Quick Start and installation guide for first-time
  setup.

## 0.1.0-rc.2

- Reject overlapping follower light groups in both setup interfaces and
  recheck group membership before dispatch.
- Cancel pending follower group work when another binding changes a member.
- Skip volume commands when a player reports no valid current volume rather
  than guessing a level; resume once it reports a valid value.
- Add installation, migration, rollback and compatibility guides.

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
