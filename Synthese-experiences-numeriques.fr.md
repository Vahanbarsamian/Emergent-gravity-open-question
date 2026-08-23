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
| Un plancher positif $R_\infty>0$ existe-t-il à long terme ? | 🔴 Non démontré | Tests recensés en §6 |

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

## 7. Ce qui n'est PAS établi (point de vigilance central)

- Aucun plancher positif $R_\infty>0$ à long terme n'a été démontré — les tests disponibles (issus d'un fil externe, non reproduits indépendamment dans ce document) concluent explicitement l'inverse : $\langle R\rangle_{\rm queue}\approx0$, signes positifs et négatifs se compensant presque exactement.
- Un « modèle tore-cône » avec système d'équations couplées de type Friedmann ($\dot C$, $\dot H$), un point fixe critique $C_c$, et un facteur $q^*$ « universel » a été proposé dans un échange avec Gemini. **Le système d'équations couplées, le point fixe $C_c$ et le facteur $q^*$ n'ont jamais été construits ni testés dans ce travail** — les chiffres qu'ils citent ($q\approx4{,}908$, asymétrie $+4{,}9$) proviennent de deux tests distincts et de nature différente (Test 20 : ratio de population ; Test 27 : asymétrie causale), fusionnés sur la seule base d'une coïncidence numérique à la 3e décimale sur un seul tirage chacun — non retenu comme résultat.

  **En revanche, l'idée géométrique sous-jacente — un domaine spatial compact (tore) parcouru par une structure causale (cône) — origine bien de cet échange avec Gemini.** Elle a été reprise et reformulée en un test rigoureux et non circulaire dans ce document (Test 28, §6) : winding number sur un anneau, un invariant topologique standard, indépendant des équations fabriquées du document original. Le résultat de ce test (§6) est réel et retenu ; les équations de Friedmann couplées à $C$ ne le sont pas.
- Aucune métrique lorentzienne complète, aucune action effective contenant $\sqrt{-g}R$, aucun $G_{\rm eff}$ ou $\Lambda_{\rm eff}$ calculé (par opposition à ajusté) n'a été obtenu à ce stade.
- Aucun test sur un système physique connu (limite newtonienne, Schwarzschild) n'a été tenté — délibérément, pour ne pas introduire la réponse recherchée dans le modèle avant d'avoir une règle de reconstruction validée.

---

## 8. Registre des contributions

Ce travail s'est construit en dialogue avec plusieurs assistants IA (Claude, ChatGPT, Perplexity, Gemini), chacun ayant contribué des idées ou des tests distincts. Conformément au principe de non-attribution sans vérification (§0), aucune contribution n'est ici qualifiée de « validée » par un assistant sans que le test correspondant soit reproductible dans ce document.

- Le mécanisme de rappel dérivé des amplitudes (Fil 1) et le critère de sélection unifié (Fil 3) ont été développés et testés dans ce fil de travail.
- La question du terme de rappel non circulaire, la structure à bassins multiples, et le troisième régime (retour/transition/décohérence) ont été explorés indépendamment dans un autre fil, dont les résultats qualitatifs (pas les chiffres non reproductibles) ont orienté les Tests 16 et suivants.
- La reproduction indépendante du §4 (facteur $q$) a confirmé, sans en dévier, les résultats et les limites déjà établis ici.
- Une synthèse ("modèle tore-cône") combinant des chiffres de tests distincts en un cadre théorique non testé a été identifiée et explicitement écartée de ce document (§7).

---

*Document de travail numérique — dépôt ouvert, corrections et répliques bienvenues. Code source de chaque test disponible sur demande ou dans le journal complet du projet.*
