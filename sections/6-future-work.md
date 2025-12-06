# **Future Work**

The empirical patterns identified in this study point toward concrete directions for further research. The limitations of CDTextLK – particularly the absence of precise filing and decision dates, incomplete records of dismissals at the leave stage, and the lack of systematic appeal data – define immediate priorities. Beyond addressing these data constraints, the substantive findings warrant targeted investigation into judicial performance, doctrinal development, and institutional dynamics.

## Improving Temporal Analysis

The approximation method employed in this study – treating filing dates as June 30 of the filing year and Court of Appeal decision dates as the 15th of the decision month – introduces substantial measurement error. Obtaining precise dates would enable accurate calculation of case duration and reveal patterns currently obscured by aggregated estimates. This requires either digitisation of court registries or systematic manual extraction from case files.

More precise temporal data would permit analysis of whether delays concentrate in particular case types, whether they correlate with specific judicial panels, and whether procedural reforms have measurable effects. It would also enable survival analysis to identify the point at which cases are most likely to resolve and the factors that predict prolonged litigation. The constitutional mandate for two-month determination of fundamental rights petitions cannot be meaningfully evaluated without knowing when petitions were actually filed and when preliminary orders, interim relief, and final judgments were issued.

## Mapping Appellate Pathways

The current dataset cannot distinguish Supreme Court decisions exercising original jurisdiction from those hearing appeals from the Court of Appeal. Coding decisions by jurisdictional basis would reveal how many Court of Appeal judgments are appealed, which substantive areas generate appeals, and what proportion of Court of Appeal decisions effectively resolve disputes without further review. 

This analysis would test the hypothesis that the Court of Appeal's numerical dominance translates into practical authority because most disputes terminate there. If appeal rates are low, the jurisprudential neglect of Court of Appeal decisions constitutes a significant gap between doctrinal attention and institutional impact. If appeal rates are high in particular areas – land disputes, state employment matters, or criminal convictions – that pattern would warrant investigation into why certain categories of decisions are more contestable or less authoritative.

Longitudinal tracking of individual cases across judicial levels would also reveal patterns in case disposition: which cases are remanded, which are reversed, and which are affirmed. This would provide empirical grounding for claims about error correction, doctrinal consistency, and the division of labour between appellate levels.

## Capturing Dismissals at Leave Stage

The dataset excludes cases dismissed at the leave to proceed stage because such dismissals often generate no written judgment. The actual dismissal rate is therefore substantially higher than the 41% (Supreme Court) and 49% (Court of Appeal) rates calculated from decided cases. Understanding judicial gatekeeping requires systematic collection of leave stage outcomes, including both grants and refusals.

This data exists in court registries but is not publicly accessible. Obtaining it would require either institutional cooperation to access registry records or systematic extraction from court databases. With this data, researchers could analyse: what proportion of filed petitions obtain leave; what distinguishes cases granted leave from those refused; whether leave grant rates vary across substantive areas, time periods, or judicial panels; and how the leave stage functions as a filter for substantive adjudication.

Leave grant rates have direct implications for access to justice. If most petitions are dismissed at the threshold, the barrier to relief may lie less in substantive adjudication than in the preliminary screening process. This would redirect reform attention toward transparency in leave determinations and development of clear standards governing threshold access to appellate jurisdiction.

## Investigating Delay Through Case Studies

While aggregate temporal data reveal systematic delays, understanding causation requires qualitative investigation. Case studies of long-duration disputes – particularly those taking ten or more years – would identify procedural bottlenecks, patterns of postponement, complexities specific to particular dispute types, and institutional practices that contribute to delay.

Land disputes dominate the longest-duration category, but the underlying reasons remain unclear. Is delay attributable to evidentiary complexity, the need for surveys and site inspections, difficulties in serving parties, postponements sought by litigants, or the time required for judicial consideration? Criminal appeals may face different delay factors: witness availability, the need for translation of lower court records, or the volume of appeals awaiting hearing. State employment disputes may involve delays in obtaining administrative records or the participation of multiple government departments.

