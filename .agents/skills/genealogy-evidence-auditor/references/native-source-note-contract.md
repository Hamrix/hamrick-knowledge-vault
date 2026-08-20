# Native Source Note Contract

Location:

`20 Knowledge/Sources/<source description>.md`

## Frontmatter

Observed native pattern:

```yaml
---
type: source
source-class: primary
repository: <archive/database/institution>
reference: "<collection/item/page/image>"
date: YYYY-MM-DD
accessed: YYYY-MM-DD
privacy: internal
---
```

Derivative source notes may use project-specific `source-class` values such as `derivative-biographical-lead`.

Follow nearby source notes rather than forcing a closed source-class enum.

## Body

Typical:

```markdown
# <source title>

## Citation

## Record examined

## Reliability and limitations

## Claims supported

## File or URL
```

Derivative sources may instead include:
- `## Citation lead`
- `## Reported contents`
- `## Correlation`
- `## Conflict discovered`
- `## Next action`

## Requirements

- identify whether the original image/page was actually inspected;
- never quote a transcription as if an original was inspected;
- distinguish hosting website from record origin;
- record exact names as written;
- record limitations;
- wikilink every durable claim supported;
- when a derivative source contains several statements, do not promote all of them equally.

## Source-class examples

- `primary`
- `secondary`
- `derivative-biographical-lead`
- other established nearby values

Do not rename existing source classes casually.
