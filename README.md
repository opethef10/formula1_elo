## THE BEST QUALIFYING DRIVERS IN THE FORMULA 1 HISTORY

**With the contributions of Formula 1 Türkiye admins Onur Arıkan, Alp Umut Kurbay and Semih Boz, we prepared the ranking of the best qualifying drivers in F1 history. In the table below you can see the scores, the ranking and the change over the years.**

#### Motivation

When we started this project, we decided that we could best compare the drivers in F1 when both drivers had the same car at the same time. In short, we thought of a scoring system that makes drivers gain / lose points by looking at the scores recorded by the pilots in the qualifying rounds against their teammates with the same vehicle over the years. For this, we used the **Elo** system, which is used especially in chess tournaments, where players gain and lose points after the match according to the result of the match.

#### Why Elo System?

According to the ELO system, since the player with the higher score has a higher probability of winning, if the match ends as expected, that is, if the player with the higher score wins, this player gains fewer points and the other side loses fewer points. However, if the match ends in a draw or the winner of the lower scorer, the player with the higher score is punished with more points for losing to someone who is lower in level, while the player with the lower score is rewarded with many points for defeating someone stronger than himself. So the first case is rewarded with more points as a draw with Hamilton would be a greater achievement than beating Vandoorne.

In Formula 1, the intra-team competition is high in some teams, while in others, one driver clearly dominates the other. Examples:

-   **2018 Fernando Alonso - Stoffel Vandoorne.** Already at the beginning of the year, Alonso's defeat of Vandoorne was expected, and Alonso gained 15 points from this season (according to the model).
    
-   **2010 Nico Rosberg - Michael Schumacher.** When Michael Schumacher retired in 2006, he was second behind Ayrton Senna with 1890 points. Nico Rosberg, on the other hand, had only 4 seasons in F1 until that year and had 1684 points. When Schumacher returned, he was almost 200 points ahead of Nico Rosberg and lost 14-5 to Nico Rosberg, with Rosberg gaining 93 points from this season alone and Schumacher losing 93 points.
    

#### **Scoring System**

Before the formula itself, let's understand the score calculation of the drivers according to the result of the matches. In chess tournaments, the winner gets 1 point, the loser gets 0 points, and 0.5 points are shared in the draws. These scores are substituted in the Elo formula and the player's total point change at the end of the match is calculated.

However, in Formula 1, even if one driver outperforms the other 11-10 in 21 races due to various factors in a season, this is not actually a win. The performances of the drivers are seen almost equally. For this reason, we thought that we could not put the drivers who were beaten 11-10 and those who were beaten 21-0 or 14-7 in the same category, so we divided the points. According to this; if the driver is in qualifying against his teammate in a season:

-   If he won 0-24%; 0 (dominated)
-   If he won 25-40%; 0.3 (loss)
-   If he won 41-59%; 0.5 (tie)
-   If he won 60-75%; 0.7 (win)
-   If he won 76-100%; 1 (dominance)

he gets such scores. If we think of each season as 1 match, the player can get 5 different points from each match as above. For example, in the 2003 season, Schumacher had a 10-6 advantage over Barrichello in qualifying. Since MSC won 10 of 16 races, 62.5%, the score for this match is calculated in favor of MSC 0.7-0.3.

#### **Model: Elo formula**

-   r1: Previous score of the winning driver
-   r2: Previous score of the losing driver
-   n1: The winning driver's new score after match
-   n2: New score of the losing driver after match
-   s: Points awarded according to the above-mentioned distribution according to the superiority in the qualifying rounds
-   m: When the winning driver's probability of winning is 10 times that of the losing driver, the required difference in points: fixed **400**
-   e: probability of driver 1 defeating driver 2 (calculated below according to the previous scores of the drivers)
-   K: Maximum points available per match: **200** in our system

**e: 1 / (1 + (10<sup>r2-r1</sup> / m))**

**n1: r1 + K \* (s-e)**  
**n2: r2 - K \* (s-e)**

Starting from 1950, the score of each driver over the years has been updated and a ranking has been made according to the end of 2022. However, since according to the formula, every driver must have a score before the match, we have considered it appropriate for each driver to start with a certain score in the first year of their career, according to some of their characteristics. If the driver

-   is a world champion: **1600**,
-   is only a race winner: **1500**
-   is none of these: **1400**

Although this assumption may seem unfair at first, due to the beauty of the Elo system, the drivers who start with high scores lose 100-150 points in their first year when they lose against their teammate, and this advantage or disadvantage is neutralised. If they start by winning, they usually gain few points because they have high points, and by getting 20-50 points, they are still not far ahead, and they are at the level they deserve.

Apart from this, especially in the last 40 years, since the teams did not race more than 2 drivers, each season the pilots had 1 match against their teammate, but since they were competing with 3-4 pilots at the same time in the 1950s and 60s, a driver had more than one teammate and more than one match. In such cases, although drivers such as Dan Gurney and Fangio competed in a small number of seasons, they were able to rise to the top with the points they achieved by playing 3-4 matches in a single season. For this reason, the average score of all matches of a driver in a season was taken into account.
