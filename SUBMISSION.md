# CineLens AI - Devpost Submission Form

## 📌 Project Overview & Metadata

* **Project Title**: CineLens AI
* **Elevator Pitch / Tagline**: The next-generation AI viewing companion for Fire TV—delivering real-time scene insights, character bios, and spoiler-free recaps powered by Amazon Bedrock.
* **Primary Track**: Fire TV (Category: *AI-Enhanced Viewing & Multi-Modal UX*)
* **Mini Challenges**: AWS Builder & Open Source
* **Repository**: Private / Public GitHub repository with MIT License.
* **Collaborators Invited**: `chris-trag`, `knmeiss`, `giolaq`, `anishamalde`, `mosesroth`, `emersonsklar`, `testing@devpost.com`.

---

## 📖 About the Project

### 💡 Inspiration
We’ve all experienced it: sitting on the couch watching a gripping film or series, turning to a friend or family member, and asking:
* *"Wait, who is that character again and what did they do in season 1?"*
* *"What did they just whisper? Did I miss an important plot clue?"*
* *"Can someone catch me up on the last 15 minutes without spoiling the ending?"*

While Amazon Prime Video revolutionized living-room metadata with **X-Ray**, static cast lists and trivia cards can only answer predefined questions. We were inspired to elevate this concept into the generative AI era. 

With **Amazon Bedrock** and **Fire TV**, we saw the opportunity to build **CineLens AI**: a dynamic, conversational living-room companion that understands exact scene timestamps, characters on screen, narrative arcs, and audio subtext—controllable entirely with a standard Fire TV remote control.

---

### 🎬 What CineLens AI Does
CineLens AI turns passive viewing into an interactive, intelligent multi-modal experience:

1. **Instant Scene Explanation**: Pausing the movie or pressing the remote's AI Lens button activates an ambient slide-over panel explaining current stakes, hidden visual clues, and dramatic tension without spoiling what happens next.
2. **Dynamic Character & Actor Deep-Dive**: Identifies actors currently on screen, their character backstory, and notable filmography.
3. **10-Minute Spoiler-Free Recaps**: Summarizes immediate preceding plot points if a viewer stepped away or arrived late, with strict guardrails preventing future spoilers.
4. **Dialogue & Subtext Decryption**: Translates idioms, quiet whispers, and symbolic references that viewers often miss.
5. **Soundtrack & Acoustic Telemetry**: Details the background score, instruments, and how the audio amplifies emotional beats.
6. **10-Foot Spatial Navigation**: Built specifically for television displays (720p/1080p/4K) with safe-zone compliance and zero mouse or touchscreen dependency.

---

### 🛠️ How We Built It

CineLens AI was architected as a cohesive full-stack TV system optimized for minimal latency:

```
[Fire TV Remote / D-Pad]
          │
          ▼
┌────────────────────────────────────────┐
│  Fire TV Frontend (10-Foot UI)         │
│  - Spatial Navigation Engine           │
│  - Playback Telemetry Tracker          │
└──────────────────┬─────────────────────┘
                   │ HTTPS POST
                   ▼
┌────────────────────────────────────────┐
│  Amazon API Gateway                    │
└──────────────────┬─────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────┐
│  AWS Lambda (Python 3.12 Serverless)   │
│  - Contextual Prompt Engineering       │
│  - Timestamp & Narrative Injection     │
└──────────────────┬─────────────────────┘
                   │ Converse API
                   ▼
┌────────────────────────────────────────┐
│  Amazon Bedrock                        │
│  - Amazon Nova Lite / Claude Models    │
└────────────────────────────────────────┘
```

* **Frontend (Fire OS & Vega OS)**: Built with standard web technologies (HTML5, modern CSS, vanilla ES6) to ensure 100% portability across Fire TV devices, the Amazon Web App Tester, and Vega OS.
* **Spatial Navigation Engine**: We developed an on-device directional graph router. When an arrow key is pressed, the engine computes Euclidean distance:
  $$d = \sqrt{(x_2 - x_1)^2 + \alpha (y_2 - y_1)^2}$$
  where $\alpha$ is a directional weighting factor ensuring intuitive focus traversal across non-grid layouts.
* **Serverless Backend (AWS SAM)**: Deployed using AWS Serverless Application Model (SAM). Incoming API requests are processed by an **AWS Lambda** function running Python 3.12.
* **Multi-Modal AI (Amazon Bedrock)**: We utilized the Amazon Bedrock Converse API with models like `amazon.nova-lite-v1:0` and Anthropic Claude. The backend constructs a targeted living-room system prompt that penalizes verbosity and enforces TV-safe formatting (short paragraphs and bullet points).

---

### 🧗 Challenges We Faced

1. **Designing for the 10-Foot Experience**:
   Standard web apps assume touchscreens or cursor precision. Adapting complex AI responses to a living room 10 feet away required strict adherence to TV safe margins (5%), high-contrast typography ($\ge 4.5:1$ contrast ratio), and foolproof focus rings (`#FF9900` Amazon orange glow).
