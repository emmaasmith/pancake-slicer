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
G0 X1.000 Y89.000 Z1.300 F2000.0
G1 X1.000 Y95.000 E2.6000 F2000.0
G1 X5.000 Y109.000 E4.0560 F2000.0
G1 X11.000 Y122.000 E5.4878 F2000.0
G1 X18.000 Y132.000 E6.7085 F2000.0
G1 X28.000 Y142.000 E8.1227 F2000.0
G1 X38.000 Y149.000 E9.3433 F2000.0
G1 X55.000 Y156.000 E11.1818 F2000.0
G1 X65.000 Y157.000 E12.1868 F2000.0
G0 X148.000 Y88.000 F2200.0
G1 X148.000 Y95.000 E12.8868 F2000.0
G1 X144.000 Y109.000 E14.3428 F2000.0
G1 X131.000 Y131.000 E16.8982 F2000.0
G1 X120.000 Y142.000 E18.4538 F2000.0
G1 X110.000 Y149.000 E19.6745 F2000.0
G1 X94.000 Y156.000 E21.4209 F2000.0
G1 X84.000 Y157.000 E22.4259 F2000.0
G0 X111.000 Y57.000 F2200.0
G1 X90.000 Y63.000 E24.6099 F2000.0
G1 X87.000 Y66.000 E25.0342 F2000.0
G1 X90.000 Y66.000 E25.3342 F2000.0
G1 X88.000 Y68.000 E25.6170 F2000.0
G1 X96.000 Y64.000 E26.5115 F2000.0
G1 X106.000 Y64.000 E27.5115 F2000.0
G1 X121.000 Y68.000 E29.0639 F2000.0
G1 X118.000 Y67.000 E29.3801 F2000.0
G1 X121.000 Y66.000 E29.6963 F2000.0
G1 X108.000 Y60.000 E31.1281 F2000.0
G0 X84.000 Y1.000 F2200.0
G1 X94.000 Y2.000 E32.1331 F2000.0
G1 X110.000 Y9.000 E33.8795 F2000.0
G1 X120.000 Y16.000 E35.1002 F2000.0
G1 X131.000 Y27.000 E36.6558 F2000.0
G1 X144.000 Y49.000 E39.2112 F2000.0
G1 X148.000 Y63.000 E40.6672 F2000.0
G1 X148.000 Y70.000 E41.3672 F2000.0
G1 X148.000 Y63.000 E42.0672 F2000.0
G0 X59.000 Y1.000 F2200.0
G1 X38.000 Y9.000 E44.3145 F2000.0
G1 X28.000 Y16.000 E45.5351 F2000.0
G1 X18.000 Y26.000 E46.9493 F2000.0
G1 X6.000 Y46.000 E49.2817 F2000.0
G1 X2.000 Y58.000 E50.5466 F2000.0
G1 X1.000 Y69.000 E51.6512 F2000.0
G1 X2.000 Y58.000 E52.7557 F2000.0
G0 X112.000 Y98.000 F2200.0
G1 X110.000 Y102.000 E53.2029 F2000.0
G1 X101.000 Y111.000 E54.4757 F2000.0
G1 X82.000 Y120.000 E56.5781 F2000.0
G1 X63.000 Y120.000 E58.4781 F2000.0
G1 X51.000 Y115.000 E59.7781 F2000.0
G1 X47.000 Y111.000 E60.3438 F2000.0
G1 X45.000 Y112.000 E60.5674 F2000.0
G1 X51.000 Y119.000 E61.4893 F2000.0
G1 X61.000 Y123.000 E62.5664 F2000.0
G1 X78.000 Y123.000 E64.2664 F2000.0
G1 X87.000 Y121.000 E65.1883 F2000.0
G1 X103.000 Y113.000 E66.9772 F2000.0
G1 X112.000 Y104.000 E68.2500 F2000.0
G1 X114.000 Y99.000 E68.7885 F2000.0
G1 X112.000 Y99.000 E68.9885 F2000.0
G0 X46.000 Y36.000 F2200.0
G1 X43.000 Y39.000 E69.4127 F2000.0
G1 X40.000 Y48.000 E70.3614 F2000.0
G1 X40.000 Y61.000 E71.6614 F2000.0
G1 X43.000 Y71.000 E72.7055 F2000.0
G1 X48.000 Y74.000 E73.2885 F2000.0
G1 X53.000 Y70.000 E73.9289 F2000.0
G1 X56.000 Y52.000 E75.7537 F2000.0
G1 X52.000 Y38.000 E77.2097 F2000.0
G1 X50.000 Y36.000 E77.4926 F2000.0
G1 X47.000 Y36.000 E77.7926 F2000.0
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