Targeted case studies would reveal whether delays concentrate at particular procedural stages: between filing and leave determination, between leave and hearing, or between hearing and judgment delivery. If delays cluster at the judgment-writing stage, interventions might focus on judicial resources and case management. If delays cluster at earlier stages, procedural reform or administrative capacity becomes the priority.

## Substantive Analysis of Dominant Topics

The identification of land disputes, state employment matters, and criminal appeals as dominant topics warrants substantive doctrinal analysis. Land dispute jurisprudence in Sri Lanka has received limited scholarly attention despite dominating appellate dockets. Systematic study of land dispute decisions would reveal patterns in how courts resolve competing claims, apply prescriptive acquisition doctrine, interpret state land alienation schemes, and manage disputes arising from incomplete or conflicting title records.

State employment disputes – particularly appointments, promotions, transfers, and disciplinary proceedings – reveal the extent to which appellate courts function as forums for resolving internal public sector disputes. Are courts effectively reviewing administrative discretion or are they substituting their judgment for administrative decisions? Do patterns in state employment cases reveal substantive inequality in how similarly situated public servants are treated? What proportion of petitioners succeed, and does success correlate with particular grounds of challenge or particular administrative bodies?

Criminal appeal patterns warrant analysis of conviction and sentence affirmation rates, the grounds on which appeals succeed, and whether particular categories of offences generate disproportionate appeals. Vehicle offences and forest offences appear as distinct topics in Court of Appeal decisions, suggesting these categories generate substantial litigation. Understanding why requires analysis of the applicable legal framework, enforcement patterns, and the availability of defences.

## Linguistic and Stylistic Analysis

The mutual information analysis identified salient terms but did not pursue detailed linguistic or stylistic analysis. Further work could employ computational linguistics methods to analyse citation practices, reasoning structures, and rhetorical patterns in judgments. Do Supreme Court decisions cite more precedent than Court of Appeal decisions? Do fundamental rights judgments cite more constitutional provisions than statutory ones? Do judgments cite foreign jurisprudence, and if so, from which jurisdictions?

Stylistic analysis could also examine variation across judicial panels. Do particular justices employ distinct linguistic patterns, reasoning structures, or citation practices? This would not assess the quality of individual justices' work but would reveal whether judicial style varies systematically and whether such variation correlates with case outcomes or substantive areas.

Computational analysis of reasoning patterns – particularly the structure of legal arguments, the weight given to different sources of law, and the methods by which courts distinguish or apply precedent – would contribute to understanding how appellate courts develop doctrine. This requires more sophisticated natural language processing methods than employed in this preliminary study but is feasible with the existing corpus.

## Comparative Institutional Analysis

The hypothesis that Supreme Court output correlates with judicial independence warrants rigorous testing through comparative analysis. This requires assembling additional variables: judicial appointment patterns, public statements by judges or judicial associations, legislative or executive actions affecting the judiciary, and external assessments of judicial independence from legal professional associations or civil society organisations.

Comparative analysis would also examine whether similar patterns exist in other common-law jurisdictions. Do courts exercising both original and appellate jurisdiction, like the Court of Appeal, consistently produce greater numerical output than apex courts exercising primarily appellate jurisdiction? Do constitutional mandates for expedited adjudication correlate with faster or slower resolution in practice? Do courts without such mandates perform better, and if so, what institutional or procedural factors explain the difference?

Such analysis would test whether the observed patterns are specific to Sri Lanka's constitutional and institutional context or reflect broader dynamics common to appellate courts in similar legal systems.

## Expanding the Temporal and Jurisdictional Scope

The dataset covers 2012–2022, but extending the temporal scope backward would reveal longer-term trends. How did the courts function before the 18th Amendment? Did output and delay patterns differ under previous constitutional frameworks? Extending forward would reveal whether post-2022 constitutional developments – particularly the 22nd Amendment – affected judicial performance.

