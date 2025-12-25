## Patterns Beyond Precedent  

The empirical analysis of SriLankaCourtDecisions reveals patterns that challenge received assumptions about the nature and distribution of judicial work in Sri Lanka’s appellate courts. These insights emerge from both descriptive statistics—the volume, timing, and length of decisions—and computational methods including topic modelling and mutual information analysis. Together, they expand the landmark case-focused understanding of judicial work by making visible the patterns that structure day-to-day judicial practice. These insights therefore broaden, deepen, and complicate our understanding of the jurisprudence on fundamental rights and writs, and of the work of the courts more broadly.

**5.1. Six-to-one: Greater numerical output by the Court of Appeal**

![The Court of Appeal issued nearly 6 times as many judgments as the Supreme Court in a given year.][image1]

*Figure 1: The Court of Appeal issued nearly 6 times as many judgments as the Supreme Court in a given year.*

The Court of Appeal issued nearly six times as many judgments as the Supreme Court in a given year. As demonstrated in Figure 1, this pattern holds consistently across the decade under study. The Court of Appeal averaged 665 decisions per year compared to the Supreme Court’s 116 decisions.

The numerical difference between writ petitions and fundamental rights petitions is substantial. Of the 7,314 Court of Appeal decisions in the dataset, 1,741 (23%) were judgments on writs. Of the 1,278 Supreme Court decisions, 361 (28%) were judgments on fundamental rights petitions. Judgments on writs are far greater in number than judgments on fundamental rights. While writ petitions substantially outnumber fundamental rights petitions in absolute terms, we note that these remedies are administered by different courts under different procedural rules: writs predominantly by the Court of Appeal under Article 140, and fundamental rights exclusively by the Supreme Court under Article 126\.

The Supreme Court’s engagement under its writ jurisdiction has been minimal during the period under review. Of the 1,278 Supreme Court decisions, 4 were original writ petitions under Article 104H (election-related writs) and 31 were appeals from Court of Appeal writ decisions (identified through normalized pattern matching for case references to Court of Appeal writ applications)—together comprising only 2.7% of the Supreme Court’s docket. The Court of Appeal’s 1,741 writ decisions thus vastly outnumber not only the Supreme Court’s original writ jurisdiction but also subsequent appellate review.

This pattern has structural explanations. The Court of Appeal has a greater number of justices than the Supreme Court.[^note_court_composition] More significantly, it is a court of first instance for writ applications under Article 140 and Article 141, whereas the Supreme Court exercises appellate jurisdiction with the exception of its original jurisdiction under Article 126 (fundamental rights) and Article 129 (election petitions) and some other matters.[^note_art118_ref] The Court of Appeal thus handles both original writ petitions and appeals from lower courts across civil, criminal, and administrative matters. Moreover, benches in the Court of Appeal comprise two justices each whereas benches in the Supreme Court comprise three. Upon request and at the discretion of the Chief Justice, bigger benches may be constituted for the Supreme Court. As a result, it may take longer for benches of the Supreme Court to finalise judgements. The Supreme Court determines questions of law and arguably therefore, the task of judicial decision-making requires more time. 

**5.2. Court of Appeal as the (Effectively) Final Arbiter on Writs**

The Court of Appeal’s dominance in writ jurisdiction extends beyond volume to practical finality. During the period 2012-2022, the Supreme Court decided only 31 appeals from Court of Appeal writ decisions—compared to 1,741 writ decisions issued by the Court of Appeal during the same period, as shown in Table 2\.

*Table 2: Court of Appeal Writ Decisions vs Supreme Court Appeals (2012-2022)*

| Metric | Value |
| :---- | ----: |
| CA Writ Decisions | 1,741 |
| SC Appeals from CA Writs | 31 |
| **Implied Appeal Rate** | **1.8%** |
| Average SC Appeals per Year | 2.8 |
| Average CA Writs per Year | 158 |

