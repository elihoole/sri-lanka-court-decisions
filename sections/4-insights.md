# **Computational Insights from CDTextLK** {#sec:insights}

## Introduction: Patterns Beyond Precedent

The study of judicial decisions in Sri Lanka has traditionally focused on landmark cases and constitutional developments—Supreme Court determinations on fundamental rights, special determinations on bills, and appellate decisions on questions of law. This approach privileges doctrinal significance and treats courts primarily as sites of legal interpretation. Yet this perspective captures only part of what courts do. The empirical analysis of CDTextLK reveals patterns that challenge received assumptions about the nature and distribution of judicial work in Sri Lanka's appellate courts.

This section presents six key insights organized around four themes: quantitative dominance, temporal dysfunction, substantive concentration, and overlooked jurisprudence. These insights emerge from both descriptive statistics—the volume, timing, and length of decisions—and computational methods including topic modeling and mutual information analysis. Together, they provide a corrective to the landmark case-focused understanding of judicial work by making visible the patterns that structure day-to-day judicial practice.

The findings demonstrate that the Court of Appeal's numerical dominance far exceeds its doctrinal recognition; that writ petitions vastly outnumber fundamental rights petitions yet remain understudied, with the Court of Appeal serving as the effective final forum in the overwhelming majority of writ cases; that constitutional time mandates are systematically violated while courts without such mandates perform better; that land disputes and state employment matters dominate appellate dockets; and that linguistic patterns confirm hierarchies embedded in judicial practice. These patterns have significant implications for access to justice, legal scholarship, and institutional reform.

## Quantitative Dominance and the Overlooked Court

### The Six-to-One Pattern

