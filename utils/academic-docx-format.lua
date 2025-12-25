-- Lua filter for academic paper DOCX formatting
--
-- Key features:
-- 1. Converts horizontal rules to page breaks
-- 2. Handles LaTeX page breaks
-- 3. Converts pandoc pagebreak divs to Word page breaks

-- Convert horizontal rules to page breaks
function HorizontalRule(el)
  return pandoc.RawBlock('openxml',
    '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
end

-- Convert LaTeX page breaks to Word page breaks
function RawBlock(el)
  if el.format == 'latex' or el.format == 'tex' then
    if el.text:match('\\newpage') or el.text:match('\\pagebreak') then
      return pandoc.RawBlock('openxml',
        '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    end
  end
  return el
end

-- Handle pandoc's ::: pagebreak ::: divs
function Div(el)
  if el.classes:includes('pagebreak') then
    return pandoc.RawBlock('openxml',
      '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  end
  return el
end
