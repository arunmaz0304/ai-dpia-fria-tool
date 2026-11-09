# Legal references

Last verified: **2026-11-09**. Source of truth: `refs/references.json`.

Items marked ⚠ need a follow-up check before you rely on the pinpoint or status.


## Legislation

| Reference | What it covers | Stages | Check |
|---|---|---|---|
| [GDPR Art. 4(1), (4), (5)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Definitions of personal data, profiling and pseudonymisation. | Screening, Scoping |  |
| [GDPR Art. 5(1)(a)–(f), 5(2)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Core principles (lawfulness, fairness, transparency, purpose limitation, minimisation, accuracy, storage limitation, security) and accountability. | Necessity |  |
| [GDPR Art. 6(1)(a)–(f)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Legal bases. Last subparagraph of Art. 6(1): point (f) does not apply to public authorities performing their tasks. | Necessity |  |
| [GDPR Art. 6(4)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Compatibility test for further processing (e.g. reusing data to train or fine-tune). | Necessity |  |
| [GDPR Art. 9(1)–(2)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Prohibition on processing special categories, and the exceptions that lift it. | Scoping, Necessity |  |
| [GDPR Art. 10](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Personal data relating to criminal convictions and offences. | Scoping, Necessity |  |
| [GDPR Arts. 13(2)(f), 14(2)(g)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Information about the existence of automated decision-making, meaningful information about the logic involved, significance and consequences. | Mitigation |  |
| [GDPR Art. 15(1)(h)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Right of access to information about automated decision-making and the logic involved. | Mitigation |  |
| [GDPR Arts. 16–17, 21](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Rectification, erasure and objection; consider retraining, unlearning or output filtering. | Mitigation |  |
| [GDPR Art. 22(1)–(4)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Right not to be subject to a decision based solely on automated processing with legal or similarly significant effects; exceptions and safeguards (human intervention, express view, contest). | Screening, Risk, Mitigation |  |
| [GDPR Art. 25](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Data protection by design and by default. | Mitigation |  |
| [GDPR Arts. 26, 28](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Joint controllers and processors: role allocation and the Art. 28(3) processor contract. | Scoping |  |
| [GDPR Art. 30](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Records of processing activities; the DPIA should be consistent with the RoPA. | Scoping |  |
| [GDPR Art. 32](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Security of processing appropriate to the risk. | Mitigation |  |
| [GDPR Arts. 33–34](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Personal data breach notification to IMY (72 hours) and communication to data subjects. | Governance |  |
| [GDPR Art. 35(1), (3)(a)–(c), (4), (7), (9), (11)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | When a DPIA is required, the mandatory categories, national lists, minimum content, seeking data subjects' views, and review on change of risk. | Screening, Scoping, Risk, Residual/sign-off, Governance |  |
| [GDPR Art. 35(2)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Controller must seek the advice of the DPO when carrying out a DPIA. | Residual/sign-off |  |
| [GDPR Art. 36(1)–(3)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Prior consultation with the supervisory authority where residual risk stays high; authority has up to eight weeks, extendable by six (Art. 36(2)). | Residual/sign-off |  |
| [GDPR Arts. 44–46, 49](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Transfers to third countries: adequacy, appropriate safeguards (SCCs), derogations. | Scoping |  |
| [Commission Implementing Decision (EU) 2023/1795 (EU–US Data Privacy Framework)](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj) | Adequacy for transfers to certified US organisations. Check certification of each US vendor. | Scoping |  |
| [GDPR Arts. 77, 82](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Right to lodge a complaint with IMY; right to compensation. | Mitigation |  |
| [GDPR Recitals 26, 71, 75, 84, 89–91](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Anonymous data (26); safeguards for automated decisions incl. explanation (71); risk sources (75); DPIA purpose and scope (84, 89–91). | Screening, Risk |  |
| [AI Act Art. 3(1), (3), (4), (23)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Definitions: AI system, provider, deployer, substantial modification. | Screening, Governance |  |
| [AI Act Art. 4 (as amended by Reg. (EU) 2026/1744)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4) | AI literacy. After the Digital Omnibus: providers and deployers take measures to support AI literacy; no specific level required. | Mitigation | ⚠ Amended text: confirm wording in the OJ version of Reg. (EU) 2026/1744. |
| [AI Act Art. 4a (inserted by Reg. (EU) 2026/1744)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) | Exceptional processing of special-category data to detect and correct bias, subject to strict necessity and safeguards. Replaces the former Art. 10(5) route and extends it beyond high-risk providers. | Mitigation | ⚠ New article reported in secondary sources; confirm numbering and conditions in the OJ text. |
| [AI Act Art. 5(1)(a)–(h)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5) | Prohibited practices, applicable since 2 February 2025. New points (ba) and (bb) (non-consensual intimate imagery, CSAM generation) apply from 2 December 2026. | Screening |  |
| [AI Act Art. 6(1)–(4), Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | High-risk classification. Art. 6(3) derogation for Annex III systems that do not pose a significant risk; documentation under Art. 6(4). | Screening |  |
| [AI Act Arts. 9–15](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | High-risk requirements: risk management (9), data governance incl. bias examination Art. 10(2)(f)–(g) (10), technical documentation (11), logging (12), instructions for use (13), human oversight (14), accuracy, robustness, cybersecurity (15). | Mitigation |  |
| [AI Act Art. 10(2)(f)–(g)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-10) | Examination of possible biases and measures to detect, prevent and mitigate them. | Risk, Mitigation |  |
| [AI Act Art. 14(4)(a)–(e)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) | Human oversight, including awareness of automation bias (Art. 14(4)(b)) and ability to override or stop the system. | Risk, Mitigation |  |
| [AI Act Art. 15(4)–(5)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15) | Robustness and cybersecurity, incl. data poisoning, model poisoning, adversarial examples. | Risk, Mitigation |  |
| [AI Act Art. 25](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-25) | Responsibilities along the value chain; a deployer can become a provider (e.g. substantial modification, own name or trademark, change of intended purpose). | Screening, Governance |  |
| [AI Act Art. 26(1)–(11)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) | Deployer obligations: use per instructions (1), competent human oversight (2), relevant input data (4), monitoring and reporting (5), keep logs at least six months (6), inform workers' representatives (7), use provider information for the DPIA (9), inform affected persons (11). | Scoping, Mitigation, Governance |  |
| [AI Act Art. 27(1)(a)–(f), (2)–(5)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27) | FRIA for deployers that are public bodies or private entities providing public services, and deployers of Annex III point 5(b) and (c) systems. Content (1)(a)–(f), notify the market surveillance authority (3), complements the DPIA (4), AI Office template (5). | Screening, Risk, Residual/sign-off |  |
| [AI Act Art. 49](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-49) | Registration in the EU database, incl. public-authority deployers (Art. 49(3)). | Mitigation |  |
| [AI Act Art. 50(1)–(4)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) | Transparency: disclose AI interaction, mark synthetic content, deepfakes, emotion recognition and biometric categorisation. Applies since 2 August 2026; Art. 50(2) grace period to 2 December 2026 for systems already on the market. | Screening, Mitigation |  |
| [AI Act Art. 53](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) | GPAI model provider obligations, incl. documentation for downstream providers. | Scoping |  |
| [AI Act Arts. 72–73](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Post-market monitoring and serious incident reporting. | Governance |  |
| [AI Act Arts. 85–86](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Right to complain to a market surveillance authority; right to explanation of individual decision-making (Annex III high-risk). | Mitigation |  |
| [AI Act Art. 113 (as amended by Reg. (EU) 2026/1744)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) | Application dates: Annex III high-risk obligations (incl. Arts. 26–27) from 2 December 2027; Annex I high-risk from 2 August 2028. | Screening | ⚠ Dates from secondary sources on Reg. (EU) 2026/1744 (OJ 24 July 2026); confirm against the OJ text. |
| [EU Charter of Fundamental Rights Arts. 1, 7, 8, 11, 21, 23–26, 31, 34–35, 38, 41, 47](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016P/TXT) | The rights assessed in the FRIA: dignity, privacy, data protection, expression, non-discrimination, children, elderly and disability, fair working conditions, social security and health care, consumer protection, good administration, effective remedy. | Risk |  |
| [Dataskyddslagen (SFS 2018:218)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218/) | Swedish supplementary provisions to the GDPR (e.g. special categories, personal identity numbers). | Scoping, Necessity |  |
| [Medbestämmandelagen (SFS 1976:580) §§ 11, 19](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1976580-om-medbestammande-i-arbetslivet_sfs-1976-580/) | Duty to negotiate before major changes and to inform unions; relevant when AI is introduced at work (alongside AI Act Art. 26(7)). | Mitigation | ⚠ Confirm section numbers against the consolidated act. |
| [Brottsdatalagen (SFS 2018:1177) 3 kap. 7 §](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/brottsdatalag-20181177_sfs-2018-1177/) | Impact assessment duty for law-enforcement processing (police, prosecutors), outside the GDPR. | Screening |  |

## Case law

| Reference | What it covers | Stages | Check |
|---|---|---|---|
| [C-634/21 SCHUFA Holding (Scoring), 7 Dec 2023](https://curia.europa.eu/juris/liste.jsf?num=C-634/21&language=en) | A credit score is an Art. 22 'decision' where a third party draws strongly on it to decide. Preparatory automated outputs can fall under Art. 22. | Screening, Risk, Mitigation |  |
| [C-203/22 Dun & Bradstreet Austria, 27 Feb 2025](https://curia.europa.eu/juris/liste.jsf?num=C-203/22&language=en) | Art. 15(1)(h): explain the procedure and principles actually applied, in an intelligible way; a formula or algorithm alone is not enough. Trade secrets go to the authority or court for balancing. | Mitigation | ⚠ Pinpoint paragraphs (reported as paras 66 and 76) to be confirmed against the judgment. |
| [C-252/21 Meta Platforms v Bundeskartellamt, 4 Jul 2023](https://curia.europa.eu/juris/liste.jsf?num=C-252/21&language=en) | Contract necessity is narrow (objectively indispensable); limits of legitimate interests; processing that reveals sensitive data falls under Art. 9. | Necessity |  |
| [C-184/20 OT v Vyriausioji tarnybinės etikos komisija, 1 Aug 2022](https://curia.europa.eu/juris/liste.jsf?num=C-184/20&language=en) | Data that indirectly reveal special-category information (by inference) are special-category data. | Scoping, Necessity |  |
| [C-21/23 Lindenapotheke, 4 Oct 2024](https://curia.europa.eu/juris/liste.jsf?num=C-21/23&language=en) | Broad reading of health data: information from which health status can be inferred. | Scoping |  |
| [C-621/22 Koninklijke Nederlandse Lawn Tennisbond, 4 Oct 2024](https://curia.europa.eu/juris/liste.jsf?num=C-621/22&language=en) | A commercial interest can be a legitimate interest, subject to the necessity and balancing conditions. | Necessity |  |
| [C-708/18 TK v Asociaţia de Proprietari bloc M5A-ScaraA, 11 Dec 2019](https://curia.europa.eu/juris/liste.jsf?num=C-708/18&language=en) | The three cumulative conditions of Art. 6(1)(f): legitimate interest, necessity, balancing. | Necessity |  |
| [C-817/19 Ligue des droits humains, 21 Jun 2022](https://curia.europa.eu/juris/liste.jsf?num=C-817/19&language=en) | Automated risk assessment must use non-discriminatory, specific and reliable pre-determined criteria; self-learning systems that change criteria without human review are excluded in that context; human review of hits. | Risk |  |
| [C-311/18 Facebook Ireland and Schrems (Schrems II), 16 Jul 2020](https://curia.europa.eu/juris/liste.jsf?num=C-311/18&language=en) | SCCs need a case-by-case assessment of the destination country and, if needed, supplementary measures. | Scoping |  |
| [C-413/23 P EDPS v SRB, 4 Sep 2025](https://curia.europa.eu/juris/liste.jsf?num=C-413/23&language=en) | Pseudonymised data may not be personal data for a recipient who cannot reasonably re-identify; the controller's own obligations are assessed from its perspective at collection. | Screening, Scoping |  |
| [C-582/14 Breyer, 19 Oct 2016](https://curia.europa.eu/juris/liste.jsf?num=C-582/14&language=en) | Identifiability depends on means reasonably likely to be used, incl. via third parties. | Screening |  |
| [C-26/22 and C-64/22 SCHUFA Holding (Discharge from remaining debts), 7 Dec 2023](https://curia.europa.eu/juris/liste.jsf?num=C-26/22&language=en) | Keeping data longer than the public source keeps it is unlawful; objection and erasure apply. | Scoping |  |
| [C-340/21 Natsionalna agentsia za prihodite, 14 Dec 2023](https://curia.europa.eu/juris/liste.jsf?num=C-340/21&language=en) | A breach does not by itself prove that measures were inappropriate; the controller bears the burden of proof; fear of misuse can be non-material damage. | Mitigation |  |
| [C-300/21 Österreichische Post, 4 May 2023](https://curia.europa.eu/juris/liste.jsf?num=C-300/21&language=en) | Compensation requires actual damage, but there is no seriousness threshold. | Residual/sign-off |  |
| [C-154/21 RW v Österreichische Post, 12 Jan 2023](https://curia.europa.eu/juris/liste.jsf?num=C-154/21&language=en) | Right of access covers the identity of the actual recipients. | Mitigation |  |
| [C-807/21 Deutsche Wohnen, 5 Dec 2023](https://curia.europa.eu/juris/liste.jsf?num=C-807/21&language=en) | Fines require intentional or negligent infringement; no need to identify a specific natural person. | Residual/sign-off |  |
| [C-683/21 Nacionalinis visuomenės sveikatos centras, 5 Dec 2023](https://curia.europa.eu/juris/liste.jsf?num=C-683/21&language=en) | Joint controllership in commissioning an app; using personal data for testing is processing. | Scoping |  |

## Guidance

| Reference | What it covers | Stages | Check |
|---|---|---|---|
| [Commission draft guidelines on high-risk classification (Art. 6)](https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems) | Draft published 2026; practical examples of high-risk and non-high-risk use cases. | Screening | ⚠ Draft. Check whether the final version has been adopted. |
| [WP29 Guidelines on DPIA, WP248 rev.01 (endorsed by EDPB)](https://ec.europa.eu/newsroom/article29/items/611236) | The nine criteria; two or more usually means a DPIA is required. | Screening, Risk |  |
| [WP29 Guidelines on automated decision-making and profiling, WP251 rev.01 (endorsed by EDPB)](https://ec.europa.eu/newsroom/article29/items/612053) | Meaning of 'solely automated', 'similarly significant effects', meaningful human involvement. | Risk, Mitigation |  |
| [EDPB Opinion 28/2024 on AI models (17 Dec 2024)](https://edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf) | When a model is anonymous; legitimate interest for development and deployment; consequences of unlawful development for later use. | Screening, Scoping, Necessity |  |
| [EDPB Guidelines 1/2024 on Art. 6(1)(f)](https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2024/guidelines-12024-processing-personal-data-based_en) | Three-step legitimate interest test. | Necessity | ⚠ Published for consultation; check whether a final version has been adopted. |
| [EDPB Guidelines 2/2019 (Art. 6(1)(b)), 05/2020 (consent), Recommendations 01/2020 (supplementary measures), Guidelines 01/2025 (pseudonymisation)](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en) | Supporting guidance for legal basis, transfers and pseudonymisation. | Scoping, Necessity |  |
| [IMY list of processing requiring a DPIA (Art. 35(4))](https://www.imy.se/globalassets/dokument/ovrigt/list-regarding-data-protection-impact-assessments.pdf) | Swedish national list; check the current version on imy.se. | Screening |  |
| [Commission guidelines on prohibited AI practices and on the AI system definition (Feb 2025)](https://ai-act-service-desk.ec.europa.eu/) | Interpretation of Art. 5 and Art. 3(1). | Screening |  |

## Supervisory decisions

| Reference | What it covers | Stages | Check |
|---|---|---|---|
| [IMY, Skellefteå kommun (Gymnasienämnden), DI-2019-2221, Aug 2019](https://www.imy.se/) | Facial recognition for school attendance: consent invalid due to imbalance of power; no adequate DPIA and no prior consultation. Sweden's first GDPR fine (SEK 200 000). | Screening, Residual/sign-off | ⚠ Confirm decision date, fine and the articles cited (reported: Arts. 5, 9, 35, 36). |
| [IMY, Polismyndigheten (Clearview AI), DI-2020-2719, 10 Feb 2021](https://www.imy.se/link/5d5e59d4e64c4dcd909c0f7d42606960.aspx) | SEK 2.5m under the Criminal Data Act: no impact assessment before using a facial recognition service from an external third-country provider; inadequate organisational measures. | Screening, Scoping |  |
| [Autoriteit Persoonsgegevens (NL), Uber, EUR 824 990 000 (EDPB news 8 Oct 2026)](https://www.edpb.europa.eu/news/dutch-dpa-fines-uber-eur-824-990-000-for-unlawful-automated-decision-making-and-insufficient_de) | Automated deactivation of drivers breached Art. 22 and Art. 13 (insufficient information on profiling). Under appeal. | Risk, Mitigation | ⚠ Under appeal; not final. |
