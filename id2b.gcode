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
G0 X50.949 Y51.120 F6000.000
G1 Z0.361 F6000.000
G1 E2.00000 F1800.000
M107
G1 F1500.0 E-6.50000
;PERIM:0
;PERIMLAYER:0
G0 X56.000 Y54.000 Z1.300 E0 F2000.0
G1 X50.000 Y57.000 E2.3354 F2000.0
G1 X57.000 Y60.000 E2.7162 F2000.0
G0 X45.000 Y51.000 E0 F2200.0
G1 X46.000 Y56.000 E2.9711 F2000.0
G1 X36.000 Y54.000 E3.4811 F2000.0
G1 X45.000 Y63.000 E4.1174 F2000.0
G1 X53.000 Y62.000 E4.5206 F2000.0
G0 X57.000 Y36.000 E0 F2200.0
G1 X65.000 Y37.000 E4.9237 F2000.0
G1 X58.000 Y42.000 E5.3538 F2000.0
G0 X49.000 Y16.000 E0 F2200.0
G1 X32.000 Y37.000 E6.7047 F2000.0
G1 X32.000 Y58.000 E7.7547 F2000.0
G1 X41.000 Y69.000 E8.4653 F2000.0
G1 X59.000 Y63.000 E9.4140 F2000.0
G1 X42.000 Y69.000 E10.3154 F2000.0
G1 X34.000 Y61.000 E10.8811 F2000.0
G1 X36.000 Y26.000 E12.6340 F2000.0
G0 X51.000 Y3.000 E0 F2200.0
G1 X33.000 Y22.000 E13.9426 F2000.0
G1 X26.000 Y74.000 E16.5660 F2000.0
G1 X33.000 Y22.000 E19.1895 F2000.0
G1 X49.000 Y4.000 E20.3936 F2000.0
G1 X59.000 Y4.000 E20.8936 F2000.0
G1 X81.000 Y31.000 E22.6351 F2000.0
G0 X38.000 Y31.000 E0 F2200.0
G1 X41.000 Y43.000 E23.2535 F2000.0
G1 X48.000 Y34.000 E23.8236 F2000.0
G1 X39.000 Y31.000 E24.2980 F2000.0
;PERIM:0
;PERIMLAYER:0
G0 X60.000 Y5.000 Z1.300 E0 F2000.0
G1 X50.000 Y4.000 E24.8004 F2000.0
G1 X37.000 Y16.000 E25.6850 F2000.0
G1 X27.000 Y77.000 E28.7757 F2000.0
G1 X2.000 Y84.000 E30.0738 F2000.0
G1 X1.000 Y98.000 E30.7756 F2000.0
G1 X42.000 Y98.000 E32.8256 F2000.0
G1 X43.000 Y85.000 E33.4775 F2000.0
G1 X51.000 Y98.000 E34.2407 F2000.0
G1 X95.000 Y98.000 E36.4407 F2000.0
G1 X82.000 Y74.000 E37.8055 F2000.0
G1 X79.000 Y28.000 E40.1104 F2000.0
G1 X60.000 Y5.000 E41.6020 F2000.0
G0 X46.000 Y14.000 E0 F2200.0
G1 X64.000 Y25.000 E42.6568 F2000.0
G1 X66.000 Y33.000 E43.0691 F2000.0
G1 X58.000 Y35.000 E43.4814 F2000.0
G1 X66.000 Y37.000 E43.8937 F2000.0
G1 X59.000 Y42.000 E44.3238 F2000.0
G1 X68.000 Y44.000 E44.7848 F2000.0
G1 X65.000 Y62.000 E45.6972 F2000.0
G1 X48.000 Y82.000 E47.0096 F2000.0
G1 X31.000 Y57.000 E48.5213 F2000.0
G1 X33.000 Y31.000 E49.8251 F2000.0
G1 X46.000 Y14.000 E50.8951 F2000.0
G0 X60.000 Y11.000 E0 F2200.0
G1 X71.000 Y15.000 E51.4804 F2000.0
G1 X70.000 Y25.000 E51.9829 F2000.0
G1 X60.000 Y11.000 E52.8431 F2000.0
;INFILL:0
G0 X2.850 Y88.762 Z1.300 E0 F3000.0
G1 X2.850 Y93.000 E52.8431 F20000.0
G0 X12.750 Y93.000 E0 F3000.0
G1 X12.750 Y85.990 E52.8431 F20000.0
G0 X22.650 Y83.218 E0 F3000.0
G1 X22.650 Y93.000 E52.8431 F20000.0
G0 X32.550 Y38.145 E0 F3000.0
G1 X32.550 Y41.850 E52.8431 F20000.0
G0 X32.550 Y64.279 E0 F3000.0
G1 X32.550 Y93.000 E52.8431 F20000.0
G0 X42.450 Y13.642 E0 F3000.0
G1 X42.450 Y15.969 E52.8431 F20000.0
G0 X42.450 Y78.838 E0 F3000.0
G1 X42.450 Y87.150 E52.8431 F20000.0
G0 X52.350 Y12.881 E0 F3000.0
G1 X52.350 Y9.235 E52.8431 F20000.0
G0 X52.350 Y81.882 E0 F3000.0
G1 X52.350 Y93.000 E52.8431 F20000.0
G0 X62.250 Y18.931 E0 F3000.0
G1 X62.250 Y19.150 E52.8431 F20000.0
G0 X62.250 Y70.235 E0 F3000.0
G1 X62.250 Y93.000 E52.8431 F20000.0
G0 X72.150 Y93.000 E0 F3000.0
G1 X72.150 Y24.708 E52.8431 F20000.0
G0 X82.050 Y79.092 E0 F3000.0
G1 X82.050 Y93.000 E52.8431 F20000.0
G0 X91.950 Y93.000 E0 F3000.0
G1 X91.950 Y97.369 E52.8431 F20000.0
;INFILL:0
G0 X3.850 Y87.109 Z1.300 E0 F3000.0
G1 X3.850 Y96.000 E52.8431 F20000.0
G0 X13.750 Y96.000 E0 F3000.0
G1 X13.750 Y82.343 E52.8431 F20000.0
G0 X23.650 Y77.576 E0 F3000.0
G1 X23.650 Y96.000 E52.8431 F20000.0
G0 X33.550 Y96.000 E0 F3000.0
G1 X33.550 Y44.856 E52.8431 F20000.0
G0 X43.450 Y16.410 E0 F3000.0
G1 X43.450 Y96.000 E52.8431 F20000.0
G0 X53.350 Y96.000 E0 F3000.0
G1 X53.350 Y9.360 E52.8431 F20000.0
G0 X63.250 Y12.000 E0 F3000.0
G1 X63.250 Y96.000 E52.8431 F20000.0
G0 X73.150 Y96.000 E0 F3000.0
G1 X73.150 Y21.682 E52.8431 F20000.0
G0 X83.050 Y35.659 E0 F3000.0
G1 X83.050 Y96.000 E52.8431 F20000.0
G0 X92.950 Y96.000 E0 F3000.0
G1 X92.950 Y93.900 E52.8431 F20000.0
G1 F1500.0 E374.01664
M107
M104 S0     ;extruder heater off
M140 S0     ;heated bed heater off (if you have it)
M106 S0     ;fan off
G91         ;relative positioning
G1 E-1 F300 ;retract the filament a bit
G28 X0 Y0   ;home X/Y, so the head is out of the way
M84         ;steppers off
G90         ;absolute positioning
M104 S0.0
;End of Gcode
