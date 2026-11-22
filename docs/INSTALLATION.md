# Installation and migration

Current source documentation: **BILRESA.MasterControl 0.2.0-rc.2**. Check the version
offered by Marketplace/HACS: a commit on `main` is not automatically a release.
Stable 0.1.0 uses the older IKEA BILRESA name and lacks the new MasterControl
hold lifecycle and shared profiles. Use a published candidate when available,
or install the intended source manually.

## Before you start

- Use Home Assistant 2026.8 or newer with Matter Server and the Matter
  integration. Commission the BILRESA device in Matter first.
- Back up Home Assistant and keep a copy of your existing integration and
  automation configuration. Test a restore separately if you need to rely on it.
- The Vituhlos integration and this project use the same integration domain.
  Install only one implementation of that domain at a time. An upgrade or
  downgrade can change the stored configuration; follow the release notes and
  retain a rollback path.

## Marketplace

Home Assistant **2026.11 and newer** include Marketplace. Open it as an
administrator and review the first-run notice.

1. Select [**Open in Marketplace**](https://my.home-assistant.io/redirect/marketplace_repository/?owner=WI-Les&repository=ha-bilresa&category=integration).
   You can also open **Settings → Marketplace → Add from link** and enter
   `https://github.com/WI-Les/ha-bilresa`. Choose **Integration** if asked for
   the type. Connect GitHub when prompted to add the custom repository.
2. On the BILRESA repository page, select **Install** and confirm the intended
   version. For a published candidate, include pre-releases as described below.
3. Restart if prompted. If the setup form does not open automatically, go to
   **Settings → Devices & services → Add integration**, select **BILRESA.MasterControl**
   and follow the Matter Server setup.

See the [Home Assistant Marketplace documentation](https://www.home-assistant.io/integrations/marketplace/)
for details on custom repositories, GitHub sign-in and pre-releases.
The [Quick Start](QUICK-START.md#2-install-bilresamastercontrol) walks through
installation and the first channel using current panel screenshots.

### Install a release candidate

Open the BILRESA repository page in Marketplace. Select **Include
pre-releases** from the three-dot menu, then select **Include**. Open
**Install** and check the version shown. To pick a different published
release, use **Install another version** from the same menu. Use
[manual installation](#manual-installation) if the version you need is
unavailable in Marketplace.

## HACS on older Home Assistant versions

On **2026.8–2026.10**, use HACS if installed. Select
[**Open in HACS**](https://my.home-assistant.io/redirect/hacs_repository/?owner=WI-Les&repository=ha-bilresa&category=integration)
or add `https://github.com/WI-Les/ha-bilresa` as an **Integration** under
**HACS → Custom repositories**. Open the repository and download the stable
release. Restart Home Assistant. Add
**BILRESA.MasterControl** in **Settings → Devices & services** and follow the Matter
Server setup.

## Manual installation

Download the source archive for the intended release, or the current
[main source archive](https://github.com/WI-Les/ha-bilresa/archive/refs/heads/main.zip)
for the documented candidate. Record the selected version/commit. Copy the complete
`custom_components/ikea_bilresa` directory, including `brand`, into your Home
Assistant configuration directory under `custom_components`. Restart Home
Assistant and add the integration as described above. Do not copy files from
multiple versions into one directory; preserve the previous copy for rollback.

For an existing installation, retain the existing config entry, subentries and
entity IDs. Do not add a second entry or re-pair remotes. After restart, check
the installed manifest version and reload the frontend. Keep private backups
outside the public repository.

## Configure and migrate

Verify the remote and channel events in the BILRESA panel. Add one binding
and choose a supported target and control mode. Before testing, make sure that
only one automation or integration controls each gesture for that channel;
retain the old controller's settings so you can restore it. Test rotation,
press and hold separately before moving additional channels. Bindings without a
configured press action do not replace an existing press automation.

See [compatibility](COMPATIBILITY.md) for device capabilities and
[hardware validation](HARDWARE-VALIDATION.md) for a test checklist.

## Rollback

Set the new button actions to observe-only and stop active holds before
re-enabling the previous button controller. Keep the channel active when that
controller depends on this integration's event entities or virtual switches;
turning off the entire channel suppresses those events too.
If rolling back the integration, restore the backed-up code and, when required,
the matching configuration; restart Home Assistant and check the restored
controllers. Do not assume that rolling back code alone reverses a configuration
migration. Never re-pair or remove Matter devices as a routine rollback step.
