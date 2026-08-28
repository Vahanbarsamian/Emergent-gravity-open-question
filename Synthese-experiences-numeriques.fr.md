🇫🇷 Français | [🇬🇧 English version](./Synthese-experiences-numeriques.en.md)

# Synthèse des expériences numériques — modèles jouets pour l'émergence gravitationnelle

> **Statut du document :** synthèse de travail numérique exploratoire, réalisée en complément du document théorique [« Question ouverte : la géométrie gravitationnelle peut-elle émerger d'une structure quantique ? »](./Question-ouverte-gravite-source.fr.md) et de sa [cartographie de la littérature](./Reflexion-ouverte-sur-la-gravite.fr.md). Ce document ne revendique la résolution d'aucun problème ouvert de physique théorique. Il documente 28 tests numériques sur des modèles jouets, avec leurs résultats positifs et négatifs, dans le même esprit méthodologique que le document source.
> **Code :** chaque test cité est reproductible ; le code correspondant est archivé dans ce document ou dans le journal complet.

---

## 0. Garde-fous méthodologiques

- **Un modèle jouet n'est pas une théorie physique.** Rien dans ce document n'établit que la gravité émerge d'un mécanisme de cohérence de phase — seulement que certains mécanismes mathématiques précis produisent, ou ne produisent pas, certaines propriétés recherchées, dans des modèles simplifiés.
- **Un résultat négatif est documenté au même titre qu'un résultat positif.** Plusieurs pistes explorées ici ont échoué explicitement (voir §7) ; les garder visibles évite de refaire les mêmes essais.
- **Aucun nombre n'est retenu sans code reproductible et sans graine aléatoire documentée.** Un chiffre qui circule entre plusieurs assistants IA sans trace de calcul (voir §6) n'est pas retenu comme résultat, quelle que soit sa plausibilité apparente.
- **Toute quantité candidate à l'universalité est testée contre les paramètres arbitraires du modèle** (taille, couplage, seuils) avant d'être présentée comme telle.

---

## 1. Vue d'ensemble — état des lieux

| Question | Statut | Test(s) |
|---|---|---|
| Un mécanisme de rappel dérivé des amplitudes (non postulé à la main) peut-il produire un retour à la cohérence après perturbation ? | 🟢 Confirmé | Test 9 |
| Ce même mécanisme peut-il produire une suppression d'énergie effective ($\rho_{\rm eff} \ll \rho_{\rm micro}$) ? | 🟠 Partiel, faible et bruité | Tests 11-13 |
| Existe-t-il une largeur de couplage dérivée (non ajustée à la main) depuis l'action microscopique ? | 🟢 Oui (courbure de l'action, Van Vleck-Morette) | Tests 14-15 |
| Un facteur de contraction $q$ universel existe-t-il entre échelles ? | 🔴 Non — dépend d'un seuil arbitraire tant que le critère de sélection n'est pas unifié | Tests 17-18 |
| Ce même $q$ devient-il stable une fois le critère de sélection unifié avec la dynamique ? | 🟠 Converge en $N$ ($q\approx4{,}9$ à $N$ élevé) mais dépend encore de $K$ | Tests 19-21, reproduction indépendante |
| Une reconstruction géométrique (ordre causal, dimension) est-elle possible depuis la dynamique ? | 🟢 Oui — dimension de Myrheim-Meyer cohérente avec la dimensionnalité connue du modèle | Test 24 (H25) |
| Une distance de corrélation de phase donne-t-elle une géométrie valide ? | 🔴 Non — dégénérée dans ce modèle | Test 26 |
| Le signe de $R$ code-t-il une orientation causale (« deux cônes symétriques ») ? | 🔴 Non confirmé — asymétrie persistante due à la dissipation du modèle | Test 27 |
| Le signe de $R$ code-t-il une frustration topologique (tore) ? | 🔴 Non — mais un effet topologique réel existe, sur $C$, pas sur $R$ | Test 28 |
| Un plancher positif $R_\infty>0$ existe-t-il à long terme ? | 🔴 Non démontré | Tests recensés en §7 |
| $R$ marque-t-il transition vs stabilisation ? | 🟢 Confirmé — pic continu (hauteur/largeur), pas un interrupteur binaire | Tests 29b, 31, 32 |
| $K$ peut-il être dérivé (pas postulé) depuis une action microscopique ? | 🟢 Oui — $K=g^2/m^2$ via élimination adiabatique d'un champ médiateur | Tests 33, 34b |
| Le modèle reproduit-il une loi newtonienne en $1/r^2$ ? | 🟠 Oui, mais seulement après correction d'un défaut structurel (instabilité linéaire) | Tests 39-42 |
| Les exposants $4/3$, $3/4$ apparaissent-ils dans la solution radiale ? | 🔴 Non confirmé — proximité approximative sur un point isolé, pas un plateau | Test 43 |