The ratio of SC appeals to CA writ decisions (31:1,741) suggests an appeal rate around 1.8%. This ratio remained consistently low across the decade, with an average of 2.8 appeals annually. While we cannot track individual case cohorts through the appellate system, due to gaps in the digitisation of case records, the low ratio of SC appeals to CA writ decisions indicates that the Court of Appeal functions as the effective final arbiter in the overwhelming majority of writ cases.

The numerical dominance of the Court of Appeal translates into greater practical impact in dispute resolution. Based on the relative volumes during this period, for the vast majority of litigants seeking writ remedies, the Court of Appeal is not merely the first forum but the only forum too. The data suggest that the Supreme Court’s appellate jurisdiction over Court of Appeal writs, while constitutionally available under Articles 127-128, is rarely invoked in practice.

Three non-exclusive explanations may account for this low ratio. First, litigants may be satisfied with Court of Appeal writ determinations and choose not to pursue further appeal. Second, the Supreme Court’s leave requirements for appeals may present a significant barrier, filtering out cases that do not meet the threshold for further review. Third, Court of Appeal writ remedies may effectively resolve the underlying disputes, rendering further litigation unnecessary or impractical. Determining which explanation predominates would require further investigation into leave applications, reasons for grant or refusal of leave, and longitudinal tracking of individual cases from the Court of Appeal through potential Supreme Court appeals. Interviews with litigants, practitioners, and justices would further reveal the reasons for this implied appeal rate.

**5.3. Patterns in the number of judgements within each court and between the two courts**

Overall, in the period under review, the Court of Appeal averaged 665 decisions per year compared to the Supreme Court’s 116 decisions. The Court of Appeal has consistently delivered more judgments than the Supreme Court throughout the decade. The Supreme Court’s output varied substantially across the decade. The court delivered 175 decisions in 2016 and 203 in 2017—the two highest annual totals in the period. Between 2012-2015, the court averaged 68 decisions per year. Between 2016-2022, it averaged 144 decisions per year, as shown in Figure 2\.

![Supreme Court and Court of Appeal decision output 2012-2022][image1]

*Figure 2: Supreme Court and Court of Appeal decision output 2012-2022*

We noticed that the variation in the number of judgements in the Court of Appeal ranged from a low of (…) in 2015 to a high of 1109 in 2013\. In the Supreme Court, the lowest number of judgements was issued in 2013 (…) and the highest number of judgements was issued in 2017 (…). Broadly speaking an inverse relationship is observable between the two courts and the increase/decrease in the number of judgements. When the number of judgements issued by the Court of Appeal increases, a decrease can be noticed in the Supreme Court. Identifying reasons for this pattern will be difficult, particularly because the data only includes the judgements that have been issued, not the number of petitions that have been filed. 

The increase in Supreme Court output following 2015 coincides with constitutional reforms aimed at enhancing judicial independence, particularly the enactment of 19th Amendment which restored the Constitutional Council and thereby also reformed the process for judicial appointments.

The relationship between judicial independence and judicial productivity, if any, is difficult to study. Enhanced independence may increase a court’s willingness to hear cases, may improve litigant confidence in seeking relief, or may reflect institutional changes that increase court capacity. Conversely, periods of judicial crisis or perceived lack of independence may depress both filing rates and adjudication rates. In this dataset, the 2013-2015 period, marked by the purported impeachment of the Chief Justice and broader concerns about judicial independence under the 18th Amendment, saw depressed output. The post-2015 period, marked by constitutional reforms enhancing independence, saw dramatic increases in output.

However, correlation does not establish causation. This pattern therefore requires further investigation beyond the current data. Multiple factors influence judicial output including the number of justices, case filing rates, procedural reforms, administrative efficiency, and judicial attitudes. The constitutional developments of this period provide one plausible explanation for the observed patterns, but a fuller account would require analysis of additional variables including appointment patterns, case filing statistics, and institutional resources. 

