## About me
- Naam: T'nayro Herdigein
- Leeftijd: 26 jaar
- Beroep: Student
- Studie: HBO ICT, Network and Systems Engineering
- Studentnummer: 18140572
- Minor: Applied Data Science

## Table of Contents  
- [DataCamp Course Certificates](#datacamp-course-certificates)
- [Research Project](#research-project)
  - [Task Definition](#task-definition)
  - [Evaluation](#evaluation)
  - [Planning](#planning)
- [Domain Knowledge](#domain-knowledge)
  - [Introduction of the subject field](#introduction-of-the-subject-field)
  - [Literature Research](#literature-research)
  - [Explanation of Terminology, jargon and definitions](#explanation-of-terminology-jargon-and-definitions)   
- [Predictive Analysis](#predictive-analysis)
  - [Selecting a Model](#selecting-a-model)
  - [Configuring a Model](#configuring-a-model)
- [Data Preprocessing](#data-preprocessing)
  - [Data Preparation](#data-preparation)
- [Communication](#communication)
  - [Presentations](#presentations)
  - [Writing Paper](#writing-paper)


## DataCamp Course Certificates
Voor de start van de minor Applied Data Science, was Python nog heel onbekend voor mij. Door de nodige python kennis te kunnen ontwikkelen kreeg ik verplichte cursussen om te volgen, die ook hebben meegeholpen aan het uiteindelijke resultaat voor de minor. Deze cursussen waren te volgen op [DataCamp](https://app.datacamp.com/learn) en hiervoor kreeg ik voor elke behaalde cursus een [certificaat](/DataCamp) 

## Research Project

#### Task Definition
De aanleiding van het project was dat wij door middel van een softwareoplosiing, het Container Loading Proces veel efficiënter en optimaal laten verlopen. Dit is belangrijk om de kosten te minimaliseren en ook om meer tijd te winnen. 
Voordat wij van start zijn gegaan met het kiezen van een model, hebben wij eerst samen de hoofdvragen en deelvragen geformuleerd. Dit heeft het makkelijker gemaakt voor ons om aan de slag te gaan.

#### Hoofdvraag
- *Hoe kan ervoor gezorgd worden dat containers op de kade op een efficiënte manier opgestapeld kunnen worden, zodat de afnemer van de containers hier makkelijk bij kan?*

De [hoofdvraag](#hoofdvraag) wordt in het kopje [Domain Knowledge](#domain-knowledge) beschreven en beantwoordt.

#### Deelvragen
- *Hoe ziet de layout van de desbetreffende kade eruit?*
Voor het trainen van een model, hebben wij eerst ervoor gekozen om een 3x3 (row x bay) kade te gebruiken. In totaal kunnen er 9 containers geplaats worden. Door het uitbreiden en verder optimaliseren van het proces, konden wij ook in de hoogte containers stapelen (row x bay x tier). Om het realistisch te houden, hebben wij de max-hoogte gelegd op 3 containers (3x3x3). 

- *Welke modellen/methodes zijn relevant om dit optimalisatieprobleem aan te pakken?*
Uit ons onderzoek en gesprekken met docenten is gebleken dat de beste oplossing voor dit probleem is, het gebruikmaken van Reinforcement Learning (RL). RL is een heel uitgebreid onderwerp en heeft een aantal modellen die gebruikt kunnen worden. Om de beste model te kunnen kiezen, moesten wij eerst alle modellen uitproberen en testen. Hieruit zijn wij met 2 modellen gekomen nl. PPO (Proximal Policy Optimization) en A2C (Advantage Actor Critic). Uiteindelijk hebben wij toch ervoor gekozen om met PPO verder te gaan en dat wordt in het kopje [Domain Knowledge](#domain-knowledge) verder uitgelegd.

#### Evaluation
Gedurende de samenwerken met het groepje, heb ik enkele dingen opgemerkt. Deze opmerking heb ik in een [Retrospective](/src/Trello/Retrospective.png) gezet, gecategoriseerd als 'Start', 'Stop' en 'Doorgaan'.

Toelichting:  
**Start**: Het is weleens voorgekomen dat we fysiek wilden afspreken op school, maar niet iedereen aanwezig kon zijn. Hierdoor doen we het of zonder de persoon of helemaal niet meer. Dit had makkelijk opgelost kunnen worden om gewoon via Teams af te spreken en de belangrijke punten door te nemen online en dan kan de rest wel fysiek ontmoeten. Bij elkaar komen heeft wel z'n voordelen en één daarvan is dat we met meer ideeën komen en we makkelijker op in kunnen gaan. Zo leren we elkaar beter kennen en ook de zwakke en sterke punten van elk groepslid. 

**Stoppen**: Laat komen en niet komen opdagen zijn normaal in elke groep. Ik heb ook een paar keren verzuimd of weleens laat aangekomen, maar belangrijk is dat er aan deze eigenschappen wordt gewerkt zodat er in de toekomst een betere band is tussen elkaar. Het laat komen en verzuimen kan maken dat een ander student je gaat vooroordelen alvorens je wat aan het project hebt gedaan. Dit wil je voorkomen omdat dit ook veel invloed op je eindresultaat zal hebben. 

**Doorgaan**: Zoals in elke groep zijn er altijd studenten die echt goed zijn in een specifieke taak. Zo ook in ons groepje was er altijd iemand die goed in Scrum was en ook iedereen een taakje kon toewijzen. Deze persoon nam de leiding meestal en deed goed zijn best. Ook zijn er anderen die meer over programmeren weten dan de rest en kunnen makkelijk code schrijven. Deze persoon twijfelde nooit eraan om degene die niet zo goed zijn in het programmeren, te helpen en uit te leggen wat hij gedaan heeft. Dit zijn enkele punten van de groep die ik extra goed vond omdat ik zo ook beter mijn taken kon doen en niet het gevoel krijgen dat ik door de rest van de groep wordt uitgesloten.

#### Planning
Als groep hadden wij besloten om niet verder te gaan met het FoodBoost project en een nieuwe uitdaging aan te gaan. 
Onze planning voor de Container research project zag er als volg uit:

**Sprint 1 (10 oct - 23 oct 2022):** 
In de eerste sprint heb ik kennisgemaakt met de opdrachtomschrijving. Het was een nieuw project dus dit eiste opnieuw veel onderzoek. Daarna heb ik naar de dataset gekeken zodat ik ongeveer een beeld had waarmee we te maken hadden. Samen met de groep hebben wij de hoofdvraag en deelvragen geformuleerd. Dit moest ook goedgekeurd worden door de projectbegeleiders. Ik heb gelijk heel wat literatuuronderzoek gedaan zonder dat we echt wisten wat we wilden doen. Ik zocht namelijk naar soortgelijke projecten die al door anderen zijn opgelost.

**Sprint 2 (31 oct - 13 nov 2022):**
Tijdens sprint 2 heb ik gericht literatuuronderzoek gedaan toen wij al wisten hoe wij Reinforcement Learningen wilden toepassen om dit probleem op te oplossen zie [afbeelding](/src/Trello/Literatuuronderzoek%20RL%20uitvoeren.png). De datapreprocessen/cleaning werd door 1 persoon gedaan omdat hij iets verder wist wat hij met de data wilde doen. Ik heb wel naar de code gekeken en geprobeerd te begrijpen. De DataCamp courses hebben hierbij heel veel geholpen. 

**Sprint 3 (14 nov - 27 nov 2022):**
Tijdens sprint 3 zagen we dat we een achterstand hadden op de andere groepen. We besloten om dus een ieder voor zich met een oplossing te komen. Een ieder moest een RL toepassen op een simpele trainingsset zie [afbeelding](/src/Trello/Alternatieve%20implementatie%20coderen%20van%20RL.png). Mijn deel wordt verder in [Predictive Analysis](#predictive-analysis) besproken. 

**Sprint 4 (28 nov - 11 dec 2022):**
Tijdens sprint 4 hebben we samen als groep besloten wie wat zou doen in de Research paper. Ik heb het hoofdstuk 'Methodologie' op mezelf genomen. zie [afbeedling](/src/Trello/Opstellen%20van%20het%20hoofdstuk%20'Methodologie'%20in%20het%20Research%20Paper.png)

**Sprint 5 (12 dec - 25 dec 2022):**
Tijdens sprint 5 heb ik grotendeels aan de Research paper gewerkt. Literatuur verzamelt en in het document gegooid. Ook heb ik een start gemaakt aan de opmaak van mijn portfolio.

**Sprint 6 (09 jan - 22 jan 2023):**
Tijdens sprint 6 ben ik verder gegaan aan de Research paper en mijn portfolio. 

**Sprint 7 (23 jan - 05 feb 2023):**
Tijdens sprint 7 hebben we zowel de paper als portfolio al afgerond en ingeleverd. De RL code wordt nog verfijnd voor betere resultaten. 

## Domain Knowledge
#### Introduction of the subject field
In dit hoofdstuk wordt kort uitgeled wat de probleemstelling en doelstelling zijn. 
Dit project is de taak van [Cofano](https://www.cofano.nl/nl/) en gaat voornamelijk over het optimalisatieproces van het in- en uitladen van containers op een kade. Momenteel wordt dit proces nog handmatig door een persoon bepaald en uitgevoerd en dit leidt tot heel veel inefficiënt geplaatste containers. Dit heeft als gevolg dat zowel het inladen als het uitladen meer tijd kost. Het is aan ons toegewezen om hiervoor een oplossing voor te bedenken door gebruik te maken van Machine Learning. Wij willen namelijk de tijd, waarbij het proces wordt uitgevoerd, verkorten. 

Om dit ook makkelijker te maken, hebben we besloten om alle containers dezelfde dimensies te geven.\
Als eerst moeten we kijken naar de kade. Zoals in [deelvraag 1](#deelvragen) besproken, hebben wij eerst gekozen om een 3x3 kade te gebruiken. Rekeninghoudend met de Reach-stacker, die de containers verplaatst, heeft dit vele beperkingen. De Reach-stacker kan alleen via de bay kant een container pakken en plaatsen. Dit heeft heel veel invloed op de manier hoe wij een model zullen trainen namelijk op de 'reward-systeem' (wordt nog uitgelegd). 

Ook moeten wij rekening houden met de verschillende containers met verschillende (eind)bestemmingen. Wij willen het makkelijker maken voor de Reach-stacker om alles in één keer te kunnen pakken, zonder eerst andere containers te verplaatsen. Dit hebben we kunnen realiseren door eerst dezelfde containers op een row of bay te sorteren alvorens een andere container te plaatsen. Ook rekeninghoudend met de volgorde waarop de containers geplaatst worden, worden de laatste containers onderaan geplaatst. Hierbij wordt naar de schema van inkomende en uitgaande schepen gekeken. 

#### Literature research
Dit hoofdstuk gaat over de literatuuronderzoek die hebben geleidt tot het kiezen van een model voor het trainen.\
Het doel is om de beste manier te vinden om containers, met verschillende bestemmingen, op te stapelen op de kade zodat het proces vlotter en sneller verloopt. Tijdens een gesprek met onze projectbegeleider hebben wij enkele opties gekregen hoe wij dit konden realiseren. Één van die opties was het gebruikmaken van Reinforcement Learning.    

1. Als eerste bron van onderzoek heb ik eerst gekeken naar wat al beschikbaar is in DataCamp. Hier vond ik een [Introduction to Reinforcement Learning](https://www.datacamp.com/tutorial/introduction-reinforcement-learning) tutorial. Hieruit heb ik kunnen leren wat de basis principes van RL zijn en alle terminologie eromheen. De belangrijkste onderdelen die ik hieruit heb gehaald waren, dat ik een Environment en Agent nodig heb. De Environment voor het project is de kade waar de containers geplaatst worden en de Agent is het model die getraind wordt, die uiteindelijk met een optimalisatieproces komt.
2. Nadat de basis van RL bekend was, heb ik verschillende opties bekeken zoals [Reinforcement Q-learning from Scratch in Python with OpenAI Gym](https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/). Alhoewel Q-learning een heel ander concept is dan wat wij wilden toepassen, heb ik uit dit onderzoek veel geleerd over States, Actions, Rewards, Penalties en Policies. Rewards en Penalties beinvloeden de manier waarop een model keuzes maakt. Ook kunnen de Policies aangepast worden naar de specificaties van de trainer. 
3. Deze bron [A Reinforcement Learning Framework for Container Selection and Ship Load Sequencing in ports](https://www.ifaamas.org/Proceedings/aamas2019/pdfs/p2250.pdf) gaat namelijk over hetzelfde probleem, maar anders aangepakt. Hier wordt meer gebruik gemaakt van Linear programmeren. Dit wilden wij niet toepassen omdat het onderwerp Linear programmeren voor vele van ons nog heel onduidelijk is en het zou ook overbodig zijn geweest. Maar het is wel handig om soortgelijke oplossingen in acht te nemen.
4. [ML| Reinforcement Learning Algorithm: Python Implementation using Q-learning](https://www.geeksforgeeks.org/ml-reinforcement-learning-algorithm-python-implementation-using-q-learning/?ref=rp). Hier heb ik voor het eerst een implementatie van RL met Q-learning kunnen toepassen. Dit was meer voor het experimenteren met de code, maar het had niets te maken met het project. Hieruit kreeg ik meer inspiratie voor het schrijven van de code voor een Environment.
5. [Hands-on Intro to Reinforcement Learning in Python](https://towardsdatascience.com/hands-on-introduction-to-reinforcement-learning-in-python-da07f7aaca88): Als laatst heb ik deze bron gevonden, waar een model from scratch is geschreven. Ik heb heel veel aan deze code aangepast om te voldoen aan de eisen van het project. De rewards en penalties heb ik aangepast. Ik moest ook heel veel over Object Oriented Programming leren. Dit maakte de code makkelijker leesbaar en schaalbaar. Ik heb m'n best gedaan dit voor elkaar te krijgen. De code wordt verder in [Predictive Analysis](#predictive-analysis) besproken.


#### Reinforcement Learning

RL kan op verschillende manieren benadert worden. Bij RL hebben wij eerst een Environment nodig. In ons geval is het een 3x3 kade die gevuld moet worden met verschillende containers. Om de optimale oplossing te krijgen, maken wij gebruik van een reward-systeem. Dit houdt in dat de Agent bij elke plaatsing van een container, een positieve of negatieve reward kan krijgen. Dit is noodzakelijk voor het trainen van het model. Uit de rewards kan het model leren welke moves beter zijn. Elke move krijgt een reward, geeft een state terug en bepaald zijn volgende actie. 

Onze reward-systeem bestaat uit enkele regels namelijk:
- Containers mogen niet op de eerste bay geplaatst worden waardoor de Reach-stacker belemmerd wordt.
- Container A moet zoveel mogelijk naast container A geplaats worden en dus geen plek ertussen openlaten.
- Container C mag niet tussen containers A en A geplaatst worden.
- Containers die eerder weggaan, mogen niet onderaan/achter geplaatst worden.

#### Explanation of Terminology, jargon and definitions
De belangrijkste terminolgies die in dit project voorkomen zijn:\
**- Reinforcement Learning**: is één van de onderdelen van Machine Learning en gaat meer over hoe een Agent leert beslissingen te nemen in een environment om zo een hoog mogelijke reward te behalen. Elke stap resulteert in een positieve of negatieve reward. Aan de hand hiervan kan de Agent betere beslissingen maken met tijd. Een soort trial-and-error. Het uiteindelijke doel hiervan is dat de agent de totale beloning op lange termijn probeert te maximaliseren.  
**- Environment**: De environment is de omgeving waar de Agent zijn interacties meeheeft, inclusief de staat waarin het systeem zich bevindt. De environment bevat onder andere ook het algoritme voor de rewards en penalties.  
**- Agent**: De Agent is het model dat beslissingen neemt en acties uitvoert aan de hand van een set van acties.  
**- Rewards en Penalties**:Het doel van de Agent is om beloningen te maximaliseren. Net zoals bij elk ML-algoritme, zullen de beloningen eerst bij 0 beginnen en veranderen volgens een bepaald algoritme. De Agent zal proberen de kosten van elke van zijn actiekeuzes te schatten, daarna zal de agent een actie ondernemen, vervolgens zal hij de echte beloning van die actie ontvangen vanuit de omgeving en uiteindelijk zijn toekomstige voorspellingen voor die specifieke actie aanpassen.\
**- Policies**: Hoe de logica en parameters gestructureerd worden.\
**- Actions**: De agent komt op één van de totaal mogelijke states tegen en verricht een actie. In ons geval kan de actie een bepaalde richting zijn zoals omhoog, omlaag, links en rechts.  


## Predictive Analysis
In deze paragraaf laat ik zien wat ik heb bijgedragen aan het opleveren van de [finalcode](/src/code/Container_Environment-almost-final.ipynb).  
Als groep hadden we eerst besloten dat een ieder een model zou proberen te trainen zodat een ieder ook weet hoe RL werkt. Ik heb een soort werkend model dat ongeveer lijkt op de environment van het project. Dit was meer voor het begrijpen hoe RL werkt. Alhoewel het niet heeft bijgedragen aan [finalcode](/src/code/Container_Environment-almost-final.ipynb), heeft het wel geholpen aan het beter begrijpen wat wij willen realiseren aan het project.  

Voor de Container project heb ik een aantal pogingen gemaakt om mijn eigen Environment en Agent te coderen.  
- [Versie 1](/src/code/Container-Environment-v1.0.ipynb) -> Een poging gemaakt om de code van mij medestudent werkend te krijgen. Hij had een Environment gemaakt en ik de Agent.

- [Versie 2](/src/code/Container-Environment-v3.0.ipynb) -> Dit is de aangepaste versie van de code die ik heb gevonden tijdens mijn literatuuronderzoek.

- [Versie 3](/src/code/Container-Environment-v2.0.ipynb) -> Dit is een verkorte versie van versie 2. Hier heb ik me meer verdiept in het OOP gedeelte en probeerde het op deze manier werkend te krijgen.

- [Versie 4](/src/code/v1.0.py) -> Dit is de laatste versie waaraan ik heb gewerkt om een model werkend te krijgen. Er is niet veel van terecht gekomen. 

Helaas hebben geen van deze versies een resultaat of een goede resultaten opgeleverd. Ik heb hieruit wel meer over OOP geleerd en kan het beter begrijpen dan voorheen.


#### Selecting a Model
Voor het trainen heb ik niet specifiek een model gekozen, maar meer de [code](/src/code/RL-test2.py) aangepast naar mijn wensen. De code had al een [Environment (Class Area)](/src/code/RL-test2.py#L35-L48) en een [Agent (Class Container)](/src/code/RL-test2.py#L52-L116) die ik heb aangepast.

#### Configuring a Model
De [Environment (Class Area)](/src/code/RL-test2.py#L35-L48) definieert een array van 3x3 gevuld met nullen. Nul stelt voor dat er op die plek nog niets staat en dus wordt het aangegeven met een ' '. Elke plek dat een container bevat wordt met een 'X' aangegeven en wordt dus een 1.

De [Agent (Class Container)](/src/code/RL-test2.py#L52-L116) kiest als eerst een random containertype en zet het neer op de kade. Het geeft de coördinaten terug en kijkt daarna wat de volgende actie is. Er wordt eerst eromheen gekeken naar [de legale moves](/src/code/RL-test2.py#L97-L110) en [de mogelijke moves](/src/code/RL-test2.py#L62-L70) en roept dan de [move functie](/src/code/RL-test2.py#L72-L84) aan om de move te maken. Elke move legaal of illegaal wordt opgeslagen in de [q-table](/src/code/RL-test2.py#L117-L128).

## Data Preprocessing
In dit hoofdstuk laat ik zien wat ik allemaal aan data preprocessing heb gedaan voor 2 projecten. De dataset heb ik van [Kaggle](https://www.kaggle.com/code/devananjelito/ml-temperature-prediction/data). Het gaat namelijk om het voorspellen van de gemiddelde temperaturen over de gehele wereld. En omdat ik uit Suriname kom wilde ik de gemiddelde temperaturen van een specifieke periode (mijn geboorte jaar 1997) middels plots laten zien. Helaas heb ik geen model kunnen trainen met deze data omdat ik tenminste 2 kolommen aan data nodig had hiervoor en dat had ik niet. Het project dat ging over het voorspellen van de gemiddelde temperaturen over de gehele wereld leg ik hieronder verder uit. Dat ander project is [hier](/src/code/temp-in-suriname.ipynb) te vinden. 

#### Data exploration
Voordat ik van start ging met het cleanen van de data, wilde ik eerst weten met wat voor data ik te maken heb. Door de .head(), .info(), .columns, .isnull() en .sum() functies aan te roepen op de dataset, kan ik in één keer zien wat ik allemaal heb. Ik zag dat ik kolommen heb die ik niet ga gebruiken, dus die kunnen alvast weg. Ook de sum van alle NaN waardes krijg ik te zien. 

#### Data cleansing
Voor het cleanen van de data heb ik het volgende gedaan:
Eerst een functie gemaakt die de ongebruikte kolommen dropped, de kolommen met 'Uncertainty' erachter (wat eigenlijk overbodig is. Dit kon ook gewoon in één regel). Daarna heb ik de 'dt' kolom omgezet naar een 'datetime' object en de naam verandert naar 'Year'. Vervolgens heb ik de 'Year' kolom als index gezet voor de dataset en de NaN waardes gedropped. Ook heb ik alle data vanaf 1915 geselecteerd. Dit was al meer dan genoeg data om te trainen en ook al genoeg cleaning gedaan.  

#### Data preparation
Nu daar de data clean is, ben ik begonnen met het setten van de ['target vector' en 'feature matrix']() voor het opsplitsen van de data naar [train en test]() data. De [MAE (mean_absolute_error)]() is berekent om een baseline waarde te krijgen.
Voor dit project heb ik 2 modellen gekozen waarvan ik dacht dat het best geschikt waren voor het voorspellen van de gemiddelde temperaturen.
De modellen die ik gekozen heb zijn de Linear Regression en de Random Forest Regression modellen. 

De [Linear Regression model]() heb ik als volg getraind. 

De [Random Forest Regression model]() heb ik als volg getraind.

#### Data explanation
De dataset bevat het gemiddelde, de min en max temperatuur dat op land is gemeten vanaf het jaar 1750. Ook is het gemiddelde temperatuur van land en oceaan gemeten. Voor dit project had ik niet alle data nodig, dus heb ik besloten om de data vanaf het jaar 1915 te gebruiken.






#### Data visualization (exploratory)
Helaas liep ik een aantal bugs tegen tijdens het plotten. Ik kreeg de 'ValueError: Expected 2D array, got 1D array instead' error en de plots zagen er niet uit als hoe met moest. 

## Communication 

#### Presentations
Ik heb me voorbereid op 2 interne en 1 externe presentaties. Voor de tweede interne presentatie had ik me niet op voorbereid. Ik moest namelijk invallen voor een medestudent die laatste moment had afgezegd. Uit ervaring kan ik zeggen dat ik minder zenuwachtig en beter presenteer wanneer ik niet erop voorbereid ben. Voor de externe presentatie had ik me echt op voorbereid en toen ik aan de beurt was, leek het alsof ik alles was vergeten en moest ik grotendeels oplezen wat ik had geschreven. Maar over het algemeen vind ik dat ik m'n best heb gedaan en dat ik ook goed de vragen van het publiek kon beantwoorden. In dit [mapje](/src/presentaties) zijn alle presentaties te vinden.

#### Writing paper
Behalve dat ik veel literatuuronderzoek heb gedaan voor de paper, heb ik ook het hoofdstuk methodologie geschreven. In dit hoofdstuk leg ik uit welke methoden en technieken we hebben toegepast voor het behalen van de eindresultaten. Hier laat ik zien, wat de verschillen tussen de 2 modellen zijn door middel van verwijzingen naar het literatuur en ook 2 afbeeldingen met de resultaten. Ook leg ik hier uit hoe de reward en penalty functies zijn ingericht in onze environment. Dit is de laatste versie van de [Research Paper](/src/docs/Research%20Paper%20Container%20Project.docx).
