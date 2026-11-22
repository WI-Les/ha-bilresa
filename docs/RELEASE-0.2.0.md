# BILRESA.MasterControl 0.2.0

Full public release of MasterControl for Home Assistant. This release uses the normal stable installation channel and is not marked as a pre-release.

## Highlights

- Real-time scrolling and single, double, triple, hold and release actions together in the existing integration.
- Optional stop-on-release for custom hold sequences, a configurable 1–300 second hold limit and optional release actions.
- Shared profiles for matching existing wheel bindings, preserving each remote's entities and independent hold sessions.
- Observe-only button actions for staged migration, plus action validation without execution.
- Consistent channel-dot and upper/lower button symbols throughout the overview, detail pages and Live test.
- Updated BILRESA.MasterControl banner, official Marketplace install button and clickable Quick Start, Full Manual and Installation Guide buttons.

## Install or update

Use Home Assistant **2026.8+** with working Matter and a commissioned BILRESA remote. On **2026.11+**, open the repository in Marketplace and select **0.2.0**. With HACS, choose stable **0.2.0**. Enabling pre-releases is not required.

For manual installation, use this release's source archive and copy the complete `custom_components/ikea_bilresa` folder into your Home Assistant configuration. Back up the previous component and its configuration first. Restart Home Assistant and reload the frontend after updating. Do not re-pair remotes or add a second implementation of the same domain.

Read the [Quick Start](https://github.com/WI-Les/ha-bilresa/blob/v0.2.0/docs/QUICK-START.md), [Full Manual](https://github.com/WI-Les/ha-bilresa/blob/v0.2.0/docs/USER-GUIDE.md) and [Installation Guide](https://github.com/WI-Les/ha-bilresa/blob/v0.2.0/docs/INSTALLATION.md).

## Compatibility and recovery

The domain remains `ikea_bilresa`. Existing Matter pairings, entity IDs, bindings, scroll settings and follower configuration are retained. The integration runtime is unchanged from **0.2.0-rc.3**; this release adds stable version metadata and public documentation/branding updates.

Avoid having direct bindings and old button automations execute the same gesture. Keep old automation configurations and a matching component/configuration backup for rollback. Observe-only retains scrolling and event entities; disabling a whole channel suppresses this integration's channel dispatch.

## Validation and remaining limits

The release is checked with the Home Assistant integration matrix, protocol and frontend suites, documentation checks, HACS and hassfest. The panel preview has been checked at desktop, tablet and phone widths with synthetic devices.

Earlier physical evidence covers scrolling on a three-light Zigbee2MQTT group. Full physical acceptance of the newly migrated MasterControl gestures remains pending. Automated tests, accepted service calls and screenshots do not establish physical button timing or every device/target combination.

## Credits

Independent community project maintained by Les., based on [Vituhlos/ha-ikea-bilresa](https://github.com/Vituhlos/ha-ikea-bilresa). The original MIT license and contributor attribution are retained.
