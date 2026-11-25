# Installeren en bijwerken — 0.2.1

[English](../INSTALLATION.md) · [Nederlandse README](../../README.nl.md) · [Snelstart](QUICK-START.md) · [Handleiding](USER-GUIDE.md)

## Vooraf

Vereist: **Home Assistant 2026.8 of nieuwer**, de Matter-integratie en een bereikbare Matter Server. Dit minimum staat in `hacs.json`. De testworkflows controleren Home Assistant 2026.9.4 en 2026.11.1; ze testen niet elke tussenversie of hardwarecombinatie.

Koppel de BILRESA eerst via Matter aan Home Assistant. Voor deze Thread-afstandsbedieningen is een werkend Thread-netwerk met borderrouter nodig. MasterControl luistert naar de bedieningen en vervangt de Matter- of Thread-installatie niet. Doelen zoals lampen mogen een andere ondersteunde integratie gebruiken.

Maak een Home Assistant-back-up en bewaar de vorige integratiemap en bijbehorende configuratie. Bewaar ook oude automatiseringen met hun aan/uit-status. Controleer vóór een belangrijke update hoe u de back-up terugzet. Bewaar privéback-ups buiten deze publieke repository.

De oorspronkelijke integratie en MasterControl gebruiken allebei `ikea_bilresa`. Er mag maar één uitvoering tegelijk geïnstalleerd zijn. Behoud bestaande entiteits-ID’s, integratie-instellingen en Matter-pairings.

## Installeren via Marketplace

Vanaf **Home Assistant 2026.11** is Marketplace ingebouwd. U moet beheerder zijn.

