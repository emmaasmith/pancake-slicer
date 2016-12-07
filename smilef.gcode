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
G0 X1.000 Y89.000 Z1.300 E0 F2000.0
G1 X1.000 Y95.000 E2.3000 F2000.0
G1 X2.000 Y96.000 E2.3707 F2000.0
G1 X2.000 Y100.000 E2.5707 F2000.0
G1 X3.000 Y101.000 E2.6414 F2000.0
G1 X5.000 Y109.000 E3.0537 F2000.0
G1 X7.000 Y112.000 E3.2340 F2000.0
G1 X7.000 Y114.000 E3.3340 F2000.0
G1 X11.000 Y122.000 E3.7812 F2000.0
G1 X13.000 Y124.000 E3.9226 F2000.0
G1 X15.000 Y128.000 E4.1463 F2000.0
G1 X18.000 Y131.000 E4.3584 F2000.0
G1 X18.000 Y132.000 E4.4084 F2000.0
G1 X28.000 Y142.000 E5.1155 F2000.0
G1 X29.000 Y142.000 E5.1655 F2000.0
G1 X32.000 Y145.000 E5.3776 F2000.0
G1 X33.000 Y145.000 E5.4276 F2000.0
G1 X38.000 Y149.000 E5.7478 F2000.0
G1 X44.000 Y152.000 E6.0832 F2000.0
G1 X46.000 Y152.000 E6.1832 F2000.0
G1 X49.000 Y154.000 E6.3635 F2000.0
G1 X54.000 Y155.000 E6.6184 F2000.0
G0 X148.000 Y88.000 E0 F2200.0
G1 X148.000 Y95.000 E6.9684 F2000.0
G1 X147.000 Y96.000 E7.0391 F2000.0
G1 X147.000 Y100.000 E7.2391 F2000.0
G1 X146.000 Y101.000 E7.3098 F2000.0
G1 X144.000 Y109.000 E7.7221 F2000.0
G1 X138.000 Y121.000 E8.3930 F2000.0
G1 X136.000 Y123.000 E8.5344 F2000.0
G1 X134.000 Y127.000 E8.7580 F2000.0
G1 X131.000 Y130.000 E8.9701 F2000.0
G1 X131.000 Y131.000 E9.0201 F2000.0
G1 X120.000 Y142.000 E9.7979 F2000.0
G1 X119.000 Y142.000 E9.8479 F2000.0
G1 X116.000 Y145.000 E10.0601 F2000.0
G1 X115.000 Y145.000 E10.1101 F2000.0
G1 X110.000 Y149.000 E10.4302 F2000.0
G1 X100.000 Y154.000 E10.9893 F2000.0
G1 X98.000 Y154.000 E11.0893 F2000.0
G1 X94.000 Y156.000 E11.3129 F2000.0
G1 X84.000 Y157.000 E11.8154 F2000.0
G1 X94.000 Y156.000 E12.3178 F2000.0
G1 X95.000 Y155.000 E12.3886 F2000.0
G0 X111.000 Y57.000 E0 F2200.0
G1 X110.000 Y58.000 E12.4593 F2000.0
G1 X107.000 Y58.000 E12.6093 F2000.0
G1 X103.000 Y60.000 E12.8329 F2000.0
G1 X99.000 Y60.000 E13.0329 F2000.0
G1 X98.000 Y61.000 E13.1036 F2000.0
G1 X90.000 Y63.000 E13.5159 F2000.0
G1 X87.000 Y66.000 E13.7280 F2000.0
G1 X88.000 Y65.000 E13.7987 F2000.0
G1 X90.000 Y66.000 E13.9105 F2000.0
G1 X88.000 Y68.000 E14.0520 F2000.0
G1 X89.000 Y68.000 E14.1020 F2000.0
G1 X90.000 Y66.000 E14.2138 F2000.0
G1 X92.000 Y66.000 E14.3138 F2000.0
G1 X96.000 Y64.000 E14.5374 F2000.0
G1 X106.000 Y64.000 E15.0374 F2000.0
G1 X107.000 Y65.000 E15.1081 F2000.0
G1 X110.000 Y65.000 E15.2581 F2000.0
G1 X111.000 Y66.000 E15.3288 F2000.0
G1 X114.000 Y66.000 E15.4788 F2000.0
G1 X115.000 Y67.000 E15.5495 F2000.0
G1 X121.000 Y68.000 E15.8536 F2000.0
G1 X119.000 Y68.000 E15.9536 F2000.0
G1 X118.000 Y67.000 E16.0244 F2000.0
G1 X119.000 Y66.000 E16.0951 F2000.0
G1 X121.000 Y66.000 E16.1951 F2000.0
G1 X118.000 Y65.000 E16.3532 F2000.0
G0 X84.000 Y1.000 E0 F2200.0
G1 X90.000 Y1.000 E16.6532 F2000.0
G1 X91.000 Y2.000 E16.7239 F2000.0
G1 X94.000 Y2.000 E16.8739 F2000.0
G1 X95.000 Y3.000 E16.9446 F2000.0
G1 X100.000 Y4.000 E17.1996 F2000.0
G1 X110.000 Y9.000 E17.7586 F2000.0
G1 X112.000 Y11.000 E17.9000 F2000.0
G1 X116.000 Y13.000 E18.1236 F2000.0
G1 X119.000 Y16.000 E18.3357 F2000.0
G1 X120.000 Y16.000 E18.3857 F2000.0
G1 X131.000 Y27.000 E19.1635 F2000.0
G1 X131.000 Y28.000 E19.2135 F2000.0
G1 X134.000 Y31.000 E19.4257 F2000.0
G1 X134.000 Y32.000 E19.4757 F2000.0
G1 X138.000 Y37.000 E19.7958 F2000.0
G1 X144.000 Y49.000 E20.4667 F2000.0
G1 X144.000 Y51.000 E20.5667 F2000.0
G1 X145.000 Y52.000 E20.6374 F2000.0
G1 X145.000 Y54.000 E20.7374 F2000.0
G1 X147.000 Y58.000 E20.9610 F2000.0
G1 X147.000 Y62.000 E21.1610 F2000.0
G1 X148.000 Y63.000 E21.2317 F2000.0
G1 X148.000 Y70.000 E21.5817 F2000.0
G1 X148.000 Y63.000 E21.9317 F2000.0
G0 X59.000 Y1.000 E0 F2200.0
G1 X58.000 Y2.000 E22.0024 F2000.0
G1 X55.000 Y2.000 E22.1524 F2000.0
G1 X54.000 Y3.000 E22.2231 F2000.0
G1 X49.000 Y4.000 E22.4781 F2000.0
G1 X46.000 Y6.000 E22.6583 F2000.0
G1 X44.000 Y6.000 E22.7583 F2000.0
G1 X38.000 Y9.000 E23.0937 F2000.0
G1 X36.000 Y11.000 E23.2352 F2000.0
G1 X32.000 Y13.000 E23.4588 F2000.0
G1 X29.000 Y16.000 E23.6709 F2000.0
G1 X28.000 Y16.000 E23.7209 F2000.0
G1 X18.000 Y26.000 E24.4280 F2000.0
G1 X18.000 Y27.000 E24.4780 F2000.0
G1 X15.000 Y30.000 E24.6901 F2000.0
G1 X15.000 Y31.000 E24.7401 F2000.0
G1 X11.000 Y36.000 E25.0603 F2000.0
G1 X6.000 Y46.000 E25.6193 F2000.0
G1 X6.000 Y48.000 E25.7193 F2000.0
G1 X5.000 Y49.000 E25.7900 F2000.0
G1 X5.000 Y51.000 E25.8900 F2000.0
G1 X4.000 Y52.000 E25.9607 F2000.0
G1 X4.000 Y54.000 E26.0607 F2000.0
G1 X2.000 Y58.000 E26.2843 F2000.0
G1 X2.000 Y62.000 E26.4843 F2000.0
G1 X1.000 Y63.000 E26.5551 F2000.0
G1 X1.000 Y69.000 E26.8551 F2000.0
G0 X112.000 Y98.000 E0 F2200.0
G1 X110.000 Y102.000 E27.0787 F2000.0
G1 X101.000 Y111.000 E27.7151 F2000.0
G1 X88.000 Y118.000 E28.4533 F2000.0
G1 X86.000 Y118.000 E28.5533 F2000.0
G1 X82.000 Y120.000 E28.7769 F2000.0
G1 X63.000 Y120.000 E29.7269 F2000.0
G1 X62.000 Y119.000 E29.7976 F2000.0
G1 X59.000 Y119.000 E29.9476 F2000.0
G1 X51.000 Y115.000 E30.3948 F2000.0
G1 X47.000 Y111.000 E30.6777 F2000.0
G1 X45.000 Y112.000 E30.7895 F2000.0
G1 X45.000 Y113.000 E30.8395 F2000.0
G1 X51.000 Y119.000 E31.2637 F2000.0
G1 X55.000 Y121.000 E31.4873 F2000.0
G1 X57.000 Y121.000 E31.5873 F2000.0
G1 X61.000 Y123.000 E31.8110 F2000.0
G1 X78.000 Y123.000 E32.6610 F2000.0
G1 X79.000 Y122.000 E32.7317 F2000.0
G1 X82.000 Y122.000 E32.8817 F2000.0
G1 X83.000 Y121.000 E32.9524 F2000.0
G1 X87.000 Y121.000 E33.1524 F2000.0
G1 X103.000 Y113.000 E34.0468 F2000.0
G1 X107.000 Y109.000 E34.3296 F2000.0
G1 X108.000 Y109.000 E34.3796 F2000.0
G1 X112.000 Y104.000 E34.6998 F2000.0
G1 X113.000 Y100.000 E34.9060 F2000.0
G1 X114.000 Y99.000 E34.9767 F2000.0
G1 X114.000 Y98.000 E35.0267 F2000.0
G1 X113.000 Y100.000 E35.1385 F2000.0
G1 X112.000 Y99.000 E35.2092 F2000.0
G0 X46.000 Y36.000 E0 F2200.0
G1 X43.000 Y39.000 E35.4213 F2000.0
G1 X42.000 Y43.000 E35.6275 F2000.0
G1 X41.000 Y44.000 E35.6982 F2000.0
G1 X41.000 Y47.000 E35.8482 F2000.0
G1 X40.000 Y48.000 E35.9189 F2000.0
G1 X40.000 Y61.000 E36.5689 F2000.0
G1 X41.000 Y62.000 E36.6396 F2000.0
G1 X41.000 Y66.000 E36.8396 F2000.0
G1 X43.000 Y69.000 E37.0199 F2000.0
G1 X43.000 Y71.000 E37.1199 F2000.0
G1 X45.000 Y73.000 E37.2613 F2000.0
G1 X47.000 Y73.000 E37.3613 F2000.0
G1 X48.000 Y74.000 E37.4320 F2000.0
G1 X53.000 Y70.000 E37.7522 F2000.0
G1 X53.000 Y68.000 E37.8522 F2000.0
G1 X55.000 Y64.000 E38.0758 F2000.0
G1 X56.000 Y52.000 E38.6779 F2000.0
G1 X55.000 Y51.000 E38.7486 F2000.0
G1 X55.000 Y45.000 E39.0486 F2000.0
G1 X54.000 Y44.000 E39.1193 F2000.0
G1 X54.000 Y42.000 E39.2193 F2000.0
G1 X52.000 Y38.000 E39.4429 F2000.0
G1 X50.000 Y36.000 E39.5843 F2000.0
G1 X47.000 Y36.000 E39.7343 F2000.0
;INFILL:0
G0 X2.275 Y60.950 Z1.300 E0 F3000.0
G1 X2.275 Y99.775 E39.7343 F20000.0
G0 X2.800 Y100.300 E0 F3000.0
G1 X2.800 Y59.900 E39.7343 F20000.0
G0 X3.325 Y58.850 E0 F3000.0
G1 X3.325 Y103.825 E39.7343 F20000.0
G0 X3.850 Y104.350 E0 F3000.0
G1 X3.850 Y57.800 E39.7343 F20000.0
G0 X4.375 Y55.125 E0 F3000.0
G1 X4.375 Y106.000 E39.7343 F20000.0
G0 X4.900 Y108.100 E0 F3000.0
G1 X4.900 Y54.600 E39.7343 F20000.0
G0 X5.425 Y51.863 E0 F3000.0
G1 X5.425 Y110.200 E39.7343 F20000.0
G0 X5.950 Y112.300 E0 F3000.0
G1 X5.950 Y51.075 E39.7343 F20000.0
G0 X6.475 Y50.288 E0 F3000.0
G1 X6.475 Y113.450 E39.7343 F20000.0
G0 X7.000 Y48.500 E0 F3000.0
G1 X7.000 Y47.500 E39.7343 F20000.0
G0 X7.525 Y46.450 E0 F3000.0
G1 X7.525 Y115.550 E39.7343 F20000.0
G0 X8.050 Y116.600 E0 F3000.0
G1 X8.050 Y45.400 E39.7343 F20000.0
G0 X8.575 Y44.350 E0 F3000.0
G1 X8.575 Y117.650 E39.7343 F20000.0
G0 X9.100 Y118.700 E0 F3000.0
G1 X9.100 Y43.300 E39.7343 F20000.0
G0 X9.625 Y42.250 E0 F3000.0
G1 X9.625 Y119.750 E39.7343 F20000.0
G0 X10.150 Y120.800 E0 F3000.0
G1 X10.150 Y41.200 E39.7343 F20000.0
G0 X10.675 Y40.150 E0 F3000.0
G1 X10.675 Y121.850 E39.7343 F20000.0
G0 X11.200 Y122.700 E0 F3000.0
G1 X11.200 Y39.233 E39.7343 F20000.0
G0 X11.725 Y38.533 E0 F3000.0
G1 X11.725 Y123.225 E39.7343 F20000.0
G0 X12.250 Y123.750 E0 F3000.0
G1 X12.250 Y37.833 E39.7343 F20000.0
G0 X12.775 Y37.133 E0 F3000.0
G1 X12.775 Y124.275 E39.7343 F20000.0
G0 X13.300 Y125.025 E0 F3000.0
G1 X13.300 Y36.433 E39.7343 F20000.0
G0 X13.825 Y35.733 E0 F3000.0
G1 X13.825 Y125.944 E39.7343 F20000.0
G0 X14.350 Y126.862 E0 F3000.0
G1 X14.350 Y35.033 E39.7343 F20000.0
G0 X14.875 Y34.333 E0 F3000.0
G1 X14.875 Y127.781 E39.7343 F20000.0
G0 X15.400 Y128.700 E0 F3000.0
G1 X15.400 Y33.633 E39.7343 F20000.0
G0 X15.925 Y32.933 E0 F3000.0
G1 X15.925 Y129.619 E39.7343 F20000.0
G0 X16.450 Y130.537 E0 F3000.0
G1 X16.450 Y32.233 E39.7343 F20000.0
G0 X16.975 Y31.533 E0 F3000.0
G1 X16.975 Y131.456 E39.7343 F20000.0
G0 X17.500 Y132.050 E0 F3000.0
G1 X17.500 Y30.000 E39.7343 F20000.0
G0 X18.025 Y29.475 E0 F3000.0
G1 X18.025 Y132.627 E39.7343 F20000.0
G0 X18.550 Y133.205 E0 F3000.0
G1 X18.550 Y28.950 E39.7343 F20000.0
G0 X19.075 Y28.425 E0 F3000.0
G1 X19.075 Y133.782 E39.7343 F20000.0
G0 X19.600 Y134.360 E0 F3000.0
G1 X19.600 Y27.900 E39.7343 F20000.0
G0 X20.125 Y27.375 E0 F3000.0
G1 X20.125 Y134.938 E39.7343 F20000.0
G0 X20.650 Y135.515 E0 F3000.0
G1 X20.650 Y26.850 E39.7343 F20000.0
G0 X21.175 Y26.325 E0 F3000.0
G1 X21.175 Y136.093 E39.7343 F20000.0
G0 X21.700 Y136.670 E0 F3000.0
G1 X21.700 Y25.800 E39.7343 F20000.0
G0 X22.225 Y24.298 E0 F3000.0
G1 X22.225 Y137.248 E39.7343 F20000.0
G0 X22.750 Y137.825 E0 F3000.0
G1 X22.750 Y23.825 E39.7343 F20000.0
G0 X23.275 Y23.353 E0 F3000.0
G1 X23.275 Y138.403 E39.7343 F20000.0
G0 X23.800 Y138.980 E0 F3000.0
G1 X23.800 Y22.880 E39.7343 F20000.0
G0 X24.325 Y22.408 E0 F3000.0
G1 X24.325 Y139.558 E39.7343 F20000.0
G0 X24.850 Y140.135 E0 F3000.0
G1 X24.850 Y21.935 E39.7343 F20000.0
G0 X25.375 Y21.463 E0 F3000.0
G1 X25.375 Y140.712 E39.7343 F20000.0
G0 X25.900 Y141.290 E0 F3000.0
G1 X25.900 Y20.990 E39.7343 F20000.0
G0 X26.425 Y20.518 E0 F3000.0
G1 X26.425 Y141.868 E39.7343 F20000.0
G0 X26.950 Y142.445 E0 F3000.0
G1 X26.950 Y20.045 E39.7343 F20000.0
G0 X27.475 Y19.573 E0 F3000.0
G1 X27.475 Y142.500 E39.7343 F20000.0
G0 X28.000 Y142.500 E0 F3000.0
G1 X28.000 Y19.100 E39.7343 F20000.0
G0 X28.525 Y18.628 E0 F3000.0
G1 X28.525 Y143.025 E39.7343 F20000.0
G0 X29.050 Y143.550 E0 F3000.0
G1 X29.050 Y18.155 E39.7343 F20000.0
G0 X29.575 Y17.683 E0 F3000.0
G1 X29.575 Y144.075 E39.7343 F20000.0
G0 X30.100 Y144.600 E0 F3000.0
G1 X30.100 Y17.210 E39.7343 F20000.0
G0 X30.625 Y16.738 E0 F3000.0
G1 X30.625 Y145.125 E39.7343 F20000.0
G0 X31.150 Y145.500 E0 F3000.0
G1 X31.150 Y16.265 E39.7343 F20000.0
G0 X31.675 Y15.793 E0 F3000.0
G1 X31.675 Y145.500 E39.7343 F20000.0
G0 X32.200 Y145.700 E0 F3000.0
G1 X32.200 Y15.500 E39.7343 F20000.0
G0 X32.725 Y15.500 E0 F3000.0
G1 X32.725 Y146.225 E39.7343 F20000.0
G0 X33.250 Y146.750 E0 F3000.0
G1 X33.250 Y15.300 E39.7343 F20000.0
G0 X33.775 Y14.880 E0 F3000.0
G1 X33.775 Y147.275 E39.7343 F20000.0
G0 X34.300 Y147.800 E0 F3000.0
G1 X34.300 Y14.460 E39.7343 F20000.0
G0 X34.825 Y14.040 E0 F3000.0
G1 X34.825 Y148.325 E39.7343 F20000.0
G0 X35.350 Y148.850 E0 F3000.0
G1 X35.350 Y13.620 E39.7343 F20000.0
G0 X35.875 Y13.200 E0 F3000.0
G1 X35.875 Y149.375 E39.7343 F20000.0
G0 X36.400 Y149.671 E0 F3000.0
G1 X36.400 Y12.780 E39.7343 F20000.0
G0 X36.925 Y12.360 E0 F3000.0
G1 X36.925 Y149.896 E39.7343 F20000.0
G0 X37.450 Y150.121 E0 F3000.0
G1 X37.450 Y11.940 E39.7343 F20000.0
G0 X37.975 Y11.520 E0 F3000.0
G1 X37.975 Y150.346 E39.7343 F20000.0
G0 X38.500 Y150.571 E0 F3000.0
G1 X38.500 Y11.333 E39.7343 F20000.0
G0 X39.025 Y11.158 E0 F3000.0
G1 X39.025 Y150.796 E39.7343 F20000.0
G0 X39.550 Y151.021 E0 F3000.0
G1 X39.550 Y10.983 E39.7343 F20000.0
G0 X40.075 Y10.808 E0 F3000.0
G1 X40.075 Y151.246 E39.7343 F20000.0
G0 X40.600 Y151.471 E0 F3000.0
G1 X40.600 Y10.633 E39.7343 F20000.0
G0 X41.125 Y10.406 E0 F3000.0
G1 X41.125 Y151.696 E39.7343 F20000.0
G0 X41.650 Y151.921 E0 F3000.0
G1 X41.650 Y10.013 E39.7343 F20000.0
G0 X42.175 Y9.619 E0 F3000.0
G1 X42.175 Y152.146 E39.7343 F20000.0
G0 X42.700 Y152.371 E0 F3000.0
G1 X42.700 Y9.225 E39.7343 F20000.0
G0 X43.225 Y8.831 E0 F3000.0
G1 X43.225 Y152.725 E39.7343 F20000.0
G0 X43.750 Y153.250 E0 F3000.0
G1 X43.750 Y8.438 E39.7343 F20000.0
G0 X44.275 Y8.044 E0 F3000.0
G1 X44.275 Y153.775 E39.7343 F20000.0
G0 X44.800 Y154.300 E0 F3000.0
G1 X44.800 Y7.650 E39.7343 F20000.0
G0 X45.325 Y7.500 E0 F3000.0
G1 X45.325 Y154.500 E39.7343 F20000.0
G0 X45.850 Y154.500 E0 F3000.0
G1 X45.850 Y7.500 E39.7343 F20000.0
G0 X46.375 Y7.500 E0 F3000.0
G1 X46.375 Y154.500 E39.7343 F20000.0
G0 X46.900 Y154.500 E0 F3000.0
G1 X46.900 Y7.500 E39.7343 F20000.0
G0 X47.425 Y7.288 E0 F3000.0
G1 X47.425 Y154.783 E39.7343 F20000.0
G0 X47.950 Y155.133 E0 F3000.0
G1 X47.950 Y7.025 E39.7343 F20000.0
G0 X48.475 Y6.763 E0 F3000.0
G1 X48.475 Y155.483 E39.7343 F20000.0
G0 X49.000 Y155.833 E0 F3000.0
G1 X49.000 Y6.500 E39.7343 F20000.0
G0 X49.525 Y6.238 E0 F3000.0
G1 X49.525 Y156.183 E39.7343 F20000.0
G0 X50.050 Y156.510 E0 F3000.0
G1 X50.050 Y5.975 E39.7343 F20000.0
G0 X50.575 Y5.713 E0 F3000.0
G1 X50.575 Y156.615 E39.7343 F20000.0
G0 X51.100 Y156.720 E0 F3000.0
G1 X51.100 Y5.450 E39.7343 F20000.0
G0 X51.625 Y5.188 E0 F3000.0
G1 X51.625 Y156.825 E39.7343 F20000.0
G0 X52.150 Y156.930 E0 F3000.0
G1 X52.150 Y4.925 E39.7343 F20000.0
G0 X52.675 Y4.663 E0 F3000.0
G1 X52.675 Y157.035 E39.7343 F20000.0
G0 X53.200 Y157.140 E0 F3000.0
G1 X53.200 Y4.500 E39.7343 F20000.0
G0 X53.725 Y4.500 E0 F3000.0
G1 X53.725 Y157.245 E39.7343 F20000.0
G0 X54.250 Y157.350 E0 F3000.0
G1 X54.250 Y4.500 E39.7343 F20000.0
G0 X54.775 Y4.500 E0 F3000.0
G1 X54.775 Y157.455 E39.7343 F20000.0
G0 X55.300 Y157.700 E0 F3000.0
G1 X55.300 Y4.300 E39.7343 F20000.0
G0 X55.825 Y3.950 E0 F3000.0
G1 X55.825 Y158.050 E39.7343 F20000.0
G0 X56.350 Y158.400 E0 F3000.0
G1 X56.350 Y3.600 E39.7343 F20000.0
G0 X56.875 Y3.250 E0 F3000.0
G1 X56.875 Y158.750 E39.7343 F20000.0
G0 X57.400 Y159.100 E0 F3000.0
G1 X57.400 Y2.900 E39.7343 F20000.0
G0 X57.925 Y2.550 E0 F3000.0
G1 X57.925 Y159.450 E39.7343 F20000.0
G0 X58.450 Y159.500 E0 F3000.0
G1 X58.450 Y2.500 E39.7343 F20000.0
G0 X58.975 Y2.500 E0 F3000.0
G1 X58.975 Y159.500 E39.7343 F20000.0
G0 X59.500 Y159.500 E0 F3000.0
G1 X59.500 Y2.500 E39.7343 F20000.0
G0 X60.025 Y2.500 E0 F3000.0
G1 X60.025 Y159.500 E39.7343 F20000.0
G0 X60.550 Y159.500 E0 F3000.0
G1 X60.550 Y2.500 E39.7343 F20000.0
G0 X61.075 Y2.500 E0 F3000.0
G1 X61.075 Y159.500 E39.7343 F20000.0
G0 X61.600 Y159.500 E0 F3000.0
G1 X61.600 Y2.500 E39.7343 F20000.0
G0 X62.125 Y2.500 E0 F3000.0
G1 X62.125 Y159.500 E39.7343 F20000.0
G0 X62.650 Y159.500 E0 F3000.0
G1 X62.650 Y2.500 E39.7343 F20000.0
G0 X63.175 Y2.500 E0 F3000.0
G1 X63.175 Y159.500 E39.7343 F20000.0
G0 X63.700 Y159.500 E0 F3000.0
G1 X63.700 Y2.500 E39.7343 F20000.0
G0 X64.225 Y2.500 E0 F3000.0
G1 X64.225 Y159.500 E39.7343 F20000.0
G0 X64.750 Y159.500 E0 F3000.0
G1 X64.750 Y2.500 E39.7343 F20000.0
G0 X65.275 Y2.500 E0 F3000.0
G1 X65.275 Y159.500 E39.7343 F20000.0
G0 X65.800 Y159.500 E0 F3000.0
G1 X65.800 Y2.500 E39.7343 F20000.0
G0 X66.325 Y2.500 E0 F3000.0
G1 X66.325 Y159.500 E39.7343 F20000.0
G0 X66.850 Y159.500 E0 F3000.0
G1 X66.850 Y2.500 E39.7343 F20000.0
G0 X67.375 Y2.500 E0 F3000.0
G1 X67.375 Y159.500 E39.7343 F20000.0
G0 X67.900 Y159.500 E0 F3000.0
G1 X67.900 Y2.500 E39.7343 F20000.0
G0 X68.425 Y2.500 E0 F3000.0
G1 X68.425 Y159.500 E39.7343 F20000.0
G0 X68.950 Y159.500 E0 F3000.0
G1 X68.950 Y2.500 E39.7343 F20000.0
G0 X69.475 Y2.500 E0 F3000.0
G1 X69.475 Y159.500 E39.7343 F20000.0
G0 X70.000 Y159.500 E0 F3000.0
G1 X70.000 Y2.500 E39.7343 F20000.0
G0 X70.525 Y2.500 E0 F3000.0
G1 X70.525 Y159.500 E39.7343 F20000.0
G0 X71.050 Y159.500 E0 F3000.0
G1 X71.050 Y2.500 E39.7343 F20000.0
G0 X71.575 Y2.500 E0 F3000.0
G1 X71.575 Y159.500 E39.7343 F20000.0
G0 X72.100 Y159.500 E0 F3000.0
G1 X72.100 Y2.500 E39.7343 F20000.0
G0 X72.625 Y2.500 E0 F3000.0
G1 X72.625 Y159.500 E39.7343 F20000.0
G0 X73.150 Y159.500 E0 F3000.0
G1 X73.150 Y2.500 E39.7343 F20000.0
G0 X73.675 Y2.500 E0 F3000.0
G1 X73.675 Y159.500 E39.7343 F20000.0
G0 X74.200 Y159.500 E0 F3000.0
G1 X74.200 Y2.500 E39.7343 F20000.0
G0 X74.725 Y2.500 E0 F3000.0
G1 X74.725 Y159.500 E39.7343 F20000.0
G0 X75.250 Y159.500 E0 F3000.0
G1 X75.250 Y2.500 E39.7343 F20000.0
G0 X75.775 Y2.500 E0 F3000.0
G1 X75.775 Y159.500 E39.7343 F20000.0
G0 X76.300 Y159.500 E0 F3000.0
G1 X76.300 Y2.500 E39.7343 F20000.0
G0 X76.825 Y2.500 E0 F3000.0
G1 X76.825 Y159.500 E39.7343 F20000.0
G0 X77.350 Y159.500 E0 F3000.0
G1 X77.350 Y2.500 E39.7343 F20000.0
G0 X77.875 Y2.500 E0 F3000.0
G1 X77.875 Y159.500 E39.7343 F20000.0
G0 X78.400 Y159.500 E0 F3000.0
G1 X78.400 Y2.500 E39.7343 F20000.0
G0 X78.925 Y2.500 E0 F3000.0
G1 X78.925 Y159.500 E39.7343 F20000.0
G0 X79.450 Y159.500 E0 F3000.0
G1 X79.450 Y2.500 E39.7343 F20000.0
G0 X79.975 Y2.500 E0 F3000.0
G1 X79.975 Y159.500 E39.7343 F20000.0
G0 X80.500 Y159.500 E0 F3000.0
G1 X80.500 Y2.500 E39.7343 F20000.0
G0 X81.025 Y2.500 E0 F3000.0
G1 X81.025 Y159.500 E39.7343 F20000.0
G0 X81.550 Y159.500 E0 F3000.0
G1 X81.550 Y2.500 E39.7343 F20000.0
G0 X82.075 Y2.500 E0 F3000.0
G1 X82.075 Y159.500 E39.7343 F20000.0
G0 X82.600 Y159.500 E0 F3000.0
G1 X82.600 Y2.500 E39.7343 F20000.0
G0 X83.125 Y2.500 E0 F3000.0
G1 X83.125 Y159.500 E39.7343 F20000.0
G0 X83.650 Y159.500 E0 F3000.0
G1 X83.650 Y2.500 E39.7343 F20000.0
G0 X84.175 Y2.500 E0 F3000.0
G1 X84.175 Y159.500 E39.7343 F20000.0
G0 X84.700 Y159.500 E0 F3000.0
G1 X84.700 Y2.500 E39.7343 F20000.0
G0 X85.225 Y2.500 E0 F3000.0
G1 X85.225 Y159.500 E39.7343 F20000.0
G0 X85.750 Y159.500 E0 F3000.0
G1 X85.750 Y2.500 E39.7343 F20000.0
G0 X86.275 Y2.500 E0 F3000.0
G1 X86.275 Y159.500 E39.7343 F20000.0
G0 X86.800 Y159.500 E0 F3000.0
G1 X86.800 Y2.500 E39.7343 F20000.0
G0 X87.325 Y2.500 E0 F3000.0
G1 X87.325 Y159.500 E39.7343 F20000.0
G0 X87.850 Y159.500 E0 F3000.0
G1 X87.850 Y2.500 E39.7343 F20000.0
G0 X88.375 Y2.500 E0 F3000.0
G1 X88.375 Y159.500 E39.7343 F20000.0
G0 X88.900 Y159.500 E0 F3000.0
G1 X88.900 Y2.500 E39.7343 F20000.0
G0 X89.425 Y2.500 E0 F3000.0
G1 X89.425 Y159.500 E39.7343 F20000.0
G0 X89.950 Y159.500 E0 F3000.0
G1 X89.950 Y2.500 E39.7343 F20000.0
G0 X90.475 Y2.500 E0 F3000.0
G1 X90.475 Y159.500 E39.7343 F20000.0
G0 X91.000 Y159.500 E0 F3000.0
G1 X91.000 Y2.500 E39.7343 F20000.0
G0 X91.525 Y2.500 E0 F3000.0
G1 X91.525 Y159.500 E39.7343 F20000.0
G0 X92.050 Y159.500 E0 F3000.0
G1 X92.050 Y2.500 E39.7343 F20000.0
G0 X92.575 Y2.500 E0 F3000.0
G1 X92.575 Y159.500 E39.7343 F20000.0
G0 X93.100 Y159.500 E0 F3000.0
G1 X93.100 Y2.500 E39.7343 F20000.0
G0 X93.625 Y2.500 E0 F3000.0
G1 X93.625 Y159.500 E39.7343 F20000.0
G0 X94.150 Y159.500 E0 F3000.0
G1 X94.150 Y2.500 E39.7343 F20000.0
G0 X94.675 Y2.500 E0 F3000.0
G1 X94.675 Y159.500 E39.7343 F20000.0
G0 X95.200 Y159.300 E0 F3000.0
G1 X95.200 Y2.600 E39.7343 F20000.0
G0 X95.725 Y2.862 E0 F3000.0
G1 X95.725 Y158.775 E39.7343 F20000.0
G0 X96.250 Y158.250 E0 F3000.0
G1 X96.250 Y3.125 E39.7343 F20000.0
G0 X96.775 Y3.387 E0 F3000.0
G1 X96.775 Y157.725 E39.7343 F20000.0
G0 X97.300 Y157.500 E0 F3000.0
G1 X97.300 Y3.650 E39.7343 F20000.0
G0 X97.825 Y3.912 E0 F3000.0
G1 X97.825 Y157.500 E39.7343 F20000.0
G0 X98.350 Y157.500 E0 F3000.0
G1 X98.350 Y4.175 E39.7343 F20000.0
G0 X98.875 Y4.437 E0 F3000.0
G1 X98.875 Y157.500 E39.7343 F20000.0
G0 X99.400 Y157.500 E0 F3000.0
G1 X99.400 Y4.700 E39.7343 F20000.0
G0 X99.925 Y4.962 E0 F3000.0
G1 X99.925 Y157.500 E39.7343 F20000.0
G0 X100.450 Y157.050 E0 F3000.0
G1 X100.450 Y5.225 E39.7343 F20000.0
G0 X100.975 Y5.487 E0 F3000.0
G1 X100.975 Y156.525 E39.7343 F20000.0
G0 X101.500 Y156.400 E0 F3000.0
G1 X101.500 Y5.600 E39.7343 F20000.0
G0 X102.025 Y5.705 E0 F3000.0
G1 X102.025 Y156.295 E39.7343 F20000.0
G0 X102.550 Y156.190 E0 F3000.0
G1 X102.550 Y5.810 E39.7343 F20000.0
G0 X103.075 Y5.915 E0 F3000.0
G1 X103.075 Y156.085 E39.7343 F20000.0
G0 X103.600 Y155.980 E0 F3000.0
G1 X103.600 Y6.020 E39.7343 F20000.0
G0 X104.125 Y6.125 E0 F3000.0
G1 X104.125 Y155.875 E39.7343 F20000.0
G0 X104.650 Y155.770 E0 F3000.0
G1 X104.650 Y6.230 E39.7343 F20000.0
G0 X105.175 Y6.335 E0 F3000.0
G1 X105.175 Y155.665 E39.7343 F20000.0
G0 X105.700 Y155.560 E0 F3000.0
G1 X105.700 Y6.440 E39.7343 F20000.0
G0 X106.225 Y6.669 E0 F3000.0
G1 X106.225 Y155.387 E39.7343 F20000.0
G0 X106.750 Y155.125 E0 F3000.0
G1 X106.750 Y7.062 E39.7343 F20000.0
G0 X107.275 Y7.456 E0 F3000.0
G1 X107.275 Y154.863 E39.7343 F20000.0
G0 X107.800 Y154.600 E0 F3000.0
G1 X107.800 Y7.850 E39.7343 F20000.0
G0 X108.325 Y8.244 E0 F3000.0
G1 X108.325 Y154.338 E39.7343 F20000.0
G0 X108.850 Y154.075 E0 F3000.0
G1 X108.850 Y8.637 E39.7343 F20000.0
G0 X109.375 Y9.031 E0 F3000.0
G1 X109.375 Y153.812 E39.7343 F20000.0
G0 X109.900 Y153.550 E0 F3000.0
G1 X109.900 Y9.425 E39.7343 F20000.0
G0 X110.425 Y9.670 E0 F3000.0
G1 X110.425 Y153.075 E39.7343 F20000.0
G0 X110.950 Y152.550 E0 F3000.0
G1 X110.950 Y9.880 E39.7343 F20000.0
G0 X111.475 Y10.090 E0 F3000.0
G1 X111.475 Y152.025 E39.7343 F20000.0
G0 X112.000 Y151.500 E0 F3000.0
G1 X112.000 Y10.300 E39.7343 F20000.0
G0 X112.525 Y10.510 E0 F3000.0
G1 X112.525 Y151.290 E39.7343 F20000.0
G0 X113.050 Y151.080 E0 F3000.0
G1 X113.050 Y10.720 E39.7343 F20000.0
G0 X113.575 Y10.930 E0 F3000.0
G1 X113.575 Y150.870 E39.7343 F20000.0
G0 X114.100 Y150.660 E0 F3000.0
G1 X114.100 Y11.140 E39.7343 F20000.0
G0 X114.625 Y11.350 E0 F3000.0
G1 X114.625 Y150.450 E39.7343 F20000.0
G0 X115.150 Y150.240 E0 F3000.0
G1 X115.150 Y11.620 E39.7343 F20000.0
G0 X115.675 Y12.040 E0 F3000.0
G1 X115.675 Y150.030 E39.7343 F20000.0
G0 X116.200 Y149.820 E0 F3000.0
G1 X116.200 Y12.460 E39.7343 F20000.0
G0 X116.725 Y12.880 E0 F3000.0
G1 X116.725 Y149.610 E39.7343 F20000.0
G0 X117.250 Y149.250 E0 F3000.0
G1 X117.250 Y13.300 E39.7343 F20000.0
G0 X117.775 Y13.720 E0 F3000.0
G1 X117.775 Y148.725 E39.7343 F20000.0
G0 X118.300 Y148.200 E0 F3000.0
G1 X118.300 Y14.140 E39.7343 F20000.0
G0 X118.825 Y14.560 E0 F3000.0
G1 X118.825 Y147.675 E39.7343 F20000.0
G0 X119.350 Y147.150 E0 F3000.0
G1 X119.350 Y14.980 E39.7343 F20000.0
G0 X119.875 Y15.400 E0 F3000.0
G1 X119.875 Y146.625 E39.7343 F20000.0
G0 X120.400 Y146.100 E0 F3000.0
G1 X120.400 Y15.500 E39.7343 F20000.0
G0 X120.925 Y15.500 E0 F3000.0
G1 X120.925 Y145.575 E39.7343 F20000.0
G0 X121.450 Y145.500 E0 F3000.0
G1 X121.450 Y15.950 E39.7343 F20000.0
G0 X121.975 Y16.475 E0 F3000.0
G1 X121.975 Y145.500 E39.7343 F20000.0
G0 X122.500 Y145.000 E0 F3000.0
G1 X122.500 Y17.000 E39.7343 F20000.0
G0 X123.025 Y17.525 E0 F3000.0
G1 X123.025 Y144.475 E39.7343 F20000.0
G0 X123.550 Y143.950 E0 F3000.0
G1 X123.550 Y18.050 E39.7343 F20000.0
G0 X124.075 Y18.575 E0 F3000.0
G1 X124.075 Y143.425 E39.7343 F20000.0
G0 X124.600 Y142.900 E0 F3000.0
G1 X124.600 Y19.100 E39.7343 F20000.0
G0 X125.125 Y19.625 E0 F3000.0
G1 X125.125 Y142.500 E39.7343 F20000.0
G0 X125.650 Y142.500 E0 F3000.0
G1 X125.650 Y20.150 E39.7343 F20000.0
G0 X126.175 Y20.500 E0 F3000.0
G1 X126.175 Y142.325 E39.7343 F20000.0
G0 X126.700 Y141.800 E0 F3000.0
G1 X126.700 Y20.500 E39.7343 F20000.0
G0 X127.225 Y20.750 E0 F3000.0
G1 X127.225 Y141.275 E39.7343 F20000.0
G0 X127.750 Y140.750 E0 F3000.0
G1 X127.750 Y21.333 E39.7343 F20000.0
G0 X128.275 Y21.917 E0 F3000.0
G1 X128.275 Y140.225 E39.7343 F20000.0
G0 X128.800 Y139.700 E0 F3000.0
G1 X128.800 Y22.500 E39.7343 F20000.0
G0 X129.325 Y23.083 E0 F3000.0
G1 X129.325 Y139.175 E39.7343 F20000.0
G0 X129.850 Y138.650 E0 F3000.0
G1 X129.850 Y23.667 E39.7343 F20000.0
G0 X130.375 Y24.250 E0 F3000.0
G1 X130.375 Y138.125 E39.7343 F20000.0
G0 X130.900 Y137.600 E0 F3000.0
G1 X130.900 Y24.833 E39.7343 F20000.0
G0 X131.425 Y25.417 E0 F3000.0
G1 X131.425 Y136.075 E39.7343 F20000.0
G0 X131.950 Y135.550 E0 F3000.0
G1 X131.950 Y26.000 E39.7343 F20000.0
G0 X132.475 Y26.583 E0 F3000.0
G1 X132.475 Y135.025 E39.7343 F20000.0
G0 X133.000 Y134.500 E0 F3000.0
G1 X133.000 Y27.167 E39.7343 F20000.0
G0 X133.525 Y27.750 E0 F3000.0
G1 X133.525 Y133.975 E39.7343 F20000.0
G0 X134.050 Y133.450 E0 F3000.0
G1 X134.050 Y28.333 E39.7343 F20000.0
G0 X134.575 Y28.917 E0 F3000.0
G1 X134.575 Y132.925 E39.7343 F20000.0
G0 X135.100 Y131.383 E0 F3000.0
G1 X135.100 Y29.500 E39.7343 F20000.0
G0 X135.625 Y30.083 E0 F3000.0
G1 X135.625 Y130.771 E39.7343 F20000.0
G0 X136.150 Y130.158 E0 F3000.0
G1 X136.150 Y31.687 E39.7343 F20000.0
G0 X136.675 Y32.344 E0 F3000.0
G1 X136.675 Y129.546 E39.7343 F20000.0
G0 X137.200 Y128.933 E0 F3000.0
G1 X137.200 Y33.000 E39.7343 F20000.0
G0 X137.725 Y33.656 E0 F3000.0
G1 X137.725 Y128.321 E39.7343 F20000.0
G0 X138.250 Y127.708 E0 F3000.0
G1 X138.250 Y34.312 E39.7343 F20000.0
G0 X138.775 Y34.969 E0 F3000.0
G1 X138.775 Y127.096 E39.7343 F20000.0
G0 X139.300 Y126.483 E0 F3000.0
G1 X139.300 Y35.625 E39.7343 F20000.0
G0 X139.825 Y36.281 E0 F3000.0
G1 X139.825 Y125.871 E39.7343 F20000.0
G0 X140.350 Y125.258 E0 F3000.0
G1 X140.350 Y37.550 E39.7343 F20000.0
G0 X140.875 Y39.125 E0 F3000.0
G1 X140.875 Y124.646 E39.7343 F20000.0
G0 X141.400 Y123.700 E0 F3000.0
G1 X141.400 Y39.900 E39.7343 F20000.0
G0 X141.925 Y40.425 E0 F3000.0
G1 X141.925 Y122.650 E39.7343 F20000.0
G0 X142.450 Y121.600 E0 F3000.0
G1 X142.450 Y40.950 E39.7343 F20000.0
G0 X142.975 Y41.475 E0 F3000.0
G1 X142.975 Y120.550 E39.7343 F20000.0
G0 X143.500 Y119.500 E0 F3000.0
G1 X143.500 Y42.500 E39.7343 F20000.0
G0 X144.025 Y43.550 E0 F3000.0
G1 X144.025 Y118.450 E39.7343 F20000.0
G0 X144.550 Y117.400 E0 F3000.0
G1 X144.550 Y44.600 E39.7343 F20000.0
G0 X145.075 Y47.650 E0 F3000.0
G1 X145.075 Y114.388 E39.7343 F20000.0
G0 X145.600 Y113.600 E0 F3000.0
G1 X145.600 Y48.700 E39.7343 F20000.0
G0 X146.125 Y49.750 E0 F3000.0
G1 X146.125 Y112.813 E39.7343 F20000.0
G0 X146.650 Y112.025 E0 F3000.0
G1 X146.650 Y50.800 E39.7343 F20000.0
G0 X147.175 Y51.850 E0 F3000.0
G1 X147.175 Y109.238 E39.7343 F20000.0
G0 X147.700 Y108.450 E0 F3000.0
G1 X147.700 Y52.900 E39.7343 F20000.0
G0 X148.225 Y53.950 E0 F3000.0
G1 X148.225 Y107.663 E39.7343 F20000.0
G0 X148.750 Y106.875 E0 F3000.0
G1 X148.750 Y55.000 E39.7343 F20000.0
G0 X149.275 Y59.050 E0 F3000.0
G1 X149.275 Y102.950 E39.7343 F20000.0
G0 X149.800 Y101.900 E0 F3000.0
G1 X149.800 Y60.100 E39.7343 F20000.0
G0 X150.325 Y61.150 E0 F3000.0
G1 X150.325 Y100.850 E39.7343 F20000.0
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
