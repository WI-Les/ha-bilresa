"""Serve the shipped panel with synthetic examples for documentation screenshots.

Run with the project's test dependencies: python tools/docs_preview.py.
Only the demo files and the two public frontend modules are served on loopback.
No Home Assistant credentials, network devices or real captures are used.
"""

# Embedded HTML/CSS/JS is kept literal for the standalone preview.
# ruff: noqa: E501

import asyncio
from copy import deepcopy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pytest import MonkeyPatch  # noqa: E402
from tests.test_panel_models import (  # noqa: E402
    _button_subentry,
    _dual_button,
    _entry,
    _hass,
    _patch,
    _state,
    _subentry,
    _wheel,
)

from custom_components.ikea_bilresa.binding_config import normalize_binding_data  # noqa: E402
from custom_components.ikea_bilresa.device_link import MatterDeviceLink  # noqa: E402
from custom_components.ikea_bilresa.panel_models import async_overview_snapshot  # noqa: E402
from custom_components.ikea_bilresa.panel_schema import panel_schema  # noqa: E402
from custom_components.ikea_bilresa.panel_strings import STRINGS  # noqa: E402


def fixture(language="en"):
    names = {101: "Living room wheel", 102: "Reading corner wheel", 103: "Desk buttons"}
    states = {
        "light.example": _state("on", "Reading lamp"),
        "light.example_a": _state("on", "Accent lamp"),
        "light.example_b": _state("on", "Ceiling lights"),
        "media_player.example": _state("paused", "Living room speaker"),
        "scene.example": _state("unknown", "Evening scene"),
        "script.example": _state("off", "Remember selected colour"),
        "switch.example": _state("off", "Desk lamp"),
    }
    cycle = [
        {
            "repeat": {
                "while": [{"condition": "template", "value_template": "{{ true }}"}],
                "sequence": [
                    {
                        "action": "light.turn_on",
                        "target": {"entity_id": "light.example"},
                        "data": {"rgb_color": [255, 70, 20], "transition": 0.9},
                    },
                    {"delay": {"seconds": 1}},
                    {
                        "action": "light.turn_on",
                        "target": {"entity_id": "light.example"},
                        "data": {"rgb_color": [20, 80, 255], "transition": 0.9},
                    },
                    {"delay": {"seconds": 1}},
                ],
            }
        }
    ]
    channels = [
        {
            "target": "light.example",
            "mode": "brightness",
            "step": 3,
            "transition": 0.6,
            "click_action": "toggle",
            "double_press_action": "run",
            "double_press_sequence": [
                {"action": "scene.turn_on", "target": {"entity_id": "scene.example"}}
            ],
            "triple_press_target": "light.example",
            "triple_press_action": "off",
            "hold_action": "run",
            "hold_sequence": cycle,
            "hold_stop_on_release": True,
            "hold_max_seconds": 60,
            "release_sequence": [
                {"action": "script.turn_on", "target": {"entity_id": "script.example"}}
            ],
        },
        {
            "target": "light.example_b",
            "mode": "brightness",
            "step": 2,
            "transition": 0.6,
            "click_action": "toggle",
            "hold_action": "ramp",
            "follower_light": "light.example_a",
            "follower_offset": -10,
            "follower_min": 1,
        },
        {
            "target": "media_player.example",
            "mode": "volume",
            "step": 3,
            "click_action": "play_pause",
            "double_press_target": "media_player.example",
            "double_press_action": "next",
            "triple_press_target": "media_player.example",
            "triple_press_action": "previous",
            "hold_action": "none",
        },
    ]
    bindings = []
    for node in (101, 102):
        for channel, data in enumerate(channels, 1):
            normalized = normalize_binding_data(
                deepcopy(data), node_id=node, channel=channel
            )
            normalized.pop("node_id")
            normalized.pop("channel")
            bindings.append(_subentry(node, channel, **normalized))
    for button, direction in ((1, "up"), (2, "down")):
        bindings.append(
            _button_subentry(
                103,
                button,
                click_action="toggle",
                click_target="switch.example",
                hold_action="ramp",
                hold_target="light.example",
                ramp_direction=direction,
            )
        )
    entry = _entry([_wheel(101), _wheel(102), _dual_button(103)], bindings)
    entry.options = {
        "shared_profiles": [{"name": "Living room pair", "nodes": ["101", "102"]}]
    }
    hass = _hass(states, language=language)
    hass.config_entries = SimpleNamespace(async_entries=lambda _: [entry])
    with MonkeyPatch.context() as patch:
        _patch(patch, area="Example home")
        patch.setattr(
            "custom_components.ikea_bilresa.panel_models.resolve_matter_device",
            lambda _hass, **kw: MatterDeviceLink(
                SimpleNamespace(
                    id=f"demo-{kw['wheel'].node_id}",
                    name_by_user=names[kw["wheel"].node_id],
                    name=names[kw["wheel"].node_id],
                    area_id="demo",
                )
            ),
        )
        snapshot = async_overview_snapshot(hass, entry)
    return {
        "snapshot": snapshot,
        "states": {
            eid: {
                "entity_id": eid,
                "state": state.state,
                "attributes": state.attributes,
            }
            for eid, state in states.items()
        },
        "config": {
            "version": json.loads(
                (ROOT / "custom_components/ikea_bilresa/manifest.json").read_text()
            )["version"],
            "language": language,
            "labels": STRINGS[language],
            "labels_by_language": STRINGS,
            "schema": panel_schema(),
        },
    }


