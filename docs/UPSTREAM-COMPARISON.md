# Upstream comparison

Reviewed **22 November 2026** against the [original community post](https://community.home-assistant.io/t/custom-integration-ikea-bilresa-matter-real-time-scroll-control-and-gui-bindings/1030242) and [Vituhlos/ha-ikea-bilresa](https://github.com/Vituhlos/ha-ikea-bilresa). The upstream main reference fetched for this review was `3060507272bce8f92e7879efdf7fb5ac9e8fd4f5`.

This fork's attributed baseline remains upstream `v0.7.0-rc.7`, commit `67639e18d6d8595e87a31993802ae76745915a97`. A newer main commit date does not imply a superset of features. The review compared behaviour and implementation rather than replacing this fork with upstream main.

## Retained capabilities

| Capability from the original project | Current implementation |
| --- | --- |
| Real-time Matter wheel interpretation, including batched notches | Gesture engines and coordinator; retained, with malformed counts bounded |
| Automatic remote discovery and reconnection | Matter client/coordinator; core connection reuse and standalone fallback |
| Wheel and dual-button variants | Separate channel/button binding models and panel views |
| Graphical binding setup | Home Assistant config flows and editable sidebar panel |
| Brightness, colour temperature, hue, volume, covers, climate, fans and values | Binding modes; availability and capability checks remain |
| Single, double, triple, hold and release gestures | Direct binding actions and event entities; model-specific gestures apply |
| Automation integration | Seven named triggers, event bus, virtual switches and channel dials |
| Optional acceleration and brightness response curve | Retained as user choices; no forced change to tuned settings |
| Live testing, diagnostics and localization | Retained; language selection follows the user where available |

No major advertised core feature needed to be added again. The useful gaps were in the fork's documentation and several editor details.

## MasterControl extensions

- Stop-on-release custom hold sequences, cancellation of delayed starts, duplicate-hold suppression and a configurable 1–300 second hold bound.
- Independent optional release action sequences after an observed hold.
- Shared profiles for matching existing wheel bindings, with independent remote identities and hold sessions.
- Observe-only direct button actions and action validation without execution for staged migrations.
- Follower-light offset/minimum, on-state preservation and overlapping-group protection.
- Retained configured scrolling, multiple-light targets and richer gesture verbs from the fork's baseline.

## Improvements in 0.2.0-rc.2

- Fix an undefined variable that prevented the binding editor rendering its shared-profile notice.
- Label **Buttons only** correctly in summaries and show no brightness action for its rotation row.
- Show release actions in both wheel and button summaries and make their editor available for every hold choice.
- Reject invalid fallback JSON and incomplete release action rows before saving.
- Use the MasterControl title consistently and replace outdated user documentation with illustrated current guides.

Acceleration and perceptual brightness remain optional. Enabling them globally would alter existing tuned behaviour. The connection architecture, entity IDs and domain are preserved. Physical acceptance remains a separate task; software tests and synthetic screenshots are not physical evidence.

See the [manual](USER-GUIDE.md), [changelog](../CHANGELOG.md), [project status](../PROJECT_STATUS.md) and [license notices](../THIRD_PARTY_NOTICES.md).
