"""Inspect light-group membership without looping over cyclic groups."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant

from .const import CONF_FOLLOWER, CONF_TARGET, binding_targets


def expand_members(hass: HomeAssistant, entities: Iterable[str]) -> set[str]:
    """Return entities and their currently reported nested members."""
    found: set[str] = set()
    todo = list(entities)
    while todo:
        entity_id = todo.pop()
        if entity_id in found:
            continue
        found.add(entity_id)
        state = hass.states.get(entity_id)
        members = state.attributes.get(ATTR_ENTITY_ID) if state else None
        if isinstance(members, (list, tuple)):
            todo.extend(member for member in members if isinstance(member, str))
    return found


def follower_overlaps(hass: HomeAssistant, data: dict[str, Any]) -> bool:
    """Check known group membership of a validated brightness binding."""
    follower = data.get(CONF_FOLLOWER)
    if not follower:
        return False
    return not expand_members(hass, binding_targets(data.get(CONF_TARGET))).isdisjoint(
        expand_members(hass, [follower])
    )