---

## 2. Fil 1 — Mécanisme de rappel dérivé des amplitudes

**Question :** un mécanisme de retour à la cohérence après perturbation peut-il être dérivé uniquement des interférences entre amplitudes $A_i=e^{iS(Q_i)/\hbar}$, sans écrire à la main un gradient de cohérence $\nabla_Q C$ ?

**Résultat (Test 9) :** un couplage de type Kuramoto, $\dot\theta_i = \frac{K}{N}\sum_j \sin(\theta_j-\theta_i)$ — dérivé de $\mathrm{Im}(A_i^*A_j)$, pas postulé — reproduit le retour à la cohérence, avec une transition progressive autour de $K_c\approx0{,}14$–$0{,}36$ (comportement de synchronisation de Kuramoto, cf. Strogatz, *From Kuramoto to Crawford*, Physica D 143, 1 (2000)).

**Précédent de circularité écarté (Test 8) :** un rappel imposé directement comme $\dot Q_i\propto\nabla_{Q_i}C$ "fonctionne" trivialement par construction — ce n'est pas une découverte, juste la vérification qu'un gradient ascendant fait ce qu'on lui demande. Le Test 9 est la version non circulaire.

---

## 3. Fil 2 — Suppression d'énergie effective (critère H10a/b/c)

**Question :** ce mécanisme peut-il produire $0 < \rho_{\rm eff} \ll \rho_{\rm micro}$ (calculé, pas ajusté) ?

**Résultat (Test 11, couplage uniforme) :** échec net. $\rho_{\rm eff}/\rho_{\rm micro} = 1{,}000$ exactement — le couplage uniforme synchronise toute la population sans aucun tri par énergie.

