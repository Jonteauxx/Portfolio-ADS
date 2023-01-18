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
  - [Conclusions](#conclusions)
  - [Planning](#planning)
- [Domain Knowledge](#domain-knowledge)
  - [Introduction of the subject field](#introduction-of-the-subject-field)
  - [Literature Research](#literature-research)
  - [Explanation of Terminology, jargon and definitions](#explanation-of-terminology-jargon-and-definitions)   
- [Predictive Analysis](#predictive-analysis)
  - [Selecting a Model](#selecting-a-model)
  - [Configuring a Model](#configuring-a-model)
  - [Training a Model](#training-a-model)
  - [Evaluating a Model](#evaluating-a-model)
  - [Visualizing the outcome of a model](#visualizing-the-outcome-of-a-model)
- [Communication](#communication)
  - [Presentations](#presentations)
  - [Writing Paper](#writing-paper)


## DataCamp Course Certificates
Voor de start van de minor Applied Data Science, was Python nog heel onbekend voor mij. Door de nodige python kennis te kunnen ontwikkellen kreeg ik verplichte cursussen om te volgen, die ook hebben meegeholpen aan het uiteindelijke resultaat voor de minor. Deze cursussen waren te volgen op DataCamp en hiervoor kreeg ik voor elke behaalde cursus een [certificaat](/DataCamp) 

## Research Project

#### Task Definition
Voordat wij van start zijn gegaan met het kiezen van een model, hebben wij eerst samen de hoofdvragen en deelvragen geformuleerd. Dit heeft het makkelijker gemaakt voor ons om aan de slag te gaan.

#### Hoofdvraag
- *Hoe kan ervoor gezorgd worden dat containers op de kade op een efficiënte manier opgestapeld kunnen worden, zodat de afnemer van de containers hier makkelijk bij kan?*

De [hoofdvraag](#hoofdvraag) wordt in het kopje [Domain Knowledge](#domain-knowledge) beschreven en beantwoordt.\

#### Deelvragen
- *Hoe ziet de layout van de desbetreffende kade eruit?*
Voor het trainen van een model, hebben wij eerst ervoor gekozen om een 3x3 (row x bay) kade te gebruiken. In totaal kunnen er 9 containers geplaats worden. Door het uitbreiden en verder optimaliseren van het proces, konden wij ook in de hoogte containers stapelen (row x bay x tier). Om het realistisch te houden, hebben wij de max-hoogte gelegd op 3 containers (3x3x3). 

- *Welke modellen/methodes zijn relevant om dit optimalisatieprobleem aan te pakken?*
Uit ons onderzoek en gesprekken met docenten is gebleken dat de beste oplossing voor dit probleem is, het gebruikmaken van Reinforcement Learning (RL). RL is een heel uitgebreid onderwerp en heeft een aantal modellen die gebruikt kunnen worden. Om de beste model te kunnen kiezen, moesten wij eerst alle modellen uitproberen en testen. Hieruit zijn wij met 2 modellen gekomen nl. PPO (Proximal Policy Optimization) en A2C (Advantage Actor Critic). Uiteindelijk hebben wij toch ervoor gekozen om met PPO verder te gaan en dat wordt in het kopje [Domain Knowledge](#domain-knowledge) verder uitgelegd.

#### Evaluation

#### Conclusions

#### Planning


## Domain Knowledge
#### Introduction of the subject field
In dit hoofdstuk wordt kort uitgeled wat de probleemstelling en doelstelling zijn. 
Dit project is de taak van [Cofano](https://www.cofano.nl/nl/) en gaat voornamelijk over het optimalisatieproces van het in- en uitladen van containers op een kade. Momenteel wordt dit proces nog handmatig door een persoon bepaald en uitgevoerd en dit leidt tot heel veel inefficiënt geplaatste containers. Dit heeft als gevolg dat zowel het inladen als het uitladen meer tijd kost. Het is aan ons toegewezen om hiervoor een oplossing voor te bedenken door gebruik te maken van Machine Learning. Wij willen namelijk de tijd, waarbij het proces wordt uitgevoerd, verkorten. 

Om dit ook makkelijker te maken, hebben we besloten om alle containers dezelfde dimensies te geven.\
Als eerst moeten we kijken naar de kade. Zoals in [deelvraag 1](#deelvragen) besproken, hebben wij eerst gekozen om een 3x3 kade te gebruiken. Rekeninghoudend met de Reach-stacker, die de containers verplaatst, heeft dit vele beperkingen. De Reach-stacker kan alleen via de bay kant een container pakken en plaatsen. Dit heeft heel veel invloed op de manier hoe wij een model zullen trainen namelijk op de 'reward-systeem' (wordt nog uitgelegd). 

Ook moeten wij rekening houden met de verschillende containers met verschillende (eind)bestemmingen. Wij willen het makkelijker maken voor de Reach-stacker om alles in één keer te kunnen pakken, zonder eerst andere containers te verplaatsen. Dit hebben we kunnen realiseren door eerst dezelfde containers op een row of bay te sorteren alvorens een andere container te plaatsen. Ook rekeninghoudend met de volgorde waarop de containers geplaatst worden, worden de laatste containers onderaan geplaatst. Hierbij wordt naar de schema van inkomende en uitgaande schepen gekeken. 

#### Reinforcement Learning en PPO

RL kan op verschillende manieren benadert worden. Bij RL hebben wij eerst een [Environment]() nodig. In ons geval is het een 3x3 kade die gevuld moet worden met verschillende containers. Om de optimale oplossing te krijgen, maken wij gebruik van een reward-systeem. Dit houdt in dat de [Agent]() bij elke plaatsing van een container, een positieve of negatieve reward kan krijgen. Dit is noodzakelijk voor het trainen van het model. Uit de rewards kan het model leren welke moves beter zijn. Elke move krijgt een reward, geeft een state terug en bepaald zijn volgende actie. 
PPO is nieuw model van [OpenAI](https://openai.com/blog/openai-baselines-ppo/) en dat is Proximal Policy Optimization.

Onze reward-systeem bestaat uit enkele regels namelijk:
- Containers mogen niet op de eerste bay geplaatst worden waardoor de Reach-stacker belemmerd wordt.
- Container A moet zoveel mogelijk naast container A geplaats worden en dus geen plek ertussen openlaten.
- Container C mag niet tussen containers A en A geplaatst worden.
(nog enkele regels hier plaatsen)

#### Literature research
Dit hoofdstuk gaat over de literatuuronderzoek die hebben geleidt tot het kiezen van een model voor het trainen.\
Het doel is om de beste manier te vinden om containers, met verschillende bestemmingen, op te stapelen op de kade zodat het proces vlotter en sneller verloopt.  

1. Als eerste bron van onderzoek heb ik eerst gekeken naar wat al beschikbaar is in DataCamp. Hier vond ik een [Introduction to Reinforcement Learning](https://www.datacamp.com/tutorial/introduction-reinforcement-learning) tutorial. Hieruit heb ik kunnen leren wat de basis principe van RL is en alle terminologie eromheen. De belangrijkste onderdelen die ik hieruit heb gehaald waren, dat ik een Environment en Agent nodig heb. De Environment voor het project is de kade waar de containers geplaatst worden en de Agent is het model die getraind wordt, die uiteindelijk met een optimalisatieproces komt.
2. Nadat de basis van RL bekend was, heb ik verschillende opties bekeken zoals [Reinforcement Q-learning from Scratch in Python with OpenAI Gym](https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/). Alhoewel Q-learning een heel ander concept is dan wat wij wilden toepassen, heb ik uit dit onderzoek veel geleerd over States, Actions, Rewards, Penalties en Policies. Rewards en Penalties beinvloeden de manier waarop een model keuzes maakt. Ook kunnen de Policies aangepast worden naar de specificaties van de trainer. 
3. Deze bron [A Reinforcement Learning Framework for Container Selection and Ship Load Sequencing in ports](https://www.ifaamas.org/Proceedings/aamas2019/pdfs/p2250.pdf) gaat namelijk over hetzelfde probleem, maar anders aangepakt. Hier wordt meer gebruik gemaakt van Linear programmeren. Dit wilden wij niet toepassen omdat het onderwerp Linear programmeren voor vele van ons nog heel onduidelijk is en het zou ook overbodig zijn geweest. Maar het is wel handig om soortgelijke oplossingen in acht te nemen.
4. [ML| Reinforcement Learning Algorithm: Python Implementation using Q-learning](https://www.geeksforgeeks.org/ml-reinforcement-learning-algorithm-python-implementation-using-q-learning/?ref=rp). Hier heb ik voor het eerst een implementatie van RL met Q-learning kunnen toepassen. Dit was meer voor het experimenteren met de code, maar het had niets te maken met het project. Hieruit kreeg ik meer inspiratie voor het schrijven van de code voor een Environment.
5. [Hands-on Intro to Reinforcement Learning in Python](https://towardsdatascience.com/hands-on-introduction-to-reinforcement-learning-in-python-da07f7aaca88): Als laatst heb ik deze bron gevonden, waar een model from scratch is geschreven. Ik heb heel veel aan deze code aangepast om te voldoen aan de eisen van het project. De rewards en penalties heb ik aangepast. Ik moest ook heel veel over Object Oriented Programming leren. Dit maakte de code makkelijker leesbaar en schaalbaar. Ik heb m'n best gedaan dit voor elkaar te krijgen. De code wordt verder in [Predictive Analysis](#predictive-analysis) besproken.


#### Explanation of Terminology, jargon and definitions
De belangrijkste terminolgies die in dit project voorkomen zijn:\
**- Reinforcement Learning**: is één van de onderdelen van Machine Learning en gaat meer over hoe een Agent leert beslissingen te nemen in een environment om zo een hoog mogelijke reward te behalen. Elke stap resulteert in een positieve of negatieve reward. Aan de hand hiervan kan de Agent betere beslissingen maken met tijd. Een soort trial-and-error. Het uiteindelijke doel hiervan is dat de agent de totale beloning op lange termijn probeert te maximaliseren.  
**- Environment**: De environment is de omgeving waar de Agent zijn interacties meeheeft, inclusief de staat waarin het systeem zich bevindt. De environment bevat onder andere ook het algoritme voor de rewards en penalties.  
**- Agent**: De Agent is het model dat beslissingen neemt en acties uitvoert aan de hand van een set van acties.  
**- Rewards en Penalties**:Het doel van de Agent is om beloningen te maximaliseren. Net zoals bij elk ML-algoritme, zullen de beloningen eerst bij 0 beginnen en veranderen volgens een bepaald algoritme. De Agent zal proberen de kosten van elke van zijn actiekeuzes te schatten, daarna zal de agent een actie ondernemen, vervolgens zal de agent de echte beloning van die actie ontvangen vanuit de omgeving en uiteindelijk zijn toekomstige voorspellingen voor die specifieke actie aanpassen.\
**- Policies**: Hoe de logica en parameters gestructureerd worden\
**- Actions**: De agent komt op één van de totaal mogelijke states tegen en verricht een actie. In ons geval kan de actie een bepaalde richting zijn.

-----------------------------




## Predictive Analysis
In deze paragraaf laat ik zien wat ik heb bijgedragen aan het opleveren van de [finalcode]().  
Als groep hadden we eerst besloten dat een ieder een model zou proberen te trainen zodat een ieder ook weet hoe RL werkt. Ik heb een soort werkend model dat ongeveer lijkt op de environment van het project. Dit was meer voor het begrijpen hoe RL werkt. Alhoewel het niet heeft bijgedragen aan [finalcode](), heeft het wel geholpen aan het beter begrijpen wat wij willen realiseren aan het project.  

#### Selecting a Model
Voor het trainen heb ik niet specifiek een model gekozen, maar meer de [code](/src/code/RL-test2.py) aangepast naar mijn wensen. De code had al een [Environment (Class Area)](/src/code/RL-test2.py#L35-L48) en een [Agent (Class Container)](/src/code/RL-test2.py#L52-L116) die ik heb aangepast.

#### Configuring a Model
De [Environment (Class Area)](/src/code/RL-test2.py#L35-L48) definieert een array van 3x3 gevuld met nullen. Nul stelt voor dat er op die plek nog niets staat en dus wordt het aangegeven met een ' '. Elke plek dat een container bevat wordt met een 'X' aangegeven en wordt dus een 1.

De [Agent (Class Container)](/src/code/RL-test2.py#L52-L116) kiest als eerst een random containertype en zet het neer op de kade. Het geeft de coördinaten terug en kijkt daarna wat de volgende actie is. Er wordt eerst eromheen gekeken naar [de legale moves](/src/code/RL-test2.py#L97-L110) en [de mogelijke moves](/src/code/RL-test2.py#L62-L70) en roept dan de [move](/src/code/RL-test2.py#L72-L84) aan om de move te maken. Elke move legaal of illegaal wordt opgeslagen in de [q-table](/src/code/RL-test2.py#L117-L128).
#### Training a Model

#### Evaluating a Model

#### Visualizing the outcome of a model


## Communication 

#### Presentations
Ik heb me voorbereid op 2 interne en 1 externe presentaties. Voor de tweede interne presentatie had ik me niet op voorbereid. Ik moest namelijk invallen voor een medestudent die laatste moment had afgezegd. Uit ervaring kan ik zeggen dat ik minder zenuwachtig en beter presenteer wanneer ik niet erop voorbereid ben. Voor de externe presentatie had ik me echt op voorbereid en toen ik aan de beurt was, leek het alsof ik alles was vergeten en moest ik grotendeels oplezen wat ik had geschreven. Maar over het algemeen vind ik dat ik m'n best heb gedaan en dat ik ook goed de vragen van het publiek kon beantwoorden. In dit [mapje](/src/presentaties) zijn alle presentaties te vinden.

#### Writing paper
Behalve dat ik veel literatuuronderzoek heb gedaan voor de paper, heb ik ook het hoofdstuk methodologie geschreven. In dit hoofdstuk leg ik uit welke methoden en technieken we hebben toegepast voor het behalen van de eindresultaten. Hier laat ik zien, wat de verschillen tussen de 2 modellen is door middel van literatuuronderzoek en ook 2 afbeeldingen met de resultaten. Ook leg ik hier uit hoe de reward en penalty functies zijn ingericht in onze environment. De laatste versie van de [research paper](/src/docs/Research%20Paper%20Container%20Project.docx).
