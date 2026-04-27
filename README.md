# AI QA Module Documentation

## What This Is

This is a reusable AI QA module for pull request review. You can adapt it for almost any software project.

Use it when you want GitHub PRs to automatically answer these questions:

1. What changed in this PR?
2. What are the QA risks?
3. Are tests covering the latest requirements?
4. Does the implementation match tickets and scope?
5. Does the UI match design files?

This is not tied to one product idea. The pattern is portable.

Do this:

- Use this suite when you want structured PR intelligence, not just static CI checks.
- Reuse the same architecture in future repos.
- Keep each bot focused on one job.

Do not do this:

- Do not combine every QA concern into one giant workflow.
- Do not make the PR overview bot responsible for ticket validation.
- Do not make the design bot responsible for test traceability.

Keep each bot separate so the outputs stay readable and maintainable.

---

## Why This Is Good For Every Project

This module works well for almost any team because every team eventually needs the same things:

- a PR summary
- QA risk detection
- requirement coverage checks
- design review
- merge confidence

You can adapt the inputs to fit the project:

- Use Linear, Jira, Azure Boards, or another ticket source.
- Use Google Docs, Confluence exports, Markdown files, or PDFs for scope.
- Use Figma or skip design checks if the project is not design-driven.
- Use Claude, OpenAI, or another LLM provider if your team standard changes.

Do this:

- Treat this module as a template, not a one-off script pack.
- Replace project-specific integrations when moving it to a new repo.
- Keep the bot responsibilities stable even if the APIs change.

If you move this to another project, the architecture should stay the same:

1. collect context
2. ask the model
3. format the result
4. post or update a PR comment

---

## Core Principle

Each workflow should answer one question clearly.

Do this:

1. Create one workflow per review concern.
2. Give each workflow its own script.
3. Give each workflow its own PR comment marker.
4. Let each workflow evolve independently.

Do not do this:

1. Do not let one bot post multiple unrelated reports.
2. Do not mix business requirement review with design fidelity review.
3. Do not rely on one comment for all PR intelligence.

This separation is what makes the module scalable across projects.

---

## Module Components

This AI QA module contains five bots:

1. Claude AI QA Review
2. Scope vs QA Gap Analysis
3. Linear + SOW Ticket Coverage Review
4. Figma vs Code Report
5. PR File Change Overview

Each one has a different job.

### 1. Claude AI QA Review

Use this for broad QA analysis.

It should answer:

- what changed
- what looks risky
- where tests are weak
- what edge cases may be missing
- what codebase-specific change the developer should make instead

Do this:

- Use this as your general-purpose AI reviewer.
- Run it on every PR if you want fast QA signal.
- Feed it the diff and any available coverage data.
- Feed it nearby changed-file context so recommendations follow existing project patterns.

Do not do this:

- Do not use this as the source of truth for product requirement coverage.
- Do not block merges on this alone unless your process explicitly wants that.
- Do not accept generic suggestions when the codebase gives enough context for a concrete replacement.

### 2. Scope vs QA Gap Analysis

Use this for requirement-to-test traceability.

It should answer:

- do current tests cover the latest scope docs
- what requirements have no tests
- what should be tested next

Do this:

- Keep scope documents current.
- Store them in a dedicated folder.
- Apply timestamp logic so the newest requirement source wins.

Do not do this:

- Do not assume old scope files are still valid.
- Do not run this without maintaining the `context/` folder.

### 3. Linear + SOW Ticket Coverage Review

Use this for checking whether the PR actually satisfies planned work.

It should answer:

- which tickets are covered
- whether acceptance criteria appear implemented
- whether the PR aligns with the scope of work
- whether merge should be blocked

Do this:

- Use this when your team manages delivery through tickets.
- Connect it to your live ticketing system.
- Keep acceptance criteria clear in the tickets.

Do not do this:

- Do not expect good output from vague tickets.
- Do not hardcode project IDs into scripts if you can avoid it.

### 4. Figma vs Code Report

Use this for design fidelity.

It should answer:

- which screens are implemented
- which components are missing
- whether the code matches the design system
- what UI gaps still exist

Do this:

- Use this for frontend-heavy projects.
- Connect it to a valid Figma file.
- Keep design files organized enough to compare.

Do not do this:

- Do not treat it like deterministic visual regression testing.
- Do not use it if the design source is stale or unmaintained.

### 5. PR File Change Overview

Use this for a lightweight summary of core code changes.

It should answer:

- which files changed
- what changed in each file
- what the overall PR is doing

Do this:

- Keep this separate from ticket review.
- Use it for reviewer orientation.
- Use it for non-technical stakeholders when they just need a quick summary.

Do not do this:

- Do not treat this as requirements validation.
- Do not expect it to replace a real code review.

---

## Files In This Repo

### Workflows

