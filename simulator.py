import streamlit as st
import random
import time
try:
    from streamlit_autorefresh import st_autorefresh
    HAS_AUTOREFRESH = True
except ImportError:
    HAS_AUTOREFRESH = False

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
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "According to BABOK® v3, what is the PRIMARY purpose of business analysis?",
        "options": [
            "A) To enable change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders",
            "B) To manage project timelines and deliverables",
            "C) To design technical architectures for software systems",
            "D) To audit business processes for regulatory compliance"
        ],
        "answer": "A) To enable change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders",
        "explanation": "BABOK® v3 §1.1 defines BA as the practice of enabling change by defining needs and recommending solutions that deliver value—it is not about managing delivery, designing systems, or auditing."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "Which statement BEST describes what business analysis enables in an organization?",
        "options": [
            "A) Faster software delivery",
            "B) Change in an enterprise through needs definition and value-delivering solutions",
            "C) Reduction of project management overhead",
            "D) Elimination of stakeholder conflicts"
        ],
        "answer": "B) Change in an enterprise through needs definition and value-delivering solutions",
        "explanation": "BABOK® v3 §1.1: BA enables organizational change—it is not limited to software delivery, PM efficiency, or conflict resolution."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "A company wants to replace its billing system. A BA is asked to determine whether the billing system is truly the root cause of the problem. This BEST illustrates which BA responsibility?",
        "options": [
            "A) System design",
            "B) Vendor negotiation",
            "C) Project scope management",
            "D) Identifying the real need before committing to a solution"
        ],
        "answer": "D) Identifying the real need before committing to a solution",
        "explanation": "BABOK® v3 §1.1: A core BA responsibility is validating that the proposed solution addresses the actual need rather than accepting a pre-defined solution."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "An organization consistently delivers projects on time and within budget, yet rarely achieves the expected business benefits. The MOST likely root cause is:",
        "options": [
            "A) Poor project management practices",
            "B) Inadequate testing processes",
            "C) Insufficient business analysis—the right problems are not being defined before solutions are built",
            "D) Weak change management"
        ],
        "answer": "C) Insufficient business analysis—the right problems are not being defined before solutions are built",
        "explanation": "BABOK® v3 §1.1: On-time/on-budget delivery without benefit realization signals that BA is absent or weak—the wrong problems are being solved correctly."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "A BA discovers the real cause of a customer service crisis is an outdated training program, not the CRM system management wants to replace. This MOST directly demonstrates:",
        "options": [
            "A) Requirements documentation skill",
            "B) Technical solution design",
            "C) Stakeholder negotiation",
            "D) Understanding the true need rather than accepting the assumed solution"
        ],
        "answer": "D) Understanding the true need rather than accepting the assumed solution",
        "explanation": "BABOK® v3 §1.1: BA requires challenging assumed solutions and investigating the real root cause before recommending action."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "Which of the following BEST distinguishes business analysis from project management?",
        "options": [
            "A) BA focuses on managing scope; PM focuses on managing requirements",
            "B) BA identifies needs and recommends value-delivering solutions; PM manages delivery within constraints of time, cost, and scope",
            "C) BA is performed only at project initiation; PM spans the entire project",
            "D) BA and PM are interchangeable in agile contexts"
        ],
        "answer": "B) BA identifies needs and recommends value-delivering solutions; PM manages delivery within constraints of time, cost, and scope",
        "explanation": "BABOK® v3 §1.1: BA is about 'what and why'—defining the right problem and solution. PM is about 'how'—delivering within constraints. Both disciplines are complementary."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "Business analysis is described in BABOK® v3 as a practice. What does this imply?",
        "options": [
            "A) It is only applicable in organizations with a formal BA department",
            "B) It must be certified before being applied",
            "C) It requires a specific software toolset",
            "D) It is a professional discipline with defined competencies that can be applied in any organizational context"
        ],
        "answer": "D) It is a professional discipline with defined competencies that can be applied in any organizational context",
        "explanation": "BABOK® v3 §1.1: Describing BA as a 'practice' means it is a professional discipline—applicable broadly, not limited to specific org structures or tools."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "An organization initiates a $2M project without any business analysis. The delivered system meets all stated requirements but does not improve business performance. This outcome BEST illustrates:",
        "options": [
            "A) The risk of building correct solutions to the wrong problem due to skipping BA",
            "B) Poor development quality",
            "C) Inadequate testing coverage",
            "D) Weak project governance"
        ],
        "answer": "A) The risk of building correct solutions to the wrong problem due to skipping BA",
        "explanation": "BABOK® v3 §1.1: Without BA, organizations risk correctly building solutions that don't address actual needs—maximizing waste while meeting technical specs."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "A skeptical executive asks a BA to justify the BA function's existence. Which argument is MOST aligned with BABOK® v3?",
        "options": [
            "A) BA reduces development costs by writing detailed specifications",
            "B) BA provides audit-ready documentation",
            "C) BA prevents scope creep",
            "D) BA ensures investment in change is directed at the right problems and solutions, maximizing business value realization"
        ],
        "answer": "D) BA ensures investment in change is directed at the right problems and solutions, maximizing business value realization",
        "explanation": "BABOK® v3 §1.1: The core value proposition of BA is directing organizational investment toward the right problems and solutions to maximize value—not just producing documents or managing scope."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "According to BABOK® v3, business analysis applies to:",
        "options": [
            "A) Only IT and software development projects",
            "B) Any initiative where change is being considered, regardless of industry, domain, or methodology",
            "C) Only large enterprises with formal BA departments",
            "D) Only projects with a dedicated BA resource"
        ],
        "answer": "B) Any initiative where change is being considered, regardless of industry, domain, or methodology",
        "explanation": "BABOK® v3 §1.1 explicitly states that BA applies to any change initiative, in any industry, regardless of size or methodology."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "A non-profit is redesigning its volunteer coordination process with no technology component. A BA is assigned. Which statement BEST justifies this?",
        "options": [
            "A) BA only applies to technology projects",
            "B) The BA will manage the project",
            "C) BA adds value whenever organizational change is being considered, including purely process-focused initiatives",
            "D) BA is required for all non-profit initiatives by regulation"
        ],
        "answer": "C) BA adds value whenever organizational change is being considered, including purely process-focused initiatives",
        "explanation": "BABOK® v3 §1.1: BA is relevant to any change initiative—technology or otherwise—because it ensures the right problem is being solved."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Advanced",
        "question": "A BA is challenged to explain how BA contributes to organizational strategy. The MOST accurate BABOK® v3-aligned response is:",
        "options": [
            "A) BA executes the strategy by managing projects",
            "B) BA has no role in strategic matters",
            "C) BA replaces strategic planning",
            "D) BA bridges the gap between organizational strategy and tactical execution by ensuring the right needs are identified and addressed"
        ],
        "answer": "D) BA bridges the gap between organizational strategy and tactical execution by ensuring the right needs are identified and addressed",
        "explanation": "BABOK® v3 §1.1: BA links strategy to execution—it ensures that the needs being addressed align with organizational strategic intent."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Foundational",
        "question": "According to BABOK® v3, who is a business analyst?",
        "options": [
            "A) Only individuals with 'Business Analyst' in their job title",
            "B) Only CBAP®-certified professionals",
            "C) Only employees of the business, not IT or vendors",
            "D) Any individual who performs the tasks described in the BABOK® Guide, regardless of job title"
        ],
        "answer": "D) Any individual who performs the tasks described in the BABOK® Guide, regardless of job title",
        "explanation": "BABOK® v3 §1.2: BA is defined by the tasks performed, not the title. Anyone performing BA tasks is a BA."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Foundational",
        "question": "Which of the following roles may perform business analysis tasks according to BABOK® v3?",
        "options": [
            "A) Only dedicated Business Analysts",
            "B) Only senior management",
            "C) Only IT professionals",
            "D) Product Owner, Project Manager, Subject Matter Expert, Consultant, or anyone performing BA tasks"
        ],
        "answer": "D) Product Owner, Project Manager, Subject Matter Expert, Consultant, or anyone performing BA tasks",
        "explanation": "BABOK® v3 §1.2 explicitly recognizes that many titles—PO, PM, SME, consultant, developer—may perform BA tasks."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Intermediate",
        "question": "A product owner writes user stories, defines acceptance criteria, and facilitates backlog refinement. According to BABOK® v3, this person:",
        "options": [
            "A) Is not performing BA because they lack a BA title",
            "B) Is performing business analysis tasks",
            "C) Needs CBAP® certification to legitimately perform these activities",
            "D) Is performing project management, not business analysis"
        ],
        "answer": "B) Is performing business analysis tasks",
        "explanation": "BABOK® v3 §1.2: BA is defined by tasks, not title. A PO performing BA tasks—user stories, acceptance criteria—is performing BA."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Intermediate",
        "question": "An agile team argues that a dedicated BA role is unnecessary because developers interview customers directly. The BABOK® v3-aligned response is:",
        "options": [
            "A) BA tasks may be distributed, but what matters is whether all BA tasks are being performed with sufficient rigor and quality",
            "B) Agree—developers can fully replace BA",
            "C) Disagree—only certified BAs can perform BA tasks",
            "D) Defer to the agile coach's decision"
        ],
        "answer": "A) BA tasks may be distributed, but what matters is whether all BA tasks are being performed with sufficient rigor and quality",
        "explanation": "BABOK® v3 §1.2: Distributing BA tasks is acceptable; the question is whether all necessary BA work is being done effectively, regardless of who does it."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Intermediate",
        "question": "A systems analyst documents current system interfaces, maps data flows, and defines data dictionaries. According to BABOK® v3, they are:",
        "options": [
            "A) Performing IT work unrelated to BA",
            "B) Only performing design work",
            "C) Performing project management tasks",
            "D) Performing business analysis tasks within an IT context"
        ],
        "answer": "D) Performing business analysis tasks within an IT context",
        "explanation": "BABOK® v3 §1.2: Documenting system interfaces, data flows, and data dictionaries are BA tasks, even if performed by a systems analyst role."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Advanced",
        "question": "An organization has no dedicated BA role. Requirements are gathered informally by developers. Which risk does this MOST create?",
        "options": [
            "A) Development will be slower",
            "B) Solutions may not address actual business needs, wasting investment and reducing value delivery",
            "C) Stakeholders will always be unhappy",
            "D) Projects will always exceed budget"
        ],
        "answer": "B) Solutions may not address actual business needs, wasting investment and reducing value delivery",
        "explanation": "BABOK® v3 §1.1, §1.2: Without rigorous BA tasks, the risk is building solutions to the wrong problems—wasting investment."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Advanced",
        "question": "A consulting firm assigns a management consultant to lead requirements elicitation on a transformation program. That consultant performs all BA tasks listed in BABOK® v3. According to BABOK® v3, this consultant is:",
        "options": [
            "A) Not a BA because they work for a consulting firm",
            "B) A BA for the purposes of that engagement",
            "C) A project manager performing BA tasks incorrectly",
            "D) Not qualified without CBAP® certification"
        ],
        "answer": "B) A BA for the purposes of that engagement",
        "explanation": "BABOK® v3 §1.2: BA is defined by task performance. A consultant performing all BA tasks is functioning as a BA regardless of their firm or title."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "How many Knowledge Areas does BABOK® v3 define?",
        "options": [
            "A) 4",
            "B) 5",
            "C) 6",
            "D) 7"
        ],
        "answer": "C) 6",
        "explanation": "BABOK® v3 §1.3 defines exactly six Knowledge Areas: Business Analysis Planning & Monitoring, Elicitation & Collaboration, Requirements Life Cycle Management, Strategy Analysis, Requirements Analysis & Design Definition, and Solution Evaluation."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area focuses on planning how BA work will be conducted?",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Elicitation and Collaboration",
            "C) Strategy Analysis",
            "D) Requirements Life Cycle Management"
        ],
        "answer": "A) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: BA Planning and Monitoring covers planning the BA approach, stakeholder engagement, governance, and performance management."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area is concerned with drawing information out from stakeholders?",
        "options": [
            "A) Strategy Analysis",
            "B) Elicitation and Collaboration",
            "C) Requirements Analysis and Design Definition",
            "D) Solution Evaluation"
        ],
        "answer": "B) Elicitation and Collaboration",
        "explanation": "BABOK® v3 §1.3: Elicitation and Collaboration focuses on drawing out information from stakeholders and working collaboratively to confirm it."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area involves understanding the business problem and defining the future state?",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Requirements Life Cycle Management",
            "C) Strategy Analysis",
            "D) Solution Evaluation"
        ],
        "answer": "C) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Strategy Analysis addresses understanding the business need, current state, future state, and the approach to bridging the gap."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area manages requirements from creation through retirement?",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Requirements Life Cycle Management",
            "C) Elicitation and Collaboration",
            "D) Requirements Analysis and Design Definition"
        ],
        "answer": "B) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: RLCM manages requirements through their entire lifecycle including tracing, prioritizing, approving, and managing changes."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area involves specifying and modeling requirements and producing solution designs?",
        "options": [
            "A) Strategy Analysis",
            "B) Requirements Life Cycle Management",
            "C) Requirements Analysis and Design Definition",
            "D) Solution Evaluation"
        ],
        "answer": "C) Requirements Analysis and Design Definition",
        "explanation": "BABOK® v3 §1.3: RADD covers specifying, modeling, verifying, validating requirements, and defining solution designs."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "Which Knowledge Area assesses whether a solution is delivering the expected business value?",
        "options": [
            "A) Solution Evaluation",
            "B) Requirements Life Cycle Management",
            "C) Strategy Analysis",
            "D) Requirements Analysis and Design Definition"
        ],
        "answer": "A) Solution Evaluation",
        "explanation": "BABOK® v3 §1.3: Solution Evaluation assesses solution performance against expected value and recommends corrective actions."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA creates a stakeholder register, defines a requirements governance approach, and selects elicitation techniques. Which Knowledge Area is she working in?",
        "options": [
            "A) Elicitation and Collaboration",
            "B) Business Analysis Planning and Monitoring",
            "C) Strategy Analysis",
            "D) Requirements Life Cycle Management"
        ],
        "answer": "B) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: Stakeholder identification, governance design, and technique selection are planning activities in BA Planning and Monitoring."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA facilitates focus groups, conducts stakeholder interviews, and runs observation sessions. Which Knowledge Area is she PRIMARILY working in?",
        "options": [
            "A) Elicitation and Collaboration",
            "B) Business Analysis Planning and Monitoring",
            "C) Requirements Analysis and Design Definition",
            "D) Strategy Analysis"
        ],
        "answer": "A) Elicitation and Collaboration",
        "explanation": "BABOK® v3 §1.3: Interviews, focus groups, and observation are elicitation techniques within Elicitation and Collaboration."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA analyzes the current state, identifies capability gaps, and defines the desired future state. Which Knowledge Area does this MOST align with?",
        "options": [
            "A) Strategy Analysis",
            "B) Requirements Life Cycle Management",
            "C) Business Analysis Planning and Monitoring",
            "D) Elicitation and Collaboration"
        ],
        "answer": "A) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Current-state analysis, gap analysis, and future-state definition are the core activities of Strategy Analysis."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA creates use cases, data flow diagrams, and state diagrams to specify requirements. Which Knowledge Area does this MOST align with?",
        "options": [
            "A) Elicitation and Collaboration",
            "B) Requirements Life Cycle Management",
            "C) Requirements Analysis and Design Definition",
            "D) Solution Evaluation"
        ],
        "answer": "C) Requirements Analysis and Design Definition",
        "explanation": "BABOK® v3 §1.3: Modeling techniques such as use cases, DFDs, and state diagrams are tools of RADD."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA establishes a traceability matrix and manages a formal change control process for requirements. This MOST aligns with which Knowledge Area?",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Strategy Analysis",
            "C) Requirements Analysis and Design Definition",
            "D) Requirements Life Cycle Management"
        ],
        "answer": "D) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Traceability management and change control are core RLCM activities."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "Six months after go-live, a BA measures KPI achievement, user adoption, and identifies improvement opportunities for the deployed system. This MOST aligns with which Knowledge Area?",
        "options": [
            "A) Strategy Analysis",
            "B) Solution Evaluation",
            "C) Requirements Analysis and Design Definition",
            "D) Requirements Life Cycle Management"
        ],
        "answer": "B) Solution Evaluation",
        "explanation": "BABOK® v3 §1.3: Post-deployment performance measurement and improvement identification is Solution Evaluation work."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "A BA is preparing a BA work plan that includes activity schedules, resource needs, and performance metrics for the BA function itself. This activity MOST aligns with:",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Strategy Analysis",
            "C) Requirements Life Cycle Management",
            "D) Solution Evaluation"
        ],
        "answer": "A) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: Planning BA activities, resources, and monitoring BA performance are core tasks in BA Planning and Monitoring."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA works on all six Knowledge Areas simultaneously on a large transformation program. BABOK® v3 describes this as:",
        "options": [
            "A) Inappropriate—Knowledge Areas must be executed sequentially",
            "B) Only possible with multiple BA resources",
            "C) Only acceptable in agile projects",
            "D) Appropriate—Knowledge Areas can be performed in any order, iteratively, and in parallel"
        ],
        "answer": "D) Appropriate—Knowledge Areas can be performed in any order, iteratively, and in parallel",
        "explanation": "BABOK® v3 §1.3: Knowledge Areas are not sequential phases—they represent related groups of tasks that may be performed in any order, iteratively, and concurrently."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "An agile team argues that BABOK® v3 Knowledge Areas apply only to waterfall projects. The BEST BABOK-aligned response is:",
        "options": [
            "A) Agree—BABOK® v3 was written for waterfall",
            "B) Defer to the scrum master's judgment",
            "C) Partially agree—only RADD and RLCM apply to agile",
            "D) Disagree—Knowledge Areas describe BA work that applies across all methodologies; execution is tailored, not applicability"
        ],
        "answer": "D) Disagree—Knowledge Areas describe BA work that applies across all methodologies; execution is tailored, not applicability",
        "explanation": "BABOK® v3 §1.3: All Knowledge Areas apply regardless of methodology. How they are executed may differ, but their relevance does not."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA discovers mid-project that the business objectives have shifted due to a market disruption. She reassesses the current state, redefines the future state, and updates the solution approach. She is working in which Knowledge Area?",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Strategy Analysis",
            "C) Requirements Life Cycle Management",
            "D) Elicitation and Collaboration"
        ],
        "answer": "B) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Reassessing current/future states and the solution approach in response to context change is Strategy Analysis."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA is asked which Knowledge Area she is working in when she reviews solution designs for completeness and alignment with requirements. The BEST answer is:",
        "options": [
            "A) Elicitation and Collaboration",
            "B) Requirements Analysis and Design Definition",
            "C) Strategy Analysis",
            "D) Solution Evaluation"
        ],
        "answer": "B) Requirements Analysis and Design Definition",
        "explanation": "BABOK® v3 §1.3: Reviewing designs for completeness and requirements alignment is an RADD activity."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA discovers that a key assumption is proven false mid-project, requiring reassessment of the entire solution approach. Which Knowledge Areas are MOST likely activated simultaneously?",
        "options": [
            "A) Only RLCM",
            "B) Only Elicitation and Collaboration",
            "C) Strategy Analysis (redefine future state), RLCM (update requirements), and RADD (revise designs)",
            "D) Only Solution Evaluation"
        ],
        "answer": "C) Strategy Analysis (redefine future state), RLCM (update requirements), and RADD (revise designs)",
        "explanation": "BABOK® v3 §1.3: A major assumption change triggers multiple KAs simultaneously—SA for re-analysis, RLCM for requirements changes, RADD for design updates."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A program manager asks a BA: 'Which Knowledge Area ensures we are solving the right problem?' The MOST accurate answer is:",
        "options": [
            "A) Business Analysis Planning and Monitoring",
            "B) Strategy Analysis",
            "C) Requirements Analysis and Design Definition",
            "D) Solution Evaluation"
        ],
        "answer": "B) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Strategy Analysis is explicitly focused on understanding whether the organization is addressing the right problem before investing in a solution."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "A BA notices that requirements are frequently added without impact assessment, causing rework. She implements a formal prioritization and change management process. This MOST aligns with which Knowledge Area?",
        "options": [
            "A) Requirements Life Cycle Management",
            "B) Business Analysis Planning and Monitoring",
            "C) Strategy Analysis",
            "D) Solution Evaluation"
        ],
        "answer": "A) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Prioritization and change management for requirements are RLCM responsibilities."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "Which statement MOST accurately characterizes the relationship between the six Knowledge Areas in BABOK® v3?",
        "options": [
            "A) They form a sequential process that must be followed from start to finish",
            "B) They are interrelated groups of tasks that collectively represent the scope of BA work",
            "C) They are independent and can each be applied without reference to the others",
            "D) They are mutually exclusive—work done in one cannot relate to another"
        ],
        "answer": "B) They are interrelated groups of tasks that collectively represent the scope of BA work",
        "explanation": "BABOK® v3 §1.3: Knowledge Areas are interrelated, not independent or sequential—inputs and outputs flow between them continuously."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "The Business Analysis Core Concept Model (BACCM) includes which six core concepts?",
        "options": [
            "A) Stakeholder, Requirement, Change, Risk, Value, Benefit",
            "B) Change, Requirement, Design, Risk, Stakeholder, Context",
            "C) Need, Solution, Value, Risk, Change, Constraint",
            "D) Change, Need, Solution, Stakeholder, Value, Context"
        ],
        "answer": "D) Change, Need, Solution, Stakeholder, Value, Context",
        "explanation": "BABOK® v3 §1.4.1: The six BACCM concepts are Change, Need, Solution, Stakeholder, Value, and Context—no more, no less."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Change' is BEST defined as:",
        "options": [
            "A) A modification to project scope",
            "B) The act of transformation in response to a need",
            "C) A new IT system",
            "D) Any deviation from the project plan"
        ],
        "answer": "B) The act of transformation in response to a need",
        "explanation": "BABOK® v3 §1.4.1: Change is the act of transformation—the actual movement from one state to another in response to a need."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Need' is BEST defined as:",
        "options": [
            "A) A stakeholder request or wish",
            "B) A business rule or constraint",
            "C) A documented requirement",
            "D) A problem or opportunity to be addressed"
        ],
        "answer": "D) A problem or opportunity to be addressed",
        "explanation": "BABOK® v3 §1.4.1: A Need is a problem or opportunity—the driver for change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Solution' is BEST defined as:",
        "options": [
            "A) A software system",
            "B) A project deliverable",
            "C) A specific way of satisfying one or more needs in a context",
            "D) A technical architecture"
        ],
        "answer": "C) A specific way of satisfying one or more needs in a context",
        "explanation": "BABOK® v3 §1.4.1: A Solution is a specific way of satisfying needs within a context—it may be a system, process, product, or service."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Stakeholder' is BEST defined as:",
        "options": [
            "A) A group or individual with a relationship to the change, the need, or the solution",
            "B) The project sponsor only",
            "C) Only those who directly use the solution",
            "D) Only internal employees"
        ],
        "answer": "A) A group or individual with a relationship to the change, the need, or the solution",
        "explanation": "BABOK® v3 §1.4.1: Stakeholders include any party with a relationship to the change, need, or solution—not just direct users."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Value' is BEST defined as:",
        "options": [
            "A) Financial return on investment",
            "B) The number of requirements satisfied",
            "C) The worth, importance, or usefulness of something to a stakeholder within a context",
            "D) Technical quality of the solution"
        ],
        "answer": "C) The worth, importance, or usefulness of something to a stakeholder within a context",
        "explanation": "BABOK® v3 §1.4.1: Value is stakeholder-specific and context-dependent—it is not purely financial."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "In the BACCM, 'Context' is BEST defined as:",
        "options": [
            "A) The technical environment",
            "B) The organizational chart",
            "C) The project schedule and budget",
            "D) The circumstances that influence, are influenced by, and provide understanding of the change"
        ],
        "answer": "D) The circumstances that influence, are influenced by, and provide understanding of the change",
        "explanation": "BABOK® v3 §1.4.1: Context encompasses all circumstances—environmental, cultural, regulatory—that surround and influence the change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A bank wants to reduce loan default rates by 20%. This objective BEST represents which BACCM concept?",
        "options": [
            "A) Need",
            "B) Solution",
            "C) Change",
            "D) Value"
        ],
        "answer": "A) Need",
        "explanation": "BABOK® v3 §1.4.1: A business objective representing a problem to solve or opportunity to capture is a Need."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A new predictive analytics platform is selected to reduce loan defaults. The platform BEST represents which BACCM concept?",
        "options": [
            "A) Change",
            "B) Stakeholder",
            "C) Need",
            "D) Solution"
        ],
        "answer": "D) Solution",
        "explanation": "BABOK® v3 §1.4.1: The platform—the specific way of satisfying the need—is a Solution."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "The deployment of the analytics platform—moving from no predictive capability to an integrated system—BEST represents which BACCM concept?",
        "options": [
            "A) Change",
            "B) Solution",
            "C) Need",
            "D) Value"
        ],
        "answer": "A) Change",
        "explanation": "BABOK® v3 §1.4.1: The act of transformation—moving from the current state to the future state—is Change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A new regulation requiring stricter lending disclosures, effective in 6 months, BEST represents which BACCM concept?",
        "options": [
            "A) Need",
            "B) Change",
            "C) Stakeholder",
            "D) Context"
        ],
        "answer": "D) Context",
        "explanation": "BABOK® v3 §1.4.1: External regulatory factors are part of the Context—the circumstances influencing the change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A BA discovers a technically sound solution was built but did not address the real business problem. Using BACCM terminology, which relationship was misaligned?",
        "options": [
            "A) Solution and Need",
            "B) Stakeholder and Value",
            "C) Change and Context",
            "D) Value and Stakeholder"
        ],
        "answer": "A) Solution and Need",
        "explanation": "BABOK® v3 §1.4.1: When a solution doesn't address the actual need, the Solution–Need relationship is misaligned."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "All six BACCM concepts are described as interrelated. This means:",
        "options": [
            "A) Each concept can be analyzed in isolation",
            "B) Only three concepts apply to any given initiative",
            "C) The concepts must be analyzed in a fixed order",
            "D) Understanding any one concept requires considering its relationships to the other five"
        ],
        "answer": "D) Understanding any one concept requires considering its relationships to the other five",
        "explanation": "BABOK® v3 §1.4.1: The BACCM concepts are mutually interrelated—changes in one affect understanding of all others."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "An insurance company's customers are BEST represented by which BACCM concept when they will directly use the new claims portal?",
        "options": [
            "A) Context",
            "B) Value",
            "C) Stakeholder",
            "D) Need"
        ],
        "answer": "C) Stakeholder",
        "explanation": "BABOK® v3 §1.4.1: End users who interact with the solution are Stakeholders—they have a relationship to the change and the solution."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "Reduced claims processing time from 10 days to 2 days for the insurance company's customers BEST represents which BACCM concept?",
        "options": [
            "A) Need",
            "B) Change",
            "C) Value",
            "D) Solution"
        ],
        "answer": "C) Value",
        "explanation": "BABOK® v3 §1.4.1: The benefit (faster processing) delivered to stakeholders is Value—the worth or usefulness of the solution."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A program sponsor defines success as 'delivering the new system on time.' A BA argues success should be 'achieving the intended business outcomes.' This disagreement reflects a misunderstanding of which BACCM concept?",
        "options": [
            "A) Change",
            "B) Value",
            "C) Solution",
            "D) Context"
        ],
        "answer": "B) Value",
        "explanation": "BABOK® v3 §1.4.1: Value is about business outcomes and worth to stakeholders—not simply delivering a solution on schedule."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A new competitor dramatically changes customer expectations. A BA updates her environmental analysis. Which BACCM concept is she updating?",
        "options": [
            "A) Context",
            "B) Stakeholder",
            "C) Need",
            "D) Value"
        ],
        "answer": "A) Context",
        "explanation": "BABOK® v3 §1.4.1: Competitive landscape changes are shifts in the Context."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A cost-reduction initiative delivers $2M in savings for shareholders but eliminates 50 jobs. The CFO views it as valuable; laid-off employees do not. This BEST reflects which BACCM principle?",
        "options": [
            "A) The Need was not properly defined",
            "B) Value is stakeholder-specific—different stakeholders perceive the value of the same change differently",
            "C) The Solution does not meet requirements",
            "D) The Context changed during execution"
        ],
        "answer": "B) Value is stakeholder-specific—different stakeholders perceive the value of the same change differently",
        "explanation": "BABOK® v3 §1.4.1: Value is stakeholder-specific and context-dependent. Different stakeholders will assess the same outcome differently."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA explains to a new team member: 'Every BA task can be described in terms of how it changes or relates to one or more of the six BACCM concepts.' This BEST illustrates that the BACCM is:",
        "options": [
            "A) A process model for executing BA tasks",
            "B) A replacement for the Knowledge Areas",
            "C) A universal conceptual framework providing shared vocabulary applicable to all BA work",
            "D) Only used during the planning phase"
        ],
        "answer": "C) A universal conceptual framework providing shared vocabulary applicable to all BA work",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is a conceptual lens—not a process—that applies to all BA activities and enables consistent vocabulary."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA identifies a solution that meets all functional requirements but will violate a new regulatory requirement effective next quarter. Which BACCM relationship does this MOST highlight?",
        "options": [
            "A) Need–Stakeholder misalignment",
            "B) Value–Stakeholder misalignment",
            "C) Solution–Context conflict—the solution is not viable within its regulatory context",
            "D) Change–Need misalignment"
        ],
        "answer": "C) Solution–Context conflict—the solution is not viable within its regulatory context",
        "explanation": "BABOK® v3 §1.4.1: A solution must be viable within its Context, including regulatory and environmental factors."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA uses the BACCM framework to explain to a new junior analyst why requirements cannot be defined in isolation. The MOST relevant BACCM principle is:",
        "options": [
            "A) Every BA task relates to at least one BACCM concept, and the concepts are interrelated—isolating any one leads to incomplete understanding",
            "B) Requirements must always be traceable to test cases",
            "C) Requirements are only written by BAs",
            "D) Requirements define the solution architecture"
        ],
        "answer": "A) Every BA task relates to at least one BACCM concept, and the concepts are interrelated—isolating any one leads to incomplete understanding",
        "explanation": "BABOK® v3 §1.4.1: The BACCM's interrelated nature means no single concept—or requirement—can be fully understood without considering its relationship to the others."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA notices that the organization's definition of 'success' for a project has never been agreed upon. Using BACCM language, what is missing?",
        "options": [
            "A) A formally documented Solution",
            "B) A Stakeholder register",
            "C) A shared understanding of Value—what worth or benefit the change is expected to deliver to stakeholders",
            "D) A defined Change management process"
        ],
        "answer": "C) A shared understanding of Value—what worth or benefit the change is expected to deliver to stakeholders",
        "explanation": "BABOK® v3 §1.4.1: Without a shared definition of Value, the organization cannot assess whether the change succeeded in delivering what was needed."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "BABOK® v3 classifies requirements into four categories. Which option lists them correctly?",
        "options": [
            "A) Business, Stakeholder, Solution, Transition",
            "B) Functional, Non-functional, Business, Technical",
            "C) Explicit, Implicit, Derived, Assumed",
            "D) Current-state, Future-state, Gap, Design"
        ],
        "answer": "A) Business, Stakeholder, Solution, Transition",
        "explanation": "BABOK® v3 §1.4.4 defines four requirement categories: Business, Stakeholder, Solution (functional + non-functional), and Transition."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Business requirements BEST describe:",
        "options": [
            "A) The high-level goals and objectives of the organization",
            "B) What each stakeholder needs from the solution",
            "C) How the system must be built technically",
            "D) Temporary needs for the cutover period"
        ],
        "answer": "A) The high-level goals and objectives of the organization",
        "explanation": "BABOK® v3 §1.4.4: Business requirements capture the organization's strategic goals and objectives that drive the initiative."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Stakeholder requirements BEST describe:",
        "options": [
            "A) The organization's strategic goals",
            "B) Technical performance metrics",
            "C) The needs of a specific stakeholder or stakeholder class",
            "D) Temporary cutover needs"
        ],
        "answer": "C) The needs of a specific stakeholder or stakeholder class",
        "explanation": "BABOK® v3 §1.4.4: Stakeholder requirements capture what specific stakeholders or stakeholder groups need from the solution."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Functional requirements describe:",
        "options": [
            "A) System performance and quality attributes",
            "B) Strategic business objectives",
            "C) Temporary cutover needs",
            "D) The behaviors and capabilities the solution must have"
        ],
        "answer": "D) The behaviors and capabilities the solution must have",
        "explanation": "BABOK® v3 §1.4.4: Functional requirements define what the solution must do—its behaviors and capabilities."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Non-functional requirements describe:",
        "options": [
            "A) System features and functions",
            "B) Quality attributes, constraints, and conditions—such as performance, security, and usability",
            "C) Temporary cutover requirements",
            "D) Business objectives"
        ],
        "answer": "B) Quality attributes, constraints, and conditions—such as performance, security, and usability",
        "explanation": "BABOK® v3 §1.4.4: Non-functional requirements define how the solution performs—quality attributes and constraints rather than behaviors."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Transition requirements describe:",
        "options": [
            "A) Permanent capabilities the solution must have after go-live",
            "B) Stakeholder expectations for the end system",
            "C) Capabilities needed only to move from the current state to the future state",
            "D) High-level business objectives"
        ],
        "answer": "C) Capabilities needed only to move from the current state to the future state",
        "explanation": "BABOK® v3 §1.4.4: Transition requirements are temporary—they exist to support the cutover and are retired once the transition is complete."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "Solution requirements are subdivided into which two types in BABOK® v3?",
        "options": [
            "A) Business and Stakeholder",
            "B) Functional and Non-functional",
            "C) Explicit and Implicit",
            "D) Transition and Operational"
        ],
        "answer": "B) Functional and Non-functional",
        "explanation": "BABOK® v3 §1.4.4: Solution requirements consist of Functional requirements (behaviors/capabilities) and Non-functional requirements (quality attributes/constraints)."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'Increase market share in the SMB segment by 15% within two years.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Stakeholder requirement",
            "C) Functional requirement",
            "D) Transition requirement"
        ],
        "answer": "A) Business requirement",
        "explanation": "BABOK® v3 §1.4.4: A high-level organizational goal is a Business requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'As a sales manager, I need a real-time pipeline dashboard showing open deals by stage.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Functional requirement",
            "C) Non-functional requirement",
            "D) Stakeholder requirement"
        ],
        "answer": "D) Stakeholder requirement",
        "explanation": "BABOK® v3 §1.4.4: A specific stakeholder's need is a Stakeholder requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must allow users to generate monthly sales reports filtered by region.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Stakeholder requirement",
            "C) Functional solution requirement",
            "D) Non-functional solution requirement"
        ],
        "answer": "C) Functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: A system capability (generating filtered reports) is a Functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must respond to user queries within 1.5 seconds for 99% of requests under normal load.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Non-functional solution requirement",
            "C) Functional requirement",
            "D) Transition requirement"
        ],
        "answer": "B) Non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Response time is a performance attribute—a Non-functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'All historical customer records from the legacy system must be migrated to the new platform before go-live.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Stakeholder requirement",
            "C) Non-functional requirement",
            "D) Transition requirement"
        ],
        "answer": "D) Transition requirement",
        "explanation": "BABOK® v3 §1.4.4: Data migration needed only for cutover is a Transition requirement—temporary and retired after go-live."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must comply with GDPR data privacy regulations.' This BEST classifies as:",
        "options": [
            "A) Non-functional solution requirement",
            "B) Functional requirement",
            "C) Business requirement",
            "D) Transition requirement"
        ],
        "answer": "A) Non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Regulatory compliance is a quality/constraint attribute—a Non-functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'Users must complete system training before accessing production.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Stakeholder requirement",
            "C) Functional requirement",
            "D) Transition requirement"
        ],
        "answer": "D) Transition requirement",
        "explanation": "BABOK® v3 §1.4.4: Training required for go-live is a Transition requirement—it supports the cutover, not the ongoing solution."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'The system must be available 99.9% of the time during business hours.' This BEST classifies as:",
        "options": [
            "A) Functional requirement",
            "B) Business requirement",
            "C) Stakeholder requirement",
            "D) Non-functional solution requirement"
        ],
        "answer": "D) Non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: System availability is a reliability attribute—a Non-functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "'Achieve cost savings of €500,000 per year by automating invoice processing.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Functional requirement",
            "C) Stakeholder requirement",
            "D) Transition requirement"
        ],
        "answer": "A) Business requirement",
        "explanation": "BABOK® v3 §1.4.4: An organizational cost-savings target is a Business requirement—it states the 'why' of the initiative."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A BA classifies four items: (A) Reduce operating costs by 10%; (B) Finance team must approve invoices over $50K; (C) System must process 500 invoices per hour; (D) Legacy invoice data must be reformatted before migration. The CORRECT sequence is:",
        "options": [
            "A) Business, Stakeholder, Functional, Non-functional",
            "B) Stakeholder, Business, Functional, Transition",
            "C) Business, Functional, Non-functional, Transition",
            "D) Business, Stakeholder, Non-functional, Transition"
        ],
        "answer": "D) Business, Stakeholder, Non-functional, Transition",
        "explanation": "BABOK® v3 §1.4.4: A=Business (org goal), B=Stakeholder (finance team need), C=Non-functional (throughput), D=Transition (pre-migration data prep)."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A stakeholder asks: 'Once the new system is live, will we still need the data migration requirement?' The CORRECT answer is:",
        "options": [
            "A) Yes—it becomes a permanent non-functional requirement",
            "B) No—it becomes a stakeholder requirement",
            "C) Yes—it becomes a business requirement",
            "D) No—transition requirements are temporary and retired once the transition is complete"
        ],
        "answer": "D) No—transition requirements are temporary and retired once the transition is complete",
        "explanation": "BABOK® v3 §1.4.4: Transition requirements are explicitly defined as temporary—needed only to move to the future state, not beyond."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A BA finds requirements in the backlog with no trace to any stakeholder or business requirement. These MOST likely represent:",
        "options": [
            "A) Non-functional requirements that don't require traceability",
            "B) Transition requirements that were missed",
            "C) Scope creep or orphaned requirements that should be assessed for validity",
            "D) Design constraints added by the architecture team"
        ],
        "answer": "C) Scope creep or orphaned requirements that should be assessed for validity",
        "explanation": "BABOK® v3 §1.4.4: Requirements without upward traceability are potentially orphaned—they may represent scope creep and require review."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "Which statement BEST describes the relationship between stakeholder requirements and business requirements?",
        "options": [
            "A) They are interchangeable",
            "B) Business requirements are derived from stakeholder requirements",
            "C) Stakeholder requirements must support and trace back to business requirements",
            "D) They are independent and need no alignment"
        ],
        "answer": "C) Stakeholder requirements must support and trace back to business requirements",
        "explanation": "BABOK® v3 §1.4.4: Stakeholder requirements describe how stakeholder needs relate to achieving organizational goals—they must align with and support business requirements."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A developer claims: 'All requirements should be functional—we can infer quality from them.' The BABOK® v3-aligned response is:",
        "options": [
            "A) Agree—functional requirements are sufficient",
            "B) Partially agree—only security requirements need to be explicit",
            "C) Disagree—non-functional requirements define quality attributes that cannot be inferred from functional behaviors and are essential to solution success",
            "D) Defer to the architect's judgment"
        ],
        "answer": "C) Disagree—non-functional requirements define quality attributes that cannot be inferred from functional behaviors and are essential to solution success",
        "explanation": "BABOK® v3 §1.4.4: Non-functional requirements (performance, security, availability, usability) are distinct from and not derivable from functional requirements."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Foundational",
        "question": "According to BABOK® v3, a stakeholder is BEST defined as:",
        "options": [
            "A) The project sponsor",
            "B) Only internal employees",
            "C) Only direct users of the solution",
            "D) A group or individual with a relationship to the change, the need, or the solution"
        ],
        "answer": "D) A group or individual with a relationship to the change, the need, or the solution",
        "explanation": "BABOK® v3 §1.4.5: Stakeholders are broadly defined—any party with a relationship to the change, need, or solution."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Foundational",
        "question": "Which of the following is a recognized stakeholder type in BABOK® v3?",
        "options": [
            "A) Only customers and end users",
            "B) Only senior management",
            "C) Sponsor, Customer, End User, Domain SME, Regulator, Supplier, Tester, Operational Support, BA, and PM",
            "D) Only the project team"
        ],
        "answer": "C) Sponsor, Customer, End User, Domain SME, Regulator, Supplier, Tester, Operational Support, BA, and PM",
        "explanation": "BABOK® v3 §1.4.5 lists a comprehensive range of stakeholder types including internal, external, and supporting roles."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Foundational",
        "question": "Which stakeholder type provides financial resources and approves the scope of a change initiative?",
        "options": [
            "A) End User",
            "B) Domain Subject Matter Expert",
            "C) Sponsor",
            "D) Operational Support"
        ],
        "answer": "C) Sponsor",
        "explanation": "BABOK® v3 §1.4.5: The Sponsor authorizes the initiative, provides resources, and approves scope and decisions."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A government regulator does not use the system but must approve its outputs. Is this regulator a stakeholder?",
        "options": [
            "A) No—only direct users are stakeholders",
            "B) Yes—they have a relationship to the change and its outputs",
            "C) No—external parties are not stakeholders",
            "D) Yes—only if they attend project meetings"
        ],
        "answer": "B) Yes—they have a relationship to the change and its outputs",
        "explanation": "BABOK® v3 §1.4.5: Regulators are stakeholders because they have a relationship to the change outcomes, even without direct system usage."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A third-party vendor will integrate their product with the solution being built. They BEST represent which stakeholder type?",
        "options": [
            "A) Supplier",
            "B) Sponsor",
            "C) End User",
            "D) Domain Subject Matter Expert"
        ],
        "answer": "A) Supplier",
        "explanation": "BABOK® v3 §1.4.5: A vendor providing products or services that integrate with the solution is a Supplier stakeholder."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "The IT operations team will support and maintain the system post-go-live. They BEST represent which stakeholder type?",
        "options": [
            "A) End User",
            "B) Tester",
            "C) Operational Support",
            "D) Implementation Subject Matter Expert"
        ],
        "answer": "C) Operational Support",
        "explanation": "BABOK® v3 §1.4.5: Teams responsible for post-deployment maintenance and support are Operational Support stakeholders."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A domain expert in the finance department provides deep knowledge about accounting rules. They BEST represent which stakeholder type?",
        "options": [
            "A) Sponsor",
            "B) Domain Subject Matter Expert",
            "C) Customer",
            "D) Supplier"
        ],
        "answer": "B) Domain Subject Matter Expert",
        "explanation": "BABOK® v3 §1.4.5: Domain SMEs provide specialized knowledge about a business area—in this case, accounting and finance."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "A BA misses the legal department during stakeholder identification. The legal team later raises compliance concerns requiring significant rework. This illustrates the risk of:",
        "options": [
            "A) Incomplete stakeholder identification leading to missed requirements and late-stage rework",
            "B) Poor requirements documentation",
            "C) Inadequate testing",
            "D) Poor project governance"
        ],
        "answer": "A) Incomplete stakeholder identification leading to missed requirements and late-stage rework",
        "explanation": "BABOK® v3 §1.4.5: Missing stakeholders during identification leads to missed requirements, discovered late when they are costlier to address."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "According to BABOK® v3, the business analyst is also a stakeholder. This means:",
        "options": [
            "A) The BA should not document their own concerns",
            "B) The BA has a relationship to the change and its outcomes and should be recognized in stakeholder analysis",
            "C) The BA manages all other stakeholders",
            "D) The BA's requirements take priority"
        ],
        "answer": "B) The BA has a relationship to the change and its outcomes and should be recognized in stakeholder analysis",
        "explanation": "BABOK® v3 §1.4.5 explicitly recognizes the BA as a stakeholder with a relationship to the change."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "A BA identifies 15 stakeholder groups, some with high influence/low interest and others with low influence/high interest. This analysis MOST directly informs:",
        "options": [
            "A) The requirements classification",
            "B) The project risk register",
            "C) The solution design",
            "D) The stakeholder engagement strategy"
        ],
        "answer": "D) The stakeholder engagement strategy",
        "explanation": "BABOK® v3 §1.4.5: Influence/interest analysis informs how and how much to engage each stakeholder group in BA activities."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "A BA realizes two stakeholder groups have conflicting needs. The MOST appropriate action according to BABOK® v3 is:",
        "options": [
            "A) Prioritize the more senior group's needs automatically",
            "B) Document both and let developers decide",
            "C) Facilitate resolution by understanding both perspectives, assessing business value, and escalating to the sponsor if needed",
            "D) Remove one group from the stakeholder register"
        ],
        "answer": "C) Facilitate resolution by understanding both perspectives, assessing business value, and escalating to the sponsor if needed",
        "explanation": "BABOK® v3 §1.4.5: Conflicting stakeholder needs require facilitated resolution with objective assessment of business value, with escalation as appropriate."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Foundational",
        "question": "According to BABOK® v3, the BEST distinction between requirements and designs is:",
        "options": [
            "A) Requirements describe what is needed; designs describe how the solution will satisfy the need",
            "B) Requirements are written by BAs; designs are created by architects",
            "C) Requirements are high-level; designs are detailed",
            "D) Requirements are for business; designs are for IT"
        ],
        "answer": "A) Requirements describe what is needed; designs describe how the solution will satisfy the need",
        "explanation": "BABOK® v3 §1.5: Requirements define what is needed (the 'what and why'); designs define how the solution will deliver it (the 'how')."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Foundational",
        "question": "A use case that describes a system behavior from the user's perspective—without specifying implementation—is BEST classified as:",
        "options": [
            "A) A design artifact",
            "B) A requirements artifact",
            "C) A non-functional requirement",
            "D) A transition requirement"
        ],
        "answer": "B) A requirements artifact",
        "explanation": "BABOK® v3 §1.5: A use case describing behavior without implementation details is a requirements artifact—it defines what the system must do."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Intermediate",
        "question": "A BA produces a wireframe showing the layout of a mobile checkout screen. This is BEST classified as:",
        "options": [
            "A) A stakeholder requirement",
            "B) A functional requirement",
            "C) A business requirement",
            "D) A design artifact"
        ],
        "answer": "D) A design artifact",
        "explanation": "BABOK® v3 §1.5: A wireframe describes how the solution will look—it is a design artifact, not a requirement."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Intermediate",
        "question": "An entity-relationship diagram (ERD) showing the data model for the solution BEST represents:",
        "options": [
            "A) A business requirement",
            "B) A design artifact describing data structure",
            "C) A stakeholder requirement",
            "D) A non-functional requirement"
        ],
        "answer": "B) A design artifact describing data structure",
        "explanation": "BABOK® v3 §1.5: An ERD defines the data structure of the solution—it is a design artifact."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Intermediate",
        "question": "A BA documents: 'The system must allow customers to track their orders in real time.' This is BEST classified as:",
        "options": [
            "A) A design artifact",
            "B) A functional solution requirement",
            "C) A non-functional requirement",
            "D) A business requirement"
        ],
        "answer": "B) A functional solution requirement",
        "explanation": "BABOK® v3 §1.5: Stating what the system must do (real-time order tracking) without specifying how is a functional requirement, not a design."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A development team argues a BPMN future-state process model is a design, not a requirement. The BA argues it is both. Which BABOK® v3 principle supports the BA?",
        "options": [
            "A) The same artifact can serve as both a requirement and a design depending on abstraction level and audience",
            "B) Requirements and designs are always mutually exclusive",
            "C) Only textual artifacts qualify as requirements",
            "D) Designs are always created after requirements are finalized"
        ],
        "answer": "A) The same artifact can serve as both a requirement and a design depending on abstraction level and audience",
        "explanation": "BABOK® v3 §1.5 acknowledges that artifacts can serve dual purposes depending on the level of abstraction and the audience consuming them."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A BA hands her requirements document directly to developers as the design specification. What risk does this create?",
        "options": [
            "A) No risk—requirements and designs are the same",
            "B) The risk of scope creep",
            "C) Requirements (what is needed) may be confused with design (how to build it), unnecessarily constraining the solution space",
            "D) The risk of missing stakeholder sign-off"
        ],
        "answer": "C) Requirements (what is needed) may be confused with design (how to build it), unnecessarily constraining the solution space",
        "explanation": "BABOK® v3 §1.5: Treating requirements as design specifications prematurely closes off design options and may lead to suboptimal solutions."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A product owner writes acceptance criteria that specify exact UI element names and pixel layouts. According to BABOK® v3, these criteria MOST represent:",
        "options": [
            "A) Pure stakeholder requirements",
            "B) Design constraints embedded within acceptance criteria",
            "C) Transition requirements",
            "D) Non-functional requirements"
        ],
        "answer": "B) Design constraints embedded within acceptance criteria",
        "explanation": "BABOK® v3 §1.5: When acceptance criteria prescribe specific implementation details, they cross into design territory, constraining how (not just what) the solution delivers."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A BA is asked why BABOK® v3 distinguishes between requirements and designs if BAs produce both. The MOST accurate answer is:",
        "options": [
            "A) Only architects should produce designs",
            "B) The distinction helps the BA know when they are defining what is needed versus how it will be delivered, avoiding premature solution commitment",
            "C) Requirements are always more important than designs",
            "D) The distinction is only relevant in waterfall projects"
        ],
        "answer": "B) The distinction helps the BA know when they are defining what is needed versus how it will be delivered, avoiding premature solution commitment",
        "explanation": "BABOK® v3 §1.5: Understanding the boundary between requirements and designs helps practitioners avoid locking solutions prematurely and maintain appropriate flexibility."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A BA starts a new project by reviewing organizational strategy, identifying stakeholders, and planning elicitation techniques. According to BABOK® v3, she is working in which Knowledge Area FIRST?",
        "options": [
            "A) Strategy Analysis",
            "B) Elicitation and Collaboration",
            "C) Requirements Life Cycle Management",
            "D) Business Analysis Planning and Monitoring"
        ],
        "answer": "D) Business Analysis Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: Planning BA activities—approach, stakeholder identification, and technique selection—is BA Planning and Monitoring."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A stakeholder says: 'I need the app to be fast.' After probing, the BA establishes this means page loads under 2 seconds for 95% of requests. What transformation occurred?",
        "options": [
            "A) A business requirement became a transition requirement",
            "B) A vague stakeholder need was refined into a measurable non-functional solution requirement",
            "C) A stakeholder requirement was elevated to a business requirement",
            "D) A functional requirement was rewritten as a design constraint"
        ],
        "answer": "B) A vague stakeholder need was refined into a measurable non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Clarifying a vague quality expectation into a measurable performance criterion produces a non-functional solution requirement."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A BA is reviewing a context diagram with a new team member. The diagram shows the system boundary, external entities, and data flows. This artifact MOST relates to which BACCM concept being defined?",
        "options": [
            "A) Context",
            "B) Stakeholder",
            "C) Need",
            "D) Value"
        ],
        "answer": "A) Context",
        "explanation": "BABOK® v3 §1.4.1: A context diagram defines the boundary of the solution and its surrounding environment—this defines Context."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A BA notices requirements conflicts between two departments. To resolve them, she facilitates workshops and documents agreed-upon prioritization. This MOST activates which two Knowledge Areas?",
        "options": [
            "A) Strategy Analysis and Solution Evaluation",
            "B) Business Analysis Planning and Monitoring, and Strategy Analysis",
            "C) Elicitation and Collaboration, and Requirements Life Cycle Management",
            "D) Requirements Analysis and Design Definition, and Solution Evaluation"
        ],
        "answer": "C) Elicitation and Collaboration, and Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Facilitated workshops for conflict resolution are Elicitation and Collaboration; documenting agreed prioritization is Requirements Life Cycle Management."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA realizes requirements reflect what stakeholders asked for but not what they need to achieve the business goal. Which gap exists?",
        "options": [
            "A) Between stakeholder requirements and transition requirements",
            "B) Between solution requirements and design",
            "C) Between stakeholder requirements and business requirements",
            "D) Between functional and non-functional requirements"
        ],
        "answer": "C) Between stakeholder requirements and business requirements",
        "explanation": "BABOK® v3 §1.4.4: Stakeholder requirements must trace to and support business requirements. A disconnect between them creates a fundamental requirements gap."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A new CRM is deployed. Six months later, customer satisfaction has not improved. A BA is asked to investigate. The MOST appropriate activity is:",
        "options": [
            "A) Re-elicit all requirements from scratch",
            "B) Update the traceability matrix",
            "C) Conduct solution evaluation to assess whether the solution delivers expected value and identify root causes",
            "D) Escalate to the project sponsor for a new project"
        ],
        "answer": "C) Conduct solution evaluation to assess whether the solution delivers expected value and identify root causes",
        "explanation": "BABOK® v3 §1.3: Post-deployment underperformance is addressed through Solution Evaluation—measuring value delivery and identifying gaps."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA argues that requirements validation cannot be skipped even after the sponsor signs off. The BEST justification is:",
        "options": [
            "A) The BA's authority supersedes the sponsor's",
            "B) BABOK® v3 mandates validation regardless of governance",
            "C) Validation ensures requirements will lead to a solution delivering intended value; sign-off confirms approval, not correctness",
            "D) Validation is required for compliance"
        ],
        "answer": "C) Validation ensures requirements will lead to a solution delivering intended value; sign-off confirms approval, not correctness",
        "explanation": "BABOK® v3 RLCM: Validation confirms that requirements will lead to value-delivering solutions. Formal approval confirms only that stakeholders agree with the documented content."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA explains BABOK® v3 to a new team: 'This is not a step-by-step process—it is a guide to generally accepted practices.' This reflects which BABOK® v3 principle?",
        "options": [
            "A) BABOK® v3 describes generally accepted BA practices that practitioners tailor based on context",
            "B) BABOK® v3 provides a prescriptive process that must be followed exactly",
            "C) BABOK® v3 replaces all organizational BA methodologies",
            "D) BABOK® v3 only applies to CBAP® candidates"
        ],
        "answer": "A) BABOK® v3 describes generally accepted BA practices that practitioners tailor based on context",
        "explanation": "BABOK® v3 §1.1: BABOK® v3 is a guide to generally accepted practices—not a prescriptive methodology. Practitioners exercise judgment in applying them."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA produces a complete, approved requirements set. The project delivers on time. But the business fails to achieve its objectives. The MOST likely BA-related root cause is:",
        "options": [
            "A) Too few requirements were produced",
            "B) Requirements were approved but not aligned with the true Need and expected Value",
            "C) The BA should have managed the project",
            "D) The developers did not follow the requirements"
        ],
        "answer": "B) Requirements were approved but not aligned with the true Need and expected Value",
        "explanation": "BABOK® v3 §1.4.1, §1.4.4: Requirements can be technically approved yet disconnected from the real Need and Value. This is a BA quality failure, not a delivery failure."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA retrospective reveals that requirements were elicited well but were never managed—they were lost, changed without documentation, and became inconsistent. The primary gap is in which Knowledge Area?",
        "options": [
            "A) Requirements Life Cycle Management",
            "B) Strategy Analysis",
            "C) Elicitation and Collaboration",
            "D) Requirements Analysis and Design Definition"
        ],
        "answer": "A) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Managing requirements through their lifecycle—preventing loss, controlling changes, maintaining consistency—is RLCM."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "An organization has a pattern: business cases are approved without needs analysis, solutions are chosen before problems are defined. The MOST impactful Knowledge Area to strengthen FIRST is:",
        "options": [
            "A) Elicitation and Collaboration",
            "B) Requirements Analysis and Design Definition",
            "C) Requirements Life Cycle Management",
            "D) Strategy Analysis"
        ],
        "answer": "D) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Choosing solutions before problems are defined is a Strategy Analysis failure. Strengthening SA ensures the right problems are identified before solutions are selected."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA is asked to explain a complete BACCM-based analysis of why a recently delivered solution failed to create value. The MOST complete explanation is:",
        "options": [
            "A) The project manager failed to deliver",
            "B) Testing was insufficient",
            "C) The Solution was not aligned with the actual Need, the expected Value was not defined correctly, or the Context changed during delivery",
            "D) Requirements were not detailed enough"
        ],
        "answer": "C) The Solution was not aligned with the actual Need, the expected Value was not defined correctly, or the Context changed during delivery",
        "explanation": "BABOK® v3 §1.4.1: A complete BACCM-based explanation covers Solution–Need misalignment, incorrect Value definition, or a Context shift that invalidated the approach."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA explains: 'The six BACCM concepts apply to everything we do. Every task affects or is informed by at least one of them.' This BEST reflects which BABOK® v3 principle?",
        "options": [
            "A) The BACCM is a process model for BA activities",
            "B) The BACCM is only used in planning phases",
            "C) The BACCM replaces the Knowledge Areas",
            "D) The BACCM provides a universal conceptual framework applicable to all BA tasks"
        ],
        "answer": "D) The BACCM provides a universal conceptual framework applicable to all BA tasks",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is a conceptual lens that applies universally to all BA work—not a process or methodology."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA notices a developer has added features not in the approved requirements baseline. She assesses impact and initiates a formal change request. This MOST aligns with:",
        "options": [
            "A) Strategy Analysis",
            "B) Requirements Life Cycle Management",
            "C) Elicitation and Collaboration",
            "D) Business Analysis Planning and Monitoring"
        ],
        "answer": "B) Requirements Life Cycle Management",
        "explanation": "BABOK® v3 §1.3: Managing unauthorized additions through formal change control is Requirements Life Cycle Management."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA is challenged: 'Why do we need you when we have project managers?' The MOST BABOK® v3-aligned response is:",
        "options": [
            "A) BA reduces PM workload",
            "B) BA ensures we solve the right problem before investing in a solution; PM ensures the chosen solution is delivered within constraints—both are essential and complementary",
            "C) BA replaces PM in agile projects",
            "D) BA is only needed for large projects"
        ],
        "answer": "B) BA ensures we solve the right problem before investing in a solution; PM ensures the chosen solution is delivered within constraints—both are essential and complementary",
        "explanation": "BABOK® v3 §1.1: BA and PM are complementary—BA focuses on the right problem and solution; PM focuses on delivering within constraints."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A product manager declares requirements 'done' because all user stories are written. A BA disagrees. What should she do FIRST?",
        "options": [
            "A) Accept the PM's declaration to avoid conflict",
            "B) Escalate directly to the executive sponsor",
            "C) Present evidence of elicitation gaps and explain the risk of proceeding with incomplete requirements",
            "D) Proceed silently and document concerns privately"
        ],
        "answer": "C) Present evidence of elicitation gaps and explain the risk of proceeding with incomplete requirements",
        "explanation": "BABOK® v3 §2.2, §2.4: Professional ethics and communication skills require the BA to present gaps and risks transparently before proceeding."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA uses the BACCM to onboard a new analyst. She explains each concept in terms of a real initiative. This demonstrates that the BACCM's PRIMARY purpose is:",
        "options": [
            "A) To provide a checklist of BA tasks",
            "B) To replace the Knowledge Areas for simpler initiatives",
            "C) To provide a common vocabulary and conceptual framework that helps all team members understand BA work consistently",
            "D) To certify BA competency"
        ],
        "answer": "C) To provide a common vocabulary and conceptual framework that helps all team members understand BA work consistently",
        "explanation": "BABOK® v3 §1.4.1: The BACCM's primary purpose is providing a shared vocabulary and conceptual framework for consistent understanding of BA work."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Foundational",
        "question": "BABOK® v3 defines business analysis as a practice focused on enabling change. Which word in this definition is MOST significant?",
        "options": [
            "A) Practice—it implies structured discipline",
            "B) Change—it means BA is only relevant when something is being transformed",
            "C) Enabling—it means BA facilitates and supports rather than directs",
            "D) Both A and C are equally significant"
        ],
        "answer": "B) Change—it means BA is only relevant when something is being transformed",
        "explanation": "BABOK® v3 §1.1: The focus on 'enabling change' is the defining characteristic—BA work is always tied to some form of organizational transformation."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Intermediate",
        "question": "An organization's IT department consistently over-delivers technically but business users remain dissatisfied. A new CBAP candidate argues this reflects a structural BA problem. Which BABOK® v3 principle supports this view?",
        "options": [
            "A) IT delivery is independent of BA quality",
            "B) Without BA rigorously defining and validating needs, technical solutions satisfy specifications rather than actual stakeholder value",
            "C) Business user satisfaction is a PM responsibility",
            "D) This is a training problem, not a BA problem"
        ],
        "answer": "B) Without BA rigorously defining and validating needs, technical solutions satisfy specifications rather than actual stakeholder value",
        "explanation": "BABOK® v3 §1.1: When BA is absent or weak, the gap between technical specifications and real needs creates dissatisfaction even when delivery is technically correct."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Foundational",
        "question": "A BA performs requirements elicitation BEFORE completing her BA plan. This is:",
        "options": [
            "A) A process violation—planning must always precede elicitation",
            "B) Only allowed in agile projects",
            "C) Acceptable—BABOK® v3 KAs can be executed iteratively and in any order based on context",
            "D) Unacceptable regardless of context"
        ],
        "answer": "C) Acceptable—BABOK® v3 KAs can be executed iteratively and in any order based on context",
        "explanation": "BABOK® v3 §1.3: Knowledge Areas are not sequential phases. Performing elicitation before completing planning can be appropriate depending on context."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Intermediate",
        "question": "Which of the following BEST describes the outputs of the Strategy Analysis Knowledge Area that feed into other Knowledge Areas?",
        "options": [
            "A) Current-state analysis, future-state definition, and the change strategy that guide elicitation, RADD, and RLCM",
            "B) A requirements document and a stakeholder register",
            "C) A project charter and business case",
            "D) A risk register and issue log"
        ],
        "answer": "A) Current-state analysis, future-state definition, and the change strategy that guide elicitation, RADD, and RLCM",
        "explanation": "BABOK® v3 §1.3: Strategy Analysis defines the problem, future state, and change approach—foundational outputs that guide downstream BA activities."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Advanced",
        "question": "The inputs to BA Planning and Monitoring include the needs of the organization and the BA's understanding of the initiative context. This MOST illustrates:",
        "options": [
            "A) That BA planning is done in isolation",
            "B) That BA planning is a one-time activity",
            "C) That BA planning must wait for full requirements",
            "D) That KAs are interconnected—Strategy Analysis outputs serve as inputs to BA Planning and Monitoring"
        ],
        "answer": "D) That KAs are interconnected—Strategy Analysis outputs serve as inputs to BA Planning and Monitoring",
        "explanation": "BABOK® v3 §1.3: Knowledge Areas are interconnected. Understanding the context and need (from SA) is prerequisite to effective BA planning."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "The BACCM was created to provide which of the following?",
        "options": [
            "A) A common vocabulary and conceptual foundation for all business analysis work",
            "B) A step-by-step process for performing BA",
            "C) A certification framework for BAs",
            "D) A measurement system for BA performance"
        ],
        "answer": "A) A common vocabulary and conceptual foundation for all business analysis work",
        "explanation": "BABOK® v3 §1.4: The BACCM provides a shared conceptual foundation and vocabulary enabling BAs to understand, discuss, and perform their work consistently."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "A retail company identifies an opportunity to enter the e-commerce market. In BACCM terms, this opportunity is BEST classified as:",
        "options": [
            "A) A Solution",
            "B) A Change",
            "C) A Need",
            "D) A Context factor"
        ],
        "answer": "C) A Need",
        "explanation": "BABOK® v3 §1.4.1: An opportunity to be captured—like entering e-commerce—is a Need. It represents the driver for change."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Intermediate",
        "question": "The retail company decides to build an online store. In BACCM terms, the decision to build the online store is BEST classified as:",
        "options": [
            "A) A Solution",
            "B) A Change",
            "C) A Need",
            "D) A Value"
        ],
        "answer": "A) A Solution",
        "explanation": "BABOK® v3 §1.4.1: The online store—the specific approach chosen to satisfy the need—is a Solution."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Advanced",
        "question": "A BA argues that all six BACCM concepts must be examined for every change initiative, regardless of size. The BEST justification is:",
        "options": [
            "A) It is a BABOK® v3 rule that must be followed",
            "B) Examining all six protects the BA from criticism",
            "C) Each concept represents a dimension of understanding necessary to ensure the change delivers genuine value; missing any one creates blind spots",
            "D) Only three concepts are relevant per initiative but all six must be documented"
        ],
        "answer": "C) Each concept represents a dimension of understanding necessary to ensure the change delivers genuine value; missing any one creates blind spots",
        "explanation": "BABOK® v3 §1.4.1: The six concepts are mutually reinforcing. Ignoring any one—such as Context or Value—risks misaligned solutions."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Foundational",
        "question": "A requirement states: 'The application must support English and Spanish languages.' This BEST classifies as:",
        "options": [
            "A) Non-functional solution requirement",
            "B) Transition requirement",
            "C) Business requirement",
            "D) Stakeholder requirement only"
        ],
        "answer": "A) Non-functional solution requirement",
        "explanation": "BABOK® v3 §1.4.4: Language support is a quality/capability attribute of the solution—it defines a constraint on how the solution must behave, making it a Non-functional solution requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "A BA documents: 'Staff must be trained on the new system within 30 days of go-live.' This BEST classifies as:",
        "options": [
            "A) Non-functional requirement",
            "B) Transition requirement",
            "C) Business requirement",
            "D) Stakeholder requirement"
        ],
        "answer": "B) Transition requirement",
        "explanation": "BABOK® v3 §1.4.4: Post-go-live training within a specific window is a Transition requirement—it supports adoption during the transition period and is not a permanent system capability."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Intermediate",
        "question": "A customer service manager states: 'I need to be able to see a customer's full interaction history on a single screen.' This BEST classifies as:",
        "options": [
            "A) Business requirement",
            "B) Non-functional requirement",
            "C) Stakeholder requirement",
            "D) Transition requirement"
        ],
        "answer": "C) Stakeholder requirement",
        "explanation": "BABOK® v3 §1.4.4: A specific need expressed by a named stakeholder group (customer service manager) is a Stakeholder requirement."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Advanced",
        "question": "A BA challenges the team: 'Show me how each solution requirement traces to a stakeholder or business requirement.' This challenge MOST serves which purpose?",
        "options": [
            "A) To increase documentation volume",
            "B) To slow down the development team",
            "C) To ensure all solution requirements have legitimate justification and link to the actual needs driving the initiative",
            "D) To satisfy audit requirements"
        ],
        "answer": "C) To ensure all solution requirements have legitimate justification and link to the actual needs driving the initiative",
        "explanation": "BABOK® v3 §1.4.4: Traceability from solution requirements to stakeholder and business requirements ensures no orphaned or unjustified requirements exist."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A QA team is responsible for validating whether the solution meets stated requirements. They BEST represent which stakeholder type?",
        "options": [
            "A) Tester",
            "B) Operational Support",
            "C) End User",
            "D) Domain Subject Matter Expert"
        ],
        "answer": "A) Tester",
        "explanation": "BABOK® v3 §1.4.5: Teams responsible for validating requirements and confirming solution quality are Tester stakeholders."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Intermediate",
        "question": "A BA is conducting a new project kickoff and realizes she has not identified all affected stakeholders. The MOST immediate risk is:",
        "options": [
            "A) The project will be cancelled",
            "B) The BA's performance review will be negative",
            "C) Key requirements from unidentified stakeholders may be missed, discovered late and at greater cost",
            "D) The sponsor will lose confidence"
        ],
        "answer": "C) Key requirements from unidentified stakeholders may be missed, discovered late and at greater cost",
        "explanation": "BABOK® v3 §1.4.5: Incomplete stakeholder identification is a primary driver of late-stage requirements discovery, which is increasingly expensive to address."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Advanced",
        "question": "A BA is onboarding onto a complex banking transformation. She spends the first week solely on stakeholder identification and analysis. This is MOST consistent with which BABOK® v3 principle?",
        "options": [
            "A) BA tasks must be performed in a fixed sequence beginning with requirements",
            "B) Only the sponsor needs to be identified at project start",
            "C) Stakeholder analysis is a PM responsibility",
            "D) Thorough stakeholder identification early is foundational—missed stakeholders lead to missed needs and failed solutions"
        ],
        "answer": "D) Thorough stakeholder identification early is foundational—missed stakeholders lead to missed needs and failed solutions",
        "explanation": "BABOK® v3 §1.4.5: Rigorous early stakeholder identification is a critical BA investment—the completeness of requirements depends on it."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Foundational",
        "question": "A BA documents: 'The system must send an automatic email notification when an order ships.' This is BEST classified as:",
        "options": [
            "A) A design specification",
            "B) A business requirement",
            "C) A non-functional solution requirement",
            "D) A functional solution requirement"
        ],
        "answer": "D) A functional solution requirement",
        "explanation": "BABOK® v3 §1.5 & §1.4.4: Describing a system behavior (automatic email on shipping) without prescribing how it is implemented is a functional requirement."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Intermediate",
        "question": "A solution architect creates a database schema defining tables, columns, and relationships. This is BEST classified as:",
        "options": [
            "A) A non-functional requirement",
            "B) A transition requirement",
            "C) A design artifact",
            "D) A functional requirement"
        ],
        "answer": "C) A design artifact",
        "explanation": "BABOK® v3 §1.5: A database schema specifies how data will be structured—it is a design artifact, not a requirement."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Advanced",
        "question": "A BA documents both 'what the system must do' (requirements) and 'how the UI should look' (wireframes) in the same artifact. According to BABOK® v3, this MOST risks:",
        "options": [
            "A) Nothing—combining them improves efficiency",
            "B) Confusing stakeholders about the technology",
            "C) Violating BABOK® v3 documentation standards",
            "D) Blurring the boundary between requirements and designs, potentially constraining solution options unnecessarily"
        ],
        "answer": "D) Blurring the boundary between requirements and designs, potentially constraining solution options unnecessarily",
        "explanation": "BABOK® v3 §1.5: Mixing requirements and designs risks premature solution commitment and reduces the design team's flexibility to find optimal approaches."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A BA is assigned to a regulatory compliance initiative. She immediately begins mapping current-state processes to identify gaps against new regulations. Which Knowledge Area is she PRIMARILY working in?",
        "options": [
            "A) Strategy Analysis",
            "B) Business Analysis Planning and Monitoring",
            "C) Elicitation and Collaboration",
            "D) Requirements Life Cycle Management"
        ],
        "answer": "A) Strategy Analysis",
        "explanation": "BABOK® v3 §1.3: Mapping current-state gaps against a desired future state (regulatory compliance) is Strategy Analysis."
    },
    {
        "chapter": "Ch1 Integration | Intermediate",
        "question": "A BA conducts stakeholder interviews to gather details about a new product launch process. The information gathered will be used to write user stories. Which Knowledge Area does the interviews MOST belong to?",
        "options": [
            "A) Requirements Analysis and Design Definition",
            "B) Requirements Life Cycle Management",
            "C) Strategy Analysis",
            "D) Elicitation and Collaboration"
        ],
        "answer": "D) Elicitation and Collaboration",
        "explanation": "BABOK® v3 §1.3: Conducting interviews to draw out information from stakeholders is Elicitation and Collaboration."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA maps a regulatory compliance need to a solution requirement, which traces to a system design. This chain BEST illustrates:",
        "options": [
            "A) The difference between BA and project management",
            "B) The BACCM in action",
            "C) Traceability—the RLCM mechanism ensuring every solution element links to a justified need",
            "D) The sequential nature of Knowledge Areas"
        ],
        "answer": "C) Traceability—the RLCM mechanism ensuring every solution element links to a justified need",
        "explanation": "BABOK® v3 §1.3 RLCM: Traceability connects needs → requirements → designs, providing justification and impact assessment capability for every element."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "An organization implements BABOK® v3 for the first time. They interpret it as a sequential methodology: first Strategy Analysis, then Planning, then Elicitation, etc. What is WRONG with this interpretation?",
        "options": [
            "A) Nothing—BABOK® v3 is intended to be sequential",
            "B) The sequential interpretation only fails for agile projects",
            "C) Only Strategy Analysis must come first; the rest can be sequential",
            "D) BABOK® v3 Knowledge Areas are not sequential phases; they are groups of related tasks that can be performed in any order, iteratively, based on context"
        ],
        "answer": "D) BABOK® v3 Knowledge Areas are not sequential phases; they are groups of related tasks that can be performed in any order, iteratively, based on context",
        "explanation": "BABOK® v3 §1.3: A common misapplication of BABOK® v3 is treating it as a waterfall methodology. KAs are conceptual groupings, not process phases."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA is evaluating whether a deployed solution is meeting its intended objectives. She finds that the original business need has changed since deployment and the solution no longer addresses it. Which BACCM concepts and Knowledge Areas are MOST relevant?",
        "options": [
            "A) Need and Context (BACCM) have shifted; Strategy Analysis (re-examine need/future state) and Solution Evaluation (assess current performance) are both relevant",
            "B) Only Solution Evaluation",
            "C) Only Requirements Life Cycle Management",
            "D) BACCM is not relevant to post-deployment assessments"
        ],
        "answer": "A) Need and Context (BACCM) have shifted; Strategy Analysis (re-examine need/future state) and Solution Evaluation (assess current performance) are both relevant",
        "explanation": "BABOK® v3 §1.3, §1.4.1: When the Need and Context have changed, both Solution Evaluation (current performance) and Strategy Analysis (revised future state) are triggered."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A BA is writing a business case for a new initiative. She must justify the investment. Which BACCM concept is MOST central to this justification?",
        "options": [
            "A) Value—demonstrating the expected worth and benefit relative to the investment",
            "B) Solution—describing what will be built",
            "C) Change—describing what will transform",
            "D) Context—describing the current environment"
        ],
        "answer": "A) Value—demonstrating the expected worth and benefit relative to the investment",
        "explanation": "BABOK® v3 §1.4.1: A business case justifies investment by demonstrating expected Value—the worth and benefit the change will deliver to stakeholders."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "An organization pursues a digital transformation without clearly defining what 'value' the transformation should deliver. According to BABOK® v3, the MOST significant risk is:",
        "options": [
            "A) The transformation will take too long",
            "B) There will be no shared basis for measuring success or making trade-off decisions, increasing the likelihood of failed outcomes",
            "C) Developers will not know what to build",
            "D) The project manager will lose control"
        ],
        "answer": "B) There will be no shared basis for measuring success or making trade-off decisions, increasing the likelihood of failed outcomes",
        "explanation": "BABOK® v3 §1.4.1: Without a defined Value concept, there is no success criterion—decisions cannot be made objectively and outcomes cannot be measured."
    },
    {
        "chapter": "Ch1 §1.2 – Who Performs BA | Advanced",
        "question": "An organization asks whether a CBAP® certification is required before a person can perform BA tasks. The BABOK® v3-aligned answer is:",
        "options": [
            "A) Yes—only certified BAs may perform tasks described in BABOK® v3",
            "B) Yes—regulations require certification for all BA activities",
            "C) No—CBAP® certifies knowledge but BABOK® v3 defines BA by the tasks performed, not certification status",
            "D) Only in financial services sectors is certification mandatory"
        ],
        "answer": "C) No—CBAP® certifies knowledge but BABOK® v3 defines BA by the tasks performed, not certification status",
        "explanation": "BABOK® v3 §1.2: BA is defined by performing the tasks in BABOK® v3. Certification demonstrates knowledge but is not a prerequisite to perform BA work."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Foundational",
        "question": "Which of the following BEST describes how the BACCM differs from the six Knowledge Areas?",
        "options": [
            "A) The BACCM organizes tasks; KAs organize concepts",
            "B) The BACCM provides a conceptual vocabulary; KAs organize the tasks and practices BAs perform",
            "C) The BACCM applies only to strategic work; KAs apply to tactical work",
            "D) They are identical—KAs are just a renamed version of the BACCM"
        ],
        "answer": "B) The BACCM provides a conceptual vocabulary; KAs organize the tasks and practices BAs perform",
        "explanation": "BABOK® v3 §1.3, §1.4: The BACCM is a conceptual framework (the 'what is') while Knowledge Areas organize practical tasks (the 'what BAs do')—complementary but distinct."
    },
    {
        "chapter": "Ch1 Integration | Advanced",
        "question": "A senior BA mentors a junior colleague: 'Understand the BACCM deeply—it is not just theoretical vocabulary. It is the lens through which every elicitation session, every requirements decision, and every solution evaluation should be viewed.' This advice BEST reflects:",
        "options": [
            "A) The BACCM as a documentation checklist",
            "B) The BACCM as a replacement for practical techniques",
            "C) The BACCM as the conceptual foundation for all BA thinking and practice",
            "D) The BACCM as a methodology for large programs only"
        ],
        "answer": "C) The BACCM as the conceptual foundation for all BA thinking and practice",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is the theoretical backbone of all BA work—a practitioner who internalizes it applies it naturally in every task, not just in documentation."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Expert",
        "question": "An organization invests heavily in BA capability but still fails to realize benefits from change initiatives. A CBAP candidate is asked to diagnose the root cause. Which scenario MOST accurately explains how a mature BA function can still fail to deliver value?",
        "options": [
            "A) The BA function is too large and creates bureaucratic overhead",
            "B) Requirements documentation is too detailed",
            "C) The BA team uses too many elicitation techniques",
            "D) BA tasks are performed rigorously but Solution Evaluation is absent—solutions are delivered and forgotten without measuring whether expected value was achieved"
        ],
        "answer": "D) BA tasks are performed rigorously but Solution Evaluation is absent—solutions are delivered and forgotten without measuring whether expected value was achieved",
        "explanation": "BABOK® v3 §1.1, §1.3: A mature BA function that skips Solution Evaluation cannot confirm value realization. Benefit delivery requires closing the loop—measuring outcomes against the original need and expected value."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Expert",
        "question": "A BA is embedded in a team that follows SAFe® (Scaled Agile Framework). The team's product manager argues that PI Planning replaces the need for formal Strategy Analysis. The MOST BABOK® v3-aligned counter-argument is:",
        "options": [
            "A) Agree—PI Planning fully covers Strategy Analysis tasks",
            "B) PI Planning is a planning ceremony; Strategy Analysis is the intellectual discipline of understanding current state, defining future state, and identifying the change strategy—these are complementary, not substitutes",
            "C) BABOK® v3 does not apply to SAFe® environments",
            "D) Strategy Analysis only applies to waterfall and is not relevant in SAFe®"
        ],
        "answer": "B) PI Planning is a planning ceremony; Strategy Analysis is the intellectual discipline of understanding current state, defining future state, and identifying the change strategy—these are complementary, not substitutes",
        "explanation": "BABOK® v3 §1.1, §1.3: Methodology ceremonies organize delivery cadence; Strategy Analysis is a distinct discipline ensuring the right problems are understood. Both are necessary regardless of framework."
    },
    {
        "chapter": "Ch1 §1.1 – Why BA Exists | Expert",
        "question": "A BA is asked to justify why requirements verification AND validation are both necessary, even when stakeholders have signed off. The MOST precise BABOK® v3-aligned explanation is:",
        "options": [
            "A) Verification checks that requirements are well-written; validation checks that stakeholders approved them",
            "B) Validation is only needed when regulatory compliance is involved",
            "C) Both are the same activity performed at different times",
            "D) Verification ensures requirements are internally consistent and complete; validation ensures they will lead to a solution that delivers the intended business value—sign-off confirms agreement, not correctness or fitness for purpose"
        ],
        "answer": "D) Verification ensures requirements are internally consistent and complete; validation ensures they will lead to a solution that delivers the intended business value—sign-off confirms agreement, not correctness or fitness for purpose",
        "explanation": "BABOK® v3 RLCM: Verification = are requirements done correctly? Validation = do requirements define the right thing? Stakeholder sign-off is an approval mechanism, not a substitute for either quality check."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Expert",
        "question": "A BA is asked to explain what distinguishes Requirements Analysis and Design Definition (RADD) from Requirements Life Cycle Management (RLCM). A senior examiner presses for the most precise distinction. The BEST answer is:",
        "options": [
            "A) RADD writes requirements; RLCM approves them",
            "B) RADD is performed before RLCM in all methodologies",
            "C) RADD applies only to functional requirements; RLCM applies to non-functional requirements",
            "D) RADD transforms elicited information into specified, modeled, verified, and validated requirements and solution designs; RLCM governs the lifecycle of those artifacts—tracing, prioritizing, controlling changes, and maintaining their integrity over time"
        ],
        "answer": "D) RADD transforms elicited information into specified, modeled, verified, and validated requirements and solution designs; RLCM governs the lifecycle of those artifacts—tracing, prioritizing, controlling changes, and maintaining their integrity over time",
        "explanation": "BABOK® v3 §1.3: RADD is about producing quality requirements and designs. RLCM is about governing those artifacts from creation to retirement. Both are essential and distinct."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Expert",
        "question": "On a complex program, a BA completes thorough elicitation and produces a validated requirements baseline. Three months later, an external audit finds that 40% of the implemented solution cannot be traced to any approved requirement. The PRIMARY Knowledge Area failure is:",
        "options": [
            "A) Elicitation and Collaboration—elicitation was insufficient",
            "B) Business Analysis Planning and Monitoring—the BA plan was inadequate",
            "C) Solution Evaluation—the solution was not assessed before delivery",
            "D) Requirements Life Cycle Management—approved requirements were not maintained, traced, or governed through implementation"
        ],
        "answer": "D) Requirements Life Cycle Management—approved requirements were not maintained, traced, or governed through implementation",
        "explanation": "BABOK® v3 §1.3: An approved requirements baseline that is not maintained through implementation indicates RLCM failure—specifically, traceability and change control were not enforced."
    },
    {
        "chapter": "Ch1 §1.3 – Knowledge Areas | Expert",
        "question": "A BA working on an enterprise transformation observes that business objectives change quarterly due to market conditions, while development sprints are two weeks long. She implements a mechanism to regularly reassess whether current sprint work still aligns to evolving business objectives. This MOST reflects sophisticated application of which Knowledge Area pairing?",
        "options": [
            "A) Elicitation and Collaboration + RADD",
            "B) Strategy Analysis (continuous current/future state reassessment) + RLCM (requirements baseline updates reflecting strategic changes)",
            "C) BA Planning and Monitoring + Solution Evaluation",
            "D) RADD + Solution Evaluation"
        ],
        "answer": "B) Strategy Analysis (continuous current/future state reassessment) + RLCM (requirements baseline updates reflecting strategic changes)",
        "explanation": "BABOK® v3 §1.3: In volatile environments, Strategy Analysis must be ongoing—not a one-time event—and RLCM must reflect approved changes to strategy in the requirements baseline."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Expert",
        "question": "A BA presents the BACCM to a board of directors. A board member challenges: 'This model has six concepts—but when we approve a project, we only think about cost, deliverable, and timeline. Your model seems academic.' The MOST compelling BABOK® v3-aligned rebuttal is:",
        "options": [
            "A) Agree—the BACCM is primarily for academic purposes",
            "B) Cost/deliverable/timeline maps to Context (constraints), Solution (deliverable), and Change (transformation)—but without explicitly examining Need, Value, and Stakeholder, organizations routinely build the right thing for the wrong people, at the right cost for the wrong outcomes. The BACCM prevents these expensive blind spots",
            "C) The board only needs to understand Value and Cost",
            "D) The BACCM is only relevant for BA practitioners, not executives"
        ],
        "answer": "B) Cost/deliverable/timeline maps to Context (constraints), Solution (deliverable), and Change (transformation)—but without explicitly examining Need, Value, and Stakeholder, organizations routinely build the right thing for the wrong people, at the right cost for the wrong outcomes. The BACCM prevents these expensive blind spots",
        "explanation": "BABOK® v3 §1.4.1: The BACCM's value to executives is in surfacing blind spots. Missing Need analysis leads to wrong solutions; missing Value definition makes success unmeasurable; missing Stakeholder analysis creates solutions that satisfy the wrong people."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Expert",
        "question": "Two competing BAs debate whether 'risk' should be a BACCM concept. One argues risk belongs in Context; the other argues it belongs in Need. The MOST BABOK® v3-consistent resolution is:",
        "options": [
            "A) Risk can manifest as both Context (environmental uncertainty affecting the change) and Need (a threat that must be addressed)—the BACCM's six concepts are sufficient to represent risk through existing relationships without requiring a seventh concept",
            "B) Risk is a separate concept that BABOK® v3 accidentally excluded",
            "C) Risk only belongs in Context",
            "D) Risk is exclusively a PM concern and has no place in the BACCM"
        ],
        "answer": "A) Risk can manifest as both Context (environmental uncertainty affecting the change) and Need (a threat that must be addressed)—the BACCM's six concepts are sufficient to represent risk through existing relationships without requiring a seventh concept",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is intentionally parsimonious. Risk as environmental uncertainty is Context; risk as a problem requiring mitigation is a Need. The six concepts are complete and sufficient."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Expert",
        "question": "A BA uses the BACCM as a post-mortem framework for a failed $5M ERP implementation. She identifies: (1) the Need was defined as 'reduce manual data entry' but the real pain was inability to generate real-time management reports; (2) the Solution addressed data entry but not reporting; (3) Stakeholders who needed reports were excluded from requirements; (4) a mid-project merger changed reporting needs. Which BACCM failure chain BEST describes the root cause?",
        "options": [
            "A) Need was incorrectly defined → Solution was built to the wrong Need → key Stakeholders were excluded → Context shift was not monitored—a cascading failure across multiple BACCM concepts",
            "B) Context–Solution mismatch only",
            "C) Stakeholder exclusion was the only failure",
            "D) The merger (Context) was the sole root cause"
        ],
        "answer": "A) Need was incorrectly defined → Solution was built to the wrong Need → key Stakeholders were excluded → Context shift was not monitored—a cascading failure across multiple BACCM concepts",
        "explanation": "BABOK® v3 §1.4.1: The BACCM reveals cascading failure: wrong Need → wrong Solution; missing Stakeholders meant reporting needs were never captured; Context change was unmonitored. True BA failure is almost always multi-concept."
    },
    {
        "chapter": "Ch1 §1.4 – BACCM | Expert",
        "question": "A BA is challenged: 'In an agile sprint, we define the Need in the sprint goal, the Solution in the backlog, and Value in the Definition of Done. Why do we need the BACCM?' The MOST precise rebuttal is:",
        "options": [
            "A) Sprint artifacts name these concepts but do not guarantee rigorous analysis of them. The BACCM ensures that Need, Value, Context, and Stakeholder are analytically examined—not just named. Sprint goals can be wrong needs; Definition of Done can measure delivery, not value",
            "B) Agree—the sprint framework replaces the BACCM",
            "C) The BACCM only applies to large programs, not sprints",
            "D) Sprint ceremonies are sufficient if the Product Owner is experienced"
        ],
        "answer": "A) Sprint artifacts name these concepts but do not guarantee rigorous analysis of them. The BACCM ensures that Need, Value, Context, and Stakeholder are analytically examined—not just named. Sprint goals can be wrong needs; Definition of Done can measure delivery, not value",
        "explanation": "BABOK® v3 §1.4.1: Agile ceremonies provide cadence; the BACCM provides analytical depth. Naming concepts in sprint artifacts does not substitute for the rigorous examination each concept demands."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Expert",
        "question": "A BA is challenged to explain why the four BABOK® v3 requirement categories form a hierarchical relationship. The MOST accurate explanation is:",
        "options": [
            "A) They are not hierarchical—they are independent categories",
            "B) Solution requirements are most important; Business requirements are least important",
            "C) Business requirements establish organizational intent; Stakeholder requirements translate that intent into specific group needs; Solution requirements define how the solution satisfies those needs; Transition requirements address temporary needs for reaching the future state—each layer traces to and must support the layer above",
            "D) The hierarchy only applies to waterfall methodologies"
        ],
        "answer": "C) Business requirements establish organizational intent; Stakeholder requirements translate that intent into specific group needs; Solution requirements define how the solution satisfies those needs; Transition requirements address temporary needs for reaching the future state—each layer traces to and must support the layer above",
        "explanation": "BABOK® v3 §1.4.4: The four requirement types form a traceability hierarchy: Business → Stakeholder → Solution, with Transition operating in parallel. Each must link to and be justified by the layer above."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Expert",
        "question": "A BA documents: 'The system must automatically flag invoices where the vendor has not submitted required tax documentation.' A senior examiner asks: is this functional or non-functional, and is it also a business requirement? The MOST nuanced correct answer is:",
        "options": [
            "A) It is purely a business requirement",
            "B) It is a transition requirement because it relates to a new process",
            "C) It is non-functional because it relates to compliance",
            "D) It is a functional solution requirement (a specific system behavior); it may also reflect a business requirement if the underlying driver is regulatory compliance—in which case the functional requirement must be traceable to that business requirement"
        ],
        "answer": "D) It is a functional solution requirement (a specific system behavior); it may also reflect a business requirement if the underlying driver is regulatory compliance—in which case the functional requirement must be traceable to that business requirement",
        "explanation": "BABOK® v3 §1.4.4: Requirements can exist at multiple levels. The auto-flag behavior is functional (what the system does); the underlying regulatory need is a Business requirement. Both exist and must be linked through traceability."
    },
    {
        "chapter": "Ch1 §1.4.4 – Requirements Types | Expert",
        "question": "During a program review, a BA discovers that transition requirements were archived at go-live but the organization still relies on a manual reconciliation process documented only as a transition requirement. The BEST diagnosis is:",
        "options": [
            "A) The reconciliation process was misclassified—if the process persists post-transition, it is a permanent operational process that should have been captured as a functional or stakeholder requirement, not a transition requirement",
            "B) The transition requirement was correctly retired",
            "C) Transition requirements should never be retired",
            "D) This is a project management gap, not a BA gap"
        ],
        "answer": "A) The reconciliation process was misclassified—if the process persists post-transition, it is a permanent operational process that should have been captured as a functional or stakeholder requirement, not a transition requirement",
        "explanation": "BABOK® v3 §1.4.4: Transition requirements are defined by temporariness. If an activity persists beyond the transition, it was misclassified and should have been documented as a permanent solution or stakeholder requirement."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Expert",
        "question": "A BA is managing a transformation with 47 identified stakeholder groups. A program director argues that engaging all 47 groups will paralyze the project. The MOST BABOK® v3-aligned resolution is:",
        "options": [
            "A) Reduce the stakeholder list to the top 10 by seniority",
            "B) Engage only stakeholders who attend project meetings",
            "C) Delegate all stakeholder engagement to the project manager",
            "D) Apply stakeholder analysis (influence, impact, attitude, availability) to define differentiated engagement strategies—high-influence/high-impact groups receive intensive engagement; others receive appropriate communication—ensuring all are accounted for without equal resource allocation"
        ],
        "answer": "D) Apply stakeholder analysis (influence, impact, attitude, availability) to define differentiated engagement strategies—high-influence/high-impact groups receive intensive engagement; others receive appropriate communication—ensuring all are accounted for without equal resource allocation",
        "explanation": "BABOK® v3 §1.4.5: Stakeholder analysis produces a differentiated engagement strategy, not equal engagement. Different stakeholders warrant different levels of involvement based on their relationship to the change."
    },
    {
        "chapter": "Ch1 §1.4.5 – Stakeholders | Expert",
        "question": "A BA discovers mid-project that a newly appointed regulatory body now has jurisdiction over the solution's outputs, but was not in the original stakeholder register. The MOST appropriate BA response is:",
        "options": [
            "A) Immediately update the stakeholder register, conduct analysis of the new body's requirements and influence, assess impact on existing requirements, and present findings to the sponsor for scope and risk review",
            "B) Continue with the existing plan—the new body was not in the original scope",
            "C) Let the legal team handle it",
            "D) Wait until go-live to assess the regulatory body's requirements"
        ],
        "answer": "A) Immediately update the stakeholder register, conduct analysis of the new body's requirements and influence, assess impact on existing requirements, and present findings to the sponsor for scope and risk review",
        "explanation": "BABOK® v3 §1.4.5: Stakeholder identification is not a one-time activity. New stakeholders discovered mid-project must be analyzed, their requirements captured, and impacts assessed—ignoring them creates compliance and value risk."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Expert",
        "question": "A BA is asked to explain when an artifact transitions from being a 'requirement' to being a 'design.' The MOST BABOK® v3-precise answer is:",
        "options": [
            "A) The boundary is defined by abstraction level and intent: requirements describe what is needed and why (solution-agnostic); designs describe how a specific solution will be structured. A single artifact can cross this boundary depending on the level of implementation detail it contains",
            "B) When it is approved by the project sponsor",
            "C) Designs are always created by architects; requirements by BAs",
            "D) When the document is passed from BA to developer"
        ],
        "answer": "A) The boundary is defined by abstraction level and intent: requirements describe what is needed and why (solution-agnostic); designs describe how a specific solution will be structured. A single artifact can cross this boundary depending on the level of implementation detail it contains",
        "explanation": "BABOK® v3 §1.5: The requirement/design distinction is not role-based or document-based—it is defined by abstraction and intent. The same artifact can contain both requirements and design elements."
    },
    {
        "chapter": "Ch1 §1.5 – Requirements vs Designs | Expert",
        "question": "A BA produces a future-state process model. The development team treats it as a technical design spec and builds accordingly. Post-go-live, the system matches the model but fails to deliver the intended business outcome. The MOST precise root cause using BABOK® v3 concepts is:",
        "options": [
            "A) The development team made implementation errors",
            "B) The process model was a requirements artifact (what the process must do) used as a design specification (how to build it)—collapsing the requirements-design boundary caused the solution to satisfy the model rather than the underlying business Need and expected Value",
            "C) The BA did not produce enough documentation",
            "D) The project manager failed to control scope"
        ],
        "answer": "B) The process model was a requirements artifact (what the process must do) used as a design specification (how to build it)—collapsing the requirements-design boundary caused the solution to satisfy the model rather than the underlying business Need and expected Value",
        "explanation": "BABOK® v3 §1.5, §1.4.1: Treating requirements artifacts as designs forces the solution to satisfy the artifact rather than the underlying Need. The solution became correct by the wrong measure—the model—rather than the right measure—business value."
    },
    {
        "chapter": "Ch1 Integration | Expert",
        "question": "A CBAP examiner presents this scenario: A BA has performed rigorous BA Planning, thorough Elicitation, complete Strategy Analysis, meticulous RADD, and disciplined RLCM. The project is delivered on time and on budget. The business unit reports no improvement in performance one year later. Using BABOK® v3 Chapter 1 concepts, identify ALL possible root causes.",
        "options": [
            "A) Only Solution Evaluation was skipped",
            "B) Multiple possibilities: (1) Need was incorrectly defined despite thorough analysis; (2) Value was never explicitly defined so success was unmeasurable; (3) Context shifted post-delivery and was not monitored; (4) Solution Evaluation was not performed to detect and respond to underperformance",
            "C) The PM failed to manage benefits realization",
            "D) Requirements were not detailed enough"
        ],
        "answer": "B) Multiple possibilities: (1) Need was incorrectly defined despite thorough analysis; (2) Value was never explicitly defined so success was unmeasurable; (3) Context shifted post-delivery and was not monitored; (4) Solution Evaluation was not performed to detect and respond to underperformance",
        "explanation": "BABOK® v3 §1.1–§1.5: Even rigorous BA execution across five KAs cannot guarantee value if Need was wrong, Value was undefined, Context changed, or Solution Evaluation was omitted. All six KAs must operate for the value loop to close."
    },
    {
        "chapter": "Ch1 Integration | Expert",
        "question": "A BA is asked to design a BABOK® v3-aligned BA function for an organization that currently has none. Which sequencing of initial priorities BEST reflects BABOK® v3 Chapter 1 principles?",
        "options": [
            "A) Start with RADD to produce requirements templates",
            "B) First establish BA Planning and Monitoring (how BA will work); concurrently activate Strategy Analysis (understand organizational needs); then build Elicitation, RLCM, and RADD capabilities; finally implement Solution Evaluation to close the value loop",
            "C) Start with Solution Evaluation to assess current solution quality",
            "D) Start with stakeholder identification and stop there until all stakeholders are fully mapped"
        ],
        "answer": "B) First establish BA Planning and Monitoring (how BA will work); concurrently activate Strategy Analysis (understand organizational needs); then build Elicitation, RLCM, and RADD capabilities; finally implement Solution Evaluation to close the value loop",
        "explanation": "BABOK® v3 §1.3: While KAs are not sequential by rule, building a BA function requires foundational capabilities first. Planning how BA will operate and understanding strategic context precede producing requirements; Solution Evaluation closes the value delivery loop."
    },
    {
        "chapter": "Ch1 Integration | Expert",
        "question": "A BA is conducting a BACCM analysis of a proposed outsourcing initiative. Need=cost reduction; Solution=third-party provider; Change=transitioning 200 staff; Context=union agreement; Stakeholders=employees, union, customers; Value is defined differently by shareholders (cost savings) and customers (service continuity). A board member asks: 'What is the single most important BACCM relationship to manage?' The BEST BABOK® v3-aligned answer is:",
        "options": [
            "A) There is no single most important relationship—the BACCM requires holistic analysis; however, Value–Stakeholder is strategically critical here because unresolved Value conflicts across stakeholder groups will undermine the initiative regardless of execution quality",
            "B) Change–Context: managing the transition within union constraints",
            "C) Solution–Need: ensuring the vendor delivers cost reduction",
            "D) Need–Context: ensuring the cost reduction target is realistic"
        ],
        "answer": "A) There is no single most important relationship—the BACCM requires holistic analysis; however, Value–Stakeholder is strategically critical here because unresolved Value conflicts across stakeholder groups will undermine the initiative regardless of execution quality",
        "explanation": "BABOK® v3 §1.4.1: The BACCM is holistic by design. In this scenario, conflicting Value definitions across Stakeholders is the highest-risk dimension—if unresolved, the initiative will satisfy one group while damaging another."
    },
    {
        "chapter": "Ch1 Integration | Expert",
        "question": "A BA must defend the practical relevance of BABOK® v3 Chapter 1 to skeptical senior executives in under two minutes. Which argument is MOST compelling and MOST aligned with BABOK® v3?",
        "options": [
            "A) 'Every project failure we have experienced can be traced to ignoring at least one Chapter 1 concept: investing in the wrong solution (Need), building for the wrong people (Stakeholder), delivering the wrong thing (Value), or being blindsided by the environment (Context). Chapter 1 is not theory—it is a diagnostic framework for the root causes of every expensive failure in this organization'",
            "B) 'BABOK® v3 is an industry standard used in over 120 countries'",
            "C) 'BABOK® v3 certification improves salary outcomes for BAs'",
            "D) 'Using BABOK® v3 will reduce project timelines by 30%'"
        ],
        "answer": "A) 'Every project failure we have experienced can be traced to ignoring at least one Chapter 1 concept: investing in the wrong solution (Need), building for the wrong people (Stakeholder), delivering the wrong thing (Value), or being blindsided by the environment (Context). Chapter 1 is not theory—it is a diagnostic framework for the root causes of every expensive failure in this organization'",
        "explanation": "BABOK® v3 §1.1–§1.5: The most compelling case for Chapter 1 is forensic: every major project failure maps to a concept that was ignored. This argument is practical, credible, and directly addresses executives' skepticism about theoretical relevance."
    },
    {
        "chapter": "Ch1 Integration | Expert",
        "question": "A BA evaluates a proposed initiative to 'replace the legacy HR system to improve employee experience.' Which analysis MOST completely applies ALL relevant BABOK® v3 Chapter 1 concepts simultaneously?",
        "options": [
            "A) Document functional requirements for the new HR system",
            "B) Run a gap analysis between current and future HR system features",
            "C) Build a requirements document and present to the sponsor",
            "D) Examine: (1) Need—is 'improve employee experience' the real need or a symptom of something deeper? (2) Context—what regulatory, cultural, and technical constraints apply? (3) Stakeholders—who defines 'employee experience' and are all affected groups identified? (4) Value—how will improvement be measured and by whom? (5) Change—what transformation is required? (6) Solution—has replacing the legacy system been validated against the actual Need, or is it a pre-defined solution masquerading as a requirement?"
        ],
        "answer": "D) Examine: (1) Need—is 'improve employee experience' the real need or a symptom of something deeper? (2) Context—what regulatory, cultural, and technical constraints apply? (3) Stakeholders—who defines 'employee experience' and are all affected groups identified? (4) Value—how will improvement be measured and by whom? (5) Change—what transformation is required? (6) Solution—has replacing the legacy system been validated against the actual Need, or is it a pre-defined solution masquerading as a requirement?",
        "explanation": "BABOK® v3 §1.1–§1.5: Expert BA application integrates all Chapter 1 concepts simultaneously. The critical insight: 'replace the legacy system' is a pre-defined Solution that may not address the actual Need—a classic BA anti-pattern that Chapter 1 is designed to prevent."
    }
]