2. **Preventing Spoilers Programmatically**:
   LLMs naturally know full movie synopses. To prevent ruining future plot twists, we engineered negative constraints and timestamp boundaries in the Bedrock system prompt, restricting responses strictly to:
   $$\text{Timestamp } t \le t_{\text{current}}$$
3. **Remote Control Latency & Focus Trapping**:
   When opening the slide-over AI drawer, focus needed to transfer seamlessly to the first inquiry chip, and pressing **Back** (`Escape` / KeyCode `8` / `10009`) had to instantly dismiss the drawer and return focus to the playback controls without navigating the browser back in history.

---

### 🎓 What We Learned

* **Amazon Bedrock Converse API**: The Converse API significantly simplifies multi-model switching, enabling seamless transitions between Amazon Nova and Claude models with zero prompt schema rework.
* **Fire TV Web App Tooling**: The Amazon Web App Tester proved to be an exceptionally rapid prototyping tool, dramatically reducing iteration time compared to traditional native APK compilation cycles.
* **Ambient TV UX**: Generative AI on TV must be non-intrusive. Glassmorphic slide-overs that retain visible video playback keep users engaged without breaking immersion.

---

### 🏆 Accomplishments We're Proud Of

* **Zero-Mouse Native Remote Navigation**: The entire app can be driven blind using only a physical Fire TV directional remote or keyboard arrows.
* **Dual AWS Deployment**: Built with both an AWS SAM Serverless production stack (`template.yaml`) and a local hybrid fallback buffer ensuring 100% demo uptime for judges.
* **1-Click Review Experience**: Anyone reviewing the code can run `python run_demo.py` and immediately test the full Fire TV experience with an interactive on-screen virtual remote HUD.

---

### 🔮 What's Next for CineLens AI

* **Alexa Voice Services Integration**: Enabling direct voice requests like *"Alexa, ask CineLens who is speaking"*.
* **Computer Vision Scene Recognition**: Integrating **Amazon Rekognition** to automatically identify background props, filming locations, and wardrobe items with direct Amazon purchase links.
* **Multi-User Living Room Voting**: Enabling companion smartphone pairing via WebSockets so multiple family members can vote on what trivia or recaps to explore.

---

## 🛠️ Product Feedback on Amazon Developer Tools & AWS

### 1. Amazon Bedrock
* **What we used it for**: Real-time generative scene analysis, character breakdown, and spoiler-free recaps.
* **What worked well**: The Converse API provides a unified, clean interface across both Amazon Nova and Claude models. Low inference latency is ideal for living room interactions where users expect instant answers.
* **What needs work**: Streaming responses directly over standard API Gateway WebSockets can be complex to wire up; native server-sent event (SSE) streaming helpers in the AWS SDK would simplify real-time streaming to TV devices.
* **Onboarding experience**: Very smooth via the AWS Console once model access was granted in `us-east-1`.
* **Would we build with it again?**: Absolutely. Bedrock is our default choice for scalable generative AI backends.

### 2. Fire TV Web App Platform & Web App Tester
* **What we used it for**: Running, testing, and debugging the 10-foot UI on Fire OS devices and simulators.
* **What worked well**: Web standards (HTML5/CSS/ES6) work out of the box. The Amazon Web App Tester makes sideloading and rapid prototyping significantly faster than compiling full native APKs.
* **What needs work**: Handling remote back button behaviors and spatial navigation focus traps requires custom code. An official Amazon-maintained React / Web spatial navigation library for Fire TV would accelerate developer onboarding.
* **Onboarding experience**: Good documentation on developer.amazon.com regarding 10-foot design guidelines, safe zones, and remote key codes.
* **Would we build with it again?**: Yes, web-based applications on Fire TV offer the best iteration speed.

---

## ⏱️ Demo Video Script (< 3 Minutes)

* **0:00 - 0:35 (Hook & Problem)**:
  * "Have you ever been watching a movie, turned to someone on the couch, and asked: *'Wait, who is that actor?'* or *'What did that character just whisper?'* Meet CineLens AI, the intelligent viewing companion built for Amazon Fire TV."
* **0:35 - 1:45 (Live Demo on Fire TV)**:
  * Show movie playback.
  * Pause video using remote; CineLens drawer slides smoothly from the right.
  * Navigate D-pad between chips:
    * Select *"🔍 Explain Scene"* -> show Amazon Bedrock analysis.
    * Select *"🎭 Who's On Screen?"* -> click on character card to inspect actor profile.
    * Select *"⏪ 10-Min Recap"* -> showcase spoiler-free catch-up summary.
  * Press Back button to immediately dismiss and resume playback.
* **1:45 - 2:30 (Architecture Walkthrough)**:
  * Diagram showing Fire TV 10-foot UI ➔ Amazon API Gateway ➔ AWS Lambda ➔ Amazon Bedrock (`amazon.nova-lite-v1:0`).
  * Emphasize zero-dependency TV remote navigation and 100% Fire OS / Vega OS compatibility.
* **2:30 - 3:00 (Conclusion & AWS Feedback)**:
  * Highlight how Amazon Bedrock makes living room ambient computing seamless.
  * Closing call to action.
