# A Research Agenda for the Future {#sec:agenda}

The empirical patterns identified in this study point toward concrete directions for further research. The limitations of the `SriLankaCourtDecisions` corpus – particularly the absence of precise filing and decision dates, incomplete records of dismissals at the leave stage, and the lack of systematic appeal data – define immediate priorities. Beyond addressing these data constraints, the substantive findings warrant targeted investigation into judicial performance, doctrinal development, and institutional dynamics.

## Improving Temporal Analysis

The approximation method employed in this study – treating filing dates as June 30 of the filing year and Court of Appeal decision dates as the 15th of the decision month – introduces substantial measurement error. Obtaining precise dates would enable accurate calculation of case duration and reveal patterns currently obscured by aggregated estimates. This requires either digitisation of court registries or systematic manual extraction from case files.

More precise temporal data would permit analysis of whether delays concentrate in particular case types, whether they correlate with specific judicial panels, and whether procedural reforms have measurable effects. It would also enable survival analysis to identify the point at which cases are most likely to resolve and the factors that predict prolonged litigation. For instance, the constitutional mandate for two-month determination of fundamental rights petitions cannot be meaningfully evaluated without knowing when petitions were actually filed and when preliminary orders, interim relief, and final judgments were issued.

## Mapping Appellate Pathways

The case-type and jurisdictional classifications employed in this study, apart from the LDA-based topic analysis, are derived from case numbers rather than from the substantive content of judgments. They should therefore be regarded as a cursory classification. At the Supreme Court level, a case number may identify a matter simply as “SC/APPEAL” without indicating whether the appeal originated in the Court of Appeal, Civil Appellate High Court, High Court, or Commercial High Court. Although some case numbers contain more specific designations, such as “SC/CA/APPEAL”, these conventions are not applied consistently.

Case-number patterns can therefore distinguish broad categories, including original and appellate jurisdiction, but cannot reliably reconstruct the appellate pathway of every case or link each Supreme Court appeal to the particular court and judgment from which it arose. Future research would require content-based coding of the judgments, together with more systematic linkage of decisions across judicial levels. This should also separately identify references made by the Court of Appeal under Article 126(3), which are distinct from appeals.

This analysis would test the hypothesis that the Court of Appeal’s numerical dominance translates into practical authority because most disputes terminate there. If appeal rates are low, the jurisprudential neglect of Court of Appeal decisions constitutes a significant gap between doctrinal attention and institutional impact. If appeal rates are high in particular areas – land disputes, state employment matters, or criminal convictions – that pattern would warrant investigation into why certain categories of decisions are more contestable or less authoritative.

Longitudinal tracking of individual cases across judicial levels would also reveal patterns in case disposition: which cases are overturned, and which are affirmed. This would provide empirical grounding for claims about error correction, doctrinal consistency, and the division of labour between appellate levels.

## Capturing Dismissals at Leave Stage

The dataset excludes cases dismissed at the leave to proceed stage because such dismissals often generate no written judgment. The actual dismissal rate may therefore be substantially higher than the 41% (Supreme Court) and 49% (Court of Appeal) rates calculated from decided cases. Understanding judicial gatekeeping requires systematic collection of leave stage outcomes, including both grants and refusals.

This data exists in court registries but is not publicly accessible. Obtaining it would require either institutional cooperation to access registry records or systematic extraction from court databases. With this data, researchers could analyse: what proportion of filed petitions obtain leave; what distinguishes cases granted leave from those refused; whether leave grant rates vary across substantive areas, time periods, or judicial panels; and how the leave stage functions as a filter for substantive adjudication.

Leave grant rates have direct implications for access to justice. If most petitions are dismissed at the threshold, the barrier to relief may lie less in substantive adjudication than in the preliminary screening process. This would redirect reform attention toward transparency in leave determinations and development of clear standards governing threshold access to appellate jurisdiction. This limitation is particularly significant for understanding writ jurisdiction, where leave stage gatekeeping may explain why only 55% of fully adjudicated Court of Appeal writs are allowed compared to 62% of Supreme Court fundamental rights petitions—and why different petitioners may strategically choose different forums despite overlapping grounds for relief.

## Investigating Delay Through Case Studies

While aggregate temporal data reveal systematic delays, understanding causation requires qualitative investigation. Case studies of long-duration disputes – particularly those taking ten or more years – would assist in identifying procedural bottlenecks, patterns of postponement, complexities specific to particular dispute types, and institutional practices that contribute to delay.

Land disputes dominate the longest-duration category, but the underlying reasons remain unclear. Is delay attributable to evidentiary complexity, the need for surveys and site inspections, difficulties in serving parties, postponements sought by litigants, or the time required for judicial consideration? Criminal appeals may face different delay factors: witness availability, the need for translation of lower court records, or the volume of appeals awaiting hearing. State employment disputes may involve delays in obtaining administrative records or the participation of multiple government departments.

Targeted case studies would reveal whether delays concentrate at particular procedural stages: between filing and leave determination, between leave and hearing, or between hearing and judgment delivery. If delays cluster at the judgment-writing stage, interventions might focus on judicial resources and case management. If delays cluster at earlier stages, procedural reform or administrative capacity becomes the priority.

