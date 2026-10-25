-- Reviewer comments are written as comment-start/comment-end spans in the Markdown.
-- Pandoc turns them into Word comments in DOCX; drop them from every other format.
function Span(el)
  if FORMAT:match('docx') then return nil end
  if el.classes:includes('comment-start') then return {} end
  if el.classes:includes('comment-end') then return el.content end
end