![The Court of Appeal issued nearly 6 times as many decisions as the Supreme Court in a given year.](images/num_decisions_per_year.png){#fig:decisions-per-year}

The Court of Appeal issued nearly six times as many judgments as the Supreme Court in a given year. As demonstrated in @fig:decisions-per-year, this pattern holds consistently across the decade under study. The Court of Appeal averaged 665 decisions per year compared to the Supreme Court's 116 decisions. 

This quantitative disparity has structural explanations. The Court of Appeal has a greater number of justices than the Supreme Court. More significantly, it is a court of first instance for writ applications under Article 140, whereas the Supreme Court primarily exercises appellate jurisdiction with the exception of its original jurisdiction under Article 126 (fundamental rights) and Article 129 (election petitions). The Court of Appeal thus handles both original writ petitions and appeals from lower courts across civil, criminal, and administrative matters.

### Implications for Jurisprudential Authority

The numerical dominance of Court of Appeal judgments stands in stark contrast to their doctrinal treatment. Jurisprudentially, decisions of the Court of Appeal are given far less significance than Supreme Court decisions. The Supreme Court is the apex court and therefore determines judicial precedent. Because it is the final court of appeal, its decisions are examined and debated more extensively in legal scholarship and practice. 

This numerical dominance translates into greater practical impact in dispute resolution. Empirical analysis confirms that most disputes are effectively resolved at the Court of Appeal level, with the Supreme Court rarely reviewing writ decisions on appeal. This finding has significant implications: if the Court of Appeal is the practical forum where writ remedies are determined, the doctrinal and normative interpretation of judicial decisions in Sri Lanka should systematically include Court of Appeal jurisprudence rather than focusing predominantly on Supreme Court precedent.

Currently, the Court of Appeal's contribution is understood only in an ad hoc manner by judiciary, practitioners, academics, and other court observers. There was a brief period in which decisions of the Court of Appeal were published as an unofficial court report by a non-government organization, Law & Society Trust.[^48] However, no systematic effort has been made to study Court of Appeal jurisprudence as a body of law with its own patterns and significance. The quantitative data point to the need for such systematic study, particularly given the court's role in both writ jurisdiction and criminal appeals—areas that, as subsequent sections demonstrate, dominate appellate dockets but remain understudied in legal scholarship.

The Court of Appeal's quantitative dominance—and the low rate of appeals to the Supreme Court—raises a further question: what types of cases account for this output? The answer lies in the distribution between writ petitions and fundamental rights petitions, and in the Supreme Court's extremely limited role in reviewing Court of Appeal writ decisions.

## The Writ Puzzle: Pervasive but Understudied

### Jurisdictional Distribution: SC vs CA

The constitutional framework establishes distinct forums for public law remedies. Article 140[@constitution1978] confers on the Court of Appeal jurisdiction to issue prerogative writs—certiorari, mandamus, prohibition, and others—for judicial review of administrative action, tribunal decisions, and jurisdictional errors. Article 126[@constitution1978] vests the Supreme Court with exclusive jurisdiction over fundamental rights petitions alleging constitutional violations. The Supreme Court's original writ jurisdiction, by contrast, is narrowly circumscribed: Article 104H[@constitution1978] limits such jurisdiction to election-related matters.

The empirical distribution confirms this constitutional design. Of the 1,278 Supreme Court decisions in the dataset, only 4 (0.3%) were original writ petitions under Article 104H. The Court of Appeal, by contrast, issued 1,741 writ decisions (23% of its docket) during the same period. In original writ jurisdiction, the Court of Appeal handles 435 times more cases than the Supreme Court. This stark disparity reflects the constitutional allocation of writ jurisdiction to the Court of Appeal as the primary forum for administrative law and judicial review.

### Quantitative Disparity

The disparity between writ petitions and fundamental rights petitions is substantial. Of the 7,314 Court of Appeal decisions in the dataset, 1,741 (23%) were judgments on writs. Of the 1,278 Supreme Court decisions, 361 (28%) were judgments on fundamental rights petitions. While writ petitions substantially outnumber fundamental rights petitions in absolute terms, these remedies are administered by different courts: writs predominantly by the Court of Appeal under Article 140, and fundamental rights exclusively by the Supreme Court under Article 126.

The Supreme Court's engagement with writ jurisdiction is minimal. Of the 1,278 Supreme Court decisions, 4 were original writ petitions under Article 104H (election-related writs) and 31 were appeals from Court of Appeal writ decisions (identified through normalized pattern matching for case references to Court of Appeal writ applications)—together comprising only 2.7% of the Supreme Court's docket. The Court of Appeal's 1,741 writ decisions thus vastly outnumber not only the Supreme Court's original writ jurisdiction but also subsequent appellate review.

The temporal patterns reveal an additional dimension to this disparity. The average time taken for writ decisions in the Court of Appeal was 3.15 years (2.80 SD) against 4.17 years (3.05 SD) for fundamental rights petitions in the Supreme Court. 25% of writs in the Court of Appeal were decided within a year of filing compared to only 20% of fundamental rights petitions in the Supreme Court resolved within one year. This performance is particularly notable given that, unlike fundamental rights petitions, no constitutional or common law time limit exists for writ determinations.

The outcome patterns also differ. Of the decisions on writs in the Court of Appeal that were fully adjudicated, 55% were allowed and 45% were dismissed. In the Supreme Court, 62% of fundamental rights decisions were allowed and 38% were dismissed. After petitions clear the leave to proceed stage in either jurisdiction, the probability favours the petitioner—but fundamental rights petitions show a slightly higher success rate than writs.

### The Court of Appeal as Effective Final Arbiter

The Court of Appeal's dominance in writ jurisdiction extends beyond volume to practical finality. During the period 2012-2022, the Supreme Court decided only 31 appeals from Court of Appeal writ decisions—compared to 1,741 writ decisions issued by the Court of Appeal during the same period, as shown in @tbl:ca-writs-vs-sc-appeals.

: Court of Appeal Writ Decisions vs Supreme Court Appeals (2012-2022) {#tbl:ca-writs-vs-sc-appeals}

| Metric | Value |
| :---- | ----: |
| CA Writ Decisions | 1,741 |
| SC Appeals from CA Writs | 31 |
| **Implied Appeal Rate** | **1.8%** |
| Average SC Appeals per Year | 2.8 |
| Average CA Writs per Year | 158 |

The ratio of SC appeals to CA writ decisions (31:1,741) suggests an appeal rate around 1.8%. This ratio remained consistently low across the decade, with an average of 2.8 appeals annually. While we cannot track individual case cohorts through the appellate system, the low ratio of SC appeals to CA writ decisions indicates that the Court of Appeal functions as the effective final arbiter in the overwhelming majority of writ cases.

This finding answers empirically the question posed earlier: whether the Court of Appeal's numerical dominance translates into greater practical impact in dispute resolution. The data confirm that it does. Based on the relative volumes during this period, for the vast majority of litigants seeking writ remedies, the Court of Appeal is not merely the first forum but the only forum. The Supreme Court's appellate jurisdiction over Court of Appeal writs, while constitutionally available under Articles 127-128[@constitution1978], is rarely invoked in practice.

Three non-exclusive explanations may account for this low ratio. First, litigants may be satisfied with Court of Appeal writ determinations and choose not to pursue further appeal. Second, the Supreme Court's leave requirements for appeals may present a significant barrier, filtering out cases that do not meet the threshold for further review. Third, Court of Appeal writ remedies may effectively resolve the underlying disputes, rendering further litigation unnecessary or impractical. Determining which explanation predominates would require further investigation into leave applications, reasons for grant or refusal of leave, and longitudinal tracking of individual cases from the Court of Appeal through potential Supreme Court appeals.

From an access to justice perspective, these findings have significant implications. The Court of Appeal provides regular, accessible, and functionally final review of administrative action and jurisdictional errors. With an average of 158 writ decisions annually, it serves as the primary mechanism for judicial review in Sri Lanka. The low ratio of Supreme Court appeals suggests that Court of Appeal writ remedies effectively resolve disputes in most cases, making this jurisdiction a more substantial avenue for access to justice than its current doctrinal recognition acknowledges.

### The Doctrinal Paradox

Despite this numerical dominance and practical finality, writ jurisprudence remains underdeveloped in Sri Lankan legal scholarship and practice. Academic study of Sri Lanka's public law focuses predominantly on the fundamental rights jurisprudence of the Supreme Court with little attention paid to writ jurisprudence *qua* writ jurisprudence.[^56] This raises questions about why doctrinal scholarship privileges fundamental rights over writs when writs quantitatively dominate and the Court of Appeal serves as the effective final forum for the overwhelming majority of writ remedies.

The empirical data provide an alternative account to the view that writs and fundamental rights are blending in practice. Fundamental rights petitions remain the exception; writs are the norm. Moreover, these remedies operate in different forums with different rates of finality. The Supreme Court's exclusive fundamental rights jurisdiction under Article 126 makes it the apex court for constitutional violations, but the Court of Appeal's near-exclusive resolution of writ petitions under Article 140 makes it the apex court for administrative law and judicial review. Yet the doctrinal weight afforded to these two jurisdictions inverts their quantitative relationship and obscures their functional separation.

The empirical-doctrinal gap reveals a structural issue in how public law scholarship understands judicial work. Courts adjudicate more writs than fundamental rights petitions, writs resolve more quickly on average, and writ decisions are rarely subject to appellate review—yet legal education, scholarly analysis, and professional discourse privilege fundamental rights jurisprudence. If writs provide more routine access to justice than the constitutionally privileged fundamental rights jurisdiction, their comparative neglect has distributive consequences. As demonstrated in the topic modelling analysis below, writ petitions disproportionately concern state employment disputes and administrative actions affecting public servants. The neglect of writ jurisprudence may thus reflect whose claims receive doctrinal attention and whose claims are treated as routine administrative matters.

The law on writs remains comparatively underdeveloped, and no systematic effort has been made to study writ jurisprudence as a distinct body of doctrine deserving scholarly attention in its own right. The quantitative and qualitative data presented here suggest that such systematic study is overdue—not merely as a complement to fundamental rights scholarship but as a necessary correction to received assumptions about where judicial impact occurs and which remedies structure day-to-day access to justice in Sri Lanka.

The prevalence of writs and their functional finality raise practical questions about judicial performance across both remedies. How long do these cases take to resolve? The Constitution mandates that fundamental rights petitions be resolved within two months, but the empirical reality diverges sharply from this constitutional promise—creating an instructive contrast with writ jurisdiction, which operates without constitutional time mandates yet resolves more quickly.

## Temporal Dysfunction: The Constitutional Time Mandate and Its Failure

As shown in @fig:time-to-decision, 37% of Supreme Court decisions and 48% of Court of Appeal decisions took more than five years to be delivered.

![37% of Supreme Court decisions and 48% of Court of Appeal decisions took more than five years to be delivered.](images/time_to_decision.png){#fig:time-to-decision}

### Methodology Note

The Supreme Court website lists the date on which each decision was issued. The Court of Appeal website, on the other hand, groups decisions by the month and the year and does not list the date. Further, since the registries of both courts are not digitised, for both courts, there is no way of knowing the date on which an application related to a decision was filed. Under these constraints, calculating the exact time taken to deliver decisions is not possible. 

To approximate the date on which an application was filed, we extracted the year in which the application related to a decision was filed from the application (or case) number. For example, the case number SC/FR/123/2012 indicates that the application was filed in 2012. Assuming that filing of applications is distributed uniformly through the year, we approximated the date of filing as {extracted\_year}-June-30 for all cases across the two courts. Making the same assumption, we approximated the date of decision delivery in the Court of Appeal as {given\_year}-{given\_month}-15. We then calculated the time taken to deliver a decision as the difference between the date of decision delivery and the date of application filing.

### Supreme Court Fundamental Rights: The Two-Month Fiction

The Constitution mandates that fundamental rights petitions be determined within two months of filing (Article 126(5)).[^note_art126_2] However, the Supreme Court has held that this requirement is directory rather than mandatory.[^54] 

As illustrated in @fig:fr-delay-distribution, the data confirm serious concerns about delays in the court system.

![37% of FR petitions took five or more years for resolution](images/image_no_6_fr_delay_distribution.png){#fig:fr-delay-distribution}

Of the 361 fundamental rights petitions in the dataset, 332 took 3 to 15 years for resolution. Of these, 140—almost half—took 10 to 15 years to be concluded. Around 37% of fundamental rights petitions took five or more years for resolution. Only 20% resolved within one year of filing. The mean time taken was 4.17 years (3.05 standard deviation)—a substantial variation from the constitutional requirement of two months.

Two months is insufficient to accommodate the practical steps involved in fundamental rights litigation, which includes filing, service, objections, counter-affidavits, reply, oral submissions, and judgment writing.

The reasons for these delays require further investigation. Contributing factors may include caseload, absence of strict time allocation for oral submissions, postponements sought by parties, and the time required to write judgments.


### Court of Appeal Writs: Faster Despite No Mandate

As demonstrated in @fig:fr-vs-writ-delay, Court of Appeal writ petitions resolve faster than Supreme Court fundamental rights applications.

![Court of Appeal writs petitions resolve faster than Supreme Court FR applications](images/image_no_8_sc_fr_vs_ca_writ_delay_distribution.png){#fig:fr-vs-writ-delay}

Unlike fundamental rights petitions, no constitutional or common law time limit governs writ determinations. Time or delay is considered when determining whether to grant leave to proceed,[^55] but no broader principles guide completion of writ petitions.

The Court of Appeal's experience provides an instructive comparison. Of the 7314 Court of Appeal decisions, 1741 (23%) were judgments on writs. Writ decisions took considerably less time to resolve than other matters in the same court. The average time taken for writ decisions was 3.15 years (2.80 SD) against 8.01 years (6.43 SD) for other matters. 25% of writs were decided within a year of filing.

The Court of Appeal thus resolves writs faster (mean 3.15 years) than the Supreme Court resolves fundamental rights petitions (mean 4.17 years), despite having no constitutional time mandate. The practical procedures are comparable in both jurisdictions, yet the court without a stipulated time limit performs better.

### Implications for Access to Justice

As per recent reports, 5,785 cases are pending before the Supreme Court and 4,572 before the Court of Appeal.[@srilankamirror2024pending] The figures are worse in lower courts: 27,324 cases pending before High Courts and 262,665 before District Courts.[@srilankamirror2024pending] The total number of cases pending is 1,131,818.[@srilankamirror2024pending]

The time taken to determine fundamental rights petitions fundamentally undermines the constitutional mandate. As demonstrated above, over a third of cases took five or more years for resolution—against a constitutional requirement of two months. These findings clarify the quality of access to justice available to petitioners who approach the appellate courts.

This comparative puzzle raises questions about structural causes: backlog, judicial resources, and procedural culture. Why does the Court of Appeal, handling a larger volume of cases, resolve writs faster than the Supreme Court resolves fundamental rights petitions? The answer likely lies in a combination of factors including case complexity, the nature of constitutional adjudication, and institutional practices—but these require further investigation.

The systematic delays demand investigation and institutional responses tailored to the types of cases that dominate the dockets. The constitutional time mandate for fundamental rights is meaningless in practice, while the court without such a mandate performs better. This inversion suggests that formal rules matter less than institutional capacity, resource allocation, and procedural culture.

The timing data reveal how long disputes take to resolve but not what those disputes are about. Topic modeling provides an answer.

## Substantive Concentration: What the Courts Actually Decide

### Computational Method: Topic Modeling

To understand the latent topics and their word distributions present in court decisions, we applied Latent Dirichlet Allocation (LDA)[^note_lda_methodology] to CDTextLK. We used the Gensim implementation of LDA with the following parameters: 20 topics and random seed of 0 with all other values set to defaults. In addition to tokenizing and stemming, we removed all tokens that appeared in less than 20 documents as well as tokens that recurred in more than 50% of documents. We also removed all tokens that were less than 3 characters long.

To find the three most common topics across Supreme Court and Court of Appeal decisions, we first ran LDA on the entirety of CDTextLK under the experiment conditions described above. Then, we computed the average probability score for each of the 20 topics identified by LDA under the two sub corpora, independently, by summing the document-topic probability for a given topic for each document in the sub corpus and dividing by the total number of documents in the sub corpus. We obtained the three most common topics by summing the average probability scores for each topic across the two sub corpora and selecting the three topics with the highest scores, as shown in @tbl:topic-modeling-top3.

: Top-3 Topics with Highest Average Probability and Top-40 Tokens {#tbl:topic-modeling-top3}

| Topic 1 | Topic 2 | Topic 3 |
| :---- | :---- | :---- |
| defend | decis | accus |
| plaintiff | writ | sentenc |
| land | mark | trial |
| district | offic | wit |
| action | servic | high |
| titl | public | polic |
| deed | board | prosecut |
| possess | author | convict |
| trial | letter | offenc |
| lot | appoint | year |
| claim | univers | charg |
| plan | commiss | statement |
| partit | certiorari | incid |
| plaint | mandamu | victim |
| mark | secretari | code |
| owner | circular | defenc |
| share | member | offic |
| prescript | inquiri | imprison |
| substitut | post | commit |
| road | administr | hous |
| decre | committe | impos |
| corpu | director | ground |
| silva | quash | inform |
| right | ministri | crimin |
| properti | document | count |
| answer | requir | consid |
| entitl | year | indict |
| schedul | natur | call |
| disput | depart | complain |
| prove | power | day |
| perera | minist | find |
| enter | petit | doubt |
| transfer | promot | punish |
| origin | approv | deceas |
| posit | observ | place |
| deceas | recommend | found |
| proceed | council | arrest |
| surveyor | duti | penal |
| year | regul | examin |
| procedur | examin | prove |

### Topic 1: Land and Property Disputes

Topic 1 concerns land and property disputes, denoted by terms such as 'defend', 'plaintiff', 'land', 'district', 'action', 'titl', 'deed', 'possess', 'lot', 'claim', 'plan', 'partit', 'owner', 'prescript', 'road', 'silva', 'properti', 'disput', 'perera', 'transfer', 'surveyor', and 'procedur'. These terms reflect the vocabulary of land litigation—title disputes, prescriptive rights, partition actions, and ownership claims.

When we ran LDA on decisions that took ten or more years for resolution (num\_topics=5 and random\_seed=0), the most common topic was land and property disputes. Given that 81% of land in Sri Lanka is state-owned, the state's role as dominant landowner generates extensive litigation over state land alienation, encroachment, competing claims, and administrative decisions regarding land use and allocation.

In terms of addressing case load and delay, this data points to land disputes as an area requiring substantive attention and institutional infrastructure. Current state interventions regarding delays—such as fast-tracking commercial disputes and promoting alternative dispute resolution—may be misplaced if they do not address the types of cases that actually dominate appellate court dockets. If land disputes are both pervasive and slow-moving, institutional reform must target this specific substantive area. This might include specialized tribunals, streamlined procedures for particular categories of land disputes, or administrative reforms to reduce the generation of land-related litigation in the first instance.

### Topic 2: State Employment and Administrative Disputes

Topic 2 captures state employment and administrative disputes, denoted by terms such as 'decis', 'writ', 'mark', 'offic', 'servic', 'public', 'board', 'author', 'letter', 'appoint', 'univers', 'commiss', 'certiorari', 'mandamu', 'secretari', 'circular', 'member', 'inquiri', 'post', 'administr', 'committe', 'director', 'quash', 'ministri', 'document', 'depart', 'minist', 'promot', 'approv', 'recommend', and 'council'. This vocabulary reflects administrative law and public sector employment disputes—appointments, promotions, transfers, disciplinary inquiries, administrative circulars, and challenges to decisions by public boards, commissions, and ministries.

The dominance of state employment disputes, particularly visible in fundamental rights petitions, suggests that the public sector places substantial burden on the court system. This finding tracks with earlier empirical work showing that Article 12 (equality) is overwhelmingly invoked by public servants challenging recruitments, transfers, or promotions. Public servants constitute a significant proportion of litigants before the appellate courts, using both writ jurisdiction and fundamental rights jurisdiction to challenge administrative decisions affecting their employment.

This pattern raises questions about administrative and quasi-judicial mechanisms. Are they functioning effectively, or do courts primarily provide access to justice for public servants rather than the broader public? If administrative tribunals, Public Service Commission procedures, and departmental appeal mechanisms were functioning effectively, fewer employment disputes would reach the appellate courts. The prevalence of such cases in the appellate dockets suggests either that administrative mechanisms are inadequate or that they are systematically bypassed in favor of judicial review. This has distributional consequences: if courts spend substantial time adjudicating public sector employment disputes, other types of claims—particularly those brought by marginalized communities or private citizens without institutional resources—may receive less attention.

### Topic 3: Criminal Proceedings

Topic 3 covers criminal proceedings, denoted by terms such as 'accus', 'sentenc', 'trial', 'wit', 'high', 'polic', 'prosecut', 'convict', 'offenc', 'charg', 'statement', 'incid', 'victim', 'code', 'defenc', 'imprison', 'commit', 'hous', 'impos', 'ground', 'inform', 'crimin', 'count', 'indict', 'complain', 'find', 'punish', 'deceas', 'place', 'found', 'arrest', 'penal', and 'examin'. This is the vocabulary of criminal appeals—charges, indictments, convictions, sentences, witnesses, evidence, and grounds of appeal.

The dominance of criminal proceedings as one of the three major topics reflects the Court of Appeal's role in hearing criminal appeals. This finding is unsurprising given the jurisdictional structure, but it confirms empirically what is known doctrinally: criminal appeals constitute a substantial portion of the Court of Appeal's workload.

### Topic Distribution Analysis

A study of non-intersecting top 10 topics between the two sub corpora corroborates what we know about the structure of the legal system in the country. For instance, while appeals on criminal matters are heard by the Court of Appeal, appeals on civil matters, following the institution of the Civil Appeal High Court, are no longer heard by the Court of Appeal. The fifth and sixth most common topics in the Court of Appeal decisions—denoted by terms such as 'vehicl', 'owner', 'offenc', 'confisc', 'charg', 'forest', 'websit', 'accus', 'polic', 'regist', 'transport', 'station', 'driver', 'prove', 'timber', 'illeg', 'deceas', 'murder', 'injuri', and 'stab'—do not appear in the top 10 topics in the Supreme Court decisions. These terms reflect specific categories of criminal appeals (vehicle offences, forest offences, violent crimes) that fall within the Court of Appeal's jurisdiction.

Similarly, disputes between central government and administrative powers such as provincial councils and pradeshya sabhas are heard by the Supreme Court. The ninth most common topic in the Supreme Court decisions—denoted by terms such as 'council', 'member', 'writ', 'elect', 'sabha', 'provinci', 'pradeshiya', 'constitut', 'articl', 'power', 'minist', 'chairman', 'local', 'presid', 'governor', 'uva', 'appoint', and 'central'—does not appear in the top 10 topics in the Court of Appeal decisions. This topic captures the Supreme Court's constitutional jurisdiction over disputes involving provincial councils, local government bodies, and the distribution of powers between central and provincial authorities.

The topic distribution analysis thus confirms empirically the jurisdictional divide between the two courts and reveals the substantive areas that dominate their respective dockets. Land disputes, state employment disputes, and criminal appeals constitute the bread and butter of appellate adjudication in Sri Lanka—yet these areas receive far less scholarly and policy attention than high-profile constitutional cases.

Topic modeling reveals what courts decide. Mutual information analysis reveals how courts write—and what those linguistic choices encode about institutional hierarchies and judicial authority.

## Linguistic Patterns: What Mutual Information Reveals

### Method and Salient Terms

We performed mutual information analysis on the Supreme Court and Court of Appeal decisions to identify the most salient words in each corpus. Mutual information analysis quantifies the presence or absence of words within a corpus. The frequency of the words used can reveal attributes of the jurisprudence of both courts, providing helpful entry points for further jurisprudential analysis. We tokenized decisions and stemmed each token. We used a simple add 1 smoothing scheme to avoid zero probabilities.

### Interpreting Linguistic Choices

The most salient word was 'grant', which appeared in 91% of Supreme Court decisions but only in 32% of Court of Appeal decisions. The underlying reason is procedural: Supreme Court decisions routinely reference the granting of leave to appeal—both the grounds on which leave was granted and the date—in the decision text. This reflects a procedural practice rather than a substantive legal distinction but nonetheless marks a clear linguistic difference between the two courts.

The words 'answer', 'question', and 'law' appear frequently in Supreme Court decisions because the court is called upon to answer questions of law. Although the Court of Appeal is also an appellate court, the same words have a lower prevalence in its decisions. This linguistic pattern reflects the Supreme Court's role as the final court of appeal on questions of law and its function in establishing legal precedent through reasoned answers to legal questions.

The word 'err' appears in 24% of Supreme Court decisions but only in 1% of Court of Appeal decisions. On closer inspection, we observed that the word appears in the context of Supreme Court justices holding a lower court judge to have erred in their judgement. Such language is almost never used in Court of Appeal decisions despite the court's appellate jurisdiction. This is a striking finding. Both courts exercise appellate jurisdiction and review decisions of lower tribunals. Yet the Supreme Court routinely employs the language of error—stating explicitly that a judge erred—while the Court of Appeal rarely does so. This may reflect the Supreme Court's hierarchical position at the apex of the judicial system, where it exercises supervisory authority not only over outcomes but over legal reasoning itself. The Court of Appeal, positioned between the High Courts and the Supreme Court, may adopt a less overtly corrective tone even when reversing lower court decisions.

The high prevalence of the words 'paragraph' and 'refer' in Supreme Court decisions arises from the court's practice of referring to specific sections of petitions, the Constitution, and other legislation. This reflects a more formal writing style in the Supreme Court compared to the Court of Appeal. Supreme Court decisions are more citation-heavy, more explicitly structured, and more systematically organized through numbered paragraphs and cross-references. This linguistic formality aligns with the court's institutional role as the authoritative interpreter of law and the generator of binding precedent.

These linguistic patterns reflect hierarchical position and institutional culture. The Supreme Court writes as the apex court—correcting error, answering questions of law, formally citing and cross-referencing legal materials. The Court of Appeal, despite its substantial caseload and significant role in dispute resolution, writes in a less formally structured style that reflects its intermediate position in the judicial hierarchy. Linguistic choices are not merely stylistic; they encode institutional roles, hierarchical relationships, and conceptions of judicial authority.

Linguistic patterns reveal how courts write, but volume patterns reveal when and how much they produce. The Supreme Court's output varied significantly across the decade under review, with notable peaks and troughs that correlate with constitutional developments affecting judicial independence.

## Variations in Supreme Court Output: Independence and Productivity

### The 2016-2017 Peak and the Low Years

The Supreme Court's output varied substantially across the decade. The court delivered 175 decisions in 2016 and 203 in 2017—the two highest annual totals in the period. Between 2012-2015, the court averaged 68 decisions per year. Between 2016-2022, it averaged 144 decisions per year, as shown in @fig:sc-output-variation.

![Supreme Court and Court of Appeal decision output 2012-2022](images/num_decisions_per_year.png){#fig:sc-output-variation}

### The Independence Hypothesis

This pattern suggests a correlation between judicial output and actual as well as perceived independence. The constitutional developments of this period may have impacted the court's work. The dramatic increase in Supreme Court output following 2015 coincides with constitutional reforms aimed at enhancing judicial independence, particularly the 19th Amendment which restored the Constitutional Council and reformed the process for judicial appointments. 

The relationship between judicial independence and judicial productivity is complex. Enhanced independence may increase a court's willingness to hear cases, may improve litigant confidence in seeking relief, or may reflect institutional changes that increase court capacity. Conversely, periods of judicial crisis or perceived lack of independence may depress both filing rates and adjudication rates. The 2013-2015 period, marked by the purported impeachment of the Chief Justice and broader concerns about judicial independence under the 18th Amendment, saw depressed output. The post-2015 period, marked by constitutional reforms enhancing independence, saw dramatic increases in output.

However, correlation does not establish causation, and this requires further investigation beyond the current data. Multiple factors influence judicial output including the number of justices, case filing rates, procedural reforms, administrative efficiency, and judicial attitudes. The constitutional developments of this period provide one plausible explanation for the observed patterns, but a fuller account would require analysis of additional variables including appointment patterns, case filing statistics, and institutional resources.

### Court of Appeal: Different Pattern

The Court of Appeal does not exhibit a comparable trend. Its best performing year was 2013, when the court delivered 1109 decisions. The high output in 2013 may reflect litigants having more confidence in the Court of Appeal than the Supreme Court during the purported impeachment. If litigants perceived the Supreme Court as compromised during the judicial crisis but viewed the Court of Appeal as relatively insulated, they may have filed more cases in the Court of Appeal or pursued remedies there rather than appealing to the Supreme Court. This would explain why the Court of Appeal's output peaked precisely when the Supreme Court's output was depressed.

Overall, in the period under review, the Court of Appeal averaged 665 decisions per year compared to the Supreme Court's 116 decisions. The Court of Appeal has consistently delivered more judgments than the Supreme Court throughout the decade, suggesting a different institutional dynamic less sensitive to constitutional crises or reforms affecting the apex court, as illustrated in @fig:ca-output-variation.

![Court of Appeal decision output showing 2013 peak](images/num_decisions_per_year.png){#fig:ca-output-variation}

Variation in output reveals institutional responsiveness to political and constitutional context. Decision length, by contrast, reveals something different: the doctrinal weight courts assign to different types of disputes. Fundamental rights cases receive significantly more extensive judicial treatment than writs, empirically confirming doctrinal hierarchies.

## Decision Length: Doctrinal Weight Made Visible

### Quantitative Patterns

We tokenized decisions using the regex pattern \[A-Za-z\]+, discounting all punctuation and numbers. The mean length of a Supreme Court decision is 3646 tokens (3038 SD) and that of a Court of Appeal decision is 1688 tokens (2091 SD). Although Supreme Court decisions are, on average, longer, the longest decision in the corpus was a Court of Appeal decision. This judgment on an appeal of a determination by the Tax Appeal Commission against Unilever Sri Lanka Limited (CA/TAX/04/2013) is 35,630 tokens long. The longest Supreme Court decision, at 29,620 tokens, was on the fundamental rights petition SC/FR/141/2015 filed by Centre for Environment and Nature Studies against Northern Power Company (Pvt) Ltd which operated a thermal power plant in Chunnakam, Jaffna and was accused of contaminating the village's groundwater.

### Judgment Length by Court and Case Type

Judgment length varies systematically across courts and case types. Supreme Court decisions are, on average, substantially longer than those of the Court of Appeal, and exhibit greater dispersion in length, as shown in @fig:length-of-decision. Across all Supreme Court cases, the median judgment length is 2,856 words, with a mean of 3,646 words and a standard deviation of 3,038 words, indicating a strongly right-skewed distribution. Court of Appeal decisions are markedly shorter, with a median length of 1,184 words, a mean of 1,688 words, and a lower standard deviation of 2,091 words, suggesting more constrained variation in judicial writing.


![Supreme Court judgments are, on average, longer than Court of Appeal ones](images/length_of_decision.png){#fig:length-of-decision}


These structural differences persist within the principal public law jurisdictions of each court. Fundamental Rights (FR) judgments of the Supreme Court are longer than the Court's overall baseline, with a median length of 3,022 words, a mean of 3,805 words, and a standard deviation of 3,157 words, reflecting both doctrinal density and substantial variation in judicial treatment. Court of Appeal writ decisions are marginally longer than the Court of Appeal average (median 1,303; mean 1,836), but remain comparatively concise and less dispersed (standard deviation 1,970). Over time, average judgment length has increased in both courts, with the most pronounced growth observed in Supreme Court Fundamental Rights cases, as illustrated in @fig:avg-words-by-type.


![Average judgment length increased over time across courts and jurisdiction](images/image_no_11_avg_words_by_decision_type.png){#fig:avg-words-by-type}


### Interpretation

There are no apparent formal guidelines or standards governing the length of judicial decisions, and length itself should not be confused with quality. The persuasiveness and authority of a judgment depend on accurate identification of material facts, engagement with relevant precedent, and coherent application of law to fact. Nonetheless, the increasing length of judgments—particularly in the Supreme Court—does reflect a growing volume of judicial labour, including more extensive factual narration, doctrinal exposition, and engagement with comparative or constitutional reasoning.

More importantly, variation in judgment length mirrors entrenched doctrinal hierarchies within Sri Lanka’s public law system. Fundamental Rights petitions, though fewer in number than writ applications, receive significantly more extensive judicial treatment, underscoring their elevated constitutional status. Similarly, Supreme Court decisions consistently exhibit greater length and variability than those of the Court of Appeal. The empirical patterns thus reinforce doctrinal expectations: constitutional adjudication commands deeper and more discursive reasoning than administrative review, and apex court judgments function as primary sites of legal exposition and norm-setting. Together with earlier findings on caseload composition, temporal delay, and output variation, judgment length provides a further window into how institutional role, jurisdiction, and doctrinal priority shape judicial practice.[^56]

The patterns identified thus far—quantitative dominance, writ prevalence, temporal dysfunction, substantive concentration, linguistic hierarchies, output variations, and decision length—describe how courts work. Outcome data provide a final empirical lens: how often do courts dismiss versus allow petitions?

## Outcomes: Dismissals and Allowances

*Proportion of decisions dismissed vs. allowed.*

### Data Limitations

Dismissal, in this section, means dismissal after a full hearing. Writs and fundamental rights petitions proceed in two stages: an initial leave determination followed by a full hearing if leave is granted. CDTextLK does not include data on dismissals at the leave stage, as these are typically not recorded as written judgments. The actual dismissal rates are therefore higher than the data suggests. For a fuller discussion of dataset scope and coverage limitations, see [Section 5](#sec:limitations).

### Observed Patterns

: Proportion of Decisions Dismissed vs Allowed {#tbl:outcomes}

|  | Dismissed | Allowed |
| :---- | :---- | :---- |
| Supreme Court | 532 (41.63%) | 746 (58.37%) |
| Court of Appeal | 3651 (49.92%) | 3663 (50.08%) |

In @tbl:outcomes, we can observe that about half of the decisions in the Court of Appeal dismissed their petitions or appeals. In the Supreme Court, however, the majority of decisions (58%) allowed the petition or appeal to stand. Of the decisions on writs in the Court of Appeal, 55% were allowed and 45% were dismissed. In the Supreme Court, 62% of the decisions on fundamental rights petitions were allowed and 38% were dismissed.

Figure: total number of FR judgments in favour of petitioners and dismissed; total number of writs in SC in favour of petitioner or dismissed, total number of writs in CA in favour of petitioner or dismissed

### Interpretation

Whether a petition is upheld or dismissed depends on multiple factors: the strength of the petitioner's claim, the applicable legal or constitutional doctrine, the quality of submissions, and the exercise of judicial discretion. Outcomes cannot be predicted based solely on empirical patterns. 

While this data does not directly reveal jurisprudential trends, perceptions abound about judicial attitudes toward petitions—whether courts are prone to dismiss or allow claims. Empirical methods can be used to test these perceptions. The observed patterns suggest rough parity: neither court is systematically biased toward dismissal or allowance. The Court of Appeal maintains near parity (50% allowed versus 49% dismissed), while the Supreme Court shows only a slight tendency to allow petitions.

After petitions clear the leave to proceed stage, the probability favors the petitioner. This suggests that the leave stage functions as a significant filter: petitions that survive this threshold have reasonable prospects of success. The slightly higher success rate for fundamental rights petitions (62%) compared to Court of Appeal writs (55%) may reflect either the nature of constitutional claims or the additional scrutiny applied at the leave stage in fundamental rights jurisdiction.

These findings—quantitative dominance, writ prevalence, temporal dysfunction, substantive concentration, linguistic patterns, output variations, decision length, and outcome distributions—collectively reveal patterns that challenge received assumptions about appellate jurisprudence in Sri Lanka. What do these patterns mean for legal scholarship and judicial reform?

## Synthesis: Implications for Legal Scholarship and Reform

### Six Core Insights

The empirical analysis of CDTextLK reveals patterns that challenge received assumptions about the work of Sri Lanka's appellate courts. These findings expose the gap between doctrinal debates and the empirical realities of judicial practice.

**1. Quantitative versus doctrinal significance.** The Court of Appeal numerically dominates—issuing nearly six times as many judgments as the Supreme Court—yet remains jurisprudentially neglected. This quantitative contribution is understood only in an ad hoc manner by judiciary, practitioners, academics, and court observers.

**2. The writ-fundamental rights gap.** Writ petitions vastly outnumber fundamental rights petitions in both courts, yet writ jurisprudence remains understudied. Fundamental rights petitions are the exception; writs are the norm. This empirical pattern suggests that academic study of Sri Lanka's public law, which focuses predominantly on fundamental rights jurisprudence, overlooks the more common exercise of writ jurisdiction. The data provide an alternative account to the view that writs and fundamental rights are blending in practice.

**3. Temporal dysfunction.** The constitutional mandate for fundamental rights determination within two months is systematically violated. 37% of fundamental rights petitions took five or more years for resolution, with a mean time of 4.17 years. Only 20% resolved within one year of filing. Yet the Court of Appeal resolves writs faster (mean 3.15 years) despite having no constitutional time limit. This inversion suggests that formal rules matter less than institutional capacity, resource allocation, and procedural culture. The structural causes remain unknown and demand investigation.

**4. Land and employment concentration.** Topic modeling identifies land disputes and state employment disputes as dominant themes. Given that 81% of land in Sri Lanka is state-owned, the state's role as landowner and employer dominates appellate dockets. Reform must address these areas specifically. Current interventions—fast-tracking commercial disputes, promoting alternative dispute resolution—may be misplaced if they do not address the types of cases that actually dominate the courts.

**5. Linguistic and length patterns confirm hierarchies.** Mutual information analysis and decision length data empirically confirm doctrinal hierarchies embedded in judicial practice. The Supreme Court writes as the apex court—correcting error, answering questions of law, formally citing legal materials. Fundamental rights judgments are longer than writ judgments. These patterns reflect institutional roles and doctrinal weight, but they also reveal what receives attention and what does not.

**6. Independence and output.** Supreme Court productivity increased following constitutional reforms enhancing judicial independence (19th Amendment). The 2013-2015 period, marked by judicial crisis, saw depressed output. The post-2015 period saw substantial increases. The Court of Appeal's output, by contrast, peaked in 2013 during the impeachment crisis, suggesting litigants had more confidence in the intermediate court. While correlation does not establish causation, the suggestive relationship between independence and output warrants further study.

### Methodological Contribution

Computational methods make visible patterns obscured by the landmark case focus that dominates legal scholarship and professional discourse. CDTextLK enables systematic study of appellate jurisprudence that was previously impossible. By analyzing the entirety of decisions issued over a decade rather than selecting landmark cases, this approach reveals what courts actually do—not just what they say in celebrated constitutional moments.


Topic modeling identifies the substantive areas that dominate dockets. Mutual information analysis reveals linguistic patterns that encode institutional hierarchies. Quantitative analysis of decision volumes, timing, length, and outcomes provides empirical grounding for claims about judicial work, independence, and access to justice. These methods do not replace doctrinal analysis but complement it by revealing the empirical realities within which doctrine operates.

The findings are preliminary but sufficient to challenge received assumptions and warrant attention in reform debates. Further research should investigate: (1) the relationship between Court of Appeal decisions and Supreme Court appeals to determine how many disputes are effectively resolved at the intermediate level; (2) the causes of systematic delays, including case complexity, judicial resources, and procedural practices; (3) the outcomes of land disputes and state employment disputes in greater detail; and (4) the relationship between constitutional developments, judicial independence, and court productivity across a longer time horizon.

### What This Means for Access to Justice

These findings have direct implications for debates about judicial reform and access to justice in Sri Lanka. First, the quantitative dominance of the Court of Appeal challenges persistent policy assumptions that treat the Supreme Court as the primary appellate institution requiring investment and reform. If meaningful access to justice for the majority of litigants depends on the Court of Appeal, reform conversations must reorient accordingly.

Second, the prevalence and understudied nature of writ jurisprudence suggests a fundamental misalignment between scholarly attention and the disputes that dominate dockets. Extraordinary writs are not exceptional or peripheral—they are the mechanism through which ordinary disputes about land, employment, and state administration are adjudicated. Understanding writ jurisprudence is essential to understanding access to justice in practice.

Third, systematic delays undermine the rule of law regardless of ultimate outcomes. Two months is fiction. The gap between procedural promise and empirical reality imposes costs on litigants—costs that fall disproportionately on those with fewer resources to sustain protracted litigation. Addressing delays requires confronting institutional capacity, case management practices, and procedural realities that quantitative analysis makes visible.

Finally, substantive concentration in land disputes and state employment cases reveals that appellate courts function primarily as forums for resolving disputes with the state or its instrumentalities. This pattern raises questions about the accessibility and effectiveness of lower courts for resolving such disputes and the role of appellate courts in managing state-citizen relations. Whether this concentration represents institutional design, litigation incentives, or systemic dysfunction warrants further investigation.

CDTextLK does not resolve these questions, but it provides an empirical foundation for engaging them. The patterns identified here—quantitative dominance, temporal dysfunction, substantive concentration—are not speculative. They are measurable features of appellate jurisprudence that demand explanation and, where warranted, reform.

[^note_lda_methodology]: [@blei2003latent]

[^note_art126_2]: Art 126

