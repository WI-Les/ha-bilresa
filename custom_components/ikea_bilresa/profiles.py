"""Keep existing channel bindings synchronized within an explicitly linked profile."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .const import CONF_CHANNEL, CONF_NODE_ID, SUBENTRY_BINDING

CONF_SHARED_PROFILES = "shared_profiles"


def synchronize_profiles(hass: Any, entry: Any, *, data: dict | None = None) -> None:
    """Copy an edited channel to its existing peers, preserving their identities.

    Called within both editors' save paths. No runtime task or household mapping
    is shared between remotes; only configuration is copied. Updates use HA's
    config-entry API, so each peer gets a new optimistic-concurrency revision.
    """
    if not data or CONF_CHANNEL not in data:
        return
    node = str(data[CONF_NODE_ID])
    channel = str(data[CONF_CHANNEL])
    for profile in getattr(entry, "options", {}).get(CONF_SHARED_PROFILES, []):
        members = {str(value) for value in profile.get("nodes", [])}
        if node not in members:
            continue
        for peer in tuple(entry.subentries.values()):
            if peer.subentry_type != SUBENTRY_BINDING:
                continue
            peer_node = str(peer.data.get(CONF_NODE_ID))
            if (
                peer_node != node
                and peer_node in members
                and str(peer.data.get(CONF_CHANNEL)) == channel
            ):
                updated = {**deepcopy(data), CONF_NODE_ID: peer_node}
                if dict(peer.data) != updated:
                    hass.config_entries.async_update_subentry(entry, peer, data=updated)


def profile_name(entry: Any, node_id: int | str) -> str | None:
    """Name of a wheel's linked profile, for the editor's explanatory text."""
    for profile in getattr(entry, "options", {}).get(CONF_SHARED_PROFILES, []):
        if str(node_id) in {str(value) for value in profile.get("nodes", [])}:
            return str(profile.get("name", "Shared profile"))
    return None
