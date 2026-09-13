from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import EnquiryForm

SERVICES = {
    'quality-strategy-governance': {
        'number': '01',
        'title': 'Quality Strategy & Governance',
        'strapline': 'Build a quality operating system that leaders can run, measure and improve.',
        'intro': 'QualiNex helps leadership teams move quality from an audit-oriented function to an enterprise management discipline. The focus is on how strategy, risk, customer voice, process controls, plant performance and management review work together.',
        'why': 'The differentiator is governance designed around decisions—not paperwork. The advisory starts with the outcomes leadership needs to control, then builds the KPI tree, review cadence, escalation paths, ownership model and risk-based routines required to sustain those outcomes.',
        'deliverables': ['Quality maturity and governance diagnostic', 'Enterprise / multi-plant quality operating model', 'KPI architecture linking leading indicators to business outcomes', 'Management review redesign with decision rights and escalation thresholds', 'Quality risk register, control-plan governance and audit-readiness roadmap', 'Plant-to-corporate performance review pack and operating cadence'],
        'questions': ['Where is quality performance actually leaking value?', 'Which KPIs predict customer and plant failure before the monthly result arrives?', 'Are corporate standards translated into executable plant routines?', 'Does management review trigger decisions, owners and deadlines—or only reporting?', 'Which risks require prevention, detection, containment or escalation?'],
        'outcomes': ['Clear ownership and decision rights', 'Comparable multi-plant performance visibility', 'Earlier detection of emerging quality risk', 'Reduced management-review noise and stronger closure discipline', 'A governance system that survives leadership and organisational changes'],
        'framework': 'Aligned in spirit with risk-based quality management and the IATF 16949 / ISO 9001 management-system environment, while remaining tailored to the client’s operating context.'
    },
    'operational-excellence': {
        'number': '02',
        'title': 'Operational Excellence',
        'strapline': 'Turn operational friction into measurable improvement in cost, flow, capability and delivery.',
        'intro': 'Operational excellence engagements connect Lean Six Sigma thinking to the real economics of the operation: COPQ, yield, cycle time, throughput, downtime, rework, labour productivity, changeover losses and process capability.',
        'why': 'QualiNex is deliberately not positioned as a “tool deployment” service. Methods are selected because they solve a business problem. The intervention combines data, process observation, root-cause analysis, leader routines and control mechanisms so gains are visible in operating performance.',
        'deliverables': ['Value-stream and performance-leakage diagnostic', 'COPQ and waste baseline with prioritised value pools', 'DMAIC / Kaizen improvement architecture', 'Process capability and variation reduction agenda', 'Daily management, leader standard work and escalation routines', 'Benefits tracking and sustainment review'],
        'questions': ['Which losses matter economically—not just statistically?', 'Where is variation created, and where is it merely detected?', 'Which problems are structural versus symptomatic?', 'Are improvement actions linked to named owners and measurable benefits?', 'What management routine will prevent performance from sliding back?'],
        'outcomes': ['Lower COPQ and waste', 'More stable processes and improved capability', 'Higher productivity and throughput', 'Faster problem escalation and resolution', 'Visible benefit ownership and sustainment'],
        'framework': 'Lean Six Sigma, structured problem solving, process capability analysis and management-system discipline are combined into a practical improvement architecture.'
    },
    'customer-supplier-quality': {
        'number': '03',
        'title': 'Customer & Supplier Quality',
        'strapline': 'Stabilise the quality chain from customer voice to supplier process capability.',
        'intro': 'Customer escalations, recurring defects and unstable suppliers rarely remain isolated quality issues. They consume engineering time, disrupt production, create concessions and weaken customer confidence. QualiNex brings customer and supplier quality into one end-to-end improvement system.',
        'why': 'The focus is on recurrence prevention. Complaints are converted into structured problem statements; supplier issues are connected to process capability; corrective actions are verified for effectiveness; and management has a transparent view of chronic versus acute risk.',
        'deliverables': ['Customer complaint and escalation diagnostic', '8D / QRCI / CAPA governance and effectiveness reviews', 'NCR, concession and waiver workflow design', 'Supplier segmentation, audit strategy and development roadmap', 'Supplier corrective-action and repeat-defect controls', 'Customer and supplier quality KPI cockpit'],
        'questions': ['How much of the complaint portfolio is recurrence?', 'Are root causes proven with evidence?', 'Are corrective actions addressing systemic causes or only symptoms?', 'Which suppliers create the highest customer and operational risk?', 'How do we verify action effectiveness after closure?'],
        'outcomes': ['Lower complaint recurrence', 'Faster containment and closure', 'Higher supplier responsiveness and capability', 'Stronger CAPA effectiveness', 'More trusted customer communication'],
        'framework': 'Uses structured problem solving, 8D/QRCI, CAPA, supplier quality engineering and risk-based escalation principles appropriate to the client’s industry.'
    },
    'npi-apqp-risk-engineering': {
        'number': '04',
        'title': 'NPI, APQP & Risk Engineering',
        'strapline': 'Make launch quality a design outcome—not a production surprise.',
        'intro': 'New-product and new-process risk is cheapest to remove before production scale. QualiNex brings APQP, FMEA, control plans, measurement confidence, process capability and launch governance together around one objective: predictable industrialisation.',
        'why': 'The differentiator is linkage. APQP is not treated as a document checklist; FMEA, control plans, MSA, SPC and PPAP are connected to the actual risk profile of the product and process. This follows the interconnected Core Tools logic promoted by AIAG, where APQP, Control Plan, PPAP, FMEA, SPC and MSA are used as a connected quality architecture.',
        'deliverables': ['NPI quality-readiness assessment and launch gates', 'APQP plan and cross-functional governance', 'PFMEA review and risk-prioritised action plan', 'Control-plan effectiveness and special-characteristic governance', 'MSA / SPC / capability-readiness review', 'PPAP readiness and safe-launch containment strategy'],
        'questions': ['Which failure modes can still escape into the customer?', 'Are FMEA actions reflected in the control plan and shop-floor controls?', 'Is measurement capability adequate for the decision being made?', 'What evidence supports launch readiness?', 'Which risks need temporary safe-launch controls?'],
        'outcomes': ['Earlier risk removal', 'More predictable launches', 'Reduced early-life defects', 'Stronger cross-functional ownership', 'Better linkage between engineering risk and production control'],
        'framework': 'The service is informed by the current AIAG Core Tool architecture—APQP, Control Plan, PPAP, FMEA, SPC and MSA—together with applicable customer-specific requirements.'
    },
    'digital-quality-transformation': {
        'number': '05',
        'title': 'Digital Quality Transformation',
        'strapline': 'Replace fragmented quality transactions with transparent, data-led management.',
        'intro': 'Digital quality is not digitising a paper form. It is redesigning the flow of quality information so that containment, decisions, ownership, escalation and learning happen faster and with better evidence.',
        'why': 'QualiNex starts with the management problem: where does information wait, where is it re-entered, where is visibility delayed, and which decisions are made with incomplete data? The technology roadmap follows the process—not the other way around.',
        'deliverables': ['Current-state quality information-flow diagnostic', 'Paperless NC / waiver / complaint workflows', 'Digital approval and escalation pathways', 'Quality KPI dashboards and executive drill-downs', 'Data dictionary, ownership and governance standards', 'Digital roadmap with phased implementation priorities'],
        'questions': ['Which quality decisions are slowed by fragmented information?', 'Where are spreadsheets creating version-control or traceability risk?', 'Which data should be captured at source?', 'What should management see daily, weekly and monthly?', 'Which workflow steps can be automated without weakening control?'],
        'outcomes': ['Faster visibility and escalation', 'Better traceability', 'Reduced administrative effort', 'More reliable management information', 'A scalable foundation for advanced analytics and automation'],
        'framework': 'Current quality technology direction increasingly emphasises collaborative digital handling of FMEA, APQP, Control Plans and PPAP; QualiNex translates that direction into practical operating-model and workflow decisions.'
    },
    'capability-academy': {
        'number': '06',
        'title': 'Capability Academy',
        'strapline': 'Build internal problem-solving capability that compounds after the consultant leaves.',
        'intro': 'A transformation is incomplete if the organisation cannot repeat the method without external support. The QualiNex Capability Academy combines targeted learning, coaching and live-project application to build a stronger quality and operational-excellence bench.',
        'why': 'Training is designed around application, not attendance. Participants learn the method, apply it to a real business problem, receive coaching, demonstrate evidence of use and embed the method into their normal management routines.',
        'deliverables': ['Role-based quality leadership academy', 'PFMEA / Core Tools practitioner development', 'Kepner-Tregoe / structured problem-solving coaching', 'Lean Six Sigma project mentoring', 'QRCI / 8D / CAPA effectiveness coaching', 'Train-the-trainer and internal facilitator development', 'Capability assessment with skill-matrix and development roadmap'],
        'questions': ['Can your teams independently define and solve chronic problems?', 'Are your best methods embedded in standard work?', 'Which capability gaps create the most quality risk?', 'Are managers coaching the process—not only reviewing the result?', 'How will competence be demonstrated and sustained?'],
        'outcomes': ['More capable frontline and quality leaders', 'Higher problem-solving consistency', 'Faster internal response to emerging problems', 'Reduced dependency on external intervention', 'A repeatable learning system linked to live business results'],
        'framework': 'The academy uses case-based learning and live application, echoing the Core Tools competency approach used by leading quality bodies such as AIAG, while tailoring content to the organisation’s maturity and risk profile.'
    },
}

