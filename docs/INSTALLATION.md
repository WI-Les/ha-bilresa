# Installation and migration

## Before you start

- Use Home Assistant 2026.8 or newer with Matter Server and the Matter
  integration. Commission the BILRESA device in Matter first.
- Back up Home Assistant and keep a copy of your existing integration and
  automation configuration. Test a restore separately if you need to rely on it.
- The Vituhlos integration and this project use the same integration domain.
  Install only one implementation of that domain at a time. An upgrade or
  downgrade can change the stored configuration; follow the release notes and
  retain a rollback path.

## Marketplace or HACS custom repository

1. Open Marketplace or HACS and select **Custom repositories** from its menu.
2. Add `https://github.com/WI-Les/ha-bilresa` with type **Integration**.
3. Open the integration in the store and download a version. For a release
   candidate, enable pre-release versions in the version selector if necessary.
4. Restart Home Assistant. Go to **Settings → Devices & services → Add
   integration**, select **IKEA BILRESA**, and follow the Matter Server setup.

The public repository is a custom repository; it is not automatically included
in the default Marketplace listing. Private development builds need a separately
authorized private installation method and are not covered by these steps.

## Manual installation

Download the source archive for the intended release and copy the complete
`custom_components/ikea_bilresa` directory, including `brand`, into your Home
Assistant configuration directory under `custom_components`. Restart Home
Assistant and add the integration as described above. Do not copy files from
multiple versions into one directory; preserve the previous copy for rollback.

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

Disable the new channel binding before re-enabling its previous controller.
If rolling back the integration, restore the backed-up code and, when required,
the matching configuration; restart Home Assistant and check the restored
controllers. Do not assume that rolling back code alone reverses a configuration
migration. Never re-pair or remove Matter devices as a routine rollback step.