**Résultat (Tests 12-13, couplage localisé en énergie) :** suppression réelle mais modeste et bruitée. $\rho_{\rm eff}/\rho_{\rm micro}$ passe de $1{,}000$ à $\approx0{,}4$–$0{,}6$ pour une largeur de localisation $\sigma\in[8,15]$, avec des écarts-types importants (jusqu'à 0,4). Sans commune mesure avec le facteur $10^{120}$ requis par le critère de validation cosmologique (cartographie, §11/47) — attendu pour un modèle jouet, mais à ne jamais présenter comme une approche de ce facteur.

**Origine de la largeur de localisation (Tests 14-15) :** une tentative de dériver $\sigma$ depuis la formule d'interférence brute ($\cos(\theta_i-\theta_j)$) échoue — la phase repliée modulo $2\pi$ perd l'information de distance métrique dès qu'elle effectue plusieurs tours. La largeur correctement dérivée vient de la **courbure de l'action** ($S''(Q)=2s$ pour $S(Q)=sQ^2$), via le déterminant de Van Vleck-Morette (Van Vleck 1928 ; Morette 1951) : $\sigma_Q = 1/\sqrt{2s}$ — un résultat standard de l'approximation de la phase stationnaire, pas un paramètre inventé.

---

## 4. Fil 3 — Universalité et recherche d'un facteur d'échelle

**Question :** existe-t-il un facteur de contraction $q$ universel entre échelles successives ?

**Résultat (Tests 17-18, critère à seuil arbitraire) :** non. $q$ varie d'un facteur 12 (de 31,6 à 2,7) selon le seuil angulaire de tolérance choisi pour définir « appartient au secteur cohérent » — un artefact de construction, pas une propriété physique.

**Résultat (Tests 19-21, critère unifié — H24) :** en remplaçant le seuil arbitraire par un critère dérivé du même poids que la dynamique ($r_i>0{,}5$, ordre local de cohérence), la dispersion s'effondre. Convergence nette en $N$ : $q=4{,}707\pm0{,}561$ ($N{=}800$) → $4{,}886\pm0{,}037$ ($N{=}1600$) → $4{,}908$ ($N{=}3200$, une graine). **Mais $q$ reste dépendant de $K$** même à $N$ élevé : $5{,}026$ ($K{=}0{,}3$) → $4{,}535$ ($K{=}0{,}7$), dépendance monotone confirmée. **$q\approx4{,}9$ n'est donc pas universel** — c'est une valeur locale, reproductible pour un $K$ donné, pas une constante.

**Reproduction indépendante (23 août 2026) :** campagne multi-graines confirmant exactement les valeurs et la conclusion ci-dessus (écart relatif ~0,12% avec les valeurs originales). Formulation recommandée et retenue : *« q≈4,9 est une valeur localement reproductible pour K=0,4 et N=1600 ; elle ne soutient pas l'énoncé q=4,9 universel. »*

**Recherche de $K_c$ intrinsèque (Test 22-23, croisement de Binder) :** pas de croisement net identifié dans les plages testées ($K\in[0{,}05,0{,}4]$ puis $[0{,}5,2{,}0]$) — recherche inconclusive, point de reprise identifié plutôt que résultat.

---

## 5. Fil 4 — Reconstruction géométrique (H25, "cône causal")

**Question :** peut-on construire une géométrie effective (ordre causal, dimension) directement depuis la dynamique microscopique, sans la présupposer ?

**Méthode (Test 24) :** ordre causal dérivé du temps de verrouillage de chaque configuration + poids de couplage dérivé (aucun seuil externe ajouté). Dimension de **Myrheim-Meyer** (Myrheim 1978 ; Meyer 1988 — estimateur standard des ensembles causaux, Bombelli-Lee-Meyer-Sorkin 1987) estimée : $d\approx1{,}85$, cohérente avec la dimensionnalité réelle du modèle jouet (1 variable spatiale + 1 temps émergent = 1+1D). Validation de sanité réussie : la méthode ne tombe pas dans le régime pathologique des ordres aléatoires non géométriques (Kleitman & Rothschild, 1975).

**Comparaison avec une distance de corrélation (Test 26) :** la méthode alternative proposée indépendamment (distance $d_{ij}=-\log|K_{ij}|$ à partir des corrélations de phase) échoue le critère de non-dégénérescence — de nombreuses paires synchronisées ont $d_{ij}=0$ exactement, et la dimension estimée (Grassberger-Procaccia, 0,38-0,42) est incohérente avec Myrheim-Meyer. **Seule l'approche par ordre causal est retenue** pour la suite.

**$R$ redéfini géométriquement (Test 25) :** un $R_{\rm causal}(t)$ = taux de formation de nouvelles relations causales (plutôt que $dC/dt$) montre un comportement qualitativement différent — décroissance quasi monotone d'un régime actif vers une saturation proche de zéro, sans oscillation aléatoire. Pas de plancher positif établi, mais une structure temporelle plus nette que les définitions précédentes de $R$.

**Test de structure "double cône" (Test 27, intuition utilisateur) :** hypothèse d'une symétrie futur/passé (cônes opposés collés en chaque point) — **non confirmée**. Asymétrie systématique persistante ($+4{,}9\pm6{,}2$ dans la partie centrale, 86% des configurations avec plus de futur que de passé), attribuable à la nature dissipative de la dynamique microscopique utilisée (Kuramoto), qui possède une flèche du temps intégrée. Deux lectures possibles laissées ouvertes : (a) une dynamique réversible donnerait la symétrie recherchée, ou (b) l'asymétrie elle-même est la source d'une flèche du temps émergente.

---

## 6. Fil 5 — Topologie compacte (tore)

**Question testée (Test 28) :** le signe de $R$ code-t-il une « frustration topologique » sur un domaine compact (tore) ?

**Résultat :** le winding number (invariant topologique standard, quantifié — physique XY/Kuramoto sur réseau périodique) ne corrèle **pas** avec le signe de $R$. En revanche, un enroulement topologique non trivial ($W\neq0$) supprime effectivement la cohérence globale $C$ ($C_{\rm moyen}=0{,}23$ contre $0{,}41$ pour $W\approx0$) — un effet réel, mais porté par $C$, pas par $R$. L'intuition topologique contenait une graine correcte, mal identifiée dans sa formulation initiale.

---

## 7. Fil 6 — R comme témoin dynamique de transition

**Question :** $R$ (sous une définition ou une autre) porte-t-il une information physique réelle, au-delà d'un simple indicateur bruité ?

**Résultat (Tests 29a/29b) :** $R=dC/dt$ marque nettement une transition suivie d'une stabilisation — pic net pendant la synchronisation, retour à ~0 une fois la cohérence atteinte, confirmé dans deux régimes de couplage $K$ bien séparés. Nécessite le modèle de couplage uniforme (Test 9/25), pas le couplage localisé (Tests 19-21) — les deux modèles ne sont pas interchangeables.

**Résultat (Test 31) :** hauteur et largeur du pic de $R$ varient de façon continue et monotone avec $K$ (largeur : 17,8 → 2,7 fenêtres entre $K=0{,}15$ et $K=1{,}5$) — un curseur continu de la vitesse de transition, pas un interrupteur binaire "lent/brutal". Cohérent avec une transition du second ordre (continue), pas un changement de régime brutal.

**Résultat (Test 32) :** modèle minimal de saturation logistique ($dC/dt=kC(1-C/C_{\max})$) — le pic de $R$ se produit exactement au point d'inflexion ($C=C_{\max}/2$), $C$ ne dépassant jamais $C_{\max}$. $R$ témoigne ainsi d'un basculement (« événement invisible ») vers un état saturé sans singularité, dans ce modèle minimal à une variable — pas encore couplé à une vraie dynamique de champ spatial.

**Résultat (Test 30) :** avec un bruit persistant irréductible, $R$ n'atteint plus jamais exactement zéro — mais c'est une propriété triviale de toute variable aléatoire continue, pas une découverte physique. La moyenne de $R$ reste centrée sur zéro ; seule sa dispersion croît avec le bruit. Aucun biais directionnel créé.

---

## 8. Fil 7 — Dérivation de K (H2/H7)

**Question :** $K$ (la constante de couplage utilisée depuis le Test 9) peut-elle être dérivée d'une action microscopique plutôt que postulée ?

**Résultat (Test 33) :** la dynamique utilisée depuis le Test 9 est exactement le flot de gradient d'un potentiel $V[\theta]=-\frac{K}{2N}\sum_{ij}w_{ij}\cos(\theta_i-\theta_j)$ (écart numérique ~$10^{-11}$, précision machine). $K$ est donc déjà, structurellement, la constante de couplage d'un terme d'interaction de type XY — pas une force ajoutée à la main.

**Résultat (Test 34, première tentative puis correction) :** dérivation de $K$ par élimination adiabatique d'un champ médiateur $\psi$ (technique de type Hubbard-Stratonovich, analogue à la gravité induite de Sakharov déjà citée en cartographie). Une erreur de signe a d'abord donné un échec complet ($C_{\rm final}=0$ partout) ; une fois corrigée (Test 34b), le système complet avec médiateur reproduit avec précision la dynamique de Kuramoto réduite avec **$K_{\rm eff}=g^2/m^2$**, sur 5 valeurs de couplage $g$ testées (accord à la 3e-4e décimale).

**Portée :** première dérivation réelle d'un paramètre du modèle, plutôt qu'un ajustement. $g$ et $m$ (couplage au médiateur, masse du médiateur) restent eux-mêmes des paramètres externes — le problème est repoussé d'un cran, pas résolu.

---

## 9. Fil 8 — Limite newtonienne et reconstruction radiale

**Question :** le modèle produit-il un champ gravitationnel effectif en $1/r^2$ à grande distance (limite newtonienne), condition nécessaire pour tout raccordement à la RG ?

**Diagnostic initial (Tests 35-37) :** une formule externe de dimension (attribuée à un rapport tiers) ne correspond à aucune quantité réelle de nos données (Test 35, rejetée). Une première tentative de résolution de l'équation de Poisson radiale (Test 37) échoue : la masse totale intégrée diverge, parce que la source $(C-C_c)$ ne s'annule pas à grande distance quand $C$ relaxe librement vers 0 au lieu de $C_c$.

**Correction de condition aux limites (Test 38) :** imposer $C(r\to\infty)=C_c$ fait converger la masse — mais un test indépendant à plus grand rayon (Test 39, $r_{\max}=40$ au lieu de 8) **révèle que cette convergence était un faux positif** : sur une fenêtre plus large, $g(r)\cdot r^2$ diverge sans limite. Correction explicite d'un résultat qu'on avait cru acquis.

**Diagnostic structurel (Test 40) :** le point fixe $C=C_c$ de l'équation de réaction-diffusion utilisée est linéairement **instable** (taux $+1{,}6$) — ce n'est pas un problème numérique, c'est un front d'invasion de Fisher-KPP qui envahit indéfiniment tout l'espace. Aucune fenêtre de calcul ne peut réparer ça.

**Correction structurelle (Tests 41-42) :** rendre le terme de croissance spatialement localisé ($k(r)=k_0 e^{-r^2/2\sigma^2}$, motivé par la largeur $\sigma_Q$ dérivée en Fil 2) restaure un point fixe stable loin du cœur. Résultat : $|g(r)|\cdot r^2$ se stabilise à grande distance (écart à $M_{\rm tot}$ de 0,65% à 2,36% sur 9 combinaisons de paramètres, diminuant systématiquement avec $\sigma$ croissant) — **première loi en $1/r^2$ authentique et robuste obtenue dans ce travail**.

**Recherche d'exposants intermédiaires (Test 43) :** extraction directe des pentes locales de $m(r)$ et $g(r)$, sans présupposer de cible. Cœur : $\alpha\approx2{,}9$, $\beta\approx0{,}9$ (cohérent avec une densité quasi uniforme). Champ lointain : $\alpha\to0$, $\beta\to-2$ (newtonien correct). Une région de transition ($r\approx7{,}5$) passe près de $4/3$ et $-3/4$ (écarts 3% et 6%) mais sans y former de plateau — **non confirmé comme exposant caractéristique**, proximité approximative du même ordre que d'autres coïncidences déjà écartées dans ce travail (facteur $q$, Fil 3).

---

## 10. Ce qui n'est PAS établi (point de vigilance central)

- Aucun plancher positif $R_\infty>0$ à long terme n'a été démontré — les tests disponibles (issus d'un fil externe, non reproduits indépendamment dans ce document) concluent explicitement l'inverse : $\langle R\rangle_{\rm queue}\approx0$, signes positifs et négatifs se compensant presque exactement.
- Un « modèle tore-cône » avec système d'équations couplées de type Friedmann ($\dot C$, $\dot H$), un point fixe critique $C_c$, et un facteur $q^*$ « universel » a été proposé dans un échange avec Gemini. **Le système d'équations couplées, le point fixe $C_c$ et le facteur $q^*$ n'ont jamais été construits ni testés dans ce travail** — les chiffres qu'ils citent ($q\approx4{,}908$, asymétrie $+4{,}9$) proviennent de deux tests distincts et de nature différente (Test 20 : ratio de population ; Test 27 : asymétrie causale), fusionnés sur la seule base d'une coïncidence numérique à la 3e décimale sur un seul tirage chacun — non retenu comme résultat.

  **En revanche, l'idée géométrique sous-jacente — un domaine spatial compact (tore) parcouru par une structure causale (cône) — origine bien de cet échange avec Gemini.** Elle a été reprise et reformulée en un test rigoureux et non circulaire dans ce document (Test 28, §6) : winding number sur un anneau, un invariant topologique standard, indépendant des équations fabriquées du document original. Le résultat de ce test (§6) est réel et retenu ; les équations de Friedmann couplées à $C$ ne le sont pas.
