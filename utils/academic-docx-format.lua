-- Lua filter for academic paper DOCX formatting
--
-- Key features:
-- 1. Converts horizontal rules to page breaks
-- 2. Handles LaTeX page breaks
-- 3. Converts pandoc pagebreak divs to Word page breaks
-- 4. Handles section breaks for page numbering (Roman/Arabic)

-- Counter to track which heading we're on
local heading_count = 0
local first_h1_found = false

-- Create a section break with specified page number format
-- format: "none" = no page numbers, "lowerRoman" = i, ii, iii, "decimal" = 1, 2, 3
local function create_section_break(format, restart)
    local restart_attr = ""
    if restart then
        restart_attr = ' w:start="1"'
    end

    local footer_ref = ""
    if format ~= "none" then
        footer_ref = [[
            <w:footerReference w:type="default" r:id="rId1"/>
        ]]
    end

    local page_num_format = ""
    if format == "lowerRoman" then
        page_num_format = [[<w:pgNumType w:fmt="lowerRoman"]] .. restart_attr .. [[/>]]
    elseif format == "decimal" then
        page_num_format = [[<w:pgNumType w:fmt="decimal"]] .. restart_attr .. [[/>]]
    end

    -- Section break (next page) with page number settings
    return pandoc.RawBlock('openxml', [[
        <w:p>
            <w:pPr>
                <w:sectPr>
                    <w:type w:val="nextPage"/>
                    ]] .. page_num_format .. [[
                </w:sectPr>
            </w:pPr>
        </w:p>
    ]])
end

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

-- Handle pandoc's ::: pagebreak ::: divs and section breaks
function Div(el)
  if el.classes:includes('pagebreak') then
    return pandoc.RawBlock('openxml',
      '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  end

  -- Handle section break for switching to Arabic numerals before first H1
  if el.classes:includes('start-arabic-numbering') then
    return create_section_break("decimal", true)
  end

  return el
end

-- Track headers and insert section break before first H1 (Introduction)
-- This switches from Roman numerals to Arabic numerals
function Header(el)
    if el.level == 1 then
        heading_count = heading_count + 1

        -- Before the first H1 (which should be Introduction/Abstract content)
        -- Insert a section break to switch to Arabic page numbers
        if not first_h1_found then
            first_h1_found = true
            -- Return section break followed by the header
            return {
                create_section_break("decimal", true),
                el
            }
        end
    end
    return el
end
