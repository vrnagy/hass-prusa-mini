# Prusa MINI/MINI+ integration for Home Assistant
![GitHub](https://img.shields.io/github/license/vrnagy/hass-prusa-mini)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![Validate with hassfest](https://github.com/vrnagy/hass-prusa-mini/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/vrnagy/hass-prusa-mini/actions/workflows/hassfest.yaml)

## Installation
---

### HACS

1. Open _HACS_ and navigate to _Integrations_ Section
2. Open the Overflow Menu (⋮) in the top right corner and click on _Custom repositories_
3. Paste `https://github.com/vrnagy/hass-prusa-mini` into the input field and select `Integration` from the dropdown
4. Click the Install Button on the highlighted Card titled _Prusa Connect_
5. Add entry in `configuration.yaml`
6. Restart Home Assistant

### Manual

1. Download the repository as a ZIP package and extract it
2. Copy `custom_components` directory to your `config` directory (this is where your `configuration.yaml` lives)
3. Add entry in `configuration.yaml`
4. Restart Home Assistant

## Example Lovelace config
---
```yaml
type: entities
entities:
  - entity: sensor.prusa_mini_192_168_1_252_status
  - entity: sensor.prusa_mini_192_168_1_252_nozzle_temp
  - entity: sensor.prusa_mini_192_168_1_252_bed_temp
  - entity: sensor.prusa_mini_192_168_1_252_material
  - entity: sensor.prusa_mini_192_168_1_252_file
  - entity: sensor.prusa_mini_192_168_1_252_progress
  - entity: sensor.prusa_mini_192_168_1_252_time_elapsed
  - entity: sensor.prusa_mini_192_168_1_252_time_remaining
  - entity: sensor.prusa_mini_192_168_1_252_flow_rate
  - entity: sensor.prusa_mini_192_168_1_252_printing_speed
  - entity: sensor.prusa_mini_192_168_1_252_z_height
title: Prusa Mini
show_header_toggle: false
```

## Screenshots
---
![image](https://user-images.githubusercontent.com/199546/122988219-c6985700-d3a1-11eb-9f1a-5d82b9aa9466.png)
