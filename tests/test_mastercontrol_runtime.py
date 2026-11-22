"""Exercise the actual HA Script engine, including serialized nested templates."""

import asyncio

from homeassistant.core import HomeAssistant, callback

from custom_components.ikea_bilresa.binding import LightBinding
from custom_components.ikea_bilresa.engine import WheelAction


async def test_a_real_templated_hold_runs_and_stops_on_release(tmp_path, monkeypatch):
    hass = HomeAssistant(str(tmp_path))
    observed = []
    ready = asyncio.Event()

    @callback
    def receive(event):
        observed.append(event.data)
        ready.set()

    unsubscribe = hass.bus.async_listen("mastercontrol_test", receive)
    binding = LightBinding(
        hass,
        {
            "node_id": "101",
            "channel": "1",
            "target": "light.example",
            "hold_action": "run",
            "hold_stop_on_release": True,
            "hold_max_seconds": 1,
            "hold_sequence": [
                {"variables": {"probe_value": "{{ 1 + 1 }}"}},
                {
                    "repeat": {
                        "while": [
                            {"condition": "template", "value_template": "{{ true }}"}
                        ],
                        "sequence": [
                            {
                                "event": "mastercontrol_test",
                                "event_data": {"value": "{{ probe_value }}"},
                            },
                            {"delay": {"seconds": 1}},
                        ],
                    }
                },
            ],
        },
    )
    # Registry extraction is covered separately; this test uses no entities.
    monkeypatch.setattr(binding, "_sequence_entities", lambda _script: set())
    action = {"node_id": 101, "wheel_name": "Example", "channel": 1, "endpoint_id": 3}
    try:
        binding._handle_action(WheelAction(**action, type="hold"))
        await asyncio.wait_for(ready.wait(), timeout=2)
        assert observed == [{"value": 2}]
        binding._handle_action(WheelAction(**action, type="release"))
        await hass.async_block_till_done()
        assert observed == [{"value": 2}]
        assert not binding._hold_active
    finally:
        binding._stop_hold_sequence()
        binding._stop_sequences()
        unsubscribe()
        await hass.async_block_till_done()