**5.4. Less time before Court of Appeal than before the Supreme Court**

![37% of Supreme Court decisions and 48% of Court of Appeal decisions took more than five years to be delivered.][image2]

*Figure 3: 37% of Supreme Court decisions and 48% of Court of Appeal decisions took more than five years to be delivered.*

As shown in Figure 3, 37% of Supreme Court decisions and 48% of Court of Appeal decisions took more than five years to be delivered. The temporal patterns that we developed from the dataset reveal an additional dimension to the numerical gap which we have discussed above. The average time taken for writ decisions in the Court of Appeal was 3.15 years (2.80 SD) against 4.17 years (3.05 SD) for fundamental rights petitions in the Supreme Court. 25% of writs in the Court of Appeal were decided within a year of filing compared to only 20% of fundamental rights petitions in the Supreme Court resolved within one year. This comparative performance is particularly notable given that, unlike fundamental rights petitions, no constitutional or common law time limit exists for judgements on writ petitions. The practical procedures are comparable in both jurisdictions, yet the court without a stipulated time limit performs better.

The Supreme Court website lists the date on which each decision was issued. The Court of Appeal website, on the other hand, groups decisions by the month and the year and does not list the date. Further, since the registries of both courts were not digitised during the period under review, for both courts, there is no way of knowing the date on which an application related to a decision was filed. Under these constraints, calculating the exact time taken to deliver decisions is not possible.

To approximate the date on which an application was filed, we extracted the year in which the application related to a decision was filed from the application (or case) number. For example, the case number SC/FR/123/2012 indicates that the application was filed in 2012\. Assuming that filing of applications is distributed uniformly through the year, we approximated the date of filing as {extracted\_year}-June-30 for all cases across the two courts. Making the same assumption, we approximated the date of decision delivery in the Court of Appeal as {given\_year}-{given\_month}-15. We then calculated the time taken to deliver a decision as the difference between the date of decision delivery and the date of application filing.

*![Court of Appeal writs petitions resolve faster than Supreme Court FR applications][image3] Figure 4: Court of Appeal writs petitions resolve faster than Supreme Court FR applications*

As demonstrated in Figure 4, Court of Appeal writ petitions resolve faster than Supreme Court fundamental rights applications.

Unlike fundamental rights petitions, no constitutional or common law time limit governs the determination of writ petitions. Time or delay is considered when determining whether to grant leave to proceed,[^note_delay_caselaw] but no broader principles guide completion of judicial determination of writ petitions.

**5.5. Fundamental Rights and the Two Months Requirement**

The Constitution mandates that fundamental rights petitions be determined within two months of filing.[^note_art126_5] However, the Supreme Court has held that this requirement is directory rather than mandatory.[^note_visuvalingam] The constitutional requirement of two months is insufficient to accommodate the practical steps involved in fundamental rights litigation, which includes filing, service, objections, counter-affidavits, reply, oral submissions, written submissions and judgment writing. The Supreme Court rules attest to this procedural issue.[^note_sc_rule45] This has led to a situation where a constitutional requirement has, in effect, been rendered meaningless.

As illustrated in Figure 5, the data confirm serious concerns already noted about delays in the court system.[^note_delays_literature]

![37% of FR petitions took five or more years for resolution][image4]

*Figure 5: 37% of FR petitions took five or more years for resolution*

Of the 361 fundamental rights petitions in the dataset, 332 took 3 to 15 years for resolution. Of these, 140—almost half—took 10 to 15 years to be concluded. Around 37% of fundamental rights petitions took five or more years for resolution. Only 20% resolved within one year of filing. The mean time taken was 4.17 years (3.05 standard deviation)—a substantial variation from the constitutional requirement of two months.

