**Exploring AI for Red Door internal processes**

| 1\.  Conversation topics |
| :---- |

* Broader conversation: where can AI help Red Door internally?  
* Share what we've already been exploring  
* Think about how to identify and evaluate opportunities for AI  
* Walk through the 'SOW generator' process as a concrete example  
* Tools that could help us specifically with internal processes  
* Next steps and open questions

| 2\.  How to spot a good opportunity for AI automation |
| :---- |

* The task is repetitive — we do a version of it regularly  
* Heavy on copy/paste or reformatting existing content  
* Relies on past examples as templates or starting points  
* More 'grunt work' than strategic thinking  
* Involves pulling from known inputs to fill a known structure  
* A rough first draft — even imperfect — would still save time  
* The human review step is already built into the process  
* Some examples that have already been working well:  
* Azure Essential Show scripts — recurring format, known structure, consistent inputs  
* Databricks SEO content (especially blogs and glossary pages) — high volume, template-driven, repetitive to produce  
* Project status updates / recaps — pulling from email threads or notes to draft a quick client-facing or internal summary  
* Meeting notes / action item summaries — turning a transcript or rough notes into a clean recap with owners and next steps

|  | Try this prompt in Claude |
| :---- | :---- |

|  | You are a workflow analyst and strategic thought partner helping a small creative agency called Red Door Collaborative identify opportunities to use AI to streamline, accelerate, or automate internal processes. Red Door is a boutique creative agency based in Bellevue, WA that produces marketing content for clients including Microsoft, Databricks, Salesforce, and Procraft. The agency has also begun producing original content for its own channels, including a video series called Open Door. The team is small and non-technical. Most internal processes involve some combination of scoping client work, building documents from past examples, drafting content to a known structure, and coordinating across stakeholders. Time is the primary constraint. I want you to interview me. Your goal is to help me surface processes in my day-to-day work that could be good candidates for AI assistance, and then help me think through what a realistic solution might look like.  Ask me one question at a time. Start by asking me to describe a task I do regularly that feels tedious, slow, or repetitive. |
| :---- | :---- |

| 3\.  Once we've identified a good opportunity, how to think it through |
| :---- |

* Understand how the process actually works today, step by step — where does it slow down or break?  
* Pinpoint the painful part specifically: is it the 'blank page' problem, the repetitive assembly, the recalculation, the inconsistency?  
* Take stock of what we already have — past examples, templates, reference docs, email threads  
* Decide what "good enough" looks like — does the output need to be perfect, or is a strong rough draft the goal?  
* Be realistic about what AI can actually take off your plate — it can handle a piece of the process well, but trying to automate the whole thing at once usually creates more friction than it saves  
* Keep humans in the loop where it matters — identify which parts of the process should stay human (approvals, pricing, strategy) and design around those  
* Start with a question, not a solution — talk to the person who owns the process before deciding what to build

| 4\.  Example: AI-assisted SOW drafting |
| :---- |

* Naj mentioned SOW creation as a pain point at an AI roundtable meeting  
* Joe followed up with a structured set of questions via email  
* Goal: understand the process before building anything

| ↳  *Reference: Example SOW (serves as model) — Content Kit* |
| :---- |

|  | Questions Joe asked |
| :---- | :---- |

* How does an SOW actually start — brief, conversation, email chain?  
* Is there a pricing book, and how do you use it?  
* How many deliverable types does Red Door scope?  
* Where does friction happen — initial build or revisions?  
* What do you most dread when an SOW lands on your plate?  
* What would make the biggest immediate difference?  
* Would a rough AI draft help, or just create more work?

|  | Pain points that Naj described |
| :---- | :---- |

* No definitive standard template or perfectly consistent language across SOWs  
* SOWs vary a lot depending on who built them and which account manager  
* Pricing book is a large, complex Excel file with 20+ tabs — still learning it  
* For unfamiliar project types, has to rely on Chris or Amy — the logic isn't visible in the SOW itself  
* When a client changes something, recalculation means going back to the Excel formulas manually  
* Slows down when the client doesn't have all the info yet

|  | What Naj said a better process would look like |
| :---- | :---- |

* Feed in a scoping conversation or email thread → get a standardized template back to edit from  
* Something that starts it for her, not just checks her work  
* Pricing still needs to go through Chris — so the draft doesn't have to be perfect on costs

|  | What Joe decided to build |
| :---- | :---- |

* A tool focused on structure and language, not pricing math  
* Input: paste in the scoping conversation or email thread  
* Output: a properly formatted SOW draft with the right sections, right level of detail, right language  
* Chris still reviews and finalizes pricing

| 5\.  What Joe ended up building |
| :---- |

|  | Approach 1: standalone app |
| :---- | :---- |

* A Python web app that runs locally in your browser, powered by Claude behind the scenes (via API key)  
* Fill out a form, paste in a scoping conversation → generates a formatted .docx SOW  
* Works well on the machine it was built on, but...  
* Hard to build and distribute without technical skills — couldn't get it fully working on Naj's Mac; when she did get it running, it threw errors  
* Any change to the SOW process means rebuilding the app and generating a new executable — not flexible over time  
* Good experiment, but the friction of building, distributing, and maintaining it points toward a simpler approach