ENGAGEMENTS = {
    'executive-advisory': {
        'title': 'Executive Advisory',
        'strapline': 'Independent senior judgement for consequential quality and transformation decisions.',
        'description': 'For boards, CXOs, business-unit leaders and plant leadership teams who need an experienced quality practitioner to challenge assumptions, sharpen priorities and convert complexity into decisions.',
        'best_when': ['Quality performance is materially affecting customer confidence or economics.', 'Leadership is evaluating a transformation, restructuring or major quality investment.', 'A multi-plant agenda needs independent prioritisation and governance.', 'A senior leader needs an external sounding board without adding a permanent layer of structure.'],
        'deliverables': ['Executive fact-base and risk narrative', 'Decision options and recommendation', 'Quality / transformation priority map', 'Governance and review cadence', '90-day leadership agenda'],
    },
    'focused-diagnostic': {
        'title': 'Focused Diagnostic',
        'strapline': 'A concentrated fact base that turns a difficult problem into an actionable agenda.',
        'description': 'A short, evidence-led intervention to establish what is really happening, quantify the problem, identify root drivers and define a practical 30–90 day response.',
        'best_when': ['There is a visible performance gap but no agreed root cause.', 'Customer escalation or recurring defects require an independent review.', 'A plant, supplier or product launch needs a rapid readiness assessment.', 'Leadership needs a fact base before committing to a major transformation.'],
        'deliverables': ['Rapid data and document review', 'Stakeholder interviews / Gemba-style observation', 'Problem statement and driver tree', 'Risk and priority heat map', '30–90 day action agenda with owners and KPIs'],
    },
    'transformation-programme': {
        'title': 'Transformation Programme',
        'strapline': 'Hands-on leadership of critical interventions, with capability transfer built in.',
        'description': 'For situations where the organisation needs an experienced practitioner to lead a quality or operational transformation until the new routines, controls and capability are established.',
        'best_when': ['A plant or network has chronic performance instability.', 'A major quality transformation requires cross-functional leadership.', 'Customer or supplier issues have become business-critical.', 'The organisation needs a temporary transformation leader with a defined exit path.'],
        'deliverables': ['Programme charter and workstreams', 'Governance and escalation model', 'Value / KPI baseline', 'Workstream leadership and coaching', 'Benefit tracking and closure governance', 'Capability handover and sustainment plan'],
    },
    'capability-academy': SERVICES['capability-academy'],
}

