# Compatibility and troubleshooting

The remote must be commissioned through Matter and expose a supported BILRESA
wheel or button. A target can use any Home Assistant integration that exposes
the required entity and service; a protocol or brand name alone does not prove
that every target supports every mode.

| Control | Target requirements and limitations |
| --- | --- |
| Brightness | A brightness-capable light. Smooth transitions require support from the target integration and device. Some lights show discrete steps. |
| Follower brightness | An optional light or group, already on, with no known members shared with the primary target. Groups without reported membership cannot be checked completely. |
| Colour and colour temperature | A light exposing the corresponding colour mode and, for temperature, a usable range. |
| Volume | A media player that reports a valid volume level and supports setting an absolute volume. A missing or invalid level pauses rotary volume commands until the player reports a valid value. |
| Cover, fan, climate or number | A target that exposes the corresponding state and service. Features and permitted ranges vary by integration. |

Home Assistant groups and Zigbee2MQTT groups can report changes at different
times. Some group membership is not exposed to Home Assistant; do not configure
the same physical light as both primary and follower. Cross-binding cycles
cannot be detected in every configuration. Individual devices and group
setups should be tested before migrating automations.

If a channel does not respond, check Matter connectivity, the selected channel,
the target's availability and the binding's action. Check whether another
controller handles the same gesture. For dimming that appears stepped, check
the target's transition support and use smaller configured steps if suitable.
For volume, check that the player reports its current volume and supports an
absolute volume command. Integration diagnostics should be reviewed for private
information before sharing; do not publish household identifiers or captures.

Automated tests and one pilot installation do not establish compatibility with
every light, speaker, firmware, Matter network or Zigbee2MQTT group.