The reasons for these delays require further investigation. Without data on the number of petitions that are dismissed by the Court at leave to proceed stage and the time taken for such dismissal. Court does not issue a judgement when a fundamental rights petition is dismissed which therefore leaves that aspect of the Court’s work beyond empirical analysis. More generally, factors that contribute to the delay may include caseload, absence of strict time allocation for oral submissions, postponements sought by parties, and the time required to write judgments. More empirical and qualitative data is required to examine these issues in more detail.

**5.6. Linguistic Patterns**

**5.6.1	Method and Salient Terms**

We performed mutual information analysis on the Supreme Court and Court of Appeal decisions to identify the most salient words in each corpus. Mutual information analysis quantifies the presence or absence of words within a corpus. The frequency of the words used can reveal attributes of the jurisprudence of both courts, providing helpful entry points for further jurisprudential analysis. We tokenized decisions and stemmed each token. We used a simple add 1 smoothing scheme to avoid zero probabilities.

**5.6.2	Interpreting Linguistic Choices**

The most salient word was ‘grant’, which appeared in 91% of Supreme Court decisions but only in 32% of Court of Appeal decisions. The underlying reason is procedural: Supreme Court decisions routinely reference the granting of leave to appeal—both the grounds on which leave was granted and the date—in the decision text. This reflects a procedural practice rather than a substantive legal distinction but nonetheless marks a clear linguistic difference between the two courts.

The words ‘answer’, ‘question’, and ‘law’ appear frequently in Supreme Court decisions because the court is called upon to answer questions of law. Although the Court of Appeal is also an appellate court, the same words have a lower prevalence in its decisions. This linguistic pattern reflects the Supreme Court’s role as the final court of appeal on questions of law and its function in establishing legal precedent through reasoned answers to legal questions.

The word ‘err’ appears in 24% of Supreme Court decisions but only in 1% of Court of Appeal decisions. On closer inspection, we observed that the word appears in the context of Supreme Court justices holding a lower court judge to have erred in their judgement. Such language is almost never used in Court of Appeal decisions despite the court’s appellate jurisdiction. This is a striking finding. Both courts exercise appellate jurisdiction and review decisions of lower tribunals. Yet the Supreme Court routinely employs the language of error—stating explicitly that a judge erred—while the Court of Appeal rarely does so. This may reflect the Supreme Court’s hierarchical position at the apex of the judicial system, where it exercises supervisory authority not only over outcomes but over legal reasoning itself. The Court of Appeal, positioned between the High Courts and the Supreme Court, may adopt a less overtly corrective tone even when reversing lower court decisions.

The high prevalence of the words ‘paragraph’ and ‘refer’ in Supreme Court decisions arises from the court’s practice of referring to specific sections of petitions, the Constitution, and other legislation. This reflects a more formal writing style in the Supreme Court compared to the Court of Appeal. Supreme Court decisions are more citation-heavy, more explicitly structured, and more systematically organized through numbered paragraphs and cross-references. This linguistic formality aligns with the court’s institutional role as the authoritative interpreter of law and the generator of binding precedent.

These linguistic patterns reflect hierarchical position and institutional culture. The Supreme Court writes as the apex court—correcting error, answering questions of law, formally citing and cross-referencing legal materials. The Court of Appeal, despite its substantial caseload and significant role in dispute resolution, writes in a less formally structured style that reflects its intermediate position in the judicial hierarchy. Linguistic choices are not merely stylistic; they encode institutional roles, hierarchical relationships, and conceptions of judicial authority.

Linguistic patterns reveal how courts write, but volume patterns reveal when and how much they produce. The Supreme Court’s output varied significantly across the decade under review, with notable peaks and troughs that correlate with constitutional developments affecting judicial independence.

**5.7	Quantitative Patterns**

