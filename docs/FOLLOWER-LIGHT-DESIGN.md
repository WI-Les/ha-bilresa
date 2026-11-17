# Optional follower light for brightness bindings

Status: implemented and automatically tested. Installed as a development
candidate on one Home Assistant instance; physical verification is pending.

## Required behavior

A brightness binding may optionally specify a second light, a signed offset in
percentage points, and a follower minimum. When the primary brightness command
is dispatched, an enabled follower receives the same transition and a brightness
of `clamp(primary_percent + offset, minimum, 100)`. The follower is updated only
if it is already on; an off, unknown or unavailable follower is never switched
on. A disabled follower has no effect on existing bindings.

The follower must not change wheel discovery, press/hold behavior or the primary
target. A group entity reports its own observed brightness and can lag a command;
the offset must be based on the primary binding's actual dispatched target, not
on an intermediate state report. Intermediate commands coalesced by the binding
must not produce follower calls after a newer value or an off/press action.

## Implemented safeguards and remaining work

- Store and validate the optional light, offset and minimum in binding data.
  The primary cannot be its own follower; non-light followers, multiple primary
  targets, unsupported modes and out-of-range values are rejected. Both setup
  forms reject overlapping known light groups with a clear field error. Before a
  follower command, recursively check known group members again and skip the follower
  if either group contains the other or they share a member. This includes
  nested groups and terminates even when group membership contains a cycle.
  Membership not reported by Home Assistant and cycles across separate bindings
  cannot be detected by this check and must still be avoided.
- Provide the same options in the native setup form and the BILRESA panel,
  with English labels, accessible controls and an explicit explanation that
  an off follower stays off. Preserve options on edits, copies and upgrades.
- Dispatch the follower from the same coalesced command path as the primary,
  preserving cancellation and cross-binding ordering. Never infer a successful
  physical state from a scheduled Home Assistant service call.
- A primary service failure prevents the follower call. Off or unavailable
  followers are skipped. A shared revision invalidates older follower tasks
  across bindings, including when another binding changes a member of a follower
  group; pending operations cannot undo a command already dispatched.
  Follower service failures are logged. Full concurrent device behavior remains
  to be validated on hardware.
- Diagnostics must redact configured entity IDs and user action data.

## Migration constraints

Take and verify a current backup and save the original listener/configuration.
Disable the existing rotary controller for the selected channel only; retain
button automations and other channels. Configure both remote bindings with the
same primary, follower and offset, and make sure one controller owns each
rotary event. Keep the old configuration available for rollback. Do not replace
the offset with a multi-light binding that sends identical values to all lights.

Automated tests do not prove physical device behavior. Do not describe this
feature as hardware-validated until the hardware checklist is completed.