# ──────────────────────────────────────────────────────────────
#  SESSION STATE
# ──────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "started": False, "questions": [], "current": 0,
        "answers": {}, "submitted": {}, "finished": False,
        "num_questions": 20, "start_time": None,
        "q_start_time": None, "q_times": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_exam():
    for k in ["started","questions","current","answers","submitted",
              "finished","start_time","q_start_time","q_times"]:
        st.session_state.pop(k, None)

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
            • {len(ALL_QUESTIONS)} questions available from Chapter 1 of BABOK® v3<br>
            • Difficulty levels: Foundational · Intermediate · Advanced · Expert<br>
            • Covers §1.1 through §1.5 — all sections included<br>
            • Questions are randomized on every exam<br>
            • One attempt per question — confirm before moving on<br>
            • Per-question timer visible on every question<br>
            • Passing score: <b style='color:#f0d080'>70%</b> (CBAP® benchmark)
        </div>
        """, unsafe_allow_html=True)

        n = st.slider("Number of questions", min_value=5,
                      max_value=len(ALL_QUESTIONS),
                      value=min(40, len(ALL_QUESTIONS)), step=1)
        st.session_state.num_questions = n

        if st.button("🚀  Start Exam", use_container_width=True):
            pool = ALL_QUESTIONS.copy()
            random.shuffle(pool)
            st.session_state.questions   = pool[:n]
            st.session_state.num_questions = n
            st.session_state.current     = 0
            st.session_state.answers     = {}
            st.session_state.submitted   = {}
            st.session_state.finished    = False
            st.session_state.started     = True
            st.session_state.start_time  = time.time()
            st.session_state.q_start_time = time.time()
            st.session_state.q_times     = {}
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
    q_times_vals = list(st.session_state.q_times.values())
    avg_q = int(sum(q_times_vals) / len(q_times_vals)) if q_times_vals else 0
    avg_m, avg_s = divmod(avg_q, 60)

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
            <div class="stat-box"><div class="stat-num">{mins}:{secs:02d}</div><div class="stat-lbl">Total Time</div></div>
            <div class="stat-box"><div class="stat-num">{avg_m}:{avg_s:02d}</div><div class="stat-lbl">Avg / Question</div></div>
            <div class="stat-box"><div class="stat-num">{pct}%</div><div class="stat-lbl">Score</div></div>
        </div>""", unsafe_allow_html=True)

        # ── Difficulty breakdown ─────────────────────────────────
        levels = ["Foundational", "Intermediate", "Advanced", "Expert"]
        rows = ""
        for lvl in levels:
            lvl_qs  = [(i, q) for i, q in enumerate(qs) if lvl in q["chapter"]]
            lvl_tot = len(lvl_qs)
            if lvl_tot == 0:
                continue
            lvl_ok  = sum(1 for i, q in lvl_qs if st.session_state.answers.get(i) == q["answer"])
            lvl_pct = round(lvl_ok / lvl_tot * 100)
            bar_color = "#6fe4a4" if lvl_pct >= 70 else ("#f0d080" if lvl_pct >= 50 else "#f4a0a0")
            rows += f"""
            <tr>
                <td style='padding:.5rem .8rem;color:#f4f1eb;font-weight:600'>{lvl}</td>
                <td style='padding:.5rem .8rem;color:#c8d4e8;text-align:center'>{lvl_tot}</td>
                <td style='padding:.5rem .8rem;color:#6fe4a4;text-align:center'>{lvl_ok}</td>
                <td style='padding:.5rem .8rem;color:#f4a0a0;text-align:center'>{lvl_tot-lvl_ok}</td>
                <td style='padding:.5rem .8rem;text-align:center'>
                    <span style='color:{bar_color};font-weight:700'>{lvl_pct}%</span>
                </td>
            </tr>"""
        st.markdown(f"""
        <div style='margin:1.5rem 0;background:rgba(255,255,255,0.04);border:1px solid rgba(201,168,76,0.2);
                    border-radius:10px;overflow:hidden;font-family:"Source Sans 3",sans-serif'>
            <div style='padding:.7rem 1rem;background:rgba(201,168,76,0.1);color:#c9a84c;
                        font-size:.8rem;font-weight:600;letter-spacing:1.5px;text-transform:uppercase'>
                Performance by Difficulty
            </div>
            <table style='width:100%;border-collapse:collapse'>
                <thead>
                    <tr style='border-bottom:1px solid rgba(255,255,255,0.08)'>
                        <th style='padding:.5rem .8rem;color:#6b7a99;font-weight:600;text-align:left;font-size:.8rem'>Level</th>
                        <th style='padding:.5rem .8rem;color:#6b7a99;font-weight:600;text-align:center;font-size:.8rem'>Total</th>
                        <th style='padding:.5rem .8rem;color:#6b7a99;font-weight:600;text-align:center;font-size:.8rem'>✅ Correct</th>
                        <th style='padding:.5rem .8rem;color:#6b7a99;font-weight:600;text-align:center;font-size:.8rem'>❌ Wrong</th>
                        <th style='padding:.5rem .8rem;color:#6b7a99;font-weight:600;text-align:center;font-size:.8rem'>Score</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
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
                        <div style='color:#c9a84c;font-size:.8rem;margin-bottom:.5rem'>Q{i+1} · {q["chapter"].split("|")[0].strip()}</div>
                        <div style='color:#f4f1eb;margin-bottom:.7rem'>{q["question"]}</div>
                        <div style='color:#f4a0a0'>❌ Your answer: {user_ans}</div>
                        <div style='color:#6fe4a4'>✅ Correct: {q["answer"]}</div>
                        <div style='color:#c8d4e8;margin-top:.5rem;font-size:.9rem'>💡 {q["explanation"]}</div>
                    </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄  New Exam", use_container_width=True):
            reset_exam()
            st.rerun()

# ──────────────────────────────────────────────────────────────
#  EXAM SCREEN
# ──────────────────────────────────────────────────────────────
else:
    qs    = st.session_state.questions
    total = len(qs)
    idx   = st.session_state.current
    q     = qs[idx]

    already_submitted = idx in st.session_state.submitted

    # ── Progress bar ────────────────────────────────────────────
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

    # ── Timer — pure JS, runs in browser, no Streamlit rerenders ─
    if already_submitted:
        q_elapsed = int(st.session_state.q_times.get(idx, 0))
        q_mins, q_secs = divmod(q_elapsed, 60)
        timer_color = "#6fe4a4" if q_elapsed < 60 else ("#f0d080" if q_elapsed < 120 else "#f4a0a0")
        st.markdown(f"""
        <div style='font-family:"Source Sans 3",sans-serif;font-size:.85rem;
                    color:{timer_color};text-align:right;margin-bottom:.5rem;letter-spacing:1px'>
            ⏱ Time on this question: <b>{q_mins:02d}:{q_secs:02d}</b>
        </div>""", unsafe_allow_html=True)
    else:
        start_ts = int(st.session_state.q_start_time or time.time())
        st.markdown(f"""
        <div id="q_timer" style='font-family:"Source Sans 3",sans-serif;font-size:.85rem;
                    color:#6fe4a4;text-align:right;margin-bottom:.5rem;letter-spacing:1px'>
            ⏱ Time on this question: <b>00:00</b>
        </div>
        <script>
        (function() {{
            var start = {start_ts};
            function tick() {{
                var el = document.getElementById('q_timer');
                if (!el) return;
                var elapsed = Math.floor(Date.now() / 1000) - start;
                var m = Math.floor(elapsed / 60);
                var s = elapsed % 60;
                var mm = String(m).padStart(2,'0');
                var ss = String(s).padStart(2,'0');
                var color = elapsed < 60 ? '#6fe4a4' : (elapsed < 120 ? '#f0d080' : '#f4a0a0');
                el.style.color = color;
                el.innerHTML = '⏱ Time on this question: <b>' + mm + ':' + ss + '</b>';
            }}
            tick();
            setInterval(tick, 1000);
        }})();
        </script>""", unsafe_allow_html=True)

    # ── Restart button + Question card ──────────────────────────
    col_q1, col_q2 = st.columns([6, 1])
    with col_q2:
        if st.button("🔄 Restart", key="restart_top", use_container_width=True):
            reset_exam()
            st.rerun()

    st.markdown(f"""
    <div class="q-card">
        <div class="q-number">Question {idx+1}</div>
        <div class="q-chapter">{q["chapter"].split("|")[0].strip()}</div>
        <p class="q-text">{q["question"]}</p>
    </div>""", unsafe_allow_html=True)

    # ── Answer options ───────────────────────────────────────────
    # Options are stored as "A) text", "B) text" etc. in the bank.
    # We display them as HTML and use tiny buttons only for selection.
    # Streamlit never touches the option text or order.
    letters = ["A", "B", "C", "D"]
    if not already_submitted:
        selected = st.session_state.get(f"pending_{idx}", None)
        st.markdown("<p style='font-family:\"Source Sans 3\",sans-serif;color:#c8d4e8;margin:.5rem 0'>Select your answer:</p>", unsafe_allow_html=True)
        for opt in q["options"]:
            is_sel = (opt == selected)
            border = "2px solid #c9a84c" if is_sel else "1px solid rgba(201,168,76,0.2)"
            bg     = "rgba(201,168,76,0.12)" if is_sel else "rgba(255,255,255,0.03)"
            icon   = "◉" if is_sel else "○"
            col_txt, col_btn = st.columns([11, 1])
            with col_txt:
                st.markdown(f"""
                <div style='padding:.6rem 1rem;border-radius:8px;background:{bg};
                            border:{border};font-family:"Source Sans 3",sans-serif;
                            color:#f4f1eb;margin:.2rem 0'>{icon} {opt}</div>
                """, unsafe_allow_html=True)
            with col_btn:
                if st.button(opt[0], key=f"btn_{idx}_{opt[0]}", use_container_width=True):
                    st.session_state[f"pending_{idx}"] = opt
                    st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns([1, 4])
        with col_a:
            if st.button("✅  Confirm Answer", key=f"confirm_{idx}", use_container_width=True):
                chosen = st.session_state.get(f"pending_{idx}", None)
                if chosen is None:
                    st.warning("Please select an answer before confirming.")
                else:
                    st.session_state.answers[idx]  = chosen
                    st.session_state.q_times[idx]  = time.time() - (st.session_state.q_start_time or time.time())
                    st.session_state.submitted[idx] = True
                    st.rerun()
    else:
        user_ans    = st.session_state.answers.get(idx)
        correct_ans = q["answer"]
        is_correct  = user_ans == correct_ans

        letters = ["A", "B", "C", "D"]
        for i, opt in enumerate(q["options"]):
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
            correct_letter = letters[q["options"].index(correct_ans)]
            st.markdown(f"""
            <div class="feedback-wrong">
                ❌ <b>Incorrect.</b> Correct answer: <b>{correct_ans}</b>
                <div class="feedback-explanation">💡 {q["explanation"]}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        is_last = idx == total - 1
        col_nav1, col_nav2 = st.columns([1, 1])
        with col_nav1:
            if idx > 0:
                if st.button("⬅  Previous", key=f"prev_{idx}", use_container_width=True):
                    st.session_state.current -= 1
                    st.session_state.q_start_time = time.time()
                    st.rerun()
        with col_nav2:
            if is_last:
                if st.button("🏁  Finish Exam", key=f"finish_{idx}", use_container_width=True):
                    st.session_state.finished = True
                    st.rerun()
            else:
                if st.button("Next  ➡", key=f"next_{idx}", use_container_width=True):
                    st.session_state.current += 1
                    st.session_state.q_start_time = time.time()
                    st.rerun()