We tokenized decisions using the regex pattern \[A-Za-z\]+, discounting all punctuation and numbers. The mean length of a Supreme Court decision is 3646 tokens (3038 SD) and that of a Court of Appeal decision is 1688 tokens (2091 SD). Although Supreme Court decisions are, on average, longer, the longest decision in the corpus was a Court of Appeal decision. This judgment on an appeal of a determination by the Tax Appeal Commission against Unilever Sri Lanka Limited (CA/TAX/04/2013) is 35,630 tokens long. The longest Supreme Court decision, at 29,620 tokens, was on the fundamental rights petition SC/FR/141/2015 filed by Centre for Environment and Nature Studies against Northern Power Company (Pvt) Ltd which operated a thermal power plant in Chunnakam, Jaffna and was alleged to have been responsible for contaminating the village’s groundwater.

**5.8	Judgment Length by Court and Case Type**

Judgment length varies systematically across courts and case types. Supreme Court decisions are, on average, substantially longer than those of the Court of Appeal, and exhibit greater dispersion in length, as shown in Figure 6\. Across all Supreme Court cases, the median judgment length is 2,856 words, with a mean of 3,646 words and a standard deviation of 3,038 words, indicating a strongly right-skewed distribution. Court of Appeal decisions are markedly shorter, with a median length of 1,184 words, a mean of 1,688 words, and a lower standard deviation of 2,091 words, suggesting more constrained variation in judicial writing.

![Supreme Court judgments are, on average, longer than Court of Appeal ones][image5]

*Figure 6: Supreme Court judgments are, on average, longer than Court of Appeal ones*

These structural differences persist within the principal public law jurisdictions of each court. Fundamental Rights (FR) judgments of the Supreme Court are longer than the Court’s overall baseline, with a median length of 3,022 words, a mean of 3,805 words, and a standard deviation of 3,157 words, reflecting both doctrinal density and substantial variation in judicial treatment. Court of Appeal writ decisions are marginally longer than the Court of Appeal average (median 1,303; mean 1,836), but remain comparatively concise and less dispersed (standard deviation 1,970). Over time, average judgment length has increased in both courts, with the most pronounced growth observed in Supreme Court Fundamental Rights cases, as illustrated in Figure 7\.

![Average judgment length increased over time across courts and jurisdiction][image6]

*Figure 7: Average judgment length increased over time across courts and jurisdiction*

There are no apparent formal guidelines or standards governing the length of judicial decisions, and length itself should not be confused with quality. The persuasiveness and authority of a judgment depend on accurate identification of material facts, engagement with relevant precedent, and coherent application of law to fact. Nonetheless, the increasing length of judgments—particularly in the Supreme Court—does reflect a growing volume of judicial labour, including more extensive factual narration, doctrinal exposition, and engagement with comparative or constitutional reasoning.

More importantly, variation in judgment length mirrors entrenched doctrinal hierarchies within Sri Lanka’s public law system. Fundamental Rights petitions, though fewer in number than writ applications, receive significantly more extensive judicial treatment, underscoring their elevated constitutional status. Similarly, Supreme Court decisions consistently exhibit greater length and variability than those of the Court of Appeal. The empirical patterns thus reinforce doctrinal expectations: constitutional adjudication commands deeper and more discursive reasoning than administrative review, and apex court judgments function as primary sites of legal exposition and norm-setting. Together with earlier findings on caseload composition, temporal delay, and output variation, judgment length provides a further window into how institutional role, jurisdiction, and doctrinal priority shape judicial practice.

The patterns identified thus far—quantitative dominance, writ prevalence, temporal dysfunction, substantive concentration, linguistic hierarchies, output variations, and decision length—describe how courts work. Outcome data provide a final empirical lens: how often do courts dismiss versus allow petitions?

**5.9. Dissmials and Leave to Proceed**

Dismissal, in this section, means dismissal after a full hearing. Writs and fundamental rights petitions proceed in two stages: an initial leave determination followed by a full hearing if leave is granted. SriLankaCourtDecisions does not include data on dismissals at the leave stage, as these are typically not recorded as written judgments. The actual dismissal rates are therefore higher than the data suggests.

