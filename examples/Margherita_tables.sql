CREATE TABLE NamedPizza ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, altLabel varchar(255), prefLabel varchar(255), label varchar(255));CREATE TABLE Base ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(255) );CREATE TABLE Topping ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(255) );INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Four Seasons,Four Seasons Pizza","Four Seasons","QuatroQueijos,FourSeasons");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Cajun,Cajun Pizza","Cajun","Cajun,Cajun");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Caprina,Caprina Pizza","Caprina","Caprina,Caprina");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("La Reine Pizza,La Reine","La Reine","LaReine,LaReine");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Margherita,Margherita Pizza","Margherita","Margherita,Margherita");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Parmese,Parmese Pizza","Parmense","Parmense,Parmense");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Veneziana Pizza,Veneziana","Veneziana","Veneziana,Veneziana");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("American Hot Pizza,American Hot","American Hot","AmericanHot,AmericanaPicante");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Quattro Formaggi,Quattro Formaggi Pizza","Quattro Formaggi","QuattroFormaggi,QuatroQueijos");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("American Pizza,American","American","American,Americana");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Capricciosa Pizza,Capricciosa","Capricciosa","Capricciosa,Capricciosa");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Giardiniera Pizza,Giardiniera","Giardiniera","Giardiniera,Giardiniera");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Siciliana Pizza,Siciliana","Siciliana","Siciliana,Siciliana");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Soho Pizza,Soho","Soho","Soho,Soho");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Prince Carlo,Prince Carlo Pizza","Prince Carlo","CoberturaPrinceCarlo,PrinceCarlo");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Sloppy Giuseppe Pizza,Sloppy Giuseppe","Sloppy Giuseppe","SloppyGiuseppe,SloppyGiuseppe");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Rosa,Rosa Pizza","Rosa","Rosa,Rosa");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Fiorentina Pizza,Fiorentina","Fiorentina","Fiorentina,Fiorentina");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Mushroom,Mushroom Pizza","Mushroom","Cogumelo,Mushroom");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Pollo Ad Astra Pizza,Pollo Ad Astra","Pollo Ad Astra","PolloAdAstra,PolloAdAstra");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Napoletana Pizza,Napoletana","Napoletana","Napoletana,Napoletana");INSERT INTO NamedPizza ( altLabel, prefLabel, label) VALUES ("Frutti Di Mare Pizza,Frutti Di Mare","Frutti Di Mare","FruttiDiMare,FrutosDoMar");CREATE TABLE NamedPizza_hasBase ( main_element_id int, prop_element_id int);CREATE TABLE NamedPizza_hasTopping ( main_element_id int, prop_element_id int);INSERT INTO Base (name) VALUES ("PizzaBase");INSERT INTO NamedPizza_hasBase VALUES ("1", "1");INSERT INTO Topping (name) VALUES ("MushroomTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "1");INSERT INTO Topping (name) VALUES ("CaperTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "2");INSERT INTO Topping (name) VALUES ("TomatoTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "3");INSERT INTO Topping (name) VALUES ("AnchoviesTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "4");INSERT INTO Topping (name) VALUES ("OliveTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "5");INSERT INTO Topping (name) VALUES ("MozzarellaTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "6");INSERT INTO Topping (name) VALUES ("PeperoniSausageTopping");INSERT INTO NamedPizza_hasTopping VALUES ("1", "7");INSERT INTO NamedPizza_hasBase VALUES ("2", "1");INSERT INTO Topping (name) VALUES ("PrawnsTopping");INSERT INTO NamedPizza_hasTopping VALUES ("2", "8");INSERT INTO Topping (name) VALUES ("TobascoPepperSauce");INSERT INTO NamedPizza_hasTopping VALUES ("2", "9");INSERT INTO Topping (name) VALUES ("PeperonataTopping");INSERT INTO NamedPizza_hasTopping VALUES ("2", "10");INSERT INTO Topping (name) VALUES ("OnionTopping");INSERT INTO NamedPizza_hasTopping VALUES ("2", "11");INSERT INTO NamedPizza_hasTopping VALUES ("2", "6");INSERT INTO NamedPizza_hasTopping VALUES ("2", "3");INSERT INTO NamedPizza_hasBase VALUES ("3", "1");INSERT INTO Topping (name) VALUES ("SundriedTomatoTopping");INSERT INTO NamedPizza_hasTopping VALUES ("3", "12");INSERT INTO NamedPizza_hasTopping VALUES ("3", "3");INSERT INTO Topping (name) VALUES ("GoatsCheeseTopping");INSERT INTO NamedPizza_hasTopping VALUES ("3", "13");INSERT INTO NamedPizza_hasTopping VALUES ("3", "6");INSERT INTO NamedPizza_hasBase VALUES ("4", "1");INSERT INTO Topping (name) VALUES ("HamTopping");INSERT INTO NamedPizza_hasTopping VALUES ("4", "14");INSERT INTO NamedPizza_hasTopping VALUES ("4", "5");INSERT INTO NamedPizza_hasTopping VALUES ("4", "3");INSERT INTO NamedPizza_hasTopping VALUES ("4", "1");INSERT INTO NamedPizza_hasTopping VALUES ("4", "6");INSERT INTO NamedPizza_hasBase VALUES ("5", "1");INSERT INTO NamedPizza_hasTopping VALUES ("5", "6");INSERT INTO NamedPizza_hasTopping VALUES ("5", "3");INSERT INTO NamedPizza_hasBase VALUES ("6", "1");INSERT INTO NamedPizza_hasTopping VALUES ("6", "14");INSERT INTO NamedPizza_hasTopping VALUES ("6", "3");INSERT INTO NamedPizza_hasTopping VALUES ("6", "6");INSERT INTO Topping (name) VALUES ("AsparagusTopping");INSERT INTO NamedPizza_hasTopping VALUES ("6", "15");INSERT INTO Topping (name) VALUES ("ParmesanTopping");INSERT INTO NamedPizza_hasTopping VALUES ("6", "16");INSERT INTO NamedPizza_hasBase VALUES ("7", "1");INSERT INTO NamedPizza_hasTopping VALUES ("7", "2");INSERT INTO NamedPizza_hasTopping VALUES ("7", "3");INSERT INTO NamedPizza_hasTopping VALUES ("7", "6");INSERT INTO NamedPizza_hasTopping VALUES ("7", "11");INSERT INTO Topping (name) VALUES ("PineKernels");INSERT INTO NamedPizza_hasTopping VALUES ("7", "17");INSERT INTO Topping (name) VALUES ("SultanaTopping");INSERT INTO NamedPizza_hasTopping VALUES ("7", "18");INSERT INTO NamedPizza_hasTopping VALUES ("7", "5");INSERT INTO NamedPizza_hasBase VALUES ("8", "1");INSERT INTO NamedPizza_hasTopping VALUES ("8", "3");INSERT INTO NamedPizza_hasTopping VALUES ("8", "6");INSERT INTO NamedPizza_hasTopping VALUES ("8", "7");INSERT INTO Topping (name) VALUES ("JalapenoPepperTopping");INSERT INTO NamedPizza_hasTopping VALUES ("8", "19");INSERT INTO Topping (name) VALUES ("HotGreenPepperTopping");INSERT INTO NamedPizza_hasTopping VALUES ("8", "20");INSERT INTO NamedPizza_hasBase VALUES ("9", "1");INSERT INTO NamedPizza_hasTopping VALUES ("9", "3");INSERT INTO Topping (name) VALUES ("FourCheesesTopping");INSERT INTO NamedPizza_hasTopping VALUES ("9", "21");INSERT INTO NamedPizza_hasBase VALUES ("10", "1");INSERT INTO NamedPizza_hasTopping VALUES ("10", "6");INSERT INTO NamedPizza_hasTopping VALUES ("10", "7");INSERT INTO NamedPizza_hasTopping VALUES ("10", "3");INSERT INTO NamedPizza_hasBase VALUES ("11", "1");INSERT INTO NamedPizza_hasTopping VALUES ("11", "5");INSERT INTO NamedPizza_hasTopping VALUES ("11", "6");INSERT INTO NamedPizza_hasTopping VALUES ("11", "14");INSERT INTO NamedPizza_hasTopping VALUES ("11", "10");INSERT INTO NamedPizza_hasTopping VALUES ("11", "2");INSERT INTO NamedPizza_hasTopping VALUES ("11", "4");INSERT INTO NamedPizza_hasTopping VALUES ("11", "3");INSERT INTO NamedPizza_hasBase VALUES ("12", "1");INSERT INTO Topping (name) VALUES ("SlicedTomatoTopping");INSERT INTO NamedPizza_hasTopping VALUES ("12", "22");INSERT INTO NamedPizza_hasTopping VALUES ("12", "6");INSERT INTO NamedPizza_hasTopping VALUES ("12", "5");INSERT INTO NamedPizza_hasTopping VALUES ("12", "1");INSERT INTO NamedPizza_hasTopping VALUES ("12", "10");INSERT INTO Topping (name) VALUES ("PetitPoisTopping");INSERT INTO NamedPizza_hasTopping VALUES ("12", "23");INSERT INTO NamedPizza_hasTopping VALUES ("12", "3");INSERT INTO Topping (name) VALUES ("LeekTopping");INSERT INTO NamedPizza_hasTopping VALUES ("12", "24");INSERT INTO NamedPizza_hasBase VALUES ("13", "1");INSERT INTO NamedPizza_hasTopping VALUES ("13", "3");INSERT INTO NamedPizza_hasTopping VALUES ("13", "4");INSERT INTO Topping (name) VALUES ("ArtichokeTopping");INSERT INTO NamedPizza_hasTopping VALUES ("13", "25");INSERT INTO NamedPizza_hasTopping VALUES ("13", "14");INSERT INTO NamedPizza_hasTopping VALUES ("13", "5");INSERT INTO Topping (name) VALUES ("GarlicTopping");INSERT INTO NamedPizza_hasTopping VALUES ("13", "26");INSERT INTO NamedPizza_hasTopping VALUES ("13", "6");INSERT INTO NamedPizza_hasBase VALUES ("14", "1");INSERT INTO NamedPizza_hasTopping VALUES ("14", "16");INSERT INTO NamedPizza_hasTopping VALUES ("14", "26");INSERT INTO NamedPizza_hasTopping VALUES ("14", "5");INSERT INTO NamedPizza_hasTopping VALUES ("14", "6");INSERT INTO Topping (name) VALUES ("RocketTopping");INSERT INTO NamedPizza_hasTopping VALUES ("14", "27");INSERT INTO NamedPizza_hasTopping VALUES ("14", "3");INSERT INTO NamedPizza_hasBase VALUES ("15", "1");INSERT INTO NamedPizza_hasTopping VALUES ("15", "16");INSERT INTO NamedPizza_hasTopping VALUES ("15", "3");INSERT INTO NamedPizza_hasTopping VALUES ("15", "24");INSERT INTO NamedPizza_hasTopping VALUES ("15", "6");INSERT INTO Topping (name) VALUES ("RosemaryTopping");INSERT INTO NamedPizza_hasTopping VALUES ("15", "28");INSERT INTO NamedPizza_hasBase VALUES ("16", "1");INSERT INTO NamedPizza_hasTopping VALUES ("16", "6");INSERT INTO NamedPizza_hasTopping VALUES ("16", "11");INSERT INTO Topping (name) VALUES ("GreenPepperTopping");INSERT INTO NamedPizza_hasTopping VALUES ("16", "29");INSERT INTO NamedPizza_hasTopping VALUES ("16", "3");INSERT INTO Topping (name) VALUES ("HotSpicedBeefTopping");INSERT INTO NamedPizza_hasTopping VALUES ("16", "30");INSERT INTO NamedPizza_hasBase VALUES ("17", "1");INSERT INTO NamedPizza_hasTopping VALUES ("17", "3");INSERT INTO NamedPizza_hasTopping VALUES ("17", "6");INSERT INTO Topping (name) VALUES ("GorgonzolaTopping");INSERT INTO NamedPizza_hasTopping VALUES ("17", "31");INSERT INTO NamedPizza_hasBase VALUES ("18", "1");INSERT INTO NamedPizza_hasTopping VALUES ("18", "5");INSERT INTO NamedPizza_hasTopping VALUES ("18", "26");INSERT INTO NamedPizza_hasTopping VALUES ("18", "6");INSERT INTO NamedPizza_hasTopping VALUES ("18", "16");INSERT INTO Topping (name) VALUES ("SpinachTopping");INSERT INTO NamedPizza_hasTopping VALUES ("18", "32");INSERT INTO NamedPizza_hasTopping VALUES ("18", "3");INSERT INTO NamedPizza_hasBase VALUES ("19", "1");INSERT INTO NamedPizza_hasTopping VALUES ("19", "1");INSERT INTO NamedPizza_hasTopping VALUES ("19", "3");INSERT INTO NamedPizza_hasTopping VALUES ("19", "6");INSERT INTO NamedPizza_hasBase VALUES ("20", "1");INSERT INTO Topping (name) VALUES ("SweetPepperTopping");INSERT INTO NamedPizza_hasTopping VALUES ("20", "33");INSERT INTO Topping (name) VALUES ("CajunSpiceTopping");INSERT INTO NamedPizza_hasTopping VALUES ("20", "34");INSERT INTO Topping (name) VALUES ("RedOnionTopping");INSERT INTO NamedPizza_hasTopping VALUES ("20", "35");INSERT INTO NamedPizza_hasTopping VALUES ("20", "6");INSERT INTO NamedPizza_hasTopping VALUES ("20", "3");INSERT INTO Topping (name) VALUES ("ChickenTopping");INSERT INTO NamedPizza_hasTopping VALUES ("20", "36");INSERT INTO NamedPizza_hasTopping VALUES ("20", "26");INSERT INTO NamedPizza_hasBase VALUES ("21", "1");INSERT INTO NamedPizza_hasTopping VALUES ("21", "4");INSERT INTO NamedPizza_hasTopping VALUES ("21", "5");INSERT INTO NamedPizza_hasTopping VALUES ("21", "6");INSERT INTO NamedPizza_hasTopping VALUES ("21", "3");INSERT INTO NamedPizza_hasTopping VALUES ("21", "2");INSERT INTO NamedPizza_hasBase VALUES ("22", "1");INSERT INTO Topping (name) VALUES ("MixedSeafoodTopping");INSERT INTO NamedPizza_hasTopping VALUES ("22", "37");INSERT INTO NamedPizza_hasTopping VALUES ("22", "26");INSERT INTO NamedPizza_hasTopping VALUES ("22", "3");