| ↳  *Reference: SOW Generator App — Guide* |
| :---- |

| ↳  *Reference: SOW generator screenshot* |
| :---- |

| ↳  *Reference: Python app — generated output example* |
| :---- |

|  | Approach 2: Claude Project (recommended) |
| :---- | :---- |

* Lives entirely inside Claude — no installation onto your computer, no file to distribute  
* This project is shared — anyone with an RDC Claude account can be granted access immediately  
* What's already been built:  
* Project-level instructions that define how Claude handles SOW requests and how to use all the inputs  
* Real example SOWs loaded as reference models — Claude draws on these for structure, language, and formatting  
* A starter prompt that Naj pastes in to kick off a new SOW chat  
* A SOW template file with placeholder tokens that Claude fills in  
* A placeholder reference doc that maps every token to a plain-English description of what goes there  
* Step-by-step instructions for how a person uses the Claude Project  
* Advantages:  
* Zero installation — works anywhere Claude works  
* Formatting fidelity is baked into the template, not dependent on AI getting it right  
* Easy to update and iterate — change the instructions or template without rebuilding anything  
* Naj can use it herself right now

| ↳  *Reference: SOW Claude Project — Guide* |
| :---- |

| ↳  *Reference: Claude Project — generated output example 1* |
| :---- |

| ↳  *Reference: Claude Project — generated output example 2* |
| :---- |

**→  Live demo**

| 6\.  Other RDC internal processes worth exploring |
| :---- |

|  | Already on the table |
| :---- | :---- |

* RFP drafting — feed in a client brief or RFP document, get a structured Red Door response draft  
* RFP discovery — AI actively searching for relevant RFPs, since no one is currently dedicated to biz dev prospecting  
* Workback schedule generation — standard templates already exist; AI could generate a first draft based on project details and team availability  
* Kickoff decks — similar pattern to SOWs: known structure, variable content, relies on past examples

|  | Other ideas |
| :---- | :---- |

* Client onboarding materials — welcome docs, project overview one-pagers, intro emails; lots of repetition project to project  
* Creative briefs — translating a client call or email thread into a structured brief for the creative team  
* Change order drafts — when scope changes, generating a formatted change order from a description of what shifted  
* Job descriptions or contractor briefs — Red Door hires freelancers regularly; these follow a pattern  
* Potential for future LinkedIn or newsletter content — Red Door's own marketing and thought leadership, repurposed from existing work

|  | What these have in common |
| :---- | :---- |

| Known structure | All follow a known structure |
| :---- | :---- |
| **Existing inputs** | All start from inputs Red Door already has — scoping notes, briefs, past examples |
| **Manual assembly** | All currently require someone to manually assemble a first draft |
| **Time savings** | A rough AI draft in any of these cases would still save meaningful time |

| 7\.  AI tools for internal processes |
| :---- |

* Focusing mostly on Claude —powerful enough to handle most of what we've been talking about, and it's what I have the most firsthand experience with  
* One thing I've learned: starting from the tool often hasn't actually moved things forward — the right starting place is the friction, the job, the goal  
* The tool almost arrives on its own once those are clear — it flows from the need rather than the other way around

|  | Claude connectors |
| :---- | :---- |

* Microsoft 365 — Claude can read and search Outlook emails, Teams messages, SharePoint docs, and calendar events; could pull a scoping thread directly rather than requiring copy/paste  
* monday.com — Claude could read task lists, project status, and team assignments to feed into status updates or workback schedules automatically  
* Box — Claude could pull templates, past SOWs, or reference docs without manual uploading  
* Figma — could assist with creative brief generation or design spec documentation

|  | Claude Cowork |
| :---- | :---- |

* Right now, working with Claude means switching back and forth — copying a scoping email from Outlook, pasting it into Claude, copying the output, opening Word, pasting it in, then opening the pricing Excel book separately to look up hours and rates. Cowork can do those steps for you — it works across your apps, not just inside a chat window  
* Can open files, navigate apps, and fill in forms on your behalf  
* For writing-focused workflows, the regular Claude chatbot has often been enough — Cowork might add more value for roles that involve managing files, coordinating across tools, and juggling a lot of moving parts  
* Probably most applicable at Red Door for project managers and account managers rather than writers or designers — just a hunch worth testing  
* For the SOW process: could theoretically open the pricing Excel book, read the relevant tab, and pull hours and rates directly

|  | Zapier |
| :---- | :---- |

* Connects two apps so that something happening in one automatically triggers an action in the other  
* You build simple "if this, then that" rules through a visual interface — no coding required  
* Could wire together tools the team already uses so that starting a new project triggers a chain of prep work automatically  
* Example: a new project in monday.com automatically creates a SharePoint folder and kicks off a Claude-assisted creative brief and RDC branded kickoff deck

| 8\.  Next steps / questions |
| :---- |

* Naj tests out the Claude Project for SOWs  
* What other processes feel like they are good opportunities for AI?  
* What are the biggest concerns about bringing AI into these workflows?  
* Who else at Red Door should be part of this conversation going forward?  
* What would make this feel real and useful vs. just fun experiments?

