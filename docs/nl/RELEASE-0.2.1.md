# Release-informatie — 0.2.1

[English release notes](../RELEASE-0.2.1.md) · [Nederlandse README](../../README.nl.md) · [Snelstart](QUICK-START.md) · [Handleiding](USER-GUIDE.md)

Deze stabiele patch voegt volledig Nederlands toe aan BILRESA.MasterControl. Engels en Tsjechisch blijven beschikbaar. Alle talen gebruiken hetzelfde installatiepakket.

## Toegevoegd

- Alle 391 paneelteksten in Nederlands: bediening, doelen, knopacties, vasthouden, loslaten, Live testen, diagnose en herstelmeldingen.
- Alle vertaalvelden uit `strings.json` en de Engelse Home Assistant-vertaling: configuratie, opties, keuzelijsten, entiteiten, gebeurtenissen, triggers, herstelmeldingen en systeemstatus.
- Ondersteuning voor `nl`, `nl-NL` en `nl-BE` via de bestaande taalresolutie.
- Een Nederlandse README, snelstart, installatie- en updatehandleiding, gebruikershandleiding en herstelprocedure met wederzijdse taallinks.
- Extra controles op taalkeuze, complete sleutels, placeholders, werkelijk vertaalde tekst, frontendtaal en door Home Assistant gemaakte entiteitsnamen.

## Installeren en taal kiezen

Kies stabiele **0.2.1** via Marketplace of HACS. Voorafgaande versies hoeven niet aan te staan. Handmatig gebruikt u het gezamenlijke bronarchief van de release en kopieert u de complete map `custom_components/ikea_bilresa`, inclusief vertalingen, frontend en merkafbeeldingen. Herstart Home Assistant en vernieuw de browser.

Vereist blijft Home Assistant **2026.8+** met werkende Matter en een gekoppelde BILRESA. Begin met de [snelstart](QUICK-START.md).

Het huidige paneel volgt de **profieltaal** van de kijker. Kies Nederlands via uw profiel onderaan de zijbalk. De **instantietaal** is de terugval voor het paneel en bepaalt de standaardentiteitsnamen. Die staat onder **Instellingen → Systeem → Algemeen**. Zie [Taal](USER-GUIDE.md#taal). Deze profieltaalondersteuning bestond al; er wordt geen nieuwe taalarchitectuur ingevoerd.

## Behoud en herstel

Domein `ikea_bilresa`, entiteits-ID’s, gebeurtenissleutels, API-contracten, opslagvelden, bedieningskoppelingen en Matter-pairings blijven behouden. Er is geen opslagmigratie voor deze vertaling. Maak toch vóór bijwerken een back-up. Zie [Terug naar de vorige versie](INSTALLATION.md#terug-naar-de-vorige-versie).

Schakel oude knopautomatiseringen uit voordat u hun directe vervangers activeert. **Alleen volgen** laat draaien en gebeurtenissen actief. De knoppen in **Live testen** kunnen echte apparaten bedienen.

## Controle en grenzen

De release wordt gecontroleerd met de Home Assistant-tests voor 2026.9.4 en 2026.11.1, frontendtests, protocoltests op Python 3.12 en 3.14, hassfest en HACS-validatie. Taal- en documentatietests controleren ook Nederlandse sleutels, placeholders, namen, lokale links en afbeeldingen.

De Nederlandse paneelpreview gebruikt uitsluitend fictieve apparaten. De bestaande afbeeldingen in de handleidingen hebben Engelse labels en gesimuleerde apparaten. Er is voor deze vertaling niets op een live Home Assistant gewijzigd of getest. Softwaretests en previews bewijzen geen fysieke timing of werking van elke hardwarecombinatie. De eerdere beperking rond volledige fysieke MasterControl-acceptatie blijft bestaan.