*Table 3: Proportion of Decisions Dismissed vs Allowed*

|  | Dismissed | Allowed |
| :---- | :---- | :---- |
| Supreme Court | 532 (41.63%) | 746 (58.37%) |
| Court of Appeal | 3651 (49.92%) | 3663 (50.08%) |

In Table 3, we can observe that about half of the decisions in the Court of Appeal dismissed their petitions or appeals. In the Supreme Court, however, the majority of decisions (58%) allowed the petition or appeal to stand. Of the decisions on writs in the Court of Appeal, 55% were allowed and 45% were dismissed. In the Supreme Court, 62% of the decisions on fundamental rights petitions were allowed and 38% were dismissed.

The outcome patterns also differ. Of the decisions on writs in the Court of Appeal that were fully adjudicated, 55% were allowed and 45% were dismissed. In the Supreme Court, 62% of fundamental rights decisions were allowed and 38% were dismissed. After petitions clear the leave to proceed stage in either jurisdiction, the probability favours the petitioner—but fundamental rights petitions show a slightly higher success rate than writs.

Whether a petition is upheld or dismissed depends on multiple factors: the strength of the petitioner’s claim, the applicable legal or constitutional doctrine, the quality of submissions, and the exercise of judicial discretion. Outcomes cannot be predicted based solely on empirical patterns.

While this data does not directly reveal jurisprudential trends, perceptions abound about judicial attitudes toward petitions—whether courts are prone to dismiss or allow claims. Empirical methods suggest rough parity: neither court is systematically biased toward dismissal or allowance. The Court of Appeal maintains near parity (50% allowed versus 49% dismissed), while the Supreme Court shows only a slight tendency to allow petitions. Only a qualitative assessment can add clarity on why and when courts dismiss or grant leave to proceed in these instances. 

After petitions clear the leave to proceed stage, the probability favors the petitioner. This suggests that the leave stage functions as a significant filter: petitions that survive this threshold have reasonable prospects of success. The slightly higher success rate for fundamental rights petitions (62%) compared to Court of Appeal writs (55%) may reflect either the nature of constitutional claims or the additional scrutiny applied at the leave stage in fundamental rights jurisdiction.

**5.10. Topics of Common Concern to both courts**

To understand the latent topics and their word distributions present in court decisions, we applied Latent Dirichlet Allocation (LDA)[@blei2003latent] to SriLankaCourtDecisions. We used the Gensim implementation of LDA with the following parameters: 20 topics and random seed of 0 with all other values set to defaults. In addition to tokenizing and stemming, we removed all tokens that appeared in less than 20 documents as well as tokens that recurred in more than 50% of documents. We also removed all tokens that were less than 3 characters long.

To find the three most common topics across Supreme Court and Court of Appeal decisions, we first ran LDA on the entirety of SriLankaCourtDecisions under the experiment conditions described above. Then, we computed the average probability score for each of the 20 topics identified by LDA under the two sub corpora, independently, by summing the document-topic probability for a given topic for each document in the sub corpus and dividing by the total number of documents in the sub corpus. We obtained the three most common topics by summing the average probability scores for each topic across the two sub corpora and selecting the three topics with the highest scores, as shown in Table 4\.

*Table 4: Top-3 Topics with Highest Average Probability and Top-40 Tokens*

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

**5.10.1. 	Topic 1: Land and Property Disputes**

Topic 1 concerns land and property disputes, denoted by terms such as ‘defend’, ‘plaintiff’, ‘land’, ‘district’, ‘action’, ‘titl’, ‘deed’, ‘possess’, ‘lot’, ‘claim’, ‘plan’, ‘partit’, ‘owner’, ‘prescript’, ‘road’, ‘silva’, ‘properti’, ‘disput’, ‘perera’, ‘transfer’, ‘surveyor’, and ‘procedur’. These terms reflect the vocabulary of land litigation—title disputes, prescriptive rights, partition actions, and ownership claims.