HTML = """<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BILRESA.MasterControl documentation preview</title>
<style>
:root{--primary-color:#6d4aff;--primary-text-color:#20232b;--secondary-text-color:#626775;--primary-background-color:#f4f5f8;--secondary-background-color:#eef0f5;--card-background-color:#fff;--divider-color:#dce0e8;--disabled-text-color:#808590;--error-color:#c33232;--success-color:#19764a;--warning-color:#9a6200;--ha-card-border-radius:16px;--ha-card-border-width:1px;--ha-card-border-color:#dde1e8;--ha-font-family-body:Arial,sans-serif;font-family:Arial,sans-serif;background:#f4f5f8;color:#20232b}
*{box-sizing:border-box}body{margin:0}header{height:64px;padding:0 24px;display:flex;align-items:center;justify-content:space-between;background:#fff;border-bottom:1px solid #dce0e8;font-size:18px;font-weight:650}header small{font-size:12px;font-weight:400;color:#626775}.demo-nav{display:flex;gap:8px;flex-wrap:wrap;padding:10px 24px;background:#fff}.demo-nav a{font-size:12px;color:#5441a9;text-decoration:none;padding:6px 10px;border-radius:6px;background:#f0edff}.frame{height:calc(100vh - 110px)}ikea-bilresa-panel{display:block;height:100%}@media(max-width:600px){header{padding:0 14px;font-size:16px}header small{max-width:140px;text-align:right}.demo-nav{padding:8px}.frame{height:calc(100vh - 120px)}}
</style>
<header><span>BILRESA.MasterControl</span><small>Documentation demo · Synthetic data<br>No devices connected or controlled</small></header>
<nav class="demo-nav"><a href="/?screen=overview">Overview</a><a href="/?screen=channels">Wheel channels</a><a href="/?screen=presses">Button actions</a><a href="/?screen=hold">Hold and release</a><a href="/?screen=buttons">Dual button</a><a href="/?screen=live">Live test</a></nav>
<main class="frame"><ikea-bilresa-panel></ikea-bilresa-panel></main>
<script type="module">
import '/component/ikea_bilresa_panel.js';
const params=new URLSearchParams(location.search);
const fixture=await(await fetch('/fixture.json?lang='+encodeURIComponent(params.get('lang') || 'en'))).json();const panel=document.querySelector('ikea-bilresa-panel');
panel.panel={config:fixture.config};
panel.hass={language:new URLSearchParams(location.search).get('lang') || 'en',states:fixture.states,entities:{},devices:{},areas:{},services:{},
  callWS:async(message)=>{if(message.type.endsWith('/overview'))return structuredClone(fixture.snapshot);if(message.type.endsWith('/binding/test'))return {ok:true,action_id:'documentation-only'};return {ok:true};},
  connection:{subscribeMessage:async()=>()=>{}},callApi:async()=>({})};
await new Promise(requestAnimationFrame);const screen=new URLSearchParams(location.search).get('screen');
if(screen&&screen!=='overview'){
 const wheel=fixture.snapshot.wheels.find(w=>w.variant===(screen==='buttons'?'dual_button':'wheel'));panel._openWheel(wheel.key);
 if(screen==='presses'||screen==='hold'){panel._startEditor(wheel,wheel.channels[0]);}
 if(screen==='live'){panel._setView('live');panel._activities=[{wheel:wheel.key,channel:1,gesture:'press',presses:1,source:'panel_test',dispatch_status:'accepted',dispatched:true,result:{kind:'entity_action',action:'toggle',target:'light.example'}},{wheel:wheel.key,channel:1,gesture:'release',source:'panel_test',dispatch_status:'completed',reason:'hold_stopped'}];panel._render();}
 await new Promise(requestAnimationFrame);
 if(screen==='hold'||screen==='presses'){
   const title=fixture.config.labels[screen==='hold'?'binding_gesture_hold':'binding_gesture_short_press'];const item=[...panel.shadowRoot.querySelectorAll('.form-section-title')].find(e=>e.textContent.trim()===title);
   item?.scrollIntoView({block:'start'});
 }
}
</script></html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = self.path.split("?", 1)[0]
        if route == "/":
            content, mime = HTML.encode(), "text/html; charset=utf-8"
        elif route == "/fixture.json":
            language = parse_qs(urlsplit(self.path).query).get("lang", ["en"])[0]
            content, mime = FIXTURES.get(language, FIXTURES["en"]), "application/json"
        elif route in (
            "/component/ikea_bilresa_panel.js",
            "/component/bilresa_icons.js",
        ):
            content = (
                ROOT
                / "custom_components/ikea_bilresa/frontend"
                / route.rsplit("/", 1)[1]
            ).read_bytes()
            mime = "text/javascript"
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)


async def build_fixture():
    from homeassistant.core import HomeAssistant

    HomeAssistant(str(ROOT / ".tooling/docs-preview"))
    return {language: json.dumps(fixture(language)).encode() for language in STRINGS}


if __name__ == "__main__":
    FIXTURES = asyncio.run(build_fixture())
    print("Documentation preview: http://127.0.0.1:8768", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8768), Handler).serve_forever()
