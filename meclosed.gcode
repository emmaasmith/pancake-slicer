M104 S200.0
M109 S200.0
G21       ;metric values
G90       ;absolute positioning
M82       ;set extruder to absolute mode
M107      ;start with the fan off
G28 X0 Y0 ;home X/Y
G28 Z0    ;home Z
G92 E0    ;zero the extruded length
G29       ;initiate auto bed leveling sequence
G92 X132.4 Y20 ;correct bed origin (G29 changes it)
G1 X50.949 Y51.120 F6000.000
G1 Z0.361 F6000.000
G1 E2.00000 F1800.000
M107
G1 F1500.0 E-6.50000
