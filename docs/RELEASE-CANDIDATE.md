# BILRESA.MasterControl 0.2.0-rc.3

Public release candidate for the existing `ikea_bilresa` integration. It combines real-time scrolling and configurable single/double/triple press, hold and release in one panel. Existing Matter pairings, entity IDs and scroll settings are retained.

## New in this candidate

- Restore the original README banner and official **Open in Marketplace** button.
- Replace numbered overview and Live test badges with the same three-dot channel symbols as the detail pages. The highlighted dot identifies the channel, not connection state.
- Use the existing upper/lower physical button symbol for dual-button remotes.
- Retain localized tooltips and accessible channel/button names.
- Refresh the seven synthetic documentation screenshots, Quick Start, manual and version-selection instructions.

## MasterControl changes since stable 0.1.0

- Bounded custom hold sequences, optional stop-on-release, cancellation of delayed starts and duplicate-hold suppression.
- Optional actions after an observed hold is released; orphan releases and timeouts do not run them.
- Linked profiles for matching existing wheel bindings, while keeping separate device identities and hold sessions.
- Observe-only direct button actions and action validation without execution for staged migration.
- Correct Buttons only summaries, release-action visibility/validation and the binding editor's shared-profile notice.

## Install or update

Home Assistant **2026.8+** with working Matter is required. Commission the remote in Home Assistant Matter first.

On **2026.11+**, open the repository in Marketplace, enable **Include pre-releases** and select **0.2.0-rc.3**. With HACS, enable beta/pre-release versions and select the same candidate. Stable **0.1.0** remains available and has the older interface.

For a manual installation, download this release's source archive and install the complete `custom_components/ikea_bilresa` directory. Back up the previous component and integration configuration first, restart Home Assistant after updating, then reload the frontend. Do not re-pair remotes or install a second component with the same domain.

See the [Quick Start](https://github.com/WI-Les/ha-bilresa/blob/v0.2.0-rc.3/docs/QUICK-START.md), [full manual](https://github.com/WI-Les/ha-bilresa/blob/v0.2.0-rc.3/docs/USER-GUIDE.md) and [installation/rollback guide](https://github.com/WI-Les/ha-bilresa/blob/v0.2.0-rc.3/docs/INSTALLATION.md).

## Validation and limits

Automated Home Assistant integration, protocol, frontend, documentation, HACS and hassfest checks run against the candidate. Browser checks cover the production panel preview at desktop, tablet and phone widths. The preview uses synthetic devices and no actuator connection.

Earlier physical evidence covers a scroll wheel controlling a three-light Zigbee2MQTT group; it does not establish every target/device combination. Full physical acceptance of the new MasterControl gestures remains pending. This candidate does not claim that software tests or screenshots prove physical button timing.

Keep old button automations disabled as a fallback when activating direct binding actions. Observe-only leaves event entities, triggers, virtual switches and scrolling active; disabling a whole channel suppresses this integration's dispatch for that channel. Keep a matching backup for rollback.

## Credits

Based on [Vituhlos/ha-ikea-bilresa](https://github.com/Vituhlos/ha-ikea-bilresa), retaining the MIT license and attribution. MasterControl is an independent community project maintained by Les.