1. Open [BILRESA in Marketplace](https://my.home-assistant.io/redirect/marketplace_repository/?owner=WI-Les&repository=ha-bilresa&category=integration).
2. Of ga naar **Instellingen → Marketplace → Toevoegen via link** (*Settings → Marketplace → Add from link*). Vul `https://github.com/WI-Les/ha-bilresa` in. Kies **Integratie** (*Integration*) als dat wordt gevraagd.
3. Lees de melding bij het eerste gebruik. Verbind GitHub als Marketplace dat vraagt voor deze eigen repository.
4. Kies **Installeren** (*Install*) en controleer **0.2.1**. **Voorafgaande versies opnemen** (*Include pre-releases*) hoeft niet aan te staan.
5. Herstart Home Assistant zoals gevraagd.

Zie de [officiële Marketplace-handleiding](https://www.home-assistant.io/integrations/marketplace/) voor de schermen en versiekeuze.

## Installeren via HACS

Gebruik op **2026.8–2026.10** HACS als dat al is geïnstalleerd, of kies de handmatige route hieronder.

1. Open [BILRESA in HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=WI-Les&repository=ha-bilresa&category=integration).
2. Staat de repository niet in HACS? Open het menu met drie stippen → **Aangepaste repositories** (*Custom repositories*). Voeg `https://github.com/WI-Les/ha-bilresa` toe als **Integratie** (*Integration*).
3. Open de repository en download stabiele **0.2.1**. Bètaversies zijn niet nodig.
4. Herstart Home Assistant.

De [officiële HACS-uitleg](https://www.hacs.xyz/docs/faq/custom_repositories/) beschrijft het toevoegen van een eigen repository.

## Handmatig installeren

1. Download het [gezamenlijke bronarchief van 0.2.1](https://github.com/WI-Les/ha-bilresa/archive/refs/tags/v0.2.1.zip). Dit bevat alle talen.
2. Pak het archief op uw computer uit. Zoek `custom_components/ikea_bilresa`.
3. Maak zo nodig `custom_components` aan in uw Home Assistant-configuratiemap, naast `configuration.yaml`.
4. Kopieer de **volledige** map `ikea_bilresa` naar die map. Neem `translations`, `frontend` en `brand` mee. Het resultaat is `custom_components/ikea_bilresa/manifest.json`, niet een extra geneste projectmap.
5. Meng geen bestanden uit verschillende versies. Bewaar bij een update de oude map apart en vervang de componentmap volledig.
6. Herstart Home Assistant. Vernieuw daarna de browser of herlaad de app.

Gebruik een releasearchief, niet zomaar de laatste broncode op `main`. In `manifest.json` moet versie **0.2.1** staan.

## De integratie toevoegen

Bestanden installeren voegt nog geen nieuwe integratie-instelling toe.

1. Ga naar **Instellingen → Apparaten & diensten → Integratie toevoegen** (*Settings → Devices & services → Add integration*).
2. Zoek **BILRESA.MasterControl**.
3. Volg de verbinding met Matter Server. Een bestaande kern-Matter-verbinding wordt waar mogelijk hergebruikt. Een gevraagd WebSocket-adres moet vanuit Home Assistant bereikbaar zijn. Gebruik niet de webpagina-URL van Home Assistant.

Bij een bestaande `ikea_bilresa`-installatie behoudt u de huidige integratie. Voeg geen tweede kopie toe. Opnieuw pairen is geen normale updatestap.

## De bediening instellen

Open **BILRESA.MasterControl** in de zijbalk. Kies één afstandsbediening en koppel één lamp aan een kanaal of knop. Een bedieningskoppeling bevat het doel en de gewenste acties. Volg de [snelstart](QUICK-START.md).

Stel de profieltaal op Nederlands in voor het paneel. Door Home Assistant gemaakte entiteitsnamen volgen de instantietaal. Zie [Taal](USER-GUIDE.md#taal).

## Bijwerken vanaf een bestaande versie

1. Maak de back-up uit [Vooraf](#vooraf). Noteer de geïnstalleerde versie.
2. Stop lopende acties bij vasthouden. Download of installeer **0.2.1** via uw bestaande installatiemethode.
3. Herstart Home Assistant en vernieuw de browser.
4. Controleer de geïnstalleerde versie, Matter-verbinding en bestaande doelen. Behoud de integratie-instelling en bestaande koppelingen.
5. Test één kanaal of knop met de fysieke afstandsbediening. Controleer ook de echte lamp.
6. Zet bestaande knopautomatiseringen alleen over volgens de [migratiestappen](USER-GUIDE.md#bestaande-automatiseringen-overzetten).

Versie 0.2.1 voegt talen en documentatie toe aan 0.2.0. Er is geen nieuwe opslagmigratie voor Nederlands. Versie 0.1.0 heeft een ouder paneel en mist de nieuwe levensduur van vasthoudacties en gedeelde profielen.

## Terug naar de vorige versie

1. Stop actieve vasthoudacties. Zet nieuwe directe knopacties op **Alleen volgen** voordat u oude knopautomatiseringen weer inschakelt.
2. Laat het kanaal actief als de oude automatisering de gebeurtenisentiteiten of virtuele schakelaars van deze integratie nodig heeft. Een volledig uitgeschakeld kanaal onderdrukt ook die gebeurtenissen. Alleen volgen laat draaien actief; voorkom ook daar dubbele bediening.
3. Kies in Marketplace **Andere versie installeren** (*Install another version*) of de overeenkomstige versieoptie in HACS. Selecteer bijvoorbeeld de [vorige stabiele 0.2.0](https://github.com/WI-Les/ha-bilresa/releases/tag/v0.2.0).
4. Handmatig: vervang de volledige componentmap door de bewaarde vorige map of het bronarchief van die versie.
5. Zet zo nodig de **bijpassende configuratieback-up** terug. Alleen oudere code terugzetten draait eerdere configuratiewijzigingen niet terug. Nederlands verdwijnt bij 0.2.0.
6. Herstart, vernieuw de browser en test de herstelde bediening. Schakel oude automatiseringen pas weer in als hun vervangers geen dubbele opdrachten meer sturen.

Verwijder de integratie of Matter-apparaten niet als gewone herstelstap. Als opstarten niet lukt, gebruik uw toegang tot de configuratiemap of het Home Assistant-back-upherstel. Zie [probleemoplossing](USER-GUIDE.md#probleemoplossing) en de [officiële back-updocumentatie](https://www.home-assistant.io/common-tasks/general/#backups).