- [`.github/workflows/ximena_claude_qa_review.yml`](C:/Users/HP/Desktop/Ximena-Frontend/.github/workflows/ximena_claude_qa_review.yml)
- [`.github/workflows/ximena_scope_gap_analysis.yml`](C:/Users/HP/Desktop/Ximena-Frontend/.github/workflows/ximena_scope_gap_analysis.yml)
- [`.github/workflows/ximena_qa_review.yml`](C:/Users/HP/Desktop/Ximena-Frontend/.github/workflows/ximena_qa_review.yml)
- [`.github/workflows/ximena_figma_check.yml`](C:/Users/HP/Desktop/Ximena-Frontend/.github/workflows/ximena_figma_check.yml)
- [`.github/workflows/ximena_pr_overview.yml`](C:/Users/HP/Desktop/Ximena-Frontend/.github/workflows/ximena_pr_overview.yml)

### Scripts

- [`.github/scripts/github_comment_utils.py`](C:/Users/HP/Desktop/Ximena-Frontend/.github/scripts/github_comment_utils.py)
- [`.github/scripts/ximena_claude_qa_review.py`](C:/Users/HP/Desktop/Ximena-Frontend/.github/scripts/ximena_claude_qa_review.py)
- [`.github/scripts/ximena_scope_gap_analysis.py`](C:/Users/HP/Desktop/Ximena-Frontend/.github/scripts/ximena_scope_gap_analysis.py)
- [`.github/scripts/ximena_qa_reviewer.py`](C:/Users/HP/Desktop/Ximena-Frontend/.github/scripts/ximena_qa_reviewer.py)
- [`.github/scripts/ximena_figma_check.py`](C:/Users/HP/Desktop/Ximena-Frontend/.github/scripts/ximena_figma_check.py)
- [`.github/scripts/ximena_pr_overview.py`](C:/Users/HP/Desktop/Ximena-Frontend/.github/scripts/ximena_pr_overview.py)

### Scope Input Folder

- [`context/README.txt`](C:/Users/HP/Desktop/Ximena-Frontend/context/README.txt)

---

## How To Set This Up In Any Project

If you want to reuse this module in another repo, follow these steps.

### Step 1: Copy The Architecture

Do this:

1. Create `.github/workflows/`
2. Create `.github/scripts/`
3. Add one workflow file per bot
4. Add one Python script per bot
5. Add a shared PR comment helper

Do not do this:

1. Do not bury everything in one workflow YAML.
2. Do not use one giant script for all bots.

### Step 2: Decide Which Bots The Project Actually Needs

Do this:

- Use all five for a mature frontend product.
- Use only the first, second, and fifth for backend or API projects.
- Skip Figma review if there is no design source.
- Skip ticket coverage if the team does not use tickets properly.

### Step 3: Configure Repository Secrets

Do this before enabling the workflows.

Required depending on workflow:

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `LINEAR_API_KEY`
- `LINEAR_PROJECT_ID`
- `GOOGLE_DOC_ID`
- `FIGMA_TOKEN`
- `FIGMA_SHARE_LINK`

Do this:

- Keep secrets in GitHub Actions secrets.
- Rotate them if owners change or tokens are exposed.
- Keep a record of which workflow depends on which secret.

Do not do this:

- Do not hardcode API keys in scripts.
- Do not hardcode Figma links or project IDs unless it is temporary local testing.

### Step 4: Prepare Scope Documents

If you want the scope gap analysis to work, maintain `context/`.

Do this:

- Store current requirement docs as `.md` or `.pdf`
- version them clearly
- prefer timestamped filenames

Use names like:

- `scope_20260427.md`
- `requirements_20260427153000.md`
- `sow_2026-04-27.pdf`

Do not do this:

- Do not dump random files into `context/`
- Do not keep obsolete docs there forever without version clarity

### Step 5: Validate External Access

Do this:

- confirm Linear API access
- confirm Google Doc export access
- confirm Figma token access
- confirm the Figma file is readable by the token
- confirm GitHub PR comments can be written

If any external dependency is broken, the workflow quality drops immediately.

### Step 6: Test On A Draft PR First

Do this:

1. Open a test PR
2. Trigger all workflows
3. Read all five comments
4. Push one more commit
5. Confirm the comments update instead of duplicating

Do not skip this.

---

## PR Comment Strategy

Each bot should own one comment.

Do this:

- assign a unique hidden marker per bot
- update the existing comment when the PR changes
- keep the format stable so reviewers learn what to expect

Do not do this:

- do not post duplicate comments on every push
- do not let different bots overwrite each other

This repo uses:

- `<!-- ximena-claude-qa-review -->`
- `<!-- ximena-scope-gap-analysis -->`
- `<!-- ximena-linear-sow-review -->`
- `<!-- ximena-figma-check -->`
- `<!-- ximena-pr-overview -->`

---

## Timestamp Logic For Scope Documents

The scope bot uses a clear precedence rule.

Do this:

1. Prefer the timestamp in the filename if present
2. Otherwise use the latest git commit timestamp for the file
3. Only then fall back to filesystem modified time

This matters because requirements change over time, and the bot should prefer the newest intended source.

Do not do this:

- Do not let two conflicting scope docs exist with no naming discipline.
- Do not assume file modified time alone is reliable in collaborative environments.

