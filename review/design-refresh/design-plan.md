# Design refresh

Audience: adults learning quantitative finance independently. The primary job is to move from a concept to a calculation, inspect evidence and explain the result.

Tokens: ink #182c49, blue #2357a5, paper #f5f7fb, white #ffffff, line #d7e0ed, muted #52647d. A restrained orange focus ring identifies keyboard focus, not performance.
Type: Avenir Next where locally available, Segoe UI and system sans fallbacks for clear lesson prose; tabular numerals for financial outputs; system monospace only for code. No font downloads.
Layout: the course map is a sequential syllabus grouped into three learning stages, alongside a compact study-route panel. Lessons keep a stable navigation rail and an open reading column. The Python editor uses the same surface hierarchy.

    Course title / start action   | Study route
    Foundations                  | prerequisites
    01 title ... open            | Python option
    02 title ... open            |
    Evidence and portfolios      |
    Research and communication   |

Critique before implementation: a blue card grid would merely recolour the previous template. Replace that grid with numbered syllabus rows because chapter order is meaningful. Put the distinctive element in the course sequence, keep lessons quiet and reduce uppercase metadata and arrow decorations. Retain meaningful synthetic-data and assessment limitations in course information; remove production-stage labels from the learner interface.

Claude Code was invoked with the official frontend-design plugin directory, restricted tools and Sonnet. It failed with ECONNREFUSED before returning an implementation. This refresh applies the locally installed official plugin's guidance directly; it is not a Claude-generated design. No Claude token or price telemetry was returned.
