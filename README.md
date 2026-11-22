# BILRESA.MasterControl

![BILRESA.MasterControl for Home Assistant with the scroll wheel and dual-button Matter remotes](docs/images/bilresa-mastercontrol-banner.png)

<!-- ha-marketplace:exclude-start -->
[![Open in Marketplace on My Home Assistant](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=WI-Les&repository=ha-bilresa&category=integration)
<!-- ha-marketplace:exclude-end -->

Real-time scrolling, single/double/triple presses, hold and release in one Home Assistant integration for IKEA BILRESA Matter remotes.

[![Quick Start](docs/images/buttons/quick-start.svg)](docs/QUICK-START.md)
[![Full Manual](docs/images/buttons/full-manual.svg)](docs/USER-GUIDE.md)
[![Installation Guide](docs/images/buttons/installation-guide.svg)](docs/INSTALLATION.md)

![MasterControl overview with two wheel remotes and a dual-button remote](docs/images/mastercontrol/01-overview.jpg)

*The shipped panel rendered with synthetic example devices. Screenshots demonstrate the interface, not physical hardware validation. [Screenshot provenance](docs/SCREENSHOTS.md).*

## What you can control

- Turn the wheel to adjust brightness, colour temperature, colour, volume, covers, climate temperature, fans or numeric values. Bind a light group or several lights together.
- Configure short, double and triple presses independently; toggle a target, select a supported action, cycle scenes or run a Home Assistant action sequence.
- Hold to ramp a light or run actions such as colour cycling. Choose stop on release, set a maximum duration and optionally run actions after release.
- Use **Buttons only** when a wheel channel needs press actions without rotation commands. Dual-button remotes have their own button bindings and fixed up/down hold ramps.
- Link wheel remotes through a shared profile while retaining each remote's entities and independent hold/release sessions.
- Inspect recognized gestures, action results and diagnostics in one panel. Keep event entities, named automation triggers, virtual switches and channel dials for automation-based setups.

Targets can use any supported Home Assistant integration; they do not need to be Matter devices. The remote itself must be commissioned into Home Assistant Matter.

## Version and installation

The current stable release is [**BILRESA.MasterControl 0.2.0**](https://github.com/WI-Les/ha-bilresa/releases/tag/v0.2.0). Install it through the normal Marketplace/HACS release channel; enabling pre-releases is not required.

- Home Assistant **2026.11+**: [Open in Marketplace](https://my.home-assistant.io/redirect/marketplace_repository/?owner=WI-Les&repository=ha-bilresa&category=integration) and select **0.2.0**.
- Home Assistant **2026.8–2026.10**: [Open in HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=WI-Les&repository=ha-bilresa&category=integration).
- For a manual installation: follow the [installation guide](docs/INSTALLATION.md#manual-installation).

The integration name and sidebar are **BILRESA.MasterControl**. Its folder and domain remain `ikea_bilresa`; upgrading an existing installation does not require re-pairing devices or changing entity IDs. Install only one implementation of this domain.

Overview and Live test identify wheel channels with the same three-dot symbols as the detail pages. The highlighted dot identifies the channel, not connection status. Dual-button remotes use the matching upper/lower button symbol.

## Start with one channel

1. Install the intended version and restart Home Assistant.
2. Add **BILRESA.MasterControl** under **Settings → Devices & services** if it is not already configured.
3. Open the sidebar panel, select a remote and edit a channel. Choose **Smooth dimming**, a light and **3%** per notch.
4. Assign the press actions you want and save. Keep **Wait for single/double/triple press** when using all gestures.
5. Check rotation, each configured press count and hold/release on the physical remote.

For an existing automation setup, use [observe-only migration](docs/USER-GUIDE.md#migrate-existing-button-automations) and keep a [rollback copy](docs/INSTALLATION.md#rollback). Avoid having both the binding and an old automation execute the same gesture.

## Read more

| Guide | Contents |
| --- | --- |
| [Quick Start](docs/QUICK-START.md) | First working channel and gesture checklist |
| [Full manual](docs/USER-GUIDE.md) | Control modes, actions, hold/release, profiles, triggers and troubleshooting |
| [Installation](docs/INSTALLATION.md) | Marketplace, HACS, manual updates and rollback |
| [MasterControl migration](docs/MASTERCONTROL.md) | Preserving an existing installation |
| [Upstream comparison](docs/UPSTREAM-COMPARISON.md) | What is retained from Vituhlos and what this fork adds |
| [Compatibility](docs/COMPATIBILITY.md) | Device capabilities and limitations |
| [Hardware validation](docs/HARDWARE-VALIDATION.md) | Physical acceptance checklist |
| [Project status](PROJECT_STATUS.md) | Software evidence and limits of hardware evidence |

Automated tests and panel simulations verify software behaviour. They cannot establish the feel, delivery or timing of every physical remote and target combination.

## Credits and license

Independent integration maintained by **Les.**, based on the MIT-licensed [Vituhlos/ha-ikea-bilresa](https://github.com/Vituhlos/ha-ikea-bilresa) project. The original real-time Matter gesture engine and binding interface are retained and extended. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
