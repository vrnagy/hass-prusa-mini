[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![Validate with hassfest](https://github.com/vrnagy/hass-prusa-mini/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/vrnagy/hass-prusa-mini/actions/workflows/hassfest.yaml)

Example Lovelace config:
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

![image](https://user-images.githubusercontent.com/199546/122988219-c6985700-d3a1-11eb-9f1a-5d82b9aa9466.png)