When we ran LDA on decisions that took ten or more years for resolution (num\_topics=5 and random\_seed=0), the most common topics were land and property disputes. The state owns most of the land in Sri Lanka.[^note_state_land] The state’s role as dominant landowner generates extensive litigation over state land alienation, encroachment, competing claims, and administrative decisions regarding land use and allocation.

In terms of addressing case load and delay, this data also points to land disputes as an area requiring substantive attention and institutional infrastructure. Current state interventions regarding delays—such as fast-tracking commercial disputes and promoting alternative dispute resolution—may be misplaced if they do not address the types of cases that actually dominate appellate court dockets. If land disputes are both pervasive and slow-moving, institutional reform ought to target this specific substantive area. This might include specialized tribunals, streamlined procedures for particular categories of land disputes, or administrative reforms to reduce the generation of land-related litigation in the first instance.

**5.10.2. 	Topic 2: State Employment and Administrative Disputes**

Topic 2 captures state employment and administrative disputes, denoted by terms such as ‘decis’, ‘writ’, ‘mark’, ‘offic’, ‘servic’, ‘public’, ‘board’, ‘author’, ‘letter’, ‘appoint’, ‘univers’, ‘commiss’, ‘certiorari’, ‘mandamu’, ‘secretari’, ‘circular’, ‘member’, ‘inquiri’, ‘post’, ‘administr’, ‘committe’, ‘director’, ‘quash’, ‘ministri’, ‘document’, ‘depart’, ‘minist’, ‘promot’, ‘approv’, ‘recommend’, and ‘council’. This vocabulary reflects administrative law and public sector employment disputes—appointments, promotions, transfers, disciplinary inquiries, administrative circulars, and challenges to decisions by public boards, commissions, and ministries.

The dominance of state employment disputes, particularly visible in fundamental rights petitions, suggests that human resource management in the public sector places substantial burden on the court system. This finding tracks with earlier empirical work showing that Article 12 (equality) is overwhelmingly invoked by public servants challenging recruitments, transfers, or promotions.

This pattern raises questions about the effectiveness and confidence in administrative and quasi-judicial mechanisms such as the Administrative Appeals Tribunal, National Police Commission, and the Public Service Commission. Are they functioning effectively, or do courts primarily provide access to justice for public servants rather than the broader public? Arguably, if administrative tribunals, Public Service Commission procedures, and departmental appeal mechanisms were functioning effectively, fewer employment disputes would reach the appellate courts. The prevalence of such cases in the appellate dockets suggests either that administrative mechanisms are inadequate or that they are systematically bypassed in favour of judicial review. This has distributional consequences: if courts spend substantial time adjudicating public sector employment disputes, other types of claims—particularly those brought by marginalized communities or private citizens without institutional resources—may receive less attention. It would be useful to study the decisions of the Court of Appeal on writs in comparison with the decisions of the Provincial High Courts which exercise writ jurisdiction under Article 154(P). Those judgements are not yet accessible in the way appellate court judgements are available and hence their empirical study is not yet possible. 

**5.10.3.	Topic 3: Criminal Proceedings**

Topic 3 covers criminal proceedings, denoted by terms such as ‘accus’, ‘sentenc’, ‘trial’, ‘wit’, ‘high’, ‘polic’, ‘prosecut’, ‘convict’, ‘offenc’, ‘charg’, ‘statement’, ‘incid’, ‘victim’, ‘code’, ‘defenc’, ‘imprison’, ‘commit’, ‘hous’, ‘impos’, ‘ground’, ‘inform’, ‘crimin’, ‘count’, ‘indict’, ‘complain’, ‘find’, ‘punish’, ‘deceas’, ‘place’, ‘found’, ‘arrest’, ‘penal’, and ‘examin’. This is the vocabulary of criminal appeals—charges, indictments, convictions, sentences, witnesses, evidence, and grounds of appeal.

