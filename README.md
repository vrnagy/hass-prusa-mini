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
