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
- [Domain Knowledge](#domain-knowledge)
- [Predictive Analysis](#predictive-analysis)
- [Communication](#communication)


## DataCamp Course Certificates
Voor de start van de minor Applied Data Science, was Python nog heel onbekend voor mij. Door de nodige python kennis te kunnen ontwikkellen kreeg ik verplichte cursussen om te volgen, die ook hebben meegeholpen aan het uiteindelijke resultaat voor de minor. Deze cursussen waren te volgen op DataCamp en hiervoor kreeg ik voor elke behaalde cursus een [certificaat](/DataCamp) 

## Research Project

#### Task Definition
#### Evaluation
#### Conclusions
#### Planning
In dit hoofdstuk wordt kort uitgeled wat de probleemstelling en doelstelling zijn en welke onderzoeksvragen hebben geleid tot het uiteindelijke resultaat.
Dit project is de taak van [Cofano](https://www.cofano.nl/nl/) en gaat voornamelijk over het optimalisatieproces van het in- en uitladen van containers op een kade. Momenteel wordt dit proces nog handmatig door een persoon bepaald en uitgevoerd en dit leidt tot heel veel inefficiënt geplaatste containers. Dit heeft als gevolg dat zowel het inladen als het uitladen meer tijd kost. Het is aan ons toegewezen om hiervoor een oplossing voor te bedenken door gebruik te maken van Machine Learning. Wij willen namelijk de tijd, waarbij het proces wordt uitgevoerd, verkorten. Voordat wij van start zijn gegaan met het kiezen van een model, hebben wij eerst hoofdvragen en deelvragen geformuleerd. Dit heeft het makkelijker gemaakt voor ons om aan de slag te gaan

#### Hoofdvraag
- *Hoe kan ervoor gezorgd worden dat containers op de kade op een efficiënte manier opgestapeld kunnen worden, zodat de afnemer van de containers hier makkelijk bij kan?*

#### Deelvragen
- *Hoe ziet de layout van de desbetreffende kade eruit?*
- *Welke modellen/methodes zijn relevant om dit optimalisatieprobleem aan te pakken?*

De [hoofdvraag](#hoofdvraag) wordt in het kopje [Domain Knowledge](#domain-knowledge) beschreven en beantwoordt.\
De [deelvragen](#deelvragen) worden hier verder besproken.

1. **Hoe ziet de layout van de desbetreffende kade eruit?**\
Voor het trainen van een model, hebben wij eerst ervoor gekozen om een 3x3 (row x bay) kade te gebruiken. In totaal kunnen er 9 containers geplaats worden. Door het uitbreiden en verder optimaliseren van het proces, konden wij ook in de hoogte containers stapelen (row x bay x tier). Om het realistisch te houden, hebben wij de max-hoogte gelegd op 3 containers (3x3x3). 

2. **Welke modellen/methodes zijn relevant om dit optimalisatieprobleen aan te pakken?**\
Uit onderzoek en gesprekken met docenten is gebleken dat de beste oplossing voor dit probleem is, het gebruikmaken van Reinforcement Learning (RL). RL is een heel uitgebreid onderwerp en heeft een aantal modellen die gebruikt kunnen worden. Om de beste model te kunnen kiezen, moesten wij eerst alle modellen uitproberen en testen. Hieruit zijn wij met 2 modellen gekomen nl. PPO (Proximal Policy Optimization) en A2C (Advantage Actor Critic). Uiteindelijk hebben wij toch ervoor gekozen om met PPO verder te gaan en dat wordt in het kopje [Domain Knowledge](#domain-knowledge) verder uitgelegd.


## Domain Knowledge
#### Introduction of the subject field
#### liuterature research
#### Explanation of Terminology, jargo and definitions
Dit hoofdstuk gaat over de literatuuronderzoek die hebben geleidt tot het kiezen van een model voor het trainen.\
Het doel is om de beste manier te vinden om containers, met verschillende bestemmingen, op te stapelen op de kade zodat het proces vlotter en sneller verloopt. Om dit ook makkelijker te maken, hebben we besloten om alle containers dezelfde dimensies te geven.\
Als eerst moeten we kijken naar de kade. Zoals in [deelvraag 1](#deelvragen) besproken, hebben wij eerst gekozen om een 3x3 kade te gebruiken. Rekeninghoudend met de Reach-stacker, die de containers verplaatst, heeft dit vele beperkingen. De Reach-stacker kan alleen via de bay kant een container pakken en plaatsen. Dit heeft heel veel invloed op de manier hoe wij een model zullen trainen namelijk op de 'reward-systeem' (wordt nog uitgelegd). 

Ook moeten wij rekening houden met de verschillende containers met verschillende (eind)bestemmingen. Wij willen het makkelijker maken voor de Reach-stacker om alles in één keer te kunnen pakken, zonder eerst andere containers te verschuiven. Dit hebben we kunnen realiseren door eerst dezelfde containers op een row of bay te sorteren alvorens een andere container te plaatsen. Ook rekeninghoudend met de volgorde waarop de containers geplaatst worden, worden de laatste containers onderaan geplaatst. Hierbij wordt naar de schema van inkomende en uitgaande schepen gekeken. 

-----------------------------

#### Reinforcement Learning en PPO

RL kan op verschillende manieren benadert worden. Bij RL hebben wij eerst een [Environment]() nodig. In ons geval is het een 3x3 kade die gevuld moet worden met verschillende containers. Om de optimale oplossing te krijgen, maken wij gebruik van een reward-systeem. Dit houdt in dat de [Agent]() bij elke plaatsing van een container, een positieve of negatieve reward kan krijgen. Dit is noodzakelijk voor het trainen van het model. Uit de rewards kan het model leren welke moves beter zijn. Elke move krijgt een reward, geeft een state terug en bepaald zijn volgende actie. 
PPO is nieuw model van [OpenAI](https://openai.com/blog/openai-baselines-ppo/) en dat is Proximal Policy Optimization. De nadruk wordt op de Policy gelegd omdat de policies aangepast kunnen worden naar de specificaties van de trainer.

Onze reward-systeem bestaat uit enkele regels namelijk:
- Containers mogen niet op de eerste bay geplaatst worden waardoor de Reach-stacker belemmerd wordt.
- Container A moet zoveel mogelijk naast container A geplaats worden en dus geen plek ertussen openlaten.
- Container C mag niet tussen containers A en A geplaatst worden.
(nog enkele regels hier plaatsen)


## Predictive Analysis
#### Selecting a Model
#### Configuring a Model
#### Training a Model
#### Evaluating a Model
#### Visualizing the outcome of a model
In deze paragraaf laat ik zien wat ik heb bijgedragen aan het opleveren van de [finalcode]().  
Als groep hadden we eerst besloten dat een ieder een model zou proberen te trainen zodat een ieder ook weet hoe RL werkt. Ik heb een soort werkend model dat ongeveer lijkt op de environment van het project. Dit was meer voor het begrijpen hoe RL werkt. Alhoewel het niet heeft bijgedragen aan [finalcode](), heeft het wel geholpen aan het beter begrijpen wat wij willen realiseren aan het project.  


## Communication 