The dominance of criminal proceedings as one of the three major topics reflects the Court of Appeal’s role in hearing criminal appeals. This finding is unsurprising given the jurisdictional structure, but it confirms empirically what is known doctrinally: criminal appeals constitute a substantial portion of the Court of Appeal’s workload.

**5.10.4.	Topic Distribution Analysis**

A study of non-intersecting top 10 topics between the two sub corpora corroborates what we know about the structure of the legal system in the country. For instance, while appeals on criminal matters are heard by the Court of Appeal, appeals on civil matters, following the institution of the Civil Appeal High Court, are no longer heard by the Court of Appeal. The fifth and sixth most common topics in the Court of Appeal decisions—denoted by terms such as ‘vehicl’, ‘owner’, ‘offenc’, ‘confisc’, ‘charg’, ‘forest’, ‘websit’, ‘accus’, ‘polic’, ‘regist’, ‘transport’, ‘station’, ‘driver’, ‘prove’, ‘timber’, ‘illeg’, ‘deceas’, ‘murder’, ‘injuri’, and ‘stab’—do not appear in the top 10 topics in the Supreme Court decisions. These terms reflect specific categories of criminal appeals (vehicle offences, forest offences, violent crimes) that fall within the Court of Appeal’s jurisdiction.

Similarly, disputes between central government and administrative powers such as provincial councils and pradeshya sabhas are heard by the Supreme Court. The ninth most common topic in the Supreme Court decisions—denoted by terms such as ‘council’, ‘member’, ‘writ’, ‘elect’, ‘sabha’, ‘provinci’, ‘pradeshiya’, ‘constitut’, ‘articl’, ‘power’, ‘minist’, ‘chairman’, ‘local’, ‘presid’, ‘governor’, ‘uva’, ‘appoint’, and ‘central’—does not appear in the top 10 topics in the Court of Appeal decisions. This topic captures the Supreme Court’s constitutional jurisdiction over disputes involving provincial councils, local government bodies, and the distribution of powers between central and provincial authorities.

The topic distribution analysis thus confirms empirically the jurisdictional divide between the two courts and reveals the substantive areas that dominate their respective dockets. Land disputes, state employment disputes, and criminal appeals constitute the bread and butter of appellate adjudication in Sri Lanka—yet these areas receive far less scholarly and policy attention than high-profile constitutional cases.

Topic modeling reveals what courts decide. Mutual information analysis reveals how courts write—and what those linguistic choices encode about institutional hierarchies and judicial authority.

[^note_court_composition]: Until 2020, the Supreme Court comprised the Chief Justice and six to ten Justices. Subsequent to the 20th Amendment the number was increased to the Chief Justice and six to sixteen (Article 118 as amended). Until 2020 Court of Appeal comprised the President and six to eleven Justices. Subsequent to the 20th Amendment it comprises the President of the Court of Appeal and six to nineteen (Article 137 as amended).

[^note_art118_ref]: For instance, see Article 118 of the Constitution.

[^note_delay_caselaw]: Case law on delays in writ proceedings indicates that delay is a relevant consideration at the leave stage.

[^note_art126_5]: Art 126(5) of the Constitution.

[^note_visuvalingam]: *Visuvalingam v Liyanage* 1 Sri LR 203 (1983) 226.

[^note_sc_rule45]: Rule 45 of the Supreme Court Rules (as published by BASL 2021).

[^note_delays_literature]: 'Laws Delays as Abuse of Process: Fresh Perspectives and Critical Analysis' LST Review 17(236) (June 2007); [Impact of legal delays](https://sundaytimes.lk/online/opinion/impact-of-legal-delays/158-1069104) TimesOnline (8 Feb 2019).

[^note_state_land]: There is no consistency in how the percentage is calculated. The Advocata Institute rates it at 82% ([@advocata2024land]) while the World Bank rates it at 85% ([@worldbank2024land]).

