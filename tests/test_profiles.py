"""Configuration is shared; physical state and subentry identities are not."""

from types import SimpleNamespace
from unittest.mock import Mock

from custom_components.ikea_bilresa.profiles import synchronize_profiles


def test_editing_a_linked_channel_updates_only_its_peer():
    source = {"node_id": "101", "channel": "2", "step": 2}
    peer = SimpleNamespace(
        subentry_type="binding", data={"node_id": "102", "channel": "2", "step": 3}
    )
    other_channel = SimpleNamespace(
        subentry_type="binding", data={"node_id": "102", "channel": "3", "step": 3}
    )
    other_room = SimpleNamespace(
        subentry_type="binding", data={"node_id": "201", "channel": "2", "step": 3}
    )
    entry = SimpleNamespace(
        options={"shared_profiles": [{"name": "Linked", "nodes": ["101", "102"]}]},
        subentries={"peer": peer, "other": other_channel, "room": other_room},
    )
    update = Mock()
    hass = SimpleNamespace(config_entries=SimpleNamespace(async_update_subentry=update))
    synchronize_profiles(hass, entry, data=source)
    update.assert_called_once_with(entry, peer, data={**source, "node_id": "102"})


def test_unlinked_profiles_and_button_endpoints_are_unchanged():
    entry = SimpleNamespace(options={}, subentries={})
    hass = SimpleNamespace(config_entries=SimpleNamespace(async_update_subentry=Mock()))
    synchronize_profiles(hass, entry, data={"node_id": "101", "endpoint": "3"})
    synchronize_profiles(hass, entry, data={"node_id": "101", "channel": "1"})
    hass.config_entries.async_update_subentry.assert_not_called()
