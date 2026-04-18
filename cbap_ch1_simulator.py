import streamlit as st
import random
import time

st.set_page_config(
    page_title="CBAP Simulator — Chapter 1",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap');
:root {
    --navy:  #0a1628;
    --blue:  #1a3a6b;
    --gold:  #c9a84c;
    --gold2: #f0d080;
    --light: #f4f1eb;
    --green: #1e7c4a;
    --red:   #9b2335;
    --mid:   #6b7a99;
}
html, body, [data-testid="stAppViewContainer"] { background-color: var(--navy) !important; color: var(--light) !important; }
[data-testid="stAppViewContainer"] > .main { background-color: var(--navy) !important; }
.exam-header { background: linear-gradient(135deg, var(--blue) 0%, var(--navy) 100%); border: 1px solid var(--gold); border-radius: 12px; padding: 2rem 2.5rem; margin-bottom: 2rem; text-align: center; }
.exam-header h1 { font-family: 'Playfair Display', serif; color: var(--gold); font-size: 2.4rem; margin: 0 0 .4rem 0; letter-spacing: 1px; }
.exam-header p { font-family:'Source Sans 3',sans-serif; color:var(--mid); margin:0; font-size:1rem; }
.progress-container { background:rgba(255,255,255,0.08); border-radius:8px; height:10px; margin:1rem 0 1.5rem; overflow:hidden; }
.progress-bar { background:linear-gradient(90deg,var(--gold),var(--gold2)); height:100%; border-radius:8px; transition:width .5s ease; }
.q-card { background: linear-gradient(160deg,#112244 0%,#0d1e3a 100%); border: 1px solid rgba(201,168,76,0.3); border-radius: 12px; padding: 1.8rem 2rem; margin-bottom: 1.5rem; box-shadow: 0 4px 24px rgba(0,0,0,0.4); }
.q-number { font-family:'Source Sans 3',sans-serif; color:var(--gold); font-size:.85rem; font-weight:600; letter-spacing:2px; text-transform:uppercase; margin-bottom:.7rem; }
.q-chapter { display:inline-block; background:rgba(201,168,76,0.15); color:var(--gold2); font-size:.75rem; padding:2px 10px; border-radius:20px; border:1px solid rgba(201,168,76,0.3); margin-bottom:.9rem; font-family:'Source Sans 3',sans-serif; }
.q-text { font-family:'Source Sans 3',sans-serif; font-size:1.05rem; line-height:1.65; color:var(--light); margin:0; }
div[data-testid="stRadio"] label p, div[data-testid="stRadio"] label span, div[data-testid="stRadio"] label { font-family: 'Source Sans 3', sans-serif !important; color: #f4f1eb !important; font-size: 1rem !important; }
div[data-testid="stRadio"] > div { gap:.5rem !important; }
.feedback-correct { background:rgba(30,124,74,0.2); border-left:4px solid var(--green); border-radius:8px; padding:1rem 1.2rem; margin-top:1rem; font-family:'Source Sans 3',sans-serif; color:#6fe4a4; }
.feedback-wrong   { background:rgba(155,35,53,0.2);  border-left:4px solid var(--red);   border-radius:8px; padding:1rem 1.2rem; margin-top:1rem; font-family:'Source Sans 3',sans-serif; color:#f4a0a0; }
.feedback-explanation { margin-top:.6rem; color:#c8d4e8; font-size:.93rem; line-height:1.55; }
.score-card { background:linear-gradient(135deg,#112244,#0d1e3a); border:1px solid var(--gold); border-radius:16px; padding:2.5rem; text-align:center; margin:1rem 0; }
.score-big  { font-family:'Playfair Display',serif; font-size:5rem; color:var(--gold); line-height:1; }
.score-label { font-family:'Source Sans 3',sans-serif; color:var(--mid); font-size:1rem; margin-top:.5rem; }
.score-verdict { font-family:'Playfair Display',serif; font-size:1.6rem; margin-top:1.2rem; }
.passed { color:#6fe4a4; } .failed { color:#f4a0a0; }
div[data-testid="stButton"] > button { background: linear-gradient(135deg,var(--gold),#a07828) !important; color: var(--navy) !important; font-family: 'Source Sans 3',sans-serif !important; font-weight: 700 !important; border: none !important; border-radius: 8px !important; padding: .7rem 2rem !important; font-size: 1rem !important; }
div[data-testid="stButton"] > button:hover { opacity:.85 !important; }
.stats-row { display:flex; gap:1rem; justify-content:center; margin:1.5rem 0; flex-wrap:wrap; }
.stat-box { background:rgba(255,255,255,0.06); border:1px solid rgba(201,168,76,0.25); border-radius:10px; padding:.9rem 1.4rem; text-align:center; min-width:120px; }
.stat-num { font-family:'Playfair Display',serif; font-size:2rem; color:var(--gold); }
.stat-lbl { font-family:'Source Sans 3',sans-serif; font-size:.78rem; color:var(--mid); text-transform:uppercase; letter-spacing:1px; }
#MainMenu, footer, header { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

ALL_QUESTIONS = [
    # ── SECTION 1.1 – Why Businesses Perform Business Analysis (25 questions) ──
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "According to BABOK® v3, what is the PRIMARY purpose of business analysis?",
        "options": ["A) To manage project timelines and deliverables","B) To enable change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders","C) To design technical architectures for software systems","D) To audit business processes for regulatory compliance"],
        "answer": "B) To enable change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders",
        "explanation": "BABOK® v3 §1.1 defines BA as the practice of enabling change by defining needs and recommending solutions that deliver value—it is not about managing delivery, designing systems, or auditing."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "Which statement BEST describes what business analysis enables in an organization?",
        "options": ["A) Faster software delivery","B) Change in an enterprise through needs definition and value-delivering solutions","C) Reduction of project management overhead","D) Elimination of stakeholder conflicts"],
        "answer": "B) Change in an enterprise through needs definition and value-delivering solutions",
        "explanation": "BABOK® v3 §1.1: BA enables organizational change—it is not limited to software delivery, PM efficiency, or conflict resolution."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "A company wants to replace its billing system. A BA is asked to determine whether the billing system is truly the root cause of the problem. This BEST illustrates which BA responsibility?",
        "options": ["A) System design","B) Identifying the real need before committing to a solution","C) Project scope management","D) Vendor negotiation"],
        "answer": "B) Identifying the real need before committing to a solution",
        "explanation": "BABOK® v3 §1.1: A core BA responsibility is validating that the proposed solution addresses the actual need rather than accepting a pre-defined solution."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "An organization consistently delivers projects on time and within budget, yet rarely achieves the expected business benefits. The MOST likely root cause is:",
        "options": ["A) Poor project management practices","B) Insufficient business analysis—the right problems are not being defined before solutions are built","C) Inadequate testing processes","D) Weak change management"],
        "answer": "B) Insufficient business analysis—the right problems are not being defined before solutions are built",
        "explanation": "BABOK® v3 §1.1: On-time/on-budget delivery without benefit realization signals that BA is absent or weak—the wrong problems are being solved correctly."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "A BA discovers the real cause of a customer service crisis is an outdated training program, not the CRM system management wants to replace. This MOST directly demonstrates:",
        "options": ["A) Requirements documentation skill","B) Understanding the true need rather than accepting the assumed solution","C) Stakeholder negotiation","D) Technical solution design"],
        "answer": "B) Understanding the true need rather than accepting the assumed solution",
        "explanation": "BABOK® v3 §1.1: BA requires challenging assumed solutions and investigating the real root cause before recommending action."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "Which of the following BEST distinguishes business analysis from project management?",
        "options": ["A) BA focuses on managing scope; PM focuses on managing requirements","B) BA identifies needs and recommends value-delivering solutions; PM manages delivery within constraints of time, cost, and scope","C) BA is performed only at project initiation; PM spans the entire project","D) BA and PM are interchangeable in agile contexts"],
        "answer": "B) BA identifies needs and recommends value-delivering solutions; PM manages delivery within constraints of time, cost, and scope",
        "explanation": "BABOK® v3 §1.1: BA is about 'what and why'—defining the right problem and solution. PM is about 'how'—delivering within constraints. Both disciplines are complementary."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "An organization initiates a $2M project without any business analysis. The delivered system meets all stated requirements but does not improve business performance. This outcome BEST illustrates:",
        "options": ["A) Poor development quality","B) The risk of building correct solutions to the wrong problem due to skipping BA","C) Inadequate testing coverage","D) Weak project governance"],
        "answer": "B) The risk of building correct solutions to the wrong problem due to skipping BA",
        "explanation": "BABOK® v3 §1.1: Without BA, organizations risk correctly building solutions that don't address actual needs—maximizing waste while meeting technical specs."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "A skeptical executive asks a BA to justify the BA function's existence. Which argument is MOST aligned with BABOK® v3?",
        "options": ["A) BA reduces development costs by writing detailed specifications","B) BA ensures investment in change is directed at the right problems and solutions, maximizing business value realization","C) BA prevents scope creep","D) BA provides audit-ready documentation"],
        "answer": "B) BA ensures investment in change is directed at the right problems and solutions, maximizing business value realization",
        "explanation": "BABOK® v3 §1.1: The core value proposition of BA is directing organizational investment toward the right problems and solutions to maximize value—not just producing documents or managing scope."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "According to BABOK® v3, business analysis applies to:",
        "options": ["A) Only IT and software development projects","B) Any initiative where change is being considered, regardless of industry, domain, or methodology","C) Only large enterprises with formal BA departments","D) Only projects with a dedicated BA resource"],
        "answer": "B) Any initiative where change is being considered, regardless of industry, domain, or methodology",
        "explanation": "BABOK® v3 §1.1 explicitly states that BA applies to any change initiative, in any industry, regardless of size or methodology."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "A non-profit is redesigning its volunteer coordination process with no technology component. A BA is assigned. Which statement BEST justifies this?",
        "options": ["A) BA only applies to technology projects","B) BA adds value whenever organizational change is being considered, including purely process-focused initiatives","C) The BA will manage the project","D) BA is required for all non-profit initiatives by regulation"],
        "answer": "B) BA adds value whenever organizational change is being considered, including purely process-focused initiatives",
        "explanation": "BABOK® v3 §1.1: BA is relevant to any change initiative—technology or otherwise—because it ensures the right problem is being solved."
    },

    # ── SECTION 1.2 – Who Performs Business Analysis (15 questions) ──
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Foundational",
        "question": "According to BABOK® v3, who is a business analyst?",
        "options": ["A) Only individuals with 'Business Analyst' in their job title","B) Only CBAP®-certified professionals","C) Any individual who performs the tasks described in the BABOK® Guide, regardless of job title","D) Only employees of the business, not IT or vendors"],
        "answer": "C) Any individual who performs the tasks described in the BABOK® Guide, regardless of job title",
        "explanation": "BABOK® v3 §1.2: BA is defined by the tasks performed, not the title. Anyone performing BA tasks is a BA."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Foundational",
        "question": "Which of the following roles may perform business analysis tasks according to BABOK® v3?",
        "options": ["A) Only dedicated Business Analysts","B) Product Owner, Project Manager, Subject Matter Expert, Consultant, or anyone performing BA tasks","C) Only IT professionals","D) Only senior management"],
        "answer": "B) Product Owner, Project Manager, Subject Matter Expert, Consultant, or anyone performing BA tasks",
        "explanation": "BABOK® v3 §1.2 explicitly recognizes that many titles—PO, PM, SME, consultant, developer—may perform BA tasks."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Intermediate",
        "question": "A product owner writes user stories, defines acceptance criteria, and facilitates backlog refinement. According to BABOK® v3, this person:",
        "options": ["A) Is not performing BA because they lack a BA title","B) Is performing business analysis tasks","C) Needs CBAP® certification to legitimately perform these activities","D) Is performing project management, not business analysis"],
        "answer": "B) Is performing business analysis tasks",
        "explanation": "BABOK® v3 §1.2: BA is defined by tasks, not title. A PO performing BA tasks—user stories, acceptance criteria—is performing BA."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Intermediate",
        "question": "An agile team argues that a dedicated BA role is unnecessary because developers interview customers directly. The BABOK® v3-aligned response is:",
        "options": ["A) Agree—developers can fully replace BA","B) BA tasks may be distributed, but what matters is whether all BA tasks are being performed with sufficient rigor and quality","C) Disagree—only certified BAs can perform BA tasks","D) Defer to the agile coach's decision"],
        "answer": "B) BA tasks may be distributed, but what matters is whether all BA tasks are being performed with sufficient rigor and quality",
        "explanation": "BABOK® v3 §1.2: Distributing BA tasks is acceptable; the question is whether all necessary BA work is being done effectively, regardless of who does it."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Advanced",
        "question": "An organization has no dedicated BA role. Requirements are gathered informally by developers. Which risk does this MOST create?",
        "options": ["A) Development will be slower","B) Solutions may not address actual business needs, wasting investment and reducing value delivery","C) Stakeholders will always be unhappy","D) Projects will always exceed budget"],
        "answer": "B) Solutions may not address actual business needs, wasting investment and reducing value delivery",
        "explanation": "BABOK® v3 §1.1, §1.2: Without rigorous BA tasks, the risk is building solutions to the wrong problems—wasting investment."
    },

    # ── SECTION 1.3 – Knowledge Areas (40 questions) ──
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "How many Knowledge Areas does BABOK® v3 define?",
        "options": ["A) 4","B) 5","C) 6","D) 7"],
        "answer": "C) 6",
        "explanation": "BABOK® v3 §1.3 defines exactly six Knowledge Areas: Business Analysis Planning & Monitoring, Elicitation & Collaboration, Requirements Life Cycle Management, Strategy Analysis, Requirements Analysis & Design Definition, and Solution Evaluation."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area focuses on planning how BA work will be conducted?",
        "options": ["A) Strategy Analysis","B) Elicitation and Collaboration","C) Business Analysis Planning and Monitoring","D) Requirements Life Cycle Management"],
        "answer": "C) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: BA Planning and Monitoring covers planning the BA approach, stakeholder engagement, governance, and performance management."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area is concerned with drawing information out from stakeholders?",
        "options": ["A) Strategy Analysis","B) Elicitation and Collaboration","C) Requirements Analysis and Design Definition","D) Solution Evaluation"],
        "answer": "B) Elicitation and Collaboration",
        "explanation": "BABOK® v3 §1.3: Elicitation and Collaboration focuses on drawing out information from stakeholders and working collaboratively to confirm it."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area involves understanding the business problem and defining the future state?",
        "options": ["A) Business Analysis Planning and Monitoring","B) Requirements Life Cycle Management","C) Strategy Analysis","D) Solution Evaluation"],
        "answer": "C) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Strategy Analysis addresses understanding the business need, current state, future state, and the approach to bridging the gap."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area manages requirements from creation through retirement?",
        "options": ["A) Business Analysis Planning and Monitoring","B) Requirements Life Cycle Management","C) Elicitation and Collaboration","D) Requirements Analysis and Design Definition"],
        "answer": "B) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: RLCM manages requirements through their entire lifecycle including tracing, prioritizing, approving, and managing changes."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area involves specifying and modeling requirements and producing solution designs?",
        "options": ["A) Strategy Analysis","B) Requirements Life Cycle Management","C) Requirements Analysis and Design Definition","D) Solution Evaluation"],
        "answer": "C) Requirements Analysis and Design Definition",
        "explanation": "BABOK® v3 §1.3: RADD covers specifying, modeling, verifying, validating requirements, and defining solution designs."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area assesses whether a solution is delivering the expected business value?",
        "options": ["A) Requirements Analysis and Design Definition","B) Requirements Life Cycle Management","C) Strategy Analysis","D) Solution Evaluation"],
        "answer": "D) Solution Evaluation",
        "explanation": "BABOK® v3 §1.3: Solution Evaluation assesses solution performance against expected value and recommends corrective actions."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA creates a stakeholder register, defines a requirements governance approach, and selects elicitation techniques. Which Knowledge Area is she working in?",
        "options": ["A) Elicitation and Collaboration","B) Strategy Analysis","C) Business Analysis Planning and Monitoring","D) Requirements Life Cycle Management"],
        "answer": "C) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: Stakeholder identification, governance design, and technique selection are planning activities in BA Planning and Monitoring."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA facilitates focus groups, conducts stakeholder interviews, and runs observation sessions. Which Knowledge Area is she PRIMARILY working in?",
        "options": ["A) Business Analysis Planning and Monitoring","B) Elicitation and Collaboration","C) Requirements Analysis and Design Definition","D) Strategy Analysis"],
        "answer": "B) Elicitation and Collaboration",
        "explanation": "BABOK® v3 §1.3: Interviews, focus groups, and observation are elicitation techniques within Elicitation and Collaboration."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA analyzes the current state, identifies capability gaps, and defines the desired future state. Which Knowledge Area does this MOST align with?",
        "options": ["A) Business Analysis Planning and Monitoring","B) Requirements Life Cycle Management","C) Strategy Analysis","D) Elicitation and Collaboration"],
        "answer": "C) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Current-state analysis, gap analysis, and future-state definition are the core activities of Strategy Analysis."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA creates use cases, data flow diagrams, and state diagrams to specify requirements. Which Knowledge Area does this MOST align with?",
        "options": ["A) Elicitation and Collaboration","B) Requirements Life Cycle Management","C) Requirements Analysis and Design Definition","D) Solution Evaluation"],
        "answer": "C) Requirements Analysis and Design Definition",
        "explanation": "BABOK® v3 §1.3: Modeling techniques such as use cases, DFDs, and state diagrams are tools of RADD."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA establishes a traceability matrix and manages a formal change control process for requirements. This MOST aligns with which Knowledge Area?",
        "options": ["A) Business Analysis Planning and Monitoring","B) Requirements Life Cycle Management","C) Requirements Analysis and Design Definition","D) Strategy Analysis"],
        "answer": "B) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Traceability management and change control are core RLCM activities."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "Six months after go-live, a BA measures KPI achievement, user adoption, and identifies improvement opportunities for the deployed system. This MOST aligns with which Knowledge Area?",
        "options": ["A) Strategy Analysis","B) Requirements Analysis and Design Definition","C) Solution Evaluation","D) Requirements Life Cycle Management"],
        "answer": "C) Solution Evaluation",
        "explanation": "BABOK® v3 §1.3: Post-deployment performance measurement and improvement identification is Solution Evaluation work."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA works on all six Knowledge Areas simultaneously on a large transformation program. BABOK® v3 describes this as:",
        "options": ["A) Inappropriate—Knowledge Areas must be executed sequentially","B) Appropriate—Knowledge Areas can be performed in any order, iteratively, and in parallel","C) Only acceptable in agile projects","D) Only possible with multiple BA resources"],
        "answer": "B) Appropriate—Knowledge Areas can be performed in any order, iteratively, and in parallel",
        "explanation": "BABOK® v3 §1.3: Knowledge Areas are not sequential phases—they represent related groups of tasks that may be performed in any order, iteratively, and concurrently."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "An agile team argues that BABOK® v3 Knowledge Areas apply only to waterfall projects. The BEST BABOK-aligned response is:",
        "options": ["A) Agree—BABOK® v3 was written for waterfall","B) Disagree—Knowledge Areas describe BA work that applies across all methodologies; execution is tailored, not applicability","C) Partially agree—only RADD and RLCM apply to agile","D) Defer to the scrum master's judgment"],
        "answer": "B) Disagree—Knowledge Areas describe BA work that applies across all methodologies; execution is tailored, not applicability",
        "explanation": "BABOK® v3 §1.3: All Knowledge Areas apply regardless of methodology. How they are executed may differ, but their relevance does not."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA discovers mid-project that the business objectives have shifted due to a market disruption. She reassesses the current state, redefines the future state, and updates the solution approach. She is working in which Knowledge Area?",
        "options": ["A) Business Analysis Planning and Monitoring","B) Requirements Life Cycle Management","C) Strategy Analysis","D) Elicitation and Collaboration"],
        "answer": "C) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Reassessing current/future states and the solution approach in response to context change is Strategy Analysis."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA is asked which Knowledge Area she is working in when she reviews solution designs for completeness and alignment with requirements. The BEST answer is:",
        "options": ["A) Elicitation and Collaboration","B) Strategy Analysis","C) Requirements Analysis and Design Definition","D) Solution Evaluation"],
        "answer": "C) Requirements Analysis and Design Definition",
        "explanation": "BABOK® v3 §1.3: Reviewing designs for completeness and requirements alignment is an RADD activity."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA discovers that a key assumption is proven false mid-project, requiring reassessment of the entire solution approach. Which Knowledge Areas are MOST likely activated simultaneously?",
        "options": ["A) Only RLCM","B) Strategy Analysis (redefine future state), RLCM (update requirements), and RADD (revise designs)","C) Only Elicitation and Collaboration","D) Only Solution Evaluation"],
        "answer": "B) Strategy Analysis (redefine future state), RLCM (update requirements), and RADD (revise designs)",
        "explanation": "BABOK® v3 §1.3: A major assumption change triggers multiple KAs simultaneously—SA for re-analysis, RLCM for requirements changes, RADD for design updates."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A program manager asks a BA: 'Which Knowledge Area ensures we are solving the right problem?' The MOST accurate answer is:",
        "options": ["A) Business Analysis Planning and Monitoring","B) Requirements Analysis and Design Definition","C) Strategy Analysis","D) Solution Evaluation"],
        "answer": "C) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Strategy Analysis is explicitly focused on understanding whether the organization is addressing the right problem before investing in a solution."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA notices that requirements are frequently added without impact assessment, causing rework. She implements a formal prioritization and change management process. This MOST aligns with which Knowledge Area?",
        "options": ["A) Strategy Analysis","B) Business Analysis Planning and Monitoring","C) Requirements Life Cycle Management","D) Solution Evaluation"],
        "answer": "C) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Prioritization and change management for requirements are RLCM responsibilities."
    },

    # ── SECTION 1.4 – Key Concepts: BACCM (35 questions) ──
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "The Business Analysis Core Concept Model (BACCM) includes which six core concepts?",
        "options": ["A) Change, Need, Solution, Stakeholder, Value, Context","B) Change, Requirement, Design, Risk, Stakeholder, Context","C) Need, Solution, Value, Risk, Change, Constraint","D) Stakeholder, Requirement, Change, Risk, Value, Benefit"],
        "answer": "A) Change, Need, Solution, Stakeholder, Value, Context",
        "explanation": "BABOK® v3 §1.4.1: The six BACCM concepts are Change, Need, Solution, Stakeholder, Value, and Context—no more, no less."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Change' is BEST defined as:",
        "options": ["A) A modification to project scope","B) The act of transformation in response to a need","C) A new IT system","D) Any deviation from the project plan"],
        "answer": "B) The act of transformation in response to a need",
        "explanation": "BABOK® v3 §1.4.1: Change is the act of transformation—the actual movement from one state to another in response to a need."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Need' is BEST defined as:",
        "options": ["A) A stakeholder request or wish","B) A problem or opportunity to be addressed","C) A documented requirement","D) A business rule or constraint"],
        "answer": "B) A problem or opportunity to be addressed",
        "explanation": "BABOK® v3 §1.4.1: A Need is a problem or opportunity—the driver for change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Solution' is BEST defined as:",
        "options": ["A) A software system","B) A specific way of satisfying one or more needs in a context","C) A project deliverable","D) A technical architecture"],
        "answer": "B) A specific way of satisfying one or more needs in a context",
        "explanation": "BABOK® v3 §1.4.1: A Solution is a specific way of satisfying needs within a context—it may be a system, process, product, or service."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Stakeholder' is BEST defined as:",
        "options": ["A) The project sponsor only","B) A group or individual with a relationship to the change, the need, or the solution","C) Only those who directly use the solution","D) Only internal employees"],
        "answer": "B) A group or individual with a relationship to the change, the need, or the solution",
        "explanation": "BABOK® v3 §1.4.1: Stakeholders include any party with a relationship to the change, need, or solution—not just direct users."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Value' is BEST defined as:",
        "options": ["A) Financial return on investment","B) The worth, importance, or usefulness of something to a stakeholder within a context","C) The number of requirements satisfied","D) Technical quality of the solution"],
        "answer": "B) The worth, importance, or usefulness of something to a stakeholder within a context",
        "explanation": "BABOK® v3 §1.4.1: Value is stakeholder-specific and context-dependent—it is not purely financial."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Context' is BEST defined as:",
        "options": ["A) The technical environment","B) The circumstances that influence, are influenced by, and provide understanding of the change","C) The project schedule and budget","D) The organizational chart"],
        "answer": "B) The circumstances that influence, are influenced by, and provide understanding of the change",
        "explanation": "BABOK® v3 §1.4.1: Context encompasses all circumstances—environmental, cultural, regulatory—that surround and influence the change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A bank wants to reduce loan default rates by 20%. This objective BEST represents which BACCM concept?",
        "options": ["A) Change","B) Solution","C) Need","D) Value"],
        "answer": "C) Need",
        "explanation": "BABOK® v3 §1.4.1: A business objective representing a problem to solve or opportunity to capture is a Need."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A new predictive analytics platform is selected to reduce loan defaults. The platform BEST represents which BACCM concept?",
        "options": ["A) Change","B) Solution","C) Need","D) Stakeholder"],
        "answer": "B) Solution",
        "explanation": "BABOK® v3 §1.4.1: The platform—the specific way of satisfying the need—is a Solution."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "The deployment of the analytics platform—moving from no predictive capability to an integrated system—BEST represents which BACCM concept?",
        "options": ["A) Need","B) Solution","C) Change","D) Value"],
        "answer": "C) Change",
        "explanation": "BABOK® v3 §1.4.1: The act of transformation—moving from the current state to the future state—is Change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A new regulation requiring stricter lending disclosures, effective in 6 months, BEST represents which BACCM concept?",
        "options": ["A) Need","B) Change","C) Stakeholder","D) Context"],
        "answer": "D) Context",
        "explanation": "BABOK® v3 §1.4.1: External regulatory factors are part of the Context—the circumstances influencing the change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A BA discovers a technically sound solution was built but did not address the real business problem. Using BACCM terminology, which relationship was misaligned?",
        "options": ["A) Stakeholder and Value","B) Solution and Need","C) Change and Context","D) Value and Stakeholder"],
        "answer": "B) Solution and Need",
        "explanation": "BABOK® v3 §1.4.1: When a solution doesn't address the actual need, the Solution–Need relationship is misaligned."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "All six BACCM concepts are described as interrelated. This means:",
        "options": ["A) Each concept can be analyzed in isolation","B) Understanding any one concept requires considering its relationships to the other five","C) The concepts must be analyzed in a fixed order","D) Only three concepts apply to any given initiative"],
        "answer": "B) Understanding any one concept requires considering its relationships to the other five",
        "explanation": "BABOK® v3 §1.4.1: The BACCM concepts are mutually interrelated—changes in one affect understanding of all others."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A program sponsor defines success as 'delivering the new system on time.' A BA argues success should be 'achieving the intended business outcomes.' This disagreement reflects a misunderstanding of which BACCM concept?",
        "options": ["A) Change","B) Solution","C) Value","D) Context"],
        "answer": "C) Value",
        "explanation": "BABOK® v3 §1.4.1: Value is about business outcomes and worth to stakeholders—not simply delivering a solution on schedule."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A new competitor dramatically changes customer expectations. A BA updates her environmental analysis. Which BACCM concept is she updating?",
        "options": ["A) Need","B) Stakeholder","C) Context","D) Value"],
        "answer": "C) Context",
        "explanation": "BABOK® v3 §1.4.1: Competitive landscape changes are shifts in the Context."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A cost-reduction initiative delivers $2M in savings for shareholders but eliminates 50 jobs. The CFO views it as valuable; laid-off employees do not. This BEST reflects which BACCM principle?",
        "options": ["A) The Need was not properly defined","B) Value is stakeholder-specific—different stakeholders perceive the value of the same change differently","C) The Solution does not meet requirements","D) The Context changed during execution"],
        "answer": "B) Value is stakeholder-specific—different stakeholders perceive the value of the same change differently",
        "explanation": "BABOK® v3 §1.4.1: Value is stakeholder-specific and context-dependent. Different stakeholders will assess the same outcome differently."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA explains to a new team member: 'Every BA task can be described in terms of how it changes or relates to one or more of the six BACCM concepts.' This BEST illustrates that the BACCM is:",
        "options": ["A) A process model for executing BA tasks","B) A universal conceptual framework providing shared vocabulary applicable to all BA work","C) A replacement for the Knowledge Areas","D) Only used during the planning phase"],
        "answer": "B) A universal conceptual framework providing shared vocabulary applicable to all BA work",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is a conceptual lens—not a process—that applies to all BA activities and enables consistent vocabulary."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA identifies a solution that meets all functional requirements but will violate a new regulatory requirement effective next quarter. Which BACCM relationship does this MOST highlight?",
        "options": ["A) Need–Stakeholder misalignment","B) Solution–Context conflict—the solution is not viable within its regulatory context","C) Value–Stakeholder misalignment","D) Change–Need misalignment"],
        "answer": "B) Solution–Context conflict—the solution is not viable within its regulatory context",
        "explanation": "BABOK® v3 §1.4.1: A solution must be viable within its Context, including regulatory and environmental factors."
    },

    # ── SECTION 1.4.4 – Requirements Classification Schema (30 questions) ──
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "BABOK® v3 classifies requirements into four categories. Which option lists them correctly?",
        "options": ["A) Functional, Non-functional, Business, Technical","B) Business, Stakeholder, Solution, Transition","C) Explicit, Implicit, Derived, Assumed","D) Current-state, Future-state, Gap, Design"],
        "answer": "B) Business, Stakeholder, Solution, Transition",
        "explanation": "BABOK® v3 §1.4.4 defines four requirement categories: Business, Stakeholder, Solution (functional + non-functional), and Transition."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Business requirements BEST describe:",
        "options": ["A) What each stakeholder needs from the solution","B) The high-level goals and objectives of the organization","C) How the system must be built technically","D) Temporary needs for the cutover period"],
        "answer": "B) The high-level goals and objectives of the organization",
        "explanation": "BABOK® v3 §1.4.4: Business requirements capture the organization's strategic goals and objectives that drive the initiative."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Stakeholder requirements BEST describe:",
        "options": ["A) The organization's strategic goals","B) The needs of a specific stakeholder or stakeholder class","C) Technical performance metrics","D) Temporary cutover needs"],
        "answer": "B) The needs of a specific stakeholder or stakeholder class",
        "explanation": "BABOK® v3 §1.4.4: Stakeholder requirements capture what specific stakeholders or stakeholder groups need from the solution."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Functional requirements describe:",
        "options": ["A) System performance and quality attributes","B) The behaviors and capabilities the solution must have","C) Temporary cutover needs","D) Strategic business objectives"],
        "answer": "B) The behaviors and capabilities the solution must have",
        "explanation": "BABOK® v3 §1.4.4: Functional requirements define what the solution must do—its behaviors and capabilities."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Non-functional requirements describe:",
        "options": ["A) System features and functions","B) Quality attributes, constraints, and conditions—such as performance, security, and usability","C) Temporary cutover requirements","D) Business objectives"],
        "answer": "B) Quality attributes, constraints, and conditions—such as performance, security, and usability",
        "explanation": "BABOK® v3 §1.4.4: Non-functional requirements define how the solution performs—quality attributes and constraints rather than behaviors."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Transition requirements describe:",
        "options": ["A) Permanent capabilities the solution must have after go-live","B) Capabilities needed only to move from the current state to the future state","C) Stakeholder expectations for the end system","D) High-level business objectives"],
        "answer": "B) Capabilities needed only to move from the current state to the future state",
        "explanation": "BABOK® v3 §1.4.4: Transition requirements are temporary—they exist to support the cutover and are retired once the transition is complete."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'Increase market share in the SMB segment by 15% within two years.' This BEST classifies as:",
        "options": ["A) Stakeholder requirement","B) Business requirement","C) Functional requirement","D) Transition requirement"],
        "answer": "B) Business requirement",
        "explanation": "BABOK® v3 §1.4.4: A high-level organizational goal is a Business requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'As a sales manager, I need a real-time pipeline dashboard showing open deals by stage.' This BEST classifies as:",
        "options": ["A) Business requirement","B) Functional requirement","C) Stakeholder requirement","D) Non-functional requirement"],
        "answer": "C) Stakeholder requirement",
        "explanation": "BABOK® v3 §1.4.4: A specific stakeholder's need is a Stakeholder requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must allow users to generate monthly sales reports filtered by region.' This BEST classifies as:",
        "options": ["A) Business requirement","B) Stakeholder requirement","C) Functional solution requirement","D) Non-functional solution requirement"],
        "answer": "C) Functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: A system capability (generating filtered reports) is a Functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must respond to user queries within 1.5 seconds for 99% of requests under normal load.' This BEST classifies as:",
        "options": ["A) Business requirement","B) Functional requirement","C) Non-functional solution requirement","D) Transition requirement"],
        "answer": "C) Non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Response time is a performance attribute—a Non-functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'All historical customer records from the legacy system must be migrated to the new platform before go-live.' This BEST classifies as:",
        "options": ["A) Business requirement","B) Stakeholder requirement","C) Non-functional requirement","D) Transition requirement"],
        "answer": "D) Transition requirement",
        "explanation": "BABOK® v3 §1.4.4: Data migration needed only for cutover is a Transition requirement—temporary and retired after go-live."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must comply with GDPR data privacy regulations.' This BEST classifies as:",
        "options": ["A) Business requirement","B) Functional requirement","C) Non-functional solution requirement","D) Transition requirement"],
        "answer": "C) Non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Regulatory compliance is a quality/constraint attribute—a Non-functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'Users must complete system training before accessing production.' This BEST classifies as:",
        "options": ["A) Business requirement","B) Stakeholder requirement","C) Functional requirement","D) Transition requirement"],
        "answer": "D) Transition requirement",
        "explanation": "BABOK® v3 §1.4.4: Training required for go-live is a Transition requirement—it supports the cutover, not the ongoing solution."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A BA classifies four items: (A) Reduce operating costs by 10%; (B) Finance team must approve invoices over $50K; (C) System must process 500 invoices per hour; (D) Legacy invoice data must be reformatted before migration. The CORRECT sequence is:",
        "options": ["A) Business, Stakeholder, Non-functional, Transition","B) Stakeholder, Business, Functional, Transition","C) Business, Functional, Non-functional, Transition","D) Business, Stakeholder, Functional, Non-functional"],
        "answer": "A) Business, Stakeholder, Non-functional, Transition",
        "explanation": "BABOK® v3 §1.4.4: A=Business (org goal), B=Stakeholder (finance team need), C=Non-functional (throughput), D=Transition (pre-migration data prep)."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A stakeholder asks: 'Once the new system is live, will we still need the data migration requirement?' The CORRECT answer is:",
        "options": ["A) Yes—it becomes a permanent non-functional requirement","B) No—transition requirements are temporary and retired once the transition is complete","C) Yes—it becomes a business requirement","D) No—it becomes a stakeholder requirement"],
        "answer": "B) No—transition requirements are temporary and retired once the transition is complete",
        "explanation": "BABOK® v3 §1.4.4: Transition requirements are explicitly defined as temporary—needed only to move to the future state, not beyond."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A BA finds requirements in the backlog with no trace to any stakeholder or business requirement. These MOST likely represent:",
        "options": ["A) Non-functional requirements that don't require traceability","B) Scope creep or orphaned requirements that should be assessed for validity","C) Transition requirements that were missed","D) Design constraints added by the architecture team"],
        "answer": "B) Scope creep or orphaned requirements that should be assessed for validity",
        "explanation": "BABOK® v3 §1.4.4: Requirements without upward traceability are potentially orphaned—they may represent scope creep and require review."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "Which statement BEST describes the relationship between stakeholder requirements and business requirements?",
        "options": ["A) They are interchangeable","B) Stakeholder requirements must support and trace back to business requirements","C) Business requirements are derived from stakeholder requirements","D) They are independent and need no alignment"],
        "answer": "B) Stakeholder requirements must support and trace back to business requirements",
        "explanation": "BABOK® v3 §1.4.4: Stakeholder requirements describe how stakeholder needs relate to achieving organizational goals—they must align with and support business requirements."
    },

    # ── SECTION 1.4.5 – Stakeholders (20 questions) ──
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Foundational",
        "question": "According to BABOK® v3, a stakeholder is BEST defined as:",
        "options": ["A) The project sponsor","B) A group or individual with a relationship to the change, the need, or the solution","C) Only direct users of the solution","D) Only internal employees"],
        "answer": "B) A group or individual with a relationship to the change, the need, or the solution",
        "explanation": "BABOK® v3 §1.4.5: Stakeholders are broadly defined—any party with a relationship to the change, need, or solution."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Foundational",
        "question": "Which of the following is a recognized stakeholder type in BABOK® v3?",
        "options": ["A) Only customers and end users","B) Sponsor, Customer, End User, Domain SME, Regulator, Supplier, Tester, Operational Support, BA, and PM","C) Only senior management","D) Only the project team"],
        "answer": "B) Sponsor, Customer, End User, Domain SME, Regulator, Supplier, Tester, Operational Support, BA, and PM",
        "explanation": "BABOK® v3 §1.4.5 lists a comprehensive range of stakeholder types including internal, external, and supporting roles."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A government regulator does not use the system but must approve its outputs. Is this regulator a stakeholder?",
        "options": ["A) No—only direct users are stakeholders","B) No—external parties are not stakeholders","C) Yes—they have a relationship to the change and its outputs","D) Yes—only if they attend project meetings"],
        "answer": "C) Yes—they have a relationship to the change and its outputs",
        "explanation": "BABOK® v3 §1.4.5: Regulators are stakeholders because they have a relationship to the change outcomes, even without direct system usage."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A third-party vendor will integrate their product with the solution being built. They BEST represent which stakeholder type?",
        "options": ["A) End User","B) Sponsor","C) Supplier","D) Domain Subject Matter Expert"],
        "answer": "C) Supplier",
        "explanation": "BABOK® v3 §1.4.5: A vendor providing products or services that integrate with the solution is a Supplier stakeholder."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "The IT operations team will support and maintain the system post-go-live. They BEST represent which stakeholder type?",
        "options": ["A) End User","B) Operational Support","C) Tester","D) Implementation Subject Matter Expert"],
        "answer": "B) Operational Support",
        "explanation": "BABOK® v3 §1.4.5: Teams responsible for post-deployment maintenance and support are Operational Support stakeholders."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "A BA misses the legal department during stakeholder identification. The legal team later raises compliance concerns requiring significant rework. This illustrates the risk of:",
        "options": ["A) Poor requirements documentation","B) Incomplete stakeholder identification leading to missed requirements and late-stage rework","C) Inadequate testing","D) Poor project governance"],
        "answer": "B) Incomplete stakeholder identification leading to missed requirements and late-stage rework",
        "explanation": "BABOK® v3 §1.4.5: Missing stakeholders during identification leads to missed requirements, discovered late when they are costlier to address."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "According to BABOK® v3, the business analyst is also a stakeholder. This means:",
        "options": ["A) The BA should not document their own concerns","B) The BA has a relationship to the change and its outcomes and should be recognized in stakeholder analysis","C) The BA manages all other stakeholders","D) The BA's requirements take priority"],
        "answer": "B) The BA has a relationship to the change and its outcomes and should be recognized in stakeholder analysis",
        "explanation": "BABOK® v3 §1.4.5 explicitly recognizes the BA as a stakeholder with a relationship to the change."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "A BA identifies 15 stakeholder groups, some with high influence/low interest and others with low influence/high interest. This analysis MOST directly informs:",
        "options": ["A) The requirements classification","B) The stakeholder engagement strategy","C) The solution design","D) The project risk register"],
        "answer": "B) The stakeholder engagement strategy",
        "explanation": "BABOK® v3 §1.4.5: Influence/interest analysis informs how and how much to engage each stakeholder group in BA activities."
    },

    # ── SECTION 1.5 – Requirements and Designs (20 questions) ──
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Foundational",
        "question": "According to BABOK® v3, the BEST distinction between requirements and designs is:",
        "options": ["A) Requirements are written by BAs; designs are created by architects","B) Requirements describe what is needed; designs describe how the solution will satisfy the need","C) Requirements are high-level; designs are detailed","D) Requirements are for business; designs are for IT"],
        "answer": "B) Requirements describe what is needed; designs describe how the solution will satisfy the need",
        "explanation": "BABOK® v3 §1.5: Requirements define what is needed (the 'what and why'); designs define how the solution will deliver it (the 'how')."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Intermediate",
        "question": "A BA produces a wireframe showing the layout of a mobile checkout screen. This is BEST classified as:",
        "options": ["A) A stakeholder requirement","B) A design artifact","C) A business requirement","D) A functional requirement"],
        "answer": "B) A design artifact",
        "explanation": "BABOK® v3 §1.5: A wireframe describes how the solution will look—it is a design artifact, not a requirement."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Intermediate",
        "question": "An entity-relationship diagram (ERD) showing the data model for the solution BEST represents:",
        "options": ["A) A business requirement","B) A design artifact describing data structure","C) A stakeholder requirement","D) A non-functional requirement"],
        "answer": "B) A design artifact describing data structure",
        "explanation": "BABOK® v3 §1.5: An ERD defines the data structure of the solution—it is a design artifact."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A development team argues a BPMN future-state process model is a design, not a requirement. The BA argues it is both. Which BABOK® v3 principle supports the BA?",
        "options": ["A) Requirements and designs are always mutually exclusive","B) The same artifact can serve as both a requirement and a design depending on abstraction level and audience","C) Only textual artifacts qualify as requirements","D) Designs are always created after requirements are finalized"],
        "answer": "B) The same artifact can serve as both a requirement and a design depending on abstraction level and audience",
        "explanation": "BABOK® v3 §1.5 acknowledges that artifacts can serve dual purposes depending on the level of abstraction and the audience consuming them."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A BA hands her requirements document directly to developers as the design specification. What risk does this create?",
        "options": ["A) No risk—requirements and designs are the same","B) Requirements (what is needed) may be confused with design (how to build it), unnecessarily constraining the solution space","C) The risk of scope creep","D) The risk of missing stakeholder sign-off"],
        "answer": "B) Requirements (what is needed) may be confused with design (how to build it), unnecessarily constraining the solution space",
        "explanation": "BABOK® v3 §1.5: Treating requirements as design specifications prematurely closes off design options and may lead to suboptimal solutions."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A product owner writes acceptance criteria that specify exact UI element names and pixel layouts. According to BABOK® v3, these criteria MOST represent:",
        "options": ["A) Pure stakeholder requirements","B) Design constraints embedded within acceptance criteria","C) Transition requirements","D) Non-functional requirements"],
        "answer": "B) Design constraints embedded within acceptance criteria",
        "explanation": "BABOK® v3 §1.5: When acceptance criteria prescribe specific implementation details, they cross into design territory, constraining how (not just what) the solution delivers."
    },

    # ── INTEGRATION: Cross-concept scenarios (35 questions) ──
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A BA starts a new project by reviewing organizational strategy, identifying stakeholders, and planning elicitation techniques. According to BABOK® v3, she is working in which Knowledge Area FIRST?",
        "options": ["A) Strategy Analysis","B) Elicitation and Collaboration","C) Business Analysis Planning and Monitoring","D) Requirements Life Cycle Management"],
        "answer": "C) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: Planning BA activities—approach, stakeholder identification, and technique selection—is BA Planning and Monitoring."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A stakeholder says: 'I need the app to be fast.' After probing, the BA establishes this means page loads under 2 seconds for 95% of requests. What transformation occurred?",
        "options": ["A) A business requirement became a transition requirement","B) A vague stakeholder need was refined into a measurable non-functional solution requirement","C) A stakeholder requirement was elevated to a business requirement","D) A functional requirement was rewritten as a design constraint"],
        "answer": "B) A vague stakeholder need was refined into a measurable non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Clarifying a vague quality expectation into a measurable performance criterion produces a non-functional solution requirement."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA realizes requirements reflect what stakeholders asked for but not what they need to achieve the business goal. Which gap exists?",
        "options": ["A) Between stakeholder requirements and transition requirements","B) Between stakeholder requirements and business requirements","C) Between solution requirements and design","D) Between functional and non-functional requirements"],
        "answer": "B) Between stakeholder requirements and business requirements",
        "explanation": "BABOK® v3 §1.4.4: Stakeholder requirements must trace to and support business requirements. A disconnect between them creates a fundamental requirements gap."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A new CRM is deployed. Six months later, customer satisfaction has not improved. A BA is asked to investigate. The MOST appropriate activity is:",
        "options": ["A) Re-elicit all requirements from scratch","B) Conduct solution evaluation to assess whether the solution delivers expected value and identify root causes","C) Update the traceability matrix","D) Escalate to the project sponsor for a new project"],
        "answer": "B) Conduct solution evaluation to assess whether the solution delivers expected value and identify root causes",
        "explanation": "BABOK® v3 §1.3: Post-deployment underperformance is addressed through Solution Evaluation—measuring value delivery and identifying gaps."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA argues that requirements validation cannot be skipped even after the sponsor signs off. The BEST justification is:",
        "options": ["A) The BA's authority supersedes the sponsor's","B) Validation ensures requirements will lead to a solution delivering intended value; sign-off confirms approval, not correctness","C) BABOK® v3 mandates validation regardless of governance","D) Validation is required for compliance"],
        "answer": "B) Validation ensures requirements will lead to a solution delivering intended value; sign-off confirms approval, not correctness",
        "explanation": "BABOK® v3 RLCM: Validation confirms that requirements will lead to value-delivering solutions. Formal approval confirms only that stakeholders agree with the documented content."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA explains BABOK® v3 to a new team: 'This is not a step-by-step process—it is a guide to generally accepted practices.' This reflects which BABOK® v3 principle?",
        "options": ["A) BABOK® v3 provides a prescriptive process that must be followed exactly","B) BABOK® v3 describes generally accepted BA practices that practitioners tailor based on context","C) BABOK® v3 replaces all organizational BA methodologies","D) BABOK® v3 only applies to CBAP® candidates"],
        "answer": "B) BABOK® v3 describes generally accepted BA practices that practitioners tailor based on context",
        "explanation": "BABOK® v3 §1.1: BABOK® v3 is a guide to generally accepted practices—not a prescriptive methodology. Practitioners exercise judgment in applying them."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA produces a complete, approved requirements set. The project delivers on time. But the business fails to achieve its objectives. The MOST likely BA-related root cause is:",
        "options": ["A) Too few requirements were produced","B) Requirements were approved but not aligned with the true Need and expected Value","C) The BA should have managed the project","D) The developers did not follow the requirements"],
        "answer": "B) Requirements were approved but not aligned with the true Need and expected Value",
        "explanation": "BABOK® v3 §1.4.1, §1.4.4: Requirements can be technically approved yet disconnected from the real Need and Value. This is a BA quality failure, not a delivery failure."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA retrospective reveals that requirements were elicited well but were never managed—they were lost, changed without documentation, and became inconsistent. The primary gap is in which Knowledge Area?",
        "options": ["A) Elicitation and Collaboration","B) Strategy Analysis","C) Requirements Life Cycle Management","D) Requirements Analysis and Design Definition"],
        "answer": "C) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Managing requirements through their lifecycle—preventing loss, controlling changes, maintaining consistency—is RLCM."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "An organization has a pattern: business cases are approved without needs analysis, solutions are chosen before problems are defined. The MOST impactful Knowledge Area to strengthen FIRST is:",
        "options": ["A) Elicitation and Collaboration","B) Requirements Analysis and Design Definition","C) Strategy Analysis","D) Requirements Life Cycle Management"],
        "answer": "C) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Choosing solutions before problems are defined is a Strategy Analysis failure. Strengthening SA ensures the right problems are identified before solutions are selected."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA is asked to explain a complete BACCM-based analysis of why a recently delivered solution failed to create value. The MOST complete explanation is:",
        "options": ["A) The project manager failed to deliver","B) The Solution was not aligned with the actual Need, the expected Value was not defined correctly, or the Context changed during delivery","C) Testing was insufficient","D) Requirements were not detailed enough"],
        "answer": "B) The Solution was not aligned with the actual Need, the expected Value was not defined correctly, or the Context changed during delivery",
        "explanation": "BABOK® v3 §1.4.1: A complete BACCM-based explanation covers Solution–Need misalignment, incorrect Value definition, or a Context shift that invalidated the approach."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA explains: 'The six BACCM concepts apply to everything we do. Every task affects or is informed by at least one of them.' This BEST reflects which BABOK® v3 principle?",
        "options": ["A) The BACCM is a process model for BA activities","B) The BACCM provides a universal conceptual framework applicable to all BA tasks","C) The BACCM replaces the Knowledge Areas","D) The BACCM is only used in planning phases"],
        "answer": "B) The BACCM provides a universal conceptual framework applicable to all BA tasks",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is a conceptual lens that applies universally to all BA work—not a process or methodology."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA notices a developer has added features not in the approved requirements baseline. She assesses impact and initiates a formal change request. This MOST aligns with:",
        "options": ["A) Strategy Analysis","B) Elicitation and Collaboration","C) Requirements Life Cycle Management","D) Business Analysis Planning and Monitoring"],
        "answer": "C) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Managing unauthorized additions through formal change control is Requirements Life Cycle Management."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA is challenged: 'Why do we need you when we have project managers?' The MOST BABOK® v3-aligned response is:",
        "options": ["A) BA reduces PM workload","B) BA ensures we solve the right problem before investing in a solution; PM ensures the chosen solution is delivered within constraints—both are essential and complementary","C) BA replaces PM in agile projects","D) BA is only needed for large projects"],
        "answer": "B) BA ensures we solve the right problem before investing in a solution; PM ensures the chosen solution is delivered within constraints—both are essential and complementary",
        "explanation": "BABOK® v3 §1.1: BA and PM are complementary—BA focuses on the right problem and solution; PM focuses on delivering within constraints."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A product manager declares requirements 'done' because all user stories are written. A BA disagrees. What should she do FIRST?",
        "options": ["A) Accept the PM's declaration to avoid conflict","B) Present evidence of elicitation gaps and explain the risk of proceeding with incomplete requirements","C) Escalate directly to the executive sponsor","D) Proceed silently and document concerns privately"],
        "answer": "B) Present evidence of elicitation gaps and explain the risk of proceeding with incomplete requirements",
        "explanation": "BABOK® v3 §2.2, §2.4: Professional ethics and communication skills require the BA to present gaps and risks transparently before proceeding—not to escalate prematurely or stay silent."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA uses the BACCM to onboard a new analyst. She explains each concept in terms of a real initiative. This demonstrates that the BACCM's PRIMARY purpose is:",
        "options": ["A) To provide a checklist of BA tasks","B) To provide a common vocabulary and conceptual framework that helps all team members understand BA work consistently","C) To replace the Knowledge Areas for simpler initiatives","D) To certify BA competency"],
        "answer": "B) To provide a common vocabulary and conceptual framework that helps all team members understand BA work consistently",
        "explanation": "BABOK® v3 §1.4.1: The BACCM's primary purpose is providing a shared vocabulary and conceptual framework for consistent understanding of BA work."
    },
]

# ──────────────────────────────────────────────────────────────
#  SESSION STATE
# ──────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "started": False, "questions": [], "current": 0,
        "answers": {}, "submitted": {}, "finished": False,
        "num_questions": 20, "start_time": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ──────────────────────────────────────────────────────────────
#  HEADER
# ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="exam-header">
    <h1>📋 CBAP® Exam Simulator</h1>
    <p>Chapter 1 — Introduction to Business Analysis · BABOK® v3 · {len(ALL_QUESTIONS)} Questions · Mixed Difficulty</p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
#  START SCREEN
# ──────────────────────────────────────────────────────────────
if not st.session_state.started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style='background:rgba(255,255,255,0.05);border:1px solid rgba(201,168,76,0.3);
                    border-radius:12px;padding:1.8rem;margin-bottom:1.5rem;
                    font-family:"Source Sans 3",sans-serif;color:#c8d4e8;line-height:1.7'>
            <b style='color:#c9a84c;font-size:1.05rem'>📌 Exam Rules</b><br><br>
            • {len(ALL_QUESTIONS)} questions from Chapter 1 of BABOK® v3<br>
            • Covers §1.1 through §1.5 with mixed difficulty levels<br>
            • One attempt per question — confirm before moving on<br>
            • Immediate explanations after each answer<br>
            • Passing score: <b style='color:#f0d080'>70%</b> (CBAP benchmark)
        </div>
        """, unsafe_allow_html=True)

        n = st.slider("Number of questions", min_value=5,
                      max_value=len(ALL_QUESTIONS),
                      value=min(20, len(ALL_QUESTIONS)), step=1)
        st.session_state.num_questions = n

        if st.button("🚀  Start Exam", use_container_width=True):
            pool = ALL_QUESTIONS.copy()
            random.shuffle(pool)
            st.session_state.questions  = pool[:n]
            st.session_state.current    = 0
            st.session_state.answers    = {}
            st.session_state.submitted  = {}
            st.session_state.finished   = False
            st.session_state.started    = True
            st.session_state.start_time = time.time()
            st.rerun()

# ──────────────────────────────────────────────────────────────
#  RESULTS SCREEN
# ──────────────────────────────────────────────────────────────
elif st.session_state.finished:
    qs      = st.session_state.questions
    correct = sum(1 for i, q in enumerate(qs)
                  if st.session_state.answers.get(i) == q["answer"])
    total   = len(qs)
    pct     = round(correct / total * 100)
    elapsed = int(time.time() - (st.session_state.start_time or time.time()))
    mins, secs = divmod(elapsed, 60)
    passed  = pct >= 70

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        vclass = "passed" if passed else "failed"
        vtext  = "✅ PASSED" if passed else "❌ NOT PASSED"
        st.markdown(f"""
        <div class="score-card">
            <div class="score-big">{pct}%</div>
            <div class="score-label">{correct} correct out of {total} questions</div>
            <div class="score-verdict {vclass}">{vtext}</div>
        </div>""", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="stats-row">
            <div class="stat-box"><div class="stat-num">{correct}</div><div class="stat-lbl">Correct</div></div>
            <div class="stat-box"><div class="stat-num">{total-correct}</div><div class="stat-lbl">Incorrect</div></div>
            <div class="stat-box"><div class="stat-num">{mins}:{secs:02d}</div><div class="stat-lbl">Time</div></div>
            <div class="stat-box"><div class="stat-num">{pct}%</div><div class="stat-lbl">Score</div></div>
        </div>""", unsafe_allow_html=True)

        wrong = [(i, q) for i, q in enumerate(qs)
                 if st.session_state.answers.get(i) != q["answer"]]
        if wrong:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander(f"📖  Review {len(wrong)} incorrect answer(s)"):
                for _, (i, q) in enumerate(wrong):
                    user_ans = st.session_state.answers.get(i, "Not answered")
                    st.markdown(f"""
                    <div style='margin-bottom:1.2rem;padding:1rem;background:rgba(155,35,53,0.12);
                                border-radius:8px;border-left:3px solid #9b2335;
                                font-family:"Source Sans 3",sans-serif'>
                        <div style='color:#c9a84c;font-size:.8rem;margin-bottom:.5rem'>Q{i+1} · {q["chapter"]}</div>
                        <div style='color:#f4f1eb;margin-bottom:.7rem'>{q["question"]}</div>
                        <div style='color:#f4a0a0'>❌ Your answer: {user_ans}</div>
                        <div style='color:#6fe4a4'>✅ Correct: {q["answer"]}</div>
                        <div style='color:#c8d4e8;margin-top:.5rem;font-size:.9rem'>💡 {q["explanation"]}</div>
                    </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄  New Exam", use_container_width=True):
            for k in ["started","questions","current","answers","submitted","finished","start_time"]:
                st.session_state.pop(k, None)
            st.rerun()

# ──────────────────────────────────────────────────────────────
#  EXAM SCREEN
# ──────────────────────────────────────────────────────────────
else:
    qs    = st.session_state.questions
    total = len(qs)
    idx   = st.session_state.current
    q     = qs[idx]

    progress_pct = int(idx / total * 100)
    st.markdown(f"""
    <div style='font-family:"Source Sans 3",sans-serif;color:#8090aa;
                font-size:.85rem;display:flex;justify-content:space-between'>
        <span>Question {idx+1} of {total}</span>
        <span>{progress_pct}% complete</span>
    </div>
    <div class="progress-container">
        <div class="progress-bar" style="width:{progress_pct}%"></div>
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="q-card">
        <div class="q-number">Question {idx+1}</div>
        <div class="q-chapter">{q["chapter"]}</div>
        <p class="q-text">{q["question"]}</p>
    </div>""", unsafe_allow_html=True)

    already_submitted = idx in st.session_state.submitted

    if not already_submitted:
        chosen = st.radio("Select your answer:", q["options"],
                          key=f"radio_{idx}", index=None)
        st.session_state.answers[idx] = chosen

        col_a, col_b = st.columns([1, 4])
        with col_a:
            if st.button("✅  Confirm Answer", use_container_width=True):
                if st.session_state.answers.get(idx) is None:
                    st.warning("Please select an answer before confirming.")
                else:
                    st.session_state.submitted[idx] = True
                    st.rerun()
    else:
        user_ans    = st.session_state.answers.get(idx)
        correct_ans = q["answer"]
        is_correct  = user_ans == correct_ans

        for opt in q["options"]:
            if opt == correct_ans:
                color, icon, bg = "#1e7c4a", "✅", "rgba(30,124,74,0.15)"
            elif opt == user_ans and not is_correct:
                color, icon, bg = "#9b2335", "❌", "rgba(155,35,53,0.15)"
            else:
                color, icon, bg = "#8090aa", "○", "transparent"
            st.markdown(f"""
            <div style='padding:.6rem 1rem;margin:.3rem 0;border-radius:8px;
                        background:{bg};border:1px solid {color}33;
                        font-family:"Source Sans 3",sans-serif;color:{color}'>
                {icon} {opt}
            </div>""", unsafe_allow_html=True)

        if is_correct:
            st.markdown(f"""
            <div class="feedback-correct">
                🎯 <b>Correct!</b>
                <div class="feedback-explanation">💡 {q["explanation"]}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="feedback-wrong">
                ❌ <b>Incorrect.</b> Correct answer: <b>{correct_ans}</b>
                <div class="feedback-explanation">💡 {q["explanation"]}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        is_last = idx == total - 1
        col_nav1, col_nav2 = st.columns(2)
        with col_nav1:
            if idx > 0:
                if st.button("⬅  Previous", use_container_width=True):
                    st.session_state.current -= 1
                    st.rerun()
        with col_nav2:
            if is_last:
                if st.button("🏁  Finish Exam", use_container_width=True):
                    st.session_state.finished = True
                    st.rerun()
            else:
                if st.button("Next  ➡", use_container_width=True):
                    st.session_state.current += 1
                    st.rerun()
