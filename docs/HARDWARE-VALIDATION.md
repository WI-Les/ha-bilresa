# Hardware validation plan

This checklist is pending execution on physical devices. Record only versions,
device models and outcomes in this repository; keep household identifiers,
credentials, traces, screenshots and backups private and outside Git.

## Preparation

- Record candidate commit, Home Assistant, Matter Server, firmware, Zigbee2MQTT,
  target type and border-router versions. Confirm a restorable full backup.
- Identify exactly one isolated wheel channel and one test light. Record its
  initial state and existing automations, bindings and integration owners.
- Initially configure no bindings. Verify discovery and events independently.
- Before assigning a binding, ensure exactly one system sends commands to the
  selected target. Record and disable only the relevant old controller path;
  restore it after the test. Never run two controllers on the same target.
- Confirm a person is available at the physical remote and can stop the test.

## Checks

1. Discovery: each wheel and channel appears once, icons render, event entities
   report availability and the panel works on desktop and phone in both themes.
2. Event oracle: count 1, 2, 5 and 18 clockwise and counter-clockwise detents,
   slowly and quickly. Compare physical counts with events including initial,
   ongoing and completion; check no duplicate events or delayed movement.
3. Binding: check dim up/down, limits, transition and first-notch response.
   Verify single/double/triple press and hold/release where the device supports
   them. Check the configured target only changes once.
4. Groups: repeat with a Zigbee2MQTT group, uneven member levels and delayed or
   unavailable members. Test external changes during and after a scroll.
5. Races: two remotes controlling one target, opposite directions, quick scroll
   then press-off, scene activation and failure/unavailable recovery.
6. Lifecycle: after agreed maintenance, restart Matter Server and Home Assistant;
   check reconnect, stable entities, restored bindings and no replayed actions.
7. Monitor logs and responsiveness during extended use; do not claim a soak
   pass until duration, environment and findings are recorded.

## Abort and recovery

Stop if unintended targets change, actions repeat, state becomes unreliable or
HA stalls. Disable the new binding, restore the documented old controller state,
and if needed restore the verified backup in the agreed maintenance window.
Never delete or re-pair Matter devices as an incidental recovery step.