- Aucune métrique lorentzienne complète, aucune action effective contenant $\sqrt{-g}R$, aucun $G_{\rm eff}$ ou $\Lambda_{\rm eff}$ calculé (par opposition à ajusté) n'a été obtenu à ce stade.
- Aucun test sur un système physique connu (limite newtonienne, Schwarzschild) n'a été tenté — délibérément, pour ne pas introduire la réponse recherchée dans le modèle avant d'avoir une règle de reconstruction validée.

---

## 11. Registre des contributions

Ce travail s'est construit en dialogue avec plusieurs assistants IA (Claude, ChatGPT, Perplexity, Gemini, Grok), chacun ayant contribué des idées ou des tests distincts. Conformément au principe de non-attribution sans vérification (§0), aucune contribution n'est ici qualifiée de « validée » par un assistant sans que le test correspondant soit reproductible dans ce document.

- Le mécanisme de rappel dérivé des amplitudes (Fil 1) et le critère de sélection unifié (Fil 3) ont été développés et testés dans ce fil de travail.
- La question du terme de rappel non circulaire, la structure à bassins multiples, et le troisième régime (retour/transition/décohérence) ont été explorés indépendamment dans un autre fil, dont les résultats qualitatifs (pas les chiffres non reproductibles) ont orienté les Tests 16 et suivants.
- La reproduction indépendante du §4 (facteur $q$) a confirmé, sans en dévier, les résultats et les limites déjà établis ici.
- Une synthèse ("modèle tore-cône") combinant des chiffres de tests distincts en un cadre théorique non testé a été identifiée et explicitement écartée de ce document (§10).
- **Gemini** a contribué un point de convergence honnête et réel (l'échec de dérivation de $G_{\rm eff}$ depuis Fisher-KPP seul, cohérent avec notre propre diagnostic), ainsi que l'idée géométrique tore+cône reprise au Test 28. Le même fil a aussi produit à plusieurs reprises des chiffres non reproductibles (formule de dimension fabriquée, Test 35 ; valeurs de déviation lumineuse physiquement absurdes ; une dérivation lagrangienne complète produite sans code malgré une règle de rigueur énoncée explicitement dans le même message) — ces éléments ont été testés indépendamment et rejetés, ou n'ont simplement pas pu être vérifiés.
- **ChatGPT** a fait preuve d'une bonne discipline épistémique dans au moins un échange (refus explicite de fabriquer un lien vers un fichier après l'échec d'un outil), avec des résultats de recherche d'exposant présentés de façon appropriément prudente (non-preuve explicitement reconnue) — non vérifiés indépendamment faute de code transmis.
- **Grok** a proposé un "Test 51" (statut $C_c=1/5$ non sélectionné dynamiquement par le mécanisme de Kuramoto pondéré, distinction entre branche dynamique et branche géométrique) présenté avec une discipline de calibration correcte — non vérifié indépendamment dans ce document, faute de code. La proposition qui en découle (chercher les exposants directement dans la solution radiale plutôt que dans la dynamique de cohérence) a mené au Test 43, exécuté et documenté ici.

---

*Document de travail numérique — dépôt ouvert, corrections et répliques bienvenues. Code source de chaque test disponible sur demande ou dans le journal complet du projet.*
