# Revit
U ovom repozitoriju mogu se pronaći odabrani Revit projekti koje sam napravila za vježbu.<br><br>

## 1. Napustena Kuca
Model napuštene kuće iz susjedstva "Napustena_Kuca.rvt". Kuća nikad nije bila izgrađena do kraja. Ima odličnu lokaciju zbog čega ima najbolji pogled sa balkona u cijelom susjedstvu.<br><br>

### CreateTopo.pushbutton
Teren u modelu je napravljen uz pomoć Blender add-on-a BlenderGIS, koji iz satelitskih podataka o geolokaciji kreira točan oblik reljefa. Prijenos modela iz Blendera u Revit predstavlja problem zbog razlike u zapisivanju i čitanju datoteka u ovim aliatima. Ovi alati koriste drugačije formate datoteka, pretvorba Blenderovog 3D modela u kompatibilan format rezultira gubitkom informacija o modelu.<br><br>
Kao riješenje problema prijenosa datoteke iz Blendera u Revit, pomoću pyRevit add-in-a kreirala sam Python skriptu koja iz .obj datoteke kreirane u Blenderu čita točke mesha i iz tih točki kreira toposurface. Taj toposurface se kasnije može koristiti za kreiranje toposolid reljefa.