## Substantive Analysis of Dominant Topics

The identification of land disputes, state employment matters, and criminal appeals as dominant topics warrants substantive doctrinal analysis. Land dispute jurisprudence in Sri Lanka has received limited scholarly attention despite dominating appellate dockets. Systematic study of land dispute decisions would reveal patterns in how courts resolve competing claims, apply prescriptive acquisition doctrine, interpret state land alienation schemes, and manage disputes arising from incomplete or conflicting title records.

State employment disputes – particularly appointments, promotions, transfers, and disciplinary proceedings – reveal the extent to which superior courts function as forums for resolving internal public sector disputes. Are courts effectively reviewing administrative discretion or are they substituting their judgment for administrative decisions? Do patterns in state employment cases reveal substantive inequality in how similarly situated public servants are treated? What proportion of petitioners succeed, and does success correlate with particular grounds of challenge or particular administrative bodies?

Criminal appeal patterns warrant analysis of conviction and sentence affirmation rates, the grounds on which appeals succeed, and whether particular categories of offences generate disproportionate appeals. Vehicle offences and forest offences appear as distinct topics in Court of Appeal decisions, suggesting these categories generate substantial litigation. Understanding why requires analysis of the applicable legal framework, enforcement patterns, and the availability of defences.

## Linguistic and Stylistic Analysis

The mutual information analysis identified salient terms but did not pursue detailed linguistic or stylistic analysis. Further work could employ computational linguistics methods to analyse citation practices, reasoning structures, and rhetorical patterns in judgments. Do Supreme Court decisions cite more precedent than Court of Appeal decisions? Do fundamental rights judgments cite more constitutional provisions than statutory ones? Do judgments cite foreign jurisprudence, international law, or academic commentary; and, if so, which jurisdictions, instruments, and scholarly sources are most influential?

Stylistic analysis could also examine variation across judicial panels. Do linguistic patterns, reasoning structures, or citation practices vary across benches or panels? This would not assess the quality of individual justices’ work but would reveal whether judicial style varies systematically and whether such variation correlates with case outcomes or substantive areas.

Computational analysis of reasoning patterns – particularly the structure of legal arguments, the weight given to different sources of law, and the methods by which courts distinguish or apply precedent – would contribute to understanding how superior courts develop doctrine. This requires more sophisticated natural language processing methods than employed in this preliminary study but is feasible with the existing corpus.

## Comparative Institutional Analysis

The hypothesis that Supreme Court output correlates with judicial independence warrants rigorous testing through comparative analysis. This requires assembling additional variables: judicial appointment patterns, public statements by judges or judicial associations, legislative or executive actions affecting the judiciary, and external assessments of judicial independence from legal professional associations or civil society organisations.

Comparative analysis would also examine whether similar patterns exist in other common-law jurisdictions. Do courts exercising both original and appellate jurisdiction, like the Court of Appeal, consistently produce greater numerical output than apex courts exercising primarily appellate jurisdiction? Do constitutional mandates for expedited adjudication correlate with faster or slower resolution in practice? Do courts without such mandates perform better, and if so, what institutional or procedural factors explain the difference?

Such analysis would test whether the observed patterns are specific to Sri Lanka’s constitutional and institutional context or reflect broader dynamics common to superior courts in similar legal systems.

## Expanding the Temporal and Jurisdictional Scope

The dataset covers 2012–2022, but extending the temporal scope backward would reveal longer-term trends. For instance, do constitutional amendments that reform the process for judicial appointments impact the work of the Court? How did the increase in the number of justices impact the same? Through a combination of empirical and qualitative study, it may be possible to seek answers to these questions. 

Expanding the jurisdictional scope to include High Court decisions – where available in digitised form – would enable analysis of how disputes move through the judicial hierarchy. What types of cases generate appeals from High Courts to the Court of Appeal? Do particular High Court circuits generate disproportionate appeals, suggesting either greater caseload or distinct patterns in decision-making?

District Court and Magistrate Court decisions are not systematically digitised, but targeted collection of decisions in particular substantive areas would enable analysis of lower court jurisprudence and the extent to which appellate decisions align with or depart from lower court patterns.

## Methodological Development

The computational methods employed in this study – topic modelling through LDA, mutual information analysis, and basic descriptive statistics – represent initial applications of established techniques. Further methodological development could employ more sophisticated approaches: dynamic topic modelling to reveal how topics shift over time, supervised machine learning to identify which textual features correlate with case outcomes (not as a step toward automated adjudication), and network analysis to map citation patterns among decisions.

The use of sentiment analysis – adapted to the specialised language of judicial decisions – could reveal whether particular dispute types or procedural contexts generate more emotive or more neutral judicial language. This would not assess the quality of decisions but would contribute to understanding how courts write about different categories of disputes.

Comparative corpus linguistics could analyse Sri Lankan judicial language against judgments from other jurisdictions, revealing distinctiveness or convergence in judicial style, citation practices, and reasoning structures.