Expanding the jurisdictional scope to include High Court decisions – where available in digitised form – would enable analysis of how disputes move through the judicial hierarchy. What types of cases generate appeals from High Courts to the Court of Appeal? Do particular High Court circuits generate disproportionate appeals, suggesting either greater caseload or distinct patterns in decision-making?

District Court and Magistrate Court decisions are not systematically digitised, but targeted collection of decisions in particular substantive areas would enable analysis of lower court jurisprudence and the extent to which appellate decisions align with or depart from lower court patterns.

## Methodological Development

The computational methods employed in this study – topic modeling through LDA, mutual information analysis, and basic descriptive statistics – represent initial applications of established techniques. Further methodological development could employ more sophisticated approaches: dynamic topic modeling to reveal how topics shift over time, supervised machine learning to predict case outcomes based on textual features, and network analysis to map citation patterns among decisions.

Sentiment analysis – adapted to the specialized language of judicial decisions – could reveal whether particular dispute types or procedural contexts generate more emotive or more neutral judicial language. This would not assess the quality of decisions but would contribute to understanding how courts write about different categories of disputes.

Comparative corpus linguistics could analyse Sri Lankan judicial language against judgments from other jurisdictions, revealing distinctiveness or convergence in judicial style, citation practices, and reasoning structures.

## Implications for Reform

The findings of this study point toward specific areas for institutional reform, but implementing such reforms requires additional empirical work. If land disputes dominate long-duration cases, would specialized land tribunals reduce the burden on appellate courts? If state employment disputes constitute a substantial proportion of writ petitions, would strengthening administrative appeal mechanisms reduce litigation?

Piloting procedural reforms – such as time limits for oral submissions, case management protocols for particular dispute types, or alternative dispute resolution mechanisms for specific categories of cases – would benefit from empirical baseline data against which to measure effectiveness. CDTextLK provides such baseline data for the appellate courts, but implementing and evaluating reform requires collaboration between researchers, judiciary, legal practitioners, and policymakers.

The constitutional mandate for two-month determination of fundamental rights petitions cannot be met under current conditions, but meaningful reform requires understanding what is feasible. Are there categories of fundamental rights petitions that could be resolved more quickly? Do particular procedural stages consume disproportionate time? Could interim relief mechanisms provide meaningful remedies while final adjudication proceeds?

## Building Infrastructure for Empirical Legal Research

The limitations of this study reflect broader limitations in Sri Lanka's legal system digitisation. Court registries are not digitised, case management systems are incomplete, and no centralised repository of judicial decisions exists. Building infrastructure for empirical legal research requires institutional investment in digitising records, standardising case numbering, and making data publicly accessible.

Such infrastructure would benefit not only researchers but also legal practitioners, policymakers, and the public. Searchable, systematically organised court decisions would improve access to justice by making legal knowledge more readily available. Digitised registries would enable better case management and reduce administrative burden on court staff. Publicly accessible data on case filings, dispositions, and timelines would enhance transparency and accountability.

The immediate priority is completing digitisation of decisions from all levels of the judicial hierarchy and making them accessible through stable, searchable platforms. CDTextLK demonstrates what is possible with publicly available data, but the dataset's limitations reflect underlying gaps in legal system infrastructure. Addressing those gaps would enable far more comprehensive empirical analysis and, more importantly, would contribute to a more transparent, accessible, and accountable justice system.

---

The patterns identified in this study are preliminary but sufficient to warrant attention in both scholarly analysis and reform debates. The research directions outlined here are neither exhaustive nor speculative – they respond directly to gaps revealed by the empirical analysis of CDTextLK and address limitations in data, method, and scope that constrain present conclusions. Pursuing these directions would advance understanding of how appellate courts function, what disputes they resolve, and how judicial work relates to broader questions of access to justice, institutional design, and the rule of law.