def common(request):
    return {'linkedin':'https://www.linkedin.com/in/subhamjit-deb-82686238','email':'mailto:subham81@yahoo.com','whatsapp':'https://wa.me/919818027177'}

def render_page(request, template, section=None, **context):
    return render(request, template, {**common(request), 'section': section, **context})

def home(request): return render_page(request,'practice/home.html','home')
def advisory(request): return render_page(request,'practice/advisory.html','advisory', services=SERVICES, engagements=ENGAGEMENTS)
def service_detail(request, slug):
    item = SERVICES.get(slug)
    if not item: return render(request, 'practice/service_detail.html', {'not_found': True}, status=404)
    return render_page(request, 'practice/service_detail.html', 'advisory', service=item, slug=slug)
def engagement_detail(request, slug):
    item = ENGAGEMENTS.get(slug)
    if not item: return render(request, 'practice/engagement_detail.html', {'not_found': True}, status=404)
    return render_page(request, 'practice/engagement_detail.html', 'advisory', engagement=item, slug=slug)
def experience(request): return render_page(request,'practice/experience.html','experience')
def credentials(request): return render_page(request,'practice/credentials.html','credentials')
def method(request): return render_page(request,'practice/method.html','method')
def contact(request):
    form = EnquiryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); messages.success(request, 'Thank you. Your enquiry has been recorded and will be reviewed confidentially.')
        return redirect('contact')
    return render(request,'practice/contact.html',{**common(request),'section':'contact','form':form})
