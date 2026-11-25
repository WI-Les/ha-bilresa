# BILRESA.MasterControl 0.2.1 — Nederlands / Dutch

## Nederlands

Volledige Nederlandse ondersteuning in de bestaande integratie. Dit is een gewone stabiele release; voorafgaande versies hoeven niet aan te staan. Engels, Tsjechisch en Nederlands zitten samen in één pakket.

- Alle 391 paneelteksten en alle Home Assistant-vertaalvelden zijn vertaald: instellingen, opties, entiteiten, gebeurtenissen, triggers, herstelmeldingen en systeemstatus.
- `nl`, `nl-NL` en `nl-BE` gebruiken dezelfde complete Nederlandse vertaling.
- Nieuwe [Nederlandse README](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/README.nl.md), [snelstart](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/docs/nl/QUICK-START.md), [gebruikershandleiding](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/docs/nl/USER-GUIDE.md) en [installatie-, update- en herstelhandleiding](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/docs/nl/INSTALLATION.md).
- Het paneel volgt de profieltaal. De instantietaal blijft de terugval en bepaalt de standaardentiteitsnamen. De bestaande architectuur is behouden.

Installeer stabiele **0.2.1** via Marketplace of HACS. Handmatig: gebruik het gezamenlijke bronarchief van deze release en kopieer de volledige map `custom_components/ikea_bilresa`, inclusief `translations`, `frontend` en `brand`. Herstart Home Assistant en vernieuw de browser. Vereist: Home Assistant **2026.8+**, werkende Matter en een gekoppelde BILRESA.

Bestaande bedieningskoppelingen, instellingen, entiteits-ID’s, technische identificatoren en Matter-pairings blijven behouden. Er is geen opslagmigratie. Maak eerst een back-up; installeer geen tweede uitvoering van hetzelfde domein. Voorkom dubbele opdrachten bij het overzetten van oude knopautomatiseringen. Testknoppen kunnen echte apparaten bedienen.

Validatie omvat de Home Assistant-matrix, frontend- en protocoltests, taal- en documentatiecontroles, hassfest en HACS. De Nederlandse preview wordt met fictieve apparaten gecontroleerd op telefoon-, tablet- en desktopbreedte. Op Windows kan de volledige Home Assistant-testsuite niet starten door de ontbrekende Unix-module `fcntl`; de volledige suites draaien daarom op GitHub Actions onder Linux. Er is niets getest of gewijzigd op een live Home Assistant. Fysieke acceptatie van alle MasterControl-bedieningen blijft een afzonderlijke controle.

## English

Complete Dutch localization in the same stable integration package as English and Czech. No separate Dutch build, repository or runtime migration.

- Translate all 391 panel labels and every Home Assistant source translation field, including configuration, options, selectors, entity/event names, triggers, Repairs and system health.
- Resolve Dutch regional tags through the existing language selection and retain the current viewer-profile language behavior, with instance-language fallback and instance-language entity names.
- Add Dutch onboarding, installation/update/rollback instructions, a full user guide and reciprocal language links. Extend key, placeholder, rendered-name, frontend and documentation regression coverage.

Install **0.2.1** through the normal Marketplace/HACS stable channel, or copy the complete `custom_components/ikea_bilresa` folder from this release's source archive. Restart Home Assistant and refresh the frontend. Home Assistant **2026.8+**, working Matter and a commissioned BILRESA remain required. Existing bindings, configuration, identifiers and Matter pairings are retained. Keep a matching backup for rollback.

Read the [English Quick Start](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/docs/QUICK-START.md), [manual](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/docs/USER-GUIDE.md) and [installation guide](https://github.com/WI-Les/ha-bilresa/blob/v0.2.1/docs/INSTALLATION.md).

Validation covers Home Assistant integration tests, protocol and frontend suites, localization/documentation checks, hassfest and HACS. The Dutch preview uses synthetic devices only. The full Home Assistant suite cannot bootstrap on local Windows because `fcntl` is unavailable; Linux GitHub Actions provide that full-suite validation. No live Home Assistant was modified or tested. Automated checks and previews do not establish physical timing or every remote/target combination.

Independent community project maintained by Les., based on the MIT-licensed work of Vituhlos and contributors.