---

## When To Use Each Bot

### Use Claude AI QA Review when

- you want a broad risk review
- you want general QA signal
- you want likely edge cases surfaced quickly

### Use Scope vs QA Gap Analysis when

- you want requirement-to-test traceability
- you want a quality gate for test coverage against stated scope

### Use Linear + SOW Review when

- you want acceptance criteria verification
- you want requirement alignment to block or allow merges

### Use Figma vs Code when

- the project has real UI ownership
- design fidelity matters
- frontend work needs structured review against Figma

### Use PR Overview when

- reviewers need a fast summary
- stakeholders want a simple breakdown of changed files

---

## Recommended Rules For Teams

If you are rolling this out across projects, use these rules.

### Rule 1: Keep The Inputs Clean

Do this:

- keep ticket descriptions clear
- keep scope docs current
- keep Figma organized
- keep PR titles and descriptions meaningful

Bad inputs produce weak AI reviews.

### Rule 2: Use AI As A Reviewer, Not A Replacement

Do this:

- use the outputs to guide reviewers
- use the outputs to spot blind spots
- use the outputs to speed up QA triage

Do not do this:

- do not skip human review because the bots commented
- do not assume model output is automatically correct

### Rule 3: Decide Which Bots Are Advisory And Which Are Blocking

Do this:

- make ticket alignment blocking if delivery discipline matters
- keep broad summary bots non-blocking
- make scope coverage blocking only if the project maintains scope docs reliably

Do not make everything blocking by default.

### Rule 4: Tune Per Project

Do this:

- adjust prompts per stack
- adjust diff filters per language
- adjust thresholds per team maturity
- adjust scope sources per project type

This module should be reused, but not copied blindly.

---

## Workflow-Specific Guidance

### Claude AI QA Review

Do this:

- run `flutter test --coverage` if the project supports it
- feed the model coverage context when available
- include changed-file code context so Claude can suggest practical "do this instead" fixes
- keep the report concise and actionable

Do not do this:

- do not make it Python-only if the repo is not Python
- do not let recommendations stay abstract when the diff shows the relevant file or function

### Scope vs QA Gap Analysis

Do this:

- keep `context/` curated
- decide on a naming convention and enforce it
- review failed threshold results manually before lowering standards

Do not do this:

- do not set a threshold if nobody maintains scope docs

### Linear + SOW Review

Do this:

- keep ticket acceptance criteria explicit
- keep the SOW accessible
- block merges when the verdict is truly meaningful

Do not do this:

- do not rely on it if the team does not keep tickets up to date

### Figma vs Code Report

Do this:

- use it for frontend flows and reusable UI systems
- keep the design file stable enough to compare

Do not do this:

- do not use it as a substitute for screenshot regression tooling

### PR Overview

Do this:

- keep it lightweight
- use it for quick PR orientation

Do not do this:

- do not overload it with product validation logic

---

## Troubleshooting Instructions

### If Claude QA fails

Do this:

- check `ANTHROPIC_API_KEY`
- check network/API availability
- check whether the PR diff is accessible

### If Scope vs QA Gap Analysis says `Not configured`

Do this:

- add `.md` or `.pdf` files to `context/`
- use clear filenames

### If Linear review finds no tickets

Do this:

- verify `LINEAR_PROJECT_ID`
- verify `LINEAR_API_KEY`
- confirm the API key can read the project

### If SOW fetch fails

Do this:

- verify `GOOGLE_DOC_ID`
- verify the document is shared correctly for export

### If Figma review fails

Do this:

- verify `FIGMA_TOKEN`
- verify `FIGMA_SHARE_LINK`
- verify the token has access to the file

### If PR overview feels too vague

Do this:

- reduce PR size
- improve PR description
- refine the prompt if the team wants more specificity

---

## Known Limitations

Be explicit about the tradeoffs.

1. AI output quality depends on prompt size and input quality.
2. Large diffs get truncated.
3. Ticket quality directly affects ticket review quality.
4. Scope traceability is only as good as the `context/` folder.
5. Figma comparison is interpretive, not deterministic visual testing.
6. PR overview is summary-grade, not audit-grade.

Do this:

- treat these bots as accelerators
- keep human review in the loop

---

## What To Improve Next

If you want to harden this module further, do this next:

1. Add `paths` filters to each workflow so only relevant bots run.
2. Add retry logic around external API calls.
3. Add artifact uploads for saved reports.
4. Add labels or PR commands to opt into expensive checks.
5. Add a final summary workflow that links all five outputs together.
6. Add model version tracking in comments.
7. Add organization-wide documentation so this module can be rolled out repo to repo.

---

## Final Guidance

If you use this module in any project, follow these rules:

1. Keep the bots separate.
2. Keep the inputs clean.
3. Keep secrets out of code.
4. Keep scope docs current.
5. Keep prompts practical.
6. Keep human review involved.
7. Keep the system reusable.

If this document and the implementation ever drift, the implementation is the source of truth:

- `.github/workflows/`
- `.github/scripts/`
- `context/`
