"""User-facing strings for the panel, in every language it speaks.

**Why these are not in `strings.json`.** Home Assistant's translation files have
fixed categories — `config`, `selector`, `system_health`, `issues`,
`device_automation` — and none of them describes a custom panel. HA has no
translation category for one. Inventing a category risks hassfest, and the
frontend would not fetch it anyway.

English, Czech and Dutch share this catalog. Tests require identical keys and
placeholders in every language.

The registered panel includes all catalogs. The frontend selects the viewer's
`hass.language` (including regional base tags) and sends it with snapshot
requests. Older clients and callers without a locale use `hass.config.language`.
Home Assistant's entity names still follow the instance language.
"""

from __future__ import annotations

from typing import Any

DEFAULT_LANGUAGE = "en"

# Keep every language aligned when adding keys.
STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "action_stop_hold_and_run": "Stop hold actions and run release actions",
        "mode_buttons": "Buttons only (scroll does nothing)",
        "gesture_activation": "Button actions",
        "gesture_active": "Active",
        "gesture_shadow": "Observe only (scrolling stays active)",
        "hold_stop_on_release": "On release",
        "hold_stop_enabled": "Stop hold actions",
        "hold_stop_disabled": "Let hold actions finish",
        "hold_max_seconds": "Maximum hold duration (seconds)",
        "release_actions": "Actions after release",
        "action_stop_hold": "Stop hold actions",
        "shared_profile_notice": (
            "Shared profile: {name}. Saving this channel updates its existing "
            "bindings on the linked remotes."
        ),
        # status
        "connected": "Connected",
        "unavailable": "Unavailable",
        "unknown": "Not reporting",
        # channels
        "not_configured": "Not configured",
        "add_binding": "Add a control binding",
        "edit_binding": "Edit binding",
        "community_tool_link": "Design labels for your switches",
        "community_tool_note": "Community tool by Liquidmasl",
        "community_tool_new_window": "opens in a new window",
        "save_short": "Save",
        "discard_changes": "Discard",
        "discard_armed": "Discard?",
        "target_unavailable": "{target} — unavailable",
        "target_missing": "{target} — no longer exists",
        "configured": "Configured",
        "button_actions": "Button actions",
        "multiple_targets": "{count} targets",
        # scroll modes — what a rotation does
        "mode_brightness": "Smooth dimming",
        "mode_color_temp": "Colour temperature",
        "mode_color": "Colour",
        "mode_volume": "Volume",
        "mode_cover_position": "Cover position",
        "mode_temperature": "Temperature",
        "mode_fan_speed": "Fan speed",
        "mode_number": "Value",
        "mode_scenes": "Scenes ({count})",
        # what a rotation changes — the gesture ledger names the quantity, while
        # the channel subtitle above it names the mode, so they must not repeat
        "quantity_brightness": "Brightness",
        "quantity_color_temp": "White temperature",
        "quantity_color": "Colour",
        "quantity_volume": "Volume",
        "quantity_cover_position": "Position",
        "quantity_temperature": "Temperature",
        "quantity_fan_speed": "Speed",
        "quantity_number": "Value",
        # wheel card
        "no_activity": "No activity yet",
        "last_on_channel": "last on channel {channel}",
        "last_on_button": "last on button {button}",
        # summary
        "overview_title": "BILRESA devices",
        "summary_connected": "{count} connected",
        "summary_unavailable": "{count} unavailable",
        "summary_unknown": "{count} not reporting",
        "matter_connected": "Matter connected",
        "matter_offline": "Matter offline",
        # banners
        "banner_matter_offline": (
            "Matter is disconnected. The devices below show their last known state."
        ),
        "banner_updates_stopped": "Live updates stopped. This view may be out of date.",
        "banner_target_missing": (
            "Bindings on {count} devices point to entities that no longer exist "
            "in Home Assistant. Open a marked control and choose another target."
        ),
        "banner_target_missing_named": (
            "The binding on channel {channel} of {wheel} points to an entity "
            "that no longer exists in Home Assistant. Open the channel and "
            "choose another target."
        ),
        "banner_target_missing_button_named": (
            "The binding on button {button} of {wheel} points to an entity "
            "that no longer exists in Home Assistant. Open the button and "
            "choose another target."
        ),
        # states
        "empty_title": "No BILRESA devices found",
        "empty_connected": (
            "The integration is connected but has not discovered a device yet."
        ),
        "empty_offline": (
            "Home Assistant is not connected to Matter, so no device can be seen."
        ),
        "error_title": "Cannot reach the integration",
        "retry": "Try again",
        # detail
        "back": "Back to all BILRESA devices",
        "detail_views": "Device detail views",
        "field_step_curve": "Step placement",
        "field_step_curve_help": (
            "If fast scrolling looks like it jumps, especially near the bottom "
            "of the range, switch to perceptual and scroll again. Leave it "
            "linear if the lamp already evens out its own dimming — correcting "
            "twice is worse than not correcting at all."
        ),
        "step_curve_linear": "Linear (default)",
        "step_curve_perceptual": "Perceptual (even to the eye)",
        "channel_off_note": "it does nothing until you switch it back on here.",
        "settings_dial_intro": (
            "Each channel's number entity (1 to 100): turning the wheel moves it "
            "and automations can read it. It does not affect the binding."
        ),
        "settings_dial_title": "Dial",
        "settings_step_help": "In the dial's own units, 1 to 100.",
        "settings_channel_enabled": "Channel {channel} active",
        "settings_step": "Dial change per notch",
        "settings_acceleration": "Dial acceleration",
        "settings_acceleration_help": (
            "Turning faster moves the dial further per notch. 0 % switches it off."
        ),
        "settings_save": "Save dial",
        "settings_saved": "Dial saved",
        "settings_disabled_badge": "Off",
        "settings_error_conflict": (
            "These settings were changed elsewhere. Reopen the wheel and try again."
        ),
        "settings_error_generic": "The settings could not be saved.",
        "tab_channels": "Channels",
        "tab_buttons": "Buttons",
        "tab_live": "Live test",
        "tab_diagnostics": "Diagnostics",
        "detail_area_none": "No area",
        "detail_last_activity": "Last activity",
        "detail_last_channel": "Last active channel",
        "detail_no_last_channel": "No channel observed yet",
        "detail_last_button": "Last active button",
        "detail_no_last_button": "No button observed yet",
        "detail_channels_heading": "Physical position behaviour",
        "channel_title": "Channel {channel}",
        "channel_binding": "Binding",
        "button_title": "Button {button}",
        "target_none": "No target configured",
        # A wheel's short press falls back to the rotation target when this is
        # left empty, so the placeholder must not claim nothing happens.
        "target_same_as_rotation": "Same as the rotation target",
        # binding editor
        "binding_editor_title": "Edit channel {channel} binding",
        "binding_editor_button_title": "Edit button {button} binding",
        "field_mode": "Mode",
        "field_target": "Target",
        "field_target_help": (
            "Choose several lights to control them together. They all receive "
            "the same value, set by the wheel."
        ),
        "field_step": "Target change per notch",
        "field_step_help": "How far one notch moves the target.",
        "field_acceleration": "Rotation acceleration",
        "field_acceleration_help": (
            "Turning faster moves the target further per notch. 0 % switches it off."
        ),
        "field_transition_help": (
            "Fast rotation arrives in batches of notches. A larger batch is "
            "spread over up to this long; 0 s turns smoothing off."
        ),
        "target_empty_is_rotation": "Leave empty to use the rotation target.",
        "scene_add": "Add a scene",
        "scene_add_placeholder": "Add a scene…",
        "scene_move_up": "Move {scene} up",
        "scene_move_down": "Move {scene} down",
        "scene_remove": "Remove {scene}",
        "ledger_then_release": "{hold}; on release: {release}",
        "field_transition": "Smoothing of large jumps",
        "field_follower_light": "Follower light (optional)",
        "field_follower_help": "Only follows brightness while already on.",
        "field_follower_offset": "Follower offset (percentage points)",
        "field_follower_min": "Follower minimum brightness",
        "field_min_brightness": "Minimum brightness",
        "field_max_brightness": "Maximum brightness",
        "field_press_response": "Response",
        "rotation_more": "More rotation settings",
        "gesture_needs_waiting": "Needs the short-press response “{response}”.",
        "gesture_action": "Action",
        "gesture_target": "Target",
        "field_ramp_direction": "Ramp direction",
        "field_scenes": "Scenes",
        "field_scenes_help": (
            "Each short press activates the next scene, in this order."
        ),
        "section_rotation": "Rotation",
        "click_toggle": "Toggle target",
        "click_on": "Turn target on",
        "click_off": "Turn target off",
        "click_none": "No action",
        "click_scenes": "Cycle scenes",
        "click_scene_on": "Run scene",
        "click_script_on": "Run script",
        "click_script_off": "Stop script",
        "click_script_toggle": "Toggle script",
        "click_play_pause": "Play / pause",
        "click_play": "Play",
        "click_pause": "Pause",
        "click_stop": "Stop",
        "click_next": "Next track",
        "click_previous": "Previous track",
        "click_volume_up": "Volume up",
        "click_volume_down": "Volume down",
        "click_mute_toggle": "Mute / unmute",
        "click_open": "Open",
        "click_close": "Close",
        "click_lock": "Lock",
        "click_start": "Start",
        "click_return_home": "Return to dock",
        "click_locate": "Locate",
        "click_press": "Press the button",
        "click_trigger": "Run the automation",
        "click_speed_up": "Speed up",
        "click_speed_down": "Slow down",
        "click_next_option": "Next option",
        "click_previous_option": "Previous option",
        "click_first_option": "First option",
        "click_last_option": "Last option",
        "click_step_up": "Increase",
        "click_step_down": "Decrease",
        "cover_open_warning": (
            "A garage door or a gate opens when this is pressed, with nobody watching."
        ),
        "script_run_help": (
            "Starts the script and tells it which gesture started it, in the "
            "variables gesture, presses, channel, endpoint and device."
        ),
        "script_toggle_help": (
            "Starts the script, or stops it if it is running. A toggle cannot "
            "pass the script any variables."
        ),
        "gesture_hold_effect": "Effect on the target",
        "hold_toggle": "Act on the hold target",
        "hold_ramp": "Ramp rotation target",
        "hold_none": "No action",
        "ramp_direction_alternate": "Alternate up and down",
        "ramp_direction_up": "Always brighten",
        "ramp_direction_down": "Always dim",
        "button_response_instant": "Run on initial press",
        "button_response_fast": "Run after the first short release",
        "button_response_multi_press": "Wait for single/double/triple press",
        "dual_button_response_instant": "Run on initial press",
        "dual_button_response_fast": "Run after the first short release",
        "dual_button_response_multi_press": "Wait for single or double press",
        "save_binding": "Save binding",
        "delete_binding": "Delete binding",
        "keep_binding": "Keep binding",
        "delete_binding_confirm": (
            "Delete this channel binding? The wheel will stop controlling its targets."
        ),
        "delete_button_binding_confirm": (
            "Delete this button binding? The button will stop controlling its targets."
        ),
        "binding_saved": "Binding saved and activated.",
        "binding_validation_failed": "Fix the marked fields and save again.",
        "binding_conflict": (
            "This binding changed elsewhere. The latest saved values are shown; "
            "review them before saving."
        ),
        "binding_save_failed": "Could not save the binding: {error}",
        "binding_delete_failed": "Could not delete the binding: {error}",
        "binding_test_failed": "Could not run the test: {error}",
        "binding_error_unloaded": "The integration is not loaded.",
        "binding_error_wheel_missing": "The wheel is no longer available.",
        "binding_error_binding_missing": "The binding no longer exists.",
        "binding_error_channel_occupied": (
            "This wheel channel already has another binding."
        ),
        "binding_error_button_occupied": ("This button already has another binding."),
        "binding_error_control_mismatch": (
            "This control does not belong to the selected BILRESA device."
        ),
        "binding_error_control_missing": "This control is no longer available.",
        "binding_error_binding_address_mismatch": (
            "This binding belongs to another control. Reload the panel and try again."
        ),
        "binding_error_gesture_unsupported": (
            "This BILRESA device does not support that gesture."
        ),
        "binding_error_binding_not_configured": (
            "Configure this control before testing it."
        ),
        "validation_invalid_value": "Choose or enter a valid value.",
        "validation_follower_overlap": (
            "Choose lights or groups that do not share any members."
        ),
        "validation_target_required": "Choose a target.",
        "validation_ramp_requires_light": "Ramping needs a light as the hold target.",
        "validation_scene_cannot_turn_off": (
            "A scene can only be run, not turned off. "
            "Choose Toggle target or Turn target on."
        ),
        "validation_scenes_required": "Add at least one scene.",
        "validation_action_not_supported": (
            "This target cannot do that. Choose one of the actions listed for it."
        ),
        "validation_actions_required": (
            "Add at least one action to run, or choose another action."
        ),
        "validation_actions_incomplete": "Choose an action for every row.",
        "validation_actions_invalid": (
            "What you typed in the actions is not valid. Correct it or reload."
        ),
        "validation_scenes_replace_short_press": (
            "Cycling scenes replaces the short press, so it cannot run actions."
        ),
        "validation_mode_target_mismatch": (
            "The selected rotation mode cannot control this entity."
        ),
        "validation_multiple_targets_require_light_mode": (
            "Several targets work only for lights in a dimming, colour "
            "temperature or colour mode."
        ),
        "validation_maximum_must_exceed_minimum": (
            "Maximum brightness must be greater than minimum brightness."
        ),
        "validation_fast_response_conflicts_with_multi_press": (
            "Fast release cannot be combined with double or triple press."
        ),
        "validation_instant_response_conflicts_with_multi_press": (
            "Instant response cannot be combined with double or triple press."
        ),
        "validation_instant_response_conflicts_with_hold": (
            "Instant response requires the hold action to be set to No action."
        ),
        "binding_gesture_rotation": "Rotate left / right",
        "binding_gesture_short_press": "Short press",
        "binding_gesture_double_press": "Double press",
        "binding_gesture_triple_press": "Triple press",
        "binding_gesture_hold": "Hold",
        "binding_gesture_release": "Release",
        "action_toggle": "Toggle",
        "action_turn_on": "Turn on",
        "action_turn_off": "Turn off",
        "action_run": "Run",
        "action_stop": "Stop",
        "action_none": "No action",
        "action_run_actions": "Run actions",
        "click_run": "Run actions",
        "hold_run": "Run actions",
        "actions_label": "Actions to run",
        "actions_help": (
            "Written as in an automation. The gesture is passed to them as the "
            "variables gesture, presses, channel, endpoint and device."
        ),
        "actions_loading": "Loading Home Assistant's action editor...",
        "actions_fallback": (
            "Home Assistant's action editor is not available here, so the "
            "actions are edited as a simple list. It is the same data: nothing "
            "is lost."
        ),
        "actions_empty": "No actions yet.",
        "actions_add": "Add an action",
        "actions_remove": "Remove",
        "actions_service": "Action",
        "actions_target_ids": "Entities, separated by commas",
        "actions_data": "Data (JSON)",
        "actions_json": "All actions as JSON",
        "actions_json_invalid": "This is not valid JSON of the expected kind.",
        "actions_choose": "Choose an action",
        "actions_complex": "A more complex action; edit it in the JSON below:",
        "action_cycle_scenes": "Cycle scenes",
        "action_ramp": "Ramp target",
        "action_ramp_alternate": "Ramp up or down",
        "action_ramp_up": "Brighten",
        "action_ramp_down": "Dim",
        "action_stop_ramp": "Stop ramp",
        "action_play_pause": "Play / pause",
        "action_play": "Play",
        "action_pause": "Pause",
        "action_next": "Next track",
        "action_previous": "Previous track",
        "action_volume_up": "Volume up",
        "action_volume_down": "Volume down",
        "action_mute_toggle": "Mute / unmute",
        "action_open": "Open",
        "action_close": "Close",
        "action_lock": "Lock",
        "action_start": "Start",
        "action_return_home": "Return to dock",
        "action_locate": "Locate",
        "action_press": "Press the button",
        "action_trigger": "Run the automation",
        "action_speed_up": "Speed up",
        "action_speed_down": "Slow down",
        "action_next_option": "Next option",
        "action_previous_option": "Previous option",
        "action_first_option": "First option",
        "action_last_option": "Last option",
        "action_step_up": "Increase",
        "action_step_down": "Decrease",
        "wheel_missing_title": "BILRESA device no longer available",
        "wheel_missing_body": (
            "The device was removed or the integration reloaded. Return to the "
            "overview."
        ),
        # live test
        "live_intro": (
            "Turn or press the wheel. You will see the recognized gesture first "
            "and, for configured channels, the action sent to its target."
        ),
        "live_button_intro": (
            "Press either button. You will see the recognized gesture first and, "
            "for configured buttons, the action sent to its target."
        ),
        "live_result_label": "Action result",
        "live_event_label": "Latest gesture",
        "live_listening": "Listening",
        "live_stopped": "Listening stopped",
        "live_waiting_title": "Waiting for the wheel",
        "live_waiting_body": (
            "Turn or press this wheel. Activity appears only while this view is open."
        ),
        "live_button_waiting_title": "Waiting for a button press",
        "live_button_waiting_body": (
            "Press, double-press or hold either button. Activity appears only while "
            "this view is open."
        ),
        "live_error": (
            "Live activity stopped. Leave and reopen Live test to try again."
        ),
        "result_unavailable": "Gesture recognized",
        "result_unavailable_detail": (
            "No detailed result is available for this event."
        ),
        "result_pending_detail": "Waiting for the configured action to finish.",
        "result_not_configured_channel_detail": ("The gesture reached Home Assistant."),
        "result_not_configured_button_detail": ("The gesture reached Home Assistant."),
        "result_gesture_rotate": "Rotation recognized",
        "result_gesture_press": "Press recognized",
        "result_gesture_double_press": "Double press recognized",
        "result_gesture_triple_press": "Triple press recognized",
        "result_gesture_hold": "Hold recognized",
        "result_gesture_release": "Release recognized",
        "result_gesture_received": "Gesture recognized",
        "dispatch_success": "Action dispatched",
        "dispatch_accepted": "Home Assistant accepted the action",
        "dispatch_pending": "Sending action to Home Assistant",
        "dispatch_skipped": "Binding skipped the action",
        "dispatch_not_configured": "This channel does not control anything yet",
        "dispatch_not_configured_button": ("This button does not control anything yet"),
        "dispatch_completed": "Binding action completed",
        "dispatch_received": "Gesture received; waiting for the result",
        "dispatch_failed": "Action not dispatched",
        "dispatch_unknown": "Action status is not available",
        "result_kind_brightness": "Brightness",
        "result_kind_color_temperature": "Colour temperature",
        "result_kind_color": "Colour",
        "result_kind_volume": "Volume",
        "result_kind_position": "Position",
        "result_kind_temperature": "Temperature",
        "result_kind_fan_speed": "Fan speed",
        "result_kind_value": "Value",
        "result_scene": "Scene {position}/{total} · {target}",
        "result_entity_action": "{action} · {target}",
        "result_ramp_stopped": "Hold ramp stopped",
        "result_fast_press_complete": "Single press dispatched immediately",
        "service_toggle": "Toggle",
        "service_turn_on": "Turn on",
        "service_turn_off": "Turn off",
        "service_run": "Run",
        "service_stop": "Stop",
        "source_panel_test": "Triggered from the panel test controls",
        "test_controls_heading": "Test configured actions",
        "test_controls_intro": (
            "These controls run the real binding without a physical wheel. They can "
            "change target entities immediately."
        ),
        "test_controls_button_intro": (
            "These controls run the real binding without pressing the physical "
            "button. They can change target entities immediately."
        ),
        "test_channel": "Test channel {channel}",
        "test_button": "Test button {button}",
        "test_rotate_down": "Rotate down",
        "test_rotate_up": "Rotate up",
        "test_single": "Single press",
        "test_double": "Double press",
        "test_triple": "Triple press",
        "test_hold": "Start hold",
        "test_release": "Release hold",
        "test_no_bindings": "Configure a channel to enable panel tests.",
        "test_no_button_bindings": "Configure a button to enable panel tests.",
        "direction_up": "up",
        "direction_down": "down",
        "gesture_rotate": "Channel {channel} · rotate {direction} · {delta} steps",
        "gesture_press_single": "Channel {channel} · single press",
        "gesture_press_double": "Channel {channel} · double press",
        "gesture_press_triple": "Channel {channel} · triple press",
        "gesture_hold": "Channel {channel} · hold",
        "gesture_release": "Channel {channel} · release",
        "gesture_unknown": "Channel {channel} · activity received",
        "live_channels_heading": "Channels",
        "gesture_button_press_single": "Button {button} · single press",
        "gesture_button_press_double": "Button {button} · double press",
        "gesture_button_hold": "Button {button} · hold",
        "gesture_button_release": "Button {button} · release",
        "gesture_button_unknown": "Button {button} · activity received",
        "gesture_observed_duration": "{duration} s observed",
        "live_buttons_heading": "Buttons",
        "live_recent": "Latest events",
        "live_setup_channel": "Configure channel {channel}",
        "live_setup_button": "Configure button {button}",
        # diagnostics
        "diagnostics_heading": "Device status",
        "diagnostics_intro": (
            "Read-only status from Home Assistant. Private Matter identifiers are "
            "not shown."
        ),
        "diagnostic_availability": "Device availability",
        "diagnostic_matter": "Matter connection",
        "diagnostic_source": "Event source",
        "diagnostic_link": "Matter device link",
        "diagnostic_linked": "Linked",
        "diagnostic_not_linked": "Not linked",
        "diagnostic_health_ok": "Wheel is ready",
        "diagnostic_health_attention": "Wheel needs attention",
        "diagnostic_health_ok_body": ("Matter and live event delivery are connected."),
        "diagnostic_connection_heading": "Connection",
        "diagnostic_activity_heading": "Activity",
        "diagnostic_technical_details": "Technical details",
        "diagnostic_contract": "Panel contract",
        "source_core": "Home Assistant Matter client",
        "source_fallback": "Passive WebSocket fallback",
        "source_unloaded": "Integration unloaded",
        "recovery_heading": "Recommended action",
        "recovery_ok": "No recovery action is needed.",
        "recovery_matter": (
            "Check the Matter integration and the Matter Server connection."
        ),
        "recovery_unavailable": (
            "Check the wheel battery and bring it closer to the Matter network."
        ),
        "recovery_unknown": (
            "Check that the wheel is present in Home Assistant, then reload the "
            "integration."
        ),
        # a11y
        "menu": "Open Home Assistant sidebar",
    },
    "cs": {
        "action_stop_hold_and_run": "Zastavit akce podržení a spustit akce uvolnění",
        "mode_buttons": "Buttons only (scroll does nothing)",
        "gesture_activation": "Button actions",
        "gesture_active": "Active",
        "gesture_shadow": "Observe only (scrolling stays active)",
        "hold_stop_on_release": "On release",
        "hold_stop_enabled": "Stop hold actions",
        "hold_stop_disabled": "Let hold actions finish",
        "hold_max_seconds": "Maximum hold duration (seconds)",
        "release_actions": "Actions after release",
        "action_stop_hold": "Stop hold actions",
        "shared_profile_notice": (
            "Shared profile: {name}. Saving this channel updates its existing "
            "bindings on the linked remotes."
        ),
        "connected": "Připojeno",
        "unavailable": "Nedostupné",
        "unknown": "Nehlásí se",
        "not_configured": "Nenastaveno",
        "add_binding": "Přidat propojení",
        "edit_binding": "Upravit propojení",
        "community_tool_link": "Navrhnout štítky pro spínače",
        "community_tool_note": "Komunitní nástroj od Liquidmasl",
        "community_tool_new_window": "otevře se v novém okně",
        "save_short": "Uložit",
        "discard_changes": "Zahodit",
        "discard_armed": "Zahodit?",
        "target_unavailable": "{target} — nedostupné",
        "target_missing": "{target} — už neexistuje",
        "configured": "Nastaveno",
        "button_actions": "Akce tlačítka",
        "multiple_targets": "{count} cíle",
        "mode_brightness": "Plynulé stmívání",
        "mode_color_temp": "Teplota bílé",
        "mode_color": "Barva",
        "mode_volume": "Hlasitost",
        "mode_cover_position": "Poloha krytu",
        "mode_temperature": "Teplota",
        "mode_fan_speed": "Rychlost ventilátoru",
        "mode_number": "Hodnota",
        "mode_scenes": "Scény ({count})",
        "quantity_brightness": "Jas",
        "quantity_color_temp": "Teplota bílé",
        "quantity_color": "Barva",
        "quantity_volume": "Hlasitost",
        "quantity_cover_position": "Poloha",
        "quantity_temperature": "Teplota",
        "quantity_fan_speed": "Otáčky",
        "quantity_number": "Hodnota",
        "no_activity": "Zatím žádná aktivita",
        "last_on_channel": "naposledy na kanálu {channel}",
        "last_on_button": "naposledy na tlačítku {button}",
        "overview_title": "Zařízení BILRESA",
        "summary_connected": "{count} připojeno",
        "summary_unavailable": "{count} nedostupné",
        "summary_unknown": "{count} se nehlásí",
        "matter_connected": "Matter připojen",
        "matter_offline": "Matter odpojen",
        "banner_matter_offline": (
            "Matter je odpojený. Zařízení níže ukazují svůj poslední známý stav."
        ),
        "banner_updates_stopped": (
            "Živé aktualizace se zastavily. Tento pohled může být zastaralý."
        ),
        "banner_target_missing": (
            "Propojení na {count} zařízeních míří na entity, které v Home "
            "Assistantu už neexistují. Otevřete označený ovládací prvek a "
            "vyberte jiný cíl."
        ),
        "banner_target_missing_named": (
            "{wheel}: propojení na kanálu {channel} míří na entitu, která "
            "v Home Assistantu už neexistuje. Otevřete kanál a vyberte jiný cíl."
        ),
        "banner_target_missing_button_named": (
            "{wheel}: propojení na tlačítku {button} míří na entitu, která "
            "v Home Assistantu už neexistuje. Otevřete tlačítko a vyberte "
            "jiný cíl."
        ),
        "empty_title": "Nenalezeno žádné zařízení BILRESA",
        "empty_connected": "Integrace je připojená, ale zatím nenašla žádné zařízení.",
        "empty_offline": (
            "Home Assistant není připojený k Matteru, takže nevidí žádné zařízení."
        ),
        "error_title": "Integrace není dostupná",
        "retry": "Zkusit znovu",
        "back": "Zpět na všechna zařízení BILRESA",
        "detail_views": "Pohledy detailu zařízení",
        "field_step_curve": "Rozložení kroků",
        "field_step_curve_help": (
            "Pokud vám rychlé otáčení skáče, hlavně u spodního konce rozsahu, "
            "přepněte na percepční a zkuste to znovu. Ponechte lineární, pokud "
            "si lampa stmívání vyrovnává sama — korigovat dvakrát je horší než "
            "nekorigovat vůbec."
        ),
        "step_curve_linear": "Lineární (výchozí)",
        "step_curve_perceptual": "Percepční (rovnoměrné pro oko)",
        "channel_off_note": "nic nedělá, dokud ho tady znovu nezapnete.",
        "settings_dial_intro": (
            "Číselná entita každého kanálu (1 až 100): otáčení ji mění a mohou "
            "ji číst automatizace. Na propojení nemá vliv."
        ),
        "settings_dial_title": "Číselník",
        "settings_step_help": "V jednotkách číselníku, 1 až 100.",
        "settings_channel_enabled": "Kanál {channel} aktivní",
        "settings_step": "Změna číselníku na jedno cvaknutí",
        "settings_acceleration": "Zrychlení číselníku",
        "settings_acceleration_help": (
            "Čím rychleji otáčíte, tím větší skok číselníku na jedno "
            "cvaknutí. 0 % znamená vypnuto."
        ),
        "settings_save": "Uložit číselník",
        "settings_saved": "Číselník uložen",
        "settings_disabled_badge": "Vypnuto",
        "settings_error_conflict": (
            "Nastavení mezitím změnil někdo jiný. Otevřete kolečko znovu a "
            "zkuste to ještě jednou."
        ),
        "settings_error_generic": "Nastavení se nepodařilo uložit.",
        "tab_channels": "Kanály",
        "tab_buttons": "Tlačítka",
        "tab_live": "Živý test",
        "tab_diagnostics": "Diagnostika",
        "detail_area_none": "Bez oblasti",
        "detail_last_activity": "Poslední aktivita",
        "detail_last_channel": "Naposledy aktivní kanál",
        "detail_no_last_channel": "Zatím nebyl pozorován žádný kanál",
        "detail_last_button": "Naposledy aktivní tlačítko",
        "detail_no_last_button": "Zatím nebylo pozorováno žádné tlačítko",
        "detail_channels_heading": "Chování fyzických poloh",
        "channel_title": "Kanál {channel}",
        "channel_binding": "Propojení",
        "button_title": "Tlačítko {button}",
        "target_none": "Není nastaven žádný cíl",
        "target_same_as_rotation": "Stejný jako cíl otáčení",
        "binding_editor_title": "Upravit propojení kanálu {channel}",
        "binding_editor_button_title": "Upravit propojení tlačítka {button}",
        "field_mode": "Režim",
        "field_target": "Cíl",
        "field_target_help": (
            "Vyberte více světel a ovládejte je společně. Všechna dostanou "
            "stejnou hodnotu, kterou nastavuje kolečko."
        ),
        "field_step": "Změna cíle na jedno cvaknutí",
        "field_step_help": "O kolik jedno cvaknutí posune cíl.",
        "field_acceleration": "Zrychlení otáčení",
        "field_acceleration_help": (
            "Čím rychleji otáčíte, tím větší změna cíle na jedno cvaknutí. "
            "0 % znamená vypnuto."
        ),
        "field_transition_help": (
            "Rychlé otáčení přichází po dávkách cvaknutí. Větší dávka se "
            "rozloží nejvýše na tuto dobu; 0 s vyhlazení vypne."
        ),
        "target_empty_is_rotation": (
            "Když pole necháte prázdné, použije se cíl otáčení."
        ),
        "scene_add": "Přidat scénu",
        "scene_add_placeholder": "Přidat scénu…",
        "scene_move_up": "Posunout scénu {scene} výš",
        "scene_move_down": "Posunout scénu {scene} níž",
        "scene_remove": "Odebrat scénu {scene}",
        "ledger_then_release": "{hold}; po uvolnění: {release}",
        "field_transition": "Vyhlazení velkých skoků",
        "field_follower_light": "Follower light (optional)",
        "field_follower_help": "Only follows brightness while already on.",
        "field_follower_offset": "Follower offset (percentage points)",
        "field_follower_min": "Follower minimum brightness",
        "field_min_brightness": "Minimální jas",
        "field_max_brightness": "Maximální jas",
        "field_press_response": "Odezva",
        "rotation_more": "Další nastavení otáčení",
        "gesture_needs_waiting": "Vyžaduje odezvu krátkého stisku „{response}“.",
        "gesture_action": "Akce",
        "gesture_target": "Cíl",
        "field_ramp_direction": "Směr plynulé změny",
        "field_scenes": "Scény",
        "field_scenes_help": (
            "Každý krátký stisk aktivuje další scénu v tomto pořadí."
        ),
        "section_rotation": "Otáčení",
        "click_toggle": "Přepnout cíl",
        "click_on": "Zapnout cíl",
        "click_off": "Vypnout cíl",
        "click_none": "Bez akce",
        "click_scenes": "Procházet scény",
        "click_scene_on": "Spustit scénu",
        "click_script_on": "Spustit skript",
        "click_script_off": "Zastavit skript",
        "click_script_toggle": "Přepnout skript",
        "click_play_pause": "Přehrát / pozastavit",
        "click_play": "Přehrát",
        "click_pause": "Pozastavit",
        "click_stop": "Zastavit",
        "click_next": "Další skladba",
        "click_previous": "Předchozí skladba",
        "click_volume_up": "Hlasitěji",
        "click_volume_down": "Tišeji",
        "click_mute_toggle": "Ztlumit / zrušit ztlumení",
        "click_open": "Otevřít",
        "click_close": "Zavřít",
        "click_lock": "Zamknout",
        "click_start": "Spustit",
        "click_return_home": "Vrátit do stanice",
        "click_locate": "Najít",
        "click_press": "Stisknout tlačítko",
        "click_trigger": "Spustit automatizaci",
        "click_speed_up": "Zrychlit",
        "click_speed_down": "Zpomalit",
        "click_next_option": "Další možnost",
        "click_previous_option": "Předchozí možnost",
        "click_first_option": "První možnost",
        "click_last_option": "Poslední možnost",
        "click_step_up": "Zvýšit",
        "click_step_down": "Snížit",
        "cover_open_warning": (
            "Garážová vrata nebo brána se po stisku otevřou, i když se nikdo nedívá."
        ),
        "script_run_help": (
            "Spustí skript a předá mu, které gesto ho spustilo, v proměnných "
            "gesture, presses, channel, endpoint a device."
        ),
        "script_toggle_help": (
            "Spustí skript, nebo ho zastaví, pokud běží. Přepnutí skriptu "
            "nemůže předat žádné proměnné."
        ),
        "gesture_hold_effect": "Účinek na cíl",
        "hold_toggle": "Provést akci na cíli podržení",
        "hold_ramp": "Plynule měnit cíl otáčení",
        "hold_none": "Bez akce",
        "ramp_direction_alternate": "Střídat zesílení a zeslabení",
        "ramp_direction_up": "Vždy zesílit",
        "ramp_direction_down": "Vždy zeslabit",
        "button_response_instant": "Spustit už při prvním stisku",
        "button_response_fast": "Spustit po prvním krátkém uvolnění",
        "button_response_multi_press": "Počkat, jestli nepřijde další stisk",
        "dual_button_response_instant": "Spustit už při prvním stisku",
        "dual_button_response_fast": "Spustit po prvním krátkém uvolnění",
        "dual_button_response_multi_press": "Počkat, jestli nepřijde další stisk",
        "save_binding": "Uložit propojení",
        "delete_binding": "Smazat propojení",
        "keep_binding": "Ponechat propojení",
        "delete_binding_confirm": (
            "Smazat propojení tohoto kanálu? Kolečko přestane ovládat jeho cíle."
        ),
        "delete_button_binding_confirm": (
            "Smazat propojení tohoto tlačítka? Tlačítko přestane ovládat své cíle."
        ),
        "binding_saved": "Propojení bylo uloženo a aktivováno.",
        "binding_validation_failed": "Opravte označená pole a uložte znovu.",
        "binding_conflict": (
            "Propojení bylo mezitím změněno jinde. Zobrazují se nejnovější uložené "
            "hodnoty; před uložením je zkontrolujte."
        ),
        "binding_save_failed": "Propojení se nepodařilo uložit: {error}",
        "binding_delete_failed": "Propojení se nepodařilo smazat: {error}",
        "binding_test_failed": "Test se nepodařilo spustit: {error}",
        "binding_error_unloaded": "Integrace není načtená.",
        "binding_error_wheel_missing": "Kolečko už není dostupné.",
        "binding_error_binding_missing": "Propojení už neexistuje.",
        "binding_error_channel_occupied": ("Tento kanál kolečka už má jiné propojení."),
        "binding_error_button_occupied": "Toto tlačítko už má jiné propojení.",
        "binding_error_control_mismatch": (
            "Tento ovládací prvek nepatří k vybranému zařízení BILRESA."
        ),
        "binding_error_control_missing": "Tento ovládací prvek už není dostupný.",
        "binding_error_binding_address_mismatch": (
            "Toto propojení patří jinému ovládacímu prvku. Obnovte panel a zkuste "
            "to znovu."
        ),
        "binding_error_gesture_unsupported": (
            "Toto zařízení BILRESA dané gesto nepodporuje."
        ),
        "binding_error_binding_not_configured": (
            "Před testem nejdřív nastavte tento ovládací prvek."
        ),
        "validation_invalid_value": "Vyberte nebo zadejte platnou hodnotu.",
        "validation_follower_overlap": (
            "Choose lights or groups that do not share any members."
        ),
        "validation_target_required": "Vyberte cíl.",
        "validation_ramp_requires_light": (
            "Pro plynulou změnu musí být cílem podržení světlo."
        ),
        "validation_scene_cannot_turn_off": (
            "Scénu lze jen spustit, ne vypnout. Zvolte Přepnout cíl nebo Zapnout cíl."
        ),
        "validation_scenes_required": "Přidejte alespoň jednu scénu.",
        "validation_action_not_supported": (
            "Tento cíl to neumí. Zvolte některou z nabízených akcí."
        ),
        "validation_actions_required": (
            "Přidejte alespoň jednu akci ke spuštění, nebo zvolte jinou akci."
        ),
        "validation_actions_incomplete": "Vyberte akci u každého řádku.",
        "validation_actions_invalid": (
            "To, co jste u akcí napsali, není platné. Opravte to, nebo "
            "stránku znovu načtěte."
        ),
        "validation_scenes_replace_short_press": (
            "Procházení scén nahrazuje krátký stisk, takže nemůže spouštět akce."
        ),
        "validation_mode_target_mismatch": (
            "Vybraný režim otáčení nemůže ovládat tuto entitu."
        ),
        "validation_multiple_targets_require_light_mode": (
            "Více cílů lze použít jen pro světla v režimu stmívání, teploty "
            "bílé nebo barvy."
        ),
        "validation_maximum_must_exceed_minimum": (
            "Maximální jas musí být vyšší než minimální jas."
        ),
        "validation_fast_response_conflicts_with_multi_press": (
            "Rychlé uvolnění nelze kombinovat s dvojitým nebo trojitým stiskem."
        ),
        "validation_instant_response_conflicts_with_multi_press": (
            "Okamžitou odezvu nelze kombinovat s dvojitým nebo trojitým stiskem."
        ),
        "validation_instant_response_conflicts_with_hold": (
            "Okamžitá odezva vyžaduje nastavit podržení na Bez akce."
        ),
        "binding_gesture_rotation": "Otočení doleva / doprava",
        "binding_gesture_short_press": "Krátký stisk",
        "binding_gesture_double_press": "Dvojitý stisk",
        "binding_gesture_triple_press": "Trojitý stisk",
        "binding_gesture_hold": "Podržení",
        "binding_gesture_release": "Uvolnění",
        "action_toggle": "Přepnout",
        "action_turn_on": "Zapnout",
        "action_turn_off": "Vypnout",
        "action_run": "Spustit",
        "action_stop": "Zastavit",
        "action_none": "Bez akce",
        "action_run_actions": "Spustit akce",
        "click_run": "Spustit akce",
        "hold_run": "Spustit akce",
        "actions_label": "Akce ke spuštění",
        "actions_help": (
            "Zapisují se jako v automatizaci. Gesto se jim předá v proměnných "
            "gesture, presses, channel, endpoint a device."
        ),
        "actions_loading": "Načítá se editor akcí Home Assistantu...",
        "actions_fallback": (
            "Editor akcí Home Assistantu tu není dostupný, proto se akce "
            "upravují v jednoduchém seznamu. Jsou to stejná data: nic se "
            "neztratí."
        ),
        "actions_empty": "Zatím žádné akce.",
        "actions_add": "Přidat akci",
        "actions_remove": "Odebrat",
        "actions_service": "Akce",
        "actions_target_ids": "Entity oddělené čárkami",
        "actions_data": "Data (JSON)",
        "actions_json": "Všechny akce jako JSON",
        "actions_json_invalid": "Neplatný JSON nebo nesprávný tvar.",
        "actions_choose": "Vyberte akci",
        "actions_complex": "Složitější akce; upravte ji v JSONu níže:",
        "action_cycle_scenes": "Procházet scény",
        "action_ramp": "Plynule měnit cíl",
        "action_ramp_alternate": "Plynule zesílit nebo zeslabit",
        "action_ramp_up": "Zesílit",
        "action_ramp_down": "Zeslabit",
        "action_stop_ramp": "Zastavit změnu",
        "action_play_pause": "Přehrát / pozastavit",
        "action_play": "Přehrát",
        "action_pause": "Pozastavit",
        "action_next": "Další skladba",
        "action_previous": "Předchozí skladba",
        "action_volume_up": "Hlasitěji",
        "action_volume_down": "Tišeji",
        "action_mute_toggle": "Ztlumit / zrušit ztlumení",
        "action_open": "Otevřít",
        "action_close": "Zavřít",
        "action_lock": "Zamknout",
        "action_start": "Spustit",
        "action_return_home": "Vrátit do stanice",
        "action_locate": "Najít",
        "action_press": "Stisknout tlačítko",
        "action_trigger": "Spustit automatizaci",
        "action_speed_up": "Zrychlit",
        "action_speed_down": "Zpomalit",
        "action_next_option": "Další možnost",
        "action_previous_option": "Předchozí možnost",
        "action_first_option": "První možnost",
        "action_last_option": "Poslední možnost",
        "action_step_up": "Zvýšit",
        "action_step_down": "Snížit",
        "wheel_missing_title": "Zařízení BILRESA už není dostupné",
        "wheel_missing_body": (
            "Zařízení bylo odebráno nebo se integrace znovu načetla. Vraťte se na "
            "přehled."
        ),
        "live_intro": (
            "Otočte kolečkem nebo ho stiskněte. Hned uvidíte rozpoznané gesto "
            "a u nastaveného kanálu také akci odeslanou do cíle."
        ),
        "live_button_intro": (
            "Stiskněte jedno z tlačítek. Hned uvidíte rozpoznané gesto a u "
            "nastaveného tlačítka také akci odeslanou do cíle."
        ),
        "live_result_label": "Výsledek akce",
        "live_event_label": "Poslední gesto",
        "live_listening": "Naslouchám",
        "live_stopped": "Naslouchání zastaveno",
        "live_waiting_title": "Čekám na kolečko",
        "live_waiting_body": (
            "Otočte kolečkem nebo ho stiskněte. Aktivita se zobrazuje jen v tomto "
            "pohledu."
        ),
        "live_button_waiting_title": "Čekám na stisk tlačítka",
        "live_button_waiting_body": (
            "Stiskněte, dvakrát stiskněte nebo podržte libovolné tlačítko. Aktivita "
            "se zobrazuje jen v tomto pohledu."
        ),
        "live_error": (
            "Živá aktivita se zastavila. Odejděte z Živého testu a znovu ho otevřete."
        ),
        "result_unavailable": "Gesto rozpoznáno",
        "result_unavailable_detail": (
            "Pro tuto událost nejsou dostupné podrobnosti výsledku."
        ),
        "result_pending_detail": "Čekám na dokončení nastavené akce.",
        "result_not_configured_channel_detail": ("Gesto dorazilo do Home Assistantu."),
        "result_not_configured_button_detail": ("Gesto dorazilo do Home Assistantu."),
        "result_gesture_rotate": "Otočení rozpoznáno",
        "result_gesture_press": "Stisk rozpoznán",
        "result_gesture_double_press": "Dvojitý stisk rozpoznán",
        "result_gesture_triple_press": "Trojitý stisk rozpoznán",
        "result_gesture_hold": "Podržení rozpoznáno",
        "result_gesture_release": "Uvolnění rozpoznáno",
        "result_gesture_received": "Gesto rozpoznáno",
        "dispatch_success": "Akce byla odeslána",
        "dispatch_accepted": "Home Assistant akci přijal",
        "dispatch_pending": "Odesílám akci do Home Assistantu",
        "dispatch_skipped": "Propojení akci přeskočilo",
        "dispatch_not_configured": "Tento kanál zatím nic neovládá",
        "dispatch_not_configured_button": ("Toto tlačítko zatím nic neovládá"),
        "dispatch_completed": "Akce propojení byla dokončena",
        "dispatch_received": "Gesto přijato; čekám na výsledek",
        "dispatch_failed": "Akce nebyla odeslána",
        "dispatch_unknown": "Stav akce není dostupný",
        "result_kind_brightness": "Jas",
        "result_kind_color_temperature": "Teplota barvy",
        "result_kind_color": "Barva",
        "result_kind_volume": "Hlasitost",
        "result_kind_position": "Poloha",
        "result_kind_temperature": "Teplota",
        "result_kind_fan_speed": "Rychlost ventilátoru",
        "result_kind_value": "Hodnota",
        "result_scene": "Scéna {position}/{total} · {target}",
        "result_entity_action": "{action} · {target}",
        "result_ramp_stopped": "Plynulá změna byla zastavena",
        "result_fast_press_complete": ("Jednoduchý stisk byl odeslán okamžitě"),
        "service_toggle": "Přepnout",
        "service_turn_on": "Zapnout",
        "service_turn_off": "Vypnout",
        "service_run": "Spustit",
        "service_stop": "Zastavit",
        "source_panel_test": "Spuštěno testovacími ovladači v panelu",
        "test_controls_heading": "Otestovat nastavené akce",
        "test_controls_intro": (
            "Tyto ovladače spustí skutečné propojení bez fyzického kolečka. "
            "Cílové entity se mohou okamžitě změnit."
        ),
        "test_controls_button_intro": (
            "Tyto ovladače spustí skutečné propojení bez stisku fyzického tlačítka. "
            "Cílové entity se mohou okamžitě změnit."
        ),
        "test_channel": "Test kanálu {channel}",
        "test_button": "Test tlačítka {button}",
        "test_rotate_down": "Otočit dolů",
        "test_rotate_up": "Otočit nahoru",
        "test_single": "Jednoduchý stisk",
        "test_double": "Dvojitý stisk",
        "test_triple": "Trojitý stisk",
        "test_hold": "Začít podržení",
        "test_release": "Uvolnit podržení",
        "test_no_bindings": "Pro testování nejdřív nastavte některý kanál.",
        "test_no_button_bindings": ("Pro testování nejdřív nastavte některé tlačítko."),
        "direction_up": "nahoru",
        "direction_down": "dolů",
        "gesture_rotate": ("Kanál {channel} · otočení {direction} · {delta} cvaknutí"),
        "gesture_press_single": "Kanál {channel} · jednoduchý stisk",
        "gesture_press_double": "Kanál {channel} · dvojitý stisk",
        "gesture_press_triple": "Kanál {channel} · trojitý stisk",
        "gesture_hold": "Kanál {channel} · podržení",
        "gesture_release": "Kanál {channel} · uvolnění",
        "gesture_unknown": "Kanál {channel} · přijata aktivita",
        "live_channels_heading": "Kanály",
        "gesture_button_press_single": "Tlačítko {button} · jednoduchý stisk",
        "gesture_button_press_double": "Tlačítko {button} · dvojitý stisk",
        "gesture_button_hold": "Tlačítko {button} · podržení",
        "gesture_button_release": "Tlačítko {button} · uvolnění",
        "gesture_button_unknown": "Tlačítko {button} · přijata aktivita",
        "gesture_observed_duration": "zachyceno {duration} s",
        "live_buttons_heading": "Tlačítka",
        "live_recent": "Poslední události",
        "live_setup_channel": "Nastavit kanál {channel}",
        "live_setup_button": "Nastavit tlačítko {button}",
        "diagnostics_heading": "Stav zařízení",
        "diagnostics_intro": (
            "Stav z Home Assistantu pouze pro čtení. Soukromé identifikátory Matter "
            "se nezobrazují."
        ),
        "diagnostic_availability": "Dostupnost zařízení",
        "diagnostic_matter": "Připojení Matter",
        "diagnostic_source": "Zdroj událostí",
        "diagnostic_link": "Propojení se zařízením Matter",
        "diagnostic_linked": "Propojeno",
        "diagnostic_not_linked": "Nepropojeno",
        "diagnostic_health_ok": "Kolečko je připravené",
        "diagnostic_health_attention": "Kolečko vyžaduje pozornost",
        "diagnostic_health_ok_body": (
            "Matter i živé doručování událostí jsou připojené."
        ),
        "diagnostic_connection_heading": "Připojení",
        "diagnostic_activity_heading": "Aktivita",
        "diagnostic_technical_details": "Technické podrobnosti",
        "diagnostic_contract": "Kontrakt panelu",
        "source_core": "Matter klient Home Assistantu",
        "source_fallback": "Pasivní záložní WebSocket",
        "source_unloaded": "Integrace není načtená",
        "recovery_heading": "Doporučený krok",
        "recovery_ok": "Není potřeba žádný opravný krok.",
        "recovery_matter": (
            "Zkontrolujte integraci Matter a připojení k Matter Serveru."
        ),
        "recovery_unavailable": (
            "Zkontrolujte baterii kolečka a přibližte ho k síti Matter."
        ),
        "recovery_unknown": (
            "Zkontrolujte, že je kolečko v Home Assistantu, a potom integraci znovu "
            "načtěte."
        ),
        "menu": "Otevřít postranní panel Home Assistant",
    },
    "nl": {
        "action_stop_hold_and_run": (
            "Acties bij vasthouden stoppen en acties na loslaten uitvoeren"
        ),
        "mode_buttons": "Alleen knoppen (draaien doet niets)",
        "gesture_activation": "Knopacties",
        "gesture_active": "Actief",
        "gesture_shadow": "Alleen volgen (draaien blijft actief)",
        "hold_stop_on_release": "Bij loslaten",
        "hold_stop_enabled": "Acties bij vasthouden stoppen",
        "hold_stop_disabled": "Acties bij vasthouden laten aflopen",
        "hold_max_seconds": "Maximale duur van vasthouden (seconden)",
        "release_actions": "Acties na loslaten",
        "action_stop_hold": "Acties bij vasthouden stoppen",
        "shared_profile_notice": (
            "Gedeeld profiel: {name}. Als u dit kanaal opslaat, worden de "
            "bestaande bedieningskoppelingen op de gekoppelde afstandsbedieningen"
            " bijgewerkt."
        ),
        "connected": "Verbonden",
        "unavailable": "Niet beschikbaar",
        "unknown": "Geen status ontvangen",
        "not_configured": "Niet ingesteld",
        "add_binding": "Bedieningskoppeling toevoegen",
        "edit_binding": "Bediening instellen",
        "community_tool_link": "Ontwerp labels voor uw schakelaars",
        "community_tool_note": "Hulpmiddel van Liquidmasl uit de community",
        "community_tool_new_window": "opent in een nieuw venster",
        "save_short": "Opslaan",
        "discard_changes": "Verwerpen",
        "discard_armed": "Verwerpen?",
        "target_unavailable": "{target} — niet beschikbaar",
        "target_missing": "{target} — bestaat niet meer",
        "configured": "Ingesteld",
        "button_actions": "Knopacties",
        "multiple_targets": "{count} doelen",
        "mode_brightness": "Vloeiend dimmen",
        "mode_color_temp": "Kleurtemperatuur",
        "mode_color": "Kleur",
        "mode_volume": "Volume",
        "mode_cover_position": "Stand van afdekking",
        "mode_temperature": "Temperatuur",
        "mode_fan_speed": "Ventilatorsnelheid",
        "mode_number": "Waarde",
        "mode_scenes": "Scènes ({count})",
        "quantity_brightness": "Helderheid",
        "quantity_color_temp": "Wittemperatuur",
        "quantity_color": "Kleur",
        "quantity_volume": "Volume",
        "quantity_cover_position": "Stand",
        "quantity_temperature": "Temperatuur",
        "quantity_fan_speed": "Snelheid",
        "quantity_number": "Waarde",
        "no_activity": "Nog geen activiteit",
        "last_on_channel": "laatst op kanaal {channel}",
        "last_on_button": "laatst op knop {button}",
        "overview_title": "BILRESA-apparaten",
        "summary_connected": "{count} verbonden",
        "summary_unavailable": "{count} niet beschikbaar",
        "summary_unknown": "{count} zonder status",
        "matter_connected": "Matter verbonden",
        "matter_offline": "Matter offline",
        "banner_matter_offline": (
            "Matter is niet verbonden. De apparaten hieronder tonen hun laatst "
            "bekende status."
        ),
        "banner_updates_stopped": (
            "Live bijwerken is gestopt. Deze weergave is mogelijk verouderd."
        ),
        "banner_target_missing": (
            "Bedieningskoppelingen op {count} apparaten verwijzen naar entiteiten"
            " die niet meer bestaan in Home Assistant. Open een gemarkeerde "
            "bediening en kies een ander doel."
        ),
        "banner_target_missing_named": (
            "De bedieningskoppeling op kanaal {channel} van {wheel} verwijst naar"
            " een entiteit die niet meer bestaat in Home Assistant. Open het "
            "kanaal en kies een ander doel."
        ),
        "banner_target_missing_button_named": (
            "De bedieningskoppeling op knop {button} van {wheel} verwijst naar "
            "een entiteit die niet meer bestaat in Home Assistant. Open de knop "
            "en kies een ander doel."
        ),
        "empty_title": "Geen BILRESA-apparaten gevonden",
        "empty_connected": (
            "De integratie is verbonden, maar heeft nog geen apparaat gevonden."
        ),
        "empty_offline": (
            "Home Assistant is niet verbonden met Matter. Daardoor zijn er geen "
            "apparaten zichtbaar."
        ),
        "error_title": "De integratie is niet bereikbaar",
        "retry": "Opnieuw proberen",
        "back": "Terug naar alle BILRESA-apparaten",
        "detail_views": "Apparaatweergaven",
        "field_step_curve": "Verdeling van draaistappen",
        "field_step_curve_help": (
            "Springt de helderheid bij snel draaien, vooral bij lage waarden? "
            "Kies dan Gelijkmatig voor het oog en probeer opnieuw. Laat dit op "
            "Lineair staan als de lamp het dimmen zelf al gelijkmatig verdeelt. "
            "Dubbel corrigeren geeft een minder goed resultaat."
        ),
        "step_curve_linear": "Lineair (standaard)",
        "step_curve_perceptual": "Gelijkmatig voor het oog",
        "channel_off_note": "doet niets totdat u het hier weer inschakelt.",
        "settings_dial_intro": (
            "Elk kanaal heeft een getalwaarde van 1 tot 100. Draaien verandert "
            "die waarde en automatiseringen kunnen ze uitlezen. Dit staat los van"
            " de bedieningskoppeling."
        ),
        "settings_dial_title": "Draaiwaarde",
        "settings_step_help": "In de eigen eenheden van de draaiwaarde, van 1 tot 100.",
        "settings_channel_enabled": "Kanaal {channel} actief",
        "settings_step": "Wijziging van draaiwaarde per draaistap",
        "settings_acceleration": "Versnelling van draaiwaarde",
        "settings_acceleration_help": (
            "Sneller draaien verandert de draaiwaarde meer per draaistap. 0 % "
            "schakelt dit uit."
        ),
        "settings_save": "Draaiwaarde opslaan",
        "settings_saved": "Draaiwaarde opgeslagen",
        "settings_disabled_badge": "Uit",
        "settings_error_conflict": (
            "Deze instellingen zijn elders gewijzigd. Open het draaiwiel opnieuw "
            "en probeer nogmaals."
        ),
        "settings_error_generic": "De instellingen konden niet worden opgeslagen.",
        "tab_channels": "Kanalen",
        "tab_buttons": "Knoppen",
        "tab_live": "Live testen",
        "tab_diagnostics": "Diagnose",
        "detail_area_none": "Geen ruimte",
        "detail_last_activity": "Laatste activiteit",
        "detail_last_channel": "Laatst actieve kanaal",
        "detail_no_last_channel": "Nog geen kanaal waargenomen",
        "detail_last_button": "Laatst actieve knop",
        "detail_no_last_button": "Nog geen knop waargenomen",
        "detail_channels_heading": "Bediening per fysieke stand",
        "channel_title": "Kanaal {channel}",
        "channel_binding": "Bedieningskoppeling",
        "button_title": "Knop {button}",
        "target_none": "Geen doel ingesteld",
        "target_same_as_rotation": "Hetzelfde doel als bij draaien",
        "binding_editor_title": "Bediening van kanaal {channel} instellen",
        "binding_editor_button_title": "Bediening van knop {button} instellen",
        "field_mode": "Modus",
        "field_target": "Doel",
        "field_target_help": (
            "Een doel is bijvoorbeeld een lamp of luidspreker. Kies meerdere "
            "lampen om ze samen te bedienen. Ze krijgen allemaal dezelfde waarde "
            "van het draaiwiel."
        ),
        "field_step": "Wijziging van doel per draaistap",
        "field_step_help": "Hoeveel één draaistap de waarde van het doel verandert.",
        "field_acceleration": "Versnelling bij draaien",
        "field_acceleration_help": (
            "Sneller draaien verandert het doel meer per draaistap. 0 % schakelt "
            "dit uit."
        ),
        "field_transition_help": (
            "Snel draaien komt binnen als groepen draaistappen. Een grotere groep"
            " wordt over maximaal deze tijd verdeeld. 0 s schakelt het vloeiend "
            "verdelen uit."
        ),
        "target_empty_is_rotation": (
            "Laat leeg om het doel van de draaibediening te gebruiken."
        ),
        "scene_add": "Scène toevoegen",
        "scene_add_placeholder": "Scène toevoegen…",
        "scene_move_up": "{scene} omhoog verplaatsen",
        "scene_move_down": "{scene} omlaag verplaatsen",
        "scene_remove": "{scene} verwijderen",
        "ledger_then_release": "{hold}; bij loslaten: {release}",
        "field_transition": "Grote sprongen vloeiend verdelen",
        "field_follower_light": "Meedimmende lamp (optioneel)",
        "field_follower_help": "Volgt de helderheid alleen als de lamp al aan is.",
        "field_follower_offset": (
            "Helderheidsverschil van meedimmende lamp (procentpunten)"
        ),
        "field_follower_min": "Minimale helderheid van meedimmende lamp",
        "field_min_brightness": "Minimale helderheid",
        "field_max_brightness": "Maximale helderheid",
        "field_press_response": "Reactie",
        "rotation_more": "Meer draai-instellingen",
        "gesture_needs_waiting": "Vereist de reactie op kort drukken ‘{response}’.",
        "gesture_action": "Actie",
        "gesture_target": "Doel",
        "field_ramp_direction": "Dimrichting",
        "field_scenes": "Scènes",
        "field_scenes_help": (
            "Elke korte druk activeert de volgende scène, in deze volgorde."
        ),
        "section_rotation": "Draaien",
        "click_toggle": "Doel aan/uit schakelen",
        "click_on": "Doel inschakelen",
        "click_off": "Doel uitschakelen",
        "click_none": "Geen actie",
        "click_scenes": "Scènes doorlopen",
        "click_scene_on": "Scène activeren",
        "click_script_on": "Script uitvoeren",
        "click_script_off": "Script stoppen",
        "click_script_toggle": "Script starten/stoppen",
        "click_play_pause": "Afspelen / pauzeren",
        "click_play": "Afspelen",
        "click_pause": "Pauzeren",
        "click_stop": "Stoppen",
        "click_next": "Volgend nummer",
        "click_previous": "Vorig nummer",
        "click_volume_up": "Volume verhogen",
        "click_volume_down": "Volume verlagen",
        "click_mute_toggle": "Geluid dempen / herstellen",
        "click_open": "Openen",
        "click_close": "Sluiten",
        "click_lock": "Vergrendelen",
        "click_start": "Starten",
        "click_return_home": "Terug naar laadstation",
        "click_locate": "Zoeken",
        "click_press": "Op de knop drukken",
        "click_trigger": "Automatisering uitvoeren",
        "click_speed_up": "Snelheid verhogen",
        "click_speed_down": "Snelheid verlagen",
        "click_next_option": "Volgende optie",
        "click_previous_option": "Vorige optie",
        "click_first_option": "Eerste optie",
        "click_last_option": "Laatste optie",
        "click_step_up": "Verhogen",
        "click_step_down": "Verlagen",
        "cover_open_warning": (
            "Een druk op deze knop opent een garagepoort of hek, ook als niemand "
            "toezicht houdt."
        ),
        "script_run_help": (
            "Start het script en geeft de herkende bediening door via de "
            "variabelen gesture, presses, channel, endpoint en device."
        ),
        "script_toggle_help": (
            "Start het script of stopt het als het al loopt. Bij starten/stoppen "
            "kunnen geen variabelen worden meegegeven."
        ),
        "gesture_hold_effect": "Effect op het doel",
        "hold_toggle": "Actie op het doel voor vasthouden",
        "hold_ramp": "Doel van draaibediening dimmen",
        "hold_none": "Geen actie",
        "ramp_direction_alternate": "Afwisselend lichter en donkerder",
        "ramp_direction_up": "Altijd lichter",
        "ramp_direction_down": "Altijd donkerder",
        "button_response_instant": "Uitvoeren zodra u drukt",
        "button_response_fast": "Uitvoeren na kort loslaten",
        "button_response_multi_press": "Enkel/dubbel/driemaal herkennen",
        "dual_button_response_instant": "Uitvoeren zodra u drukt",
        "dual_button_response_fast": "Uitvoeren na kort loslaten",
        "dual_button_response_multi_press": "Enkel of dubbel herkennen",
        "save_binding": "Bedieningskoppeling opslaan",
        "delete_binding": "Bedieningskoppeling verwijderen",
        "keep_binding": "Bedieningskoppeling behouden",
        "delete_binding_confirm": (
            "Deze bedieningskoppeling verwijderen? Dit kanaal van het draaiwiel "
            "bedient de doelen dan niet meer."
        ),
        "delete_button_binding_confirm": (
            "Deze bedieningskoppeling verwijderen? Deze knop bedient de doelen "
            "dan niet meer."
        ),
        "binding_saved": "Bedieningskoppeling opgeslagen en geactiveerd.",
        "binding_validation_failed": (
            "Verbeter de gemarkeerde velden en sla opnieuw op."
        ),
        "binding_conflict": (
            "Deze bedieningskoppeling is elders gewijzigd. De laatst opgeslagen "
            "waarden staan nu in beeld. Controleer ze voordat u opslaat."
        ),
        "binding_save_failed": (
            "De bedieningskoppeling kon niet worden opgeslagen: {error}"
        ),
        "binding_delete_failed": (
            "De bedieningskoppeling kon niet worden verwijderd: {error}"
        ),
        "binding_test_failed": "De test kon niet worden uitgevoerd: {error}",
        "binding_error_unloaded": "De integratie is niet geladen.",
        "binding_error_wheel_missing": "Het draaiwiel is niet meer beschikbaar.",
        "binding_error_binding_missing": "De bedieningskoppeling bestaat niet meer.",
        "binding_error_channel_occupied": (
            "Dit kanaal heeft al een andere bedieningskoppeling."
        ),
        "binding_error_button_occupied": (
            "Deze knop heeft al een andere bedieningskoppeling."
        ),
        "binding_error_control_mismatch": (
            "Deze bediening hoort niet bij het gekozen BILRESA-apparaat."
        ),
        "binding_error_control_missing": "Deze bediening is niet meer beschikbaar.",
        "binding_error_binding_address_mismatch": (
            "Deze bedieningskoppeling hoort bij een andere bediening. Laad het "
            "paneel opnieuw en probeer nogmaals."
        ),
        "binding_error_gesture_unsupported": (
            "Dit BILRESA-apparaat ondersteunt deze bediening niet."
        ),
        "binding_error_binding_not_configured": (
            "Stel deze bediening in voordat u ze test."
        ),
        "validation_invalid_value": "Kies of vul een geldige waarde in.",
        "validation_follower_overlap": (
            "Kies lampen of groepen zonder gemeenschappelijke leden."
        ),
        "validation_target_required": "Kies een doel.",
        "validation_ramp_requires_light": (
            "Dimmen bij vasthouden vereist een lamp als doel."
        ),
        "validation_scene_cannot_turn_off": (
            "Een scène kan alleen worden geactiveerd. U kunt ze niet "
            "uitschakelen. Kies Doel aan/uit schakelen of Doel inschakelen."
        ),
        "validation_scenes_required": "Voeg minstens één scène toe.",
        "validation_action_not_supported": (
            "Dit doel ondersteunt deze actie niet. Kies een van de beschikbare acties."
        ),
        "validation_actions_required": (
            "Voeg minstens één uit te voeren actie toe of kies een andere actie."
        ),
        "validation_actions_incomplete": "Kies voor elke rij een actie.",
        "validation_actions_invalid": (
            "De ingevoerde acties zijn ongeldig. Verbeter ze of laad opnieuw."
        ),
        "validation_scenes_replace_short_press": (
            "Scènes doorlopen vervangt kort drukken. Die druk kan dan geen andere"
            " acties uitvoeren."
        ),
        "validation_mode_target_mismatch": (
            "De gekozen draaimodus kan deze entiteit niet bedienen."
        ),
        "validation_multiple_targets_require_light_mode": (
            "Meerdere doelen werken alleen voor lampen in de modi dimmen, "
            "kleurtemperatuur of kleur."
        ),
        "validation_maximum_must_exceed_minimum": (
            "De maximale helderheid moet groter zijn dan de minimale helderheid."
        ),
        "validation_fast_response_conflicts_with_multi_press": (
            "Reageren na kort loslaten kan niet samen met dubbel of driemaal drukken."
        ),
        "validation_instant_response_conflicts_with_multi_press": (
            "Meteen reageren kan niet samen met dubbel of driemaal drukken."
        ),
        "validation_instant_response_conflicts_with_hold": (
            "Meteen reageren vereist dat de actie bij vasthouden op Geen actie staat."
        ),
        "binding_gesture_rotation": "Links / rechts draaien",
        "binding_gesture_short_press": "Kort drukken",
        "binding_gesture_double_press": "Dubbel drukken",
        "binding_gesture_triple_press": "Driemaal drukken",
        "binding_gesture_hold": "Vasthouden",
        "binding_gesture_release": "Loslaten",
        "action_toggle": "Aan/uit schakelen",
        "action_turn_on": "Inschakelen",
        "action_turn_off": "Uitschakelen",
        "action_run": "Uitvoeren",
        "action_stop": "Stoppen",
        "action_none": "Geen actie",
        "action_run_actions": "Acties uitvoeren",
        "click_run": "Acties uitvoeren",
        "hold_run": "Acties uitvoeren",
        "actions_label": "Uit te voeren acties",
        "actions_help": (
            "Schrijf de acties zoals in een automatisering. De bediening wordt "
            "doorgegeven via de variabelen gesture, presses, channel, endpoint en"
            " device."
        ),
        "actions_loading": "De actie-editor van Home Assistant wordt geladen…",
        "actions_fallback": (
            "De actie-editor van Home Assistant is hier niet beschikbaar. U kunt "
            "de acties als eenvoudige lijst bewerken. De gegevens blijven "
            "dezelfde; er gaat niets verloren."
        ),
        "actions_empty": "Nog geen acties.",
        "actions_add": "Actie toevoegen",
        "actions_remove": "Verwijderen",
        "actions_service": "Actie",
        "actions_target_ids": "Entiteiten, gescheiden door komma’s",
        "actions_data": "Gegevens (JSON)",
        "actions_json": "Alle acties als JSON",
        "actions_json_invalid": "Dit is geen geldige JSON in de verwachte vorm.",
        "actions_choose": "Kies een actie",
        "actions_complex": (
            "Dit is een uitgebreidere actie. Bewerk ze hieronder in JSON:"
        ),
        "action_cycle_scenes": "Scènes doorlopen",
        "action_ramp": "Doel dimmen",
        "action_ramp_alternate": "Lichter of donkerder dimmen",
        "action_ramp_up": "Lichter dimmen",
        "action_ramp_down": "Donkerder dimmen",
        "action_stop_ramp": "Dimmen stoppen",
        "action_play_pause": "Afspelen / pauzeren",
        "action_play": "Afspelen",
        "action_pause": "Pauzeren",
        "action_next": "Volgend nummer",
        "action_previous": "Vorig nummer",
        "action_volume_up": "Volume verhogen",
        "action_volume_down": "Volume verlagen",
        "action_mute_toggle": "Geluid dempen / herstellen",
        "action_open": "Openen",
        "action_close": "Sluiten",
        "action_lock": "Vergrendelen",
        "action_start": "Starten",
        "action_return_home": "Terug naar laadstation",
        "action_locate": "Zoeken",
        "action_press": "Op de knop drukken",
        "action_trigger": "Automatisering uitvoeren",
        "action_speed_up": "Snelheid verhogen",
        "action_speed_down": "Snelheid verlagen",
        "action_next_option": "Volgende optie",
        "action_previous_option": "Vorige optie",
        "action_first_option": "Eerste optie",
        "action_last_option": "Laatste optie",
        "action_step_up": "Verhogen",
        "action_step_down": "Verlagen",
        "wheel_missing_title": "BILRESA-apparaat niet meer beschikbaar",
        "wheel_missing_body": (
            "Het apparaat is verwijderd of de integratie is opnieuw geladen. Ga "
            "terug naar het overzicht."
        ),
        "live_intro": (
            "Draai aan het wiel of druk erop. U ziet eerst de herkende bediening."
            " Bij ingestelde kanalen ziet u daarna de actie die naar het doel is "
            "gestuurd."
        ),
        "live_button_intro": (
            "Druk op een van de knoppen. U ziet eerst de herkende bediening. Bij "
            "ingestelde knoppen ziet u daarna de actie die naar het doel is "
            "gestuurd."
        ),
        "live_result_label": "Actieresultaat",
        "live_event_label": "Laatste bediening",
        "live_listening": "Luisteren",
        "live_stopped": "Luisteren gestopt",
        "live_waiting_title": "Wachten op het draaiwiel",
        "live_waiting_body": (
            "Draai aan dit wiel of druk erop. Activiteit verschijnt alleen "
            "terwijl deze weergave open is."
        ),
        "live_button_waiting_title": "Wachten op een druk op de knop",
        "live_button_waiting_body": (
            "Druk eenmaal of tweemaal op een knop of houd ze vast. Activiteit "
            "verschijnt alleen terwijl deze weergave open is."
        ),
        "live_error": (
            "Live activiteit is gestopt. Sluit Live testen en open het opnieuw om"
            " nogmaals te proberen."
        ),
        "result_unavailable": "Bediening herkend",
        "result_unavailable_detail": (
            "Voor deze gebeurtenis is geen gedetailleerd resultaat beschikbaar."
        ),
        "result_pending_detail": "Wachten tot de ingestelde actie klaar is.",
        "result_not_configured_channel_detail": (
            "De bediening heeft Home Assistant bereikt."
        ),
        "result_not_configured_button_detail": (
            "De bediening heeft Home Assistant bereikt."
        ),
        "result_gesture_rotate": "Draaien herkend",
        "result_gesture_press": "Drukken herkend",
        "result_gesture_double_press": "Dubbel drukken herkend",
        "result_gesture_triple_press": "Driemaal drukken herkend",
        "result_gesture_hold": "Vasthouden herkend",
        "result_gesture_release": "Loslaten herkend",
        "result_gesture_received": "Bediening herkend",
        "dispatch_success": "Actie verstuurd",
        "dispatch_accepted": "Home Assistant heeft de actie aanvaard",
        "dispatch_pending": "Actie wordt naar Home Assistant gestuurd",
        "dispatch_skipped": "Bedieningskoppeling heeft de actie overgeslagen",
        "dispatch_not_configured": "Dit kanaal bedient nog niets",
        "dispatch_not_configured_button": "Deze knop bedient nog niets",
        "dispatch_completed": "Actie van bedieningskoppeling voltooid",
        "dispatch_received": "Bediening ontvangen; wachten op resultaat",
        "dispatch_failed": "Actie niet verstuurd",
        "dispatch_unknown": "Actiestatus niet beschikbaar",
        "result_kind_brightness": "Helderheid",
        "result_kind_color_temperature": "Kleurtemperatuur",
        "result_kind_color": "Kleur",
        "result_kind_volume": "Volume",
        "result_kind_position": "Stand",
        "result_kind_temperature": "Temperatuur",
        "result_kind_fan_speed": "Ventilatorsnelheid",
        "result_kind_value": "Waarde",
        "result_scene": "Scène {position}/{total} · {target}",
        "result_entity_action": "{action} · {target}",
        "result_ramp_stopped": "Dimmen bij vasthouden gestopt",
        "result_fast_press_complete": "Enkel drukken meteen verwerkt",
        "service_toggle": "Aan/uit schakelen",
        "service_turn_on": "Inschakelen",
        "service_turn_off": "Uitschakelen",
        "service_run": "Uitvoeren",
        "service_stop": "Stoppen",
        "source_panel_test": "Gestart met de testknoppen in het paneel",
        "test_controls_heading": "Ingestelde acties testen",
        "test_controls_intro": (
            "Deze knoppen voeren de echte bedieningskoppeling uit zonder fysiek "
            "draaiwiel. Ze kunnen doelen onmiddellijk veranderen."
        ),
        "test_controls_button_intro": (
            "Deze knoppen voeren de echte bedieningskoppeling uit zonder op de "
            "fysieke knop te drukken. Ze kunnen doelen onmiddellijk veranderen."
        ),
        "test_channel": "Kanaal {channel} testen",
        "test_button": "Knop {button} testen",
        "test_rotate_down": "Omlaag draaien",
        "test_rotate_up": "Omhoog draaien",
        "test_single": "Enkel drukken",
        "test_double": "Dubbel drukken",
        "test_triple": "Driemaal drukken",
        "test_hold": "Vasthouden starten",
        "test_release": "Loslaten na vasthouden",
        "test_no_bindings": "Stel een kanaal in om de paneeltests te gebruiken.",
        "test_no_button_bindings": "Stel een knop in om de paneeltests te gebruiken.",
        "direction_up": "omhoog",
        "direction_down": "omlaag",
        "gesture_rotate": (
            "Kanaal {channel} · {direction} draaien · {delta} draaistappen"
        ),
        "gesture_press_single": "Kanaal {channel} · enkel drukken",
        "gesture_press_double": "Kanaal {channel} · dubbel drukken",
        "gesture_press_triple": "Kanaal {channel} · driemaal drukken",
        "gesture_hold": "Kanaal {channel} · vasthouden",
        "gesture_release": "Kanaal {channel} · loslaten",
        "gesture_unknown": "Kanaal {channel} · activiteit ontvangen",
        "live_channels_heading": "Kanalen",
        "gesture_button_press_single": "Knop {button} · enkel drukken",
        "gesture_button_press_double": "Knop {button} · dubbel drukken",
        "gesture_button_hold": "Knop {button} · vasthouden",
        "gesture_button_release": "Knop {button} · loslaten",
        "gesture_button_unknown": "Knop {button} · activiteit ontvangen",
        "gesture_observed_duration": "{duration} s waargenomen",
        "live_buttons_heading": "Knoppen",
        "live_recent": "Laatste gebeurtenissen",
        "live_setup_channel": "Kanaal {channel} instellen",
        "live_setup_button": "Knop {button} instellen",
        "diagnostics_heading": "Apparaatstatus",
        "diagnostics_intro": (
            "Status uit Home Assistant, alleen om te lezen. Privé-identificatoren"
            " van Matter worden niet getoond."
        ),
        "diagnostic_availability": "Beschikbaarheid van apparaat",
        "diagnostic_matter": "Matter-verbinding",
        "diagnostic_source": "Bron van gebeurtenissen",
        "diagnostic_link": "Koppeling met Matter-apparaat",
        "diagnostic_linked": "Gekoppeld",
        "diagnostic_not_linked": "Niet gekoppeld",
        "diagnostic_health_ok": "Draaiwiel is klaar",
        "diagnostic_health_attention": "Draaiwiel vraagt aandacht",
        "diagnostic_health_ok_body": (
            "Matter en de live ontvangst van gebeurtenissen zijn verbonden."
        ),
        "diagnostic_connection_heading": "Verbinding",
        "diagnostic_activity_heading": "Activiteit",
        "diagnostic_technical_details": "Technische gegevens",
        "diagnostic_contract": "Paneelcontract",
        "source_core": "Matter-client van Home Assistant",
        "source_fallback": "Passieve reserveverbinding via WebSocket",
        "source_unloaded": "Integratie niet geladen",
        "recovery_heading": "Aanbevolen stap",
        "recovery_ok": "Er is geen herstelactie nodig.",
        "recovery_matter": (
            "Controleer de Matter-integratie en de verbinding met Matter Server."
        ),
        "recovery_unavailable": (
            "Controleer de batterij van het draaiwiel en breng het dichter bij "
            "het Matter-netwerk."
        ),
        "recovery_unknown": (
            "Controleer of het draaiwiel aanwezig is in Home Assistant. Laad "
            "daarna de integratie opnieuw."
        ),
        "menu": "Zijbalk van Home Assistant openen",
    },
}


def resolve_language(language: str | None) -> str:
    """Pick the closest language we speak.

    `hass.config.language` can be a regional tag such as `en-GB`; match on the
    base tag before giving up, so a British install does not silently fall back
    when English exists.
    """
    if not language:
        return DEFAULT_LANGUAGE
    if language in STRINGS:
        return language
    base = language.split("-", 1)[0].lower()
    return base if base in STRINGS else DEFAULT_LANGUAGE


def panel_strings(language: str | None) -> dict[str, str]:
    """Every string the frontend renders, in the requested language."""
    return dict(STRINGS[resolve_language(language)])


def localize(language: str | None, key: str, **placeholders: Any) -> str:
    """One string, with its placeholders filled.

    Falls back to English for a key missing from another language rather than
    rendering the raw key at a user. The alignment test should make that
    unreachable, but a user seeing `mode_brightness` is worse than a user seeing
    English.
    """
    resolved = resolve_language(language)
    template = STRINGS[resolved].get(key) or STRINGS[DEFAULT_LANGUAGE].get(key, key)
    try:
        return template.format(**placeholders)
    except (KeyError, IndexError):
        return template
