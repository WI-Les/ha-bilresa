# BILRESA.MasterControl

For 0.2.0-rc.2. See the illustrated [Quick Start](QUICK-START.md) and
[full manual](USER-GUIDE.md) for everyday configuration.

MasterControl keeps real-time scrolling and single, double, triple, hold and
release actions in the existing integration. The domain remains `ikea_bilresa`;
existing Matter pairings, channel entities and binding IDs are retained.

## Configure a channel

Open **BILRESA.MasterControl** in the sidebar, choose a remote and edit a channel.
Keep the current rotation target, step, transition, range and follower settings.
Assign short, double and triple presses independently. **Run actions** accepts
Home Assistant action sequences, including conditions, templates and repeats.
Use **Buttons only** when a channel should have press actions without scrolling.
Its target is the default button target; rotation sends no command.

For a hold set to **Run actions**, **On release → Stop hold actions** cancels
that binding's running or not-yet-started hold. Repeated hold reports start it
only once. **Maximum hold duration** defaults to 60 seconds and accepts 1–300
seconds. It also stops on disconnect, removal or unload. Existing bindings
default to letting a hold finish on release until this option is enabled.

Use an action sequence containing a repeat and delay for continuous colour
cycling. An optional **Actions after release** sequence runs after an observed
hold, not on an orphan release or a timeout. A light transition already accepted
by the device can finish after new commands have stopped.

For migration, **Button actions → Observe only** recognizes gestures and reports
them in Live test without executing their binding actions. Scrolling stays
active. Disable the corresponding old button automations before changing this
to **Active**. Do not leave both implementations controlling the same gestures.
Observe-only suppresses direct binding actions only: event entities, named
triggers and virtual switches still operate and can drive external automations.

## Shared profiles

Under **Settings → Devices & services → BILRESA.MasterControl → Configure**,
name a profile and select its linked wheel remotes. The first selected remote
supplies the initial settings for the same channels already bound on its peers.
Saving a linked channel in either editor updates the matching existing channel
bindings of the other members. The panel identifies the shared profile before
the channel editor. Clearing the selection unlinks the remotes without deleting
their settings. This version supports one linked group in the options dialog.

Bindings keep their original IDs, revisions and individual gesture sessions.
Releasing one remote never stops another remote's hold. An unconfigured peer
channel must be added before it participates. Deleting a binding removes that
binding only; it does not delete the other remotes' bindings.

## Validate and migrate

Before installing, back up the entire `custom_components/ikea_bilresa` folder,
the integration's config entry and subentries, and the old automations and
their enabled states. Keep household exports and credentials out of Git.

1. Install the component, preserving its folder/domain. Restart Home Assistant
   once to load the new Python code and versioned frontend. Verify the integration
   is loaded and its existing scrolling bindings and channel entities remain.
2. Import the intended actions with button actions in observe-only mode.
3. An administrator may call `ikea_bilresa/binding/validate` with `node_id`,
   `channel` and binding `data`. It validates the binding and all action sequences
   without saving, running a script or controlling an entity.
4. Disable the old button automations for one room, then activate its bindings.
   Check the room before switching the next. Keep old automations disabled as
   a fallback. Colour-memory helpers can remain in place.
5. Check all three click counts, hold/release, opposite scroll directions,
   shared remotes, unavailable targets and reconnects. Automated tests and panel
   simulations do not establish physical button response.

## Roll back

First set the new button actions to observe-only and stop active holds. Restore
the original binding data and parent options through Home Assistant's editors
or config-entry APIs, and remove only bindings newly created by the migration.
Restore the previous component folder and restart Home Assistant. Restore each
old automation's original enabled state. Verify the loaded version, original
bindings and scrolling before testing buttons.

Keep the complete `.storage/core.config_entries` backup for disaster recovery;
do not overwrite that file in a running Home Assistant instance. A rollback
should restore only this integration's configuration, preserving unrelated
changes made since the backup.

## Public source and provenance

The integration remains MIT licensed, with the upstream attribution in
`LICENSE` and `THIRD_PARTY_NOTICES.md`. Public source contains reusable logic,
synthetic tests and instructions. Household mappings, OAuth files, device
captures and restoration archives are excluded.
