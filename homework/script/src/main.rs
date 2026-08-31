use std::{
    env,
    fmt::Write as _,
    fs,
    path::{Path, PathBuf},
    process,
};

const ANSWER_MARKER: &str = "+++";

#[derive(Debug, PartialEq)]
struct OptionItem<'a> {
    text: &'a str,
    correct: bool,
}

fn main() {
    if let Err(error) = run() {
        eprintln!("{error}");
        process::exit(1);
    }
}

fn run() -> Result<(), String> {
    let homework_dir = Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("script directory must have a parent");
    let mut args = env::args_os().skip(1);
    let input = args
        .next()
        .map(PathBuf::from)
        .unwrap_or_else(|| homework_dir.join("main.md"));
    let output = args
        .next()
        .map(PathBuf::from)
        .unwrap_or_else(|| input.with_file_name("homework.md"));

    if args.next().is_some() {
        return Err("用法：homework-script [输入文件] [输出文件]".into());
    }
    if input == output {
        return Err("输入文件和输出文件不能相同".into());
    }

    let source = fs::read_to_string(&input)
        .map_err(|error| format!("无法读取 {}：{error}", input.display()))?;
    let rendered = transform(&source)?;
    fs::write(&output, rendered)
        .map_err(|error| format!("无法写入 {}：{error}", output.display()))?;

    println!("已生成 {}", output.display());
    Ok(())
}

fn transform(source: &str) -> Result<String, String> {
    let lines: Vec<_> = source.lines().collect();
    validate_heading_syntax(&lines)?;

    let headings: Vec<_> = lines
        .iter()
        .enumerate()
        .filter_map(|(index, line)| heading_title(line).map(|_| index))
        .collect();
    let first_heading = headings
        .first()
        .copied()
        .ok_or_else(|| "格式错误：未找到以“## ”开头的题目".to_string())?;

    let mut rendered_questions = Vec::with_capacity(headings.len());
    for (position, start) in headings.iter().copied().enumerate() {
        let end = headings.get(position + 1).copied().unwrap_or(lines.len());
        rendered_questions.push(render_question(&lines, start, end)?);
    }

    let preamble = format_markdown(trim_blank(&lines[..first_heading]));
    let questions = rendered_questions.join("\n\n");
    let mut output = if preamble.is_empty() {
        questions
    } else {
        format!("{preamble}\n\n{questions}")
    };
    output.push('\n');
    Ok(output)
}

fn render_question(lines: &[&str], start: usize, end: usize) -> Result<String, String> {
    let body = &lines[start + 1..end];
    let separators: Vec<_> = body
        .iter()
        .enumerate()
        .filter_map(|(index, line)| (line.trim() == "---").then_some((index, line)))
        .map(|(index, line)| {
            if *line == "---" {
                Ok(index)
            } else {
                Err(format_error(start + index + 2, "分割线前后不能有空格"))
            }
        })
        .collect::<Result<_, _>>()?;

    if separators.len() != 2 {
        return Err(format_error(
            start + 1,
            &format!("每道题必须恰有两条分割线，实际为 {} 条", separators.len()),
        ));
    }
    for separator in separators.iter().copied() {
        validate_separator_spacing(body, separator, start + separator + 2)?;
    }

    let question_region = &body[..separators[0]];
    reject_marker(question_region, start + 2, "题目")?;
    let question = trim_blank(question_region);
    if question.is_empty() {
        return Err(format_error(start + 1, "题目内容不能为空"));
    }

    let option_region = &body[separators[0] + 1..separators[1]];
    let options = parse_options(option_region, start + separators[0] + 3)?;

    let analysis_region = &body[separators[1] + 1..];
    reject_marker(analysis_region, start + separators[1] + 3, "解析")?;
    let analysis = trim_blank(analysis_region);

    let title = heading_title(lines[start]).expect("question heading was collected earlier");
    let mut output = format!("## {}\n\n{}", title.trim(), format_markdown(question));
    if !options.is_empty() {
        output.push_str("\n\n");
        for (index, option) in options.iter().enumerate() {
            let label = (b'A' + index as u8) as char;
            let answer_badge = if option.correct { "✅ " } else { "" };
            writeln!(output, "- **{answer_badge}{label}.** {}", option.text)
                .expect("writing to a String cannot fail");
        }
        output.pop();
    }
    if !analysis.is_empty() {
        output.push_str("\n\n");
        output.push_str(&format_markdown(analysis));
    }
    Ok(output)
}

fn validate_heading_syntax(lines: &[&str]) -> Result<(), String> {
    for (index, line) in lines.iter().enumerate() {
        if line.starts_with("##") && !line.starts_with("###") && heading_title(line).is_none() {
            return Err(format_error(index + 1, "二级标题必须写成“## 标题”"));
        }
    }
    Ok(())
}

fn heading_title(line: &str) -> Option<&str> {
    line.strip_prefix("## ")
        .filter(|title| !title.trim().is_empty())
}

fn validate_separator_spacing(
    body: &[&str],
    separator: usize,
    line_number: usize,
) -> Result<(), String> {
    if separator > 0 && !body[separator - 1].trim().is_empty() {
        return Err(format_error(line_number, "分割线前必须有空行"));
    }
    if separator + 1 < body.len() && !body[separator + 1].trim().is_empty() {
        return Err(format_error(line_number, "分割线后必须有空行"));
    }
    Ok(())
}

fn parse_options<'a>(lines: &[&'a str], first_line: usize) -> Result<Vec<OptionItem<'a>>, String> {
    let mut options = Vec::new();
    for (offset, line) in lines.iter().enumerate() {
        if line.trim().is_empty() {
            continue;
        }

        let line_number = first_line + offset;
        let trimmed = line.trim_start();
        let indentation = line.len() - trimmed.len();
        if indentation > 3 || line[..indentation].contains('\t') {
            return Err(format_error(line_number, "选项最多缩进三个空格"));
        }

        let digit_count = trimmed.bytes().take_while(u8::is_ascii_digit).count();
        let Some(rest) = trimmed
            .get(digit_count..)
            .and_then(|rest| rest.strip_prefix('.'))
        else {
            return Err(format_error(line_number, "选项必须使用“数字. 内容”格式"));
        };
        if digit_count == 0 || !rest.starts_with(char::is_whitespace) {
            return Err(format_error(line_number, "选项必须使用“数字. 内容”格式"));
        }

        let number = trimmed[..digit_count]
            .parse::<usize>()
            .map_err(|_| format_error(line_number, "选项序号无效"))?;
        if number != options.len() + 1 {
            return Err(format_error(line_number, "选项序号必须从 1 开始连续递增"));
        }
        if options.len() == 26 {
            return Err(format_error(line_number, "选项不能超过 26 个"));
        }

        let marked_text = rest.trim();
        let (text, correct) = if let Some(text) = marked_text.strip_suffix(ANSWER_MARKER) {
            if !text.ends_with(char::is_whitespace) {
                return Err(format_error(line_number, "答案标记“+++”前必须有空格"));
            }
            (text.trim_end(), true)
        } else {
            (marked_text, false)
        };
        if text.is_empty() {
            return Err(format_error(line_number, "选项内容不能为空"));
        }
        if text.contains(ANSWER_MARKER) {
            return Err(format_error(line_number, "答案标记“+++”只能出现在选项行尾"));
        }
        options.push(OptionItem { text, correct });
    }
    Ok(options)
}

fn trim_blank<'a, 'b>(mut lines: &'a [&'b str]) -> &'a [&'b str] {
    while lines.first().is_some_and(|line| line.trim().is_empty()) {
        lines = &lines[1..];
    }
    while lines.last().is_some_and(|line| line.trim().is_empty()) {
        lines = &lines[..lines.len() - 1];
    }
    lines
}

fn format_markdown(lines: &[&str]) -> String {
    let mut output = String::new();
    for (index, line) in lines.iter().enumerate() {
        if index > 0 {
            if starts_table(lines, index) && !lines[index - 1].trim().is_empty() {
                output.push('\n');
            }
            output.push('\n');
        }
        output.push_str(line);
    }
    output
}

fn starts_table(lines: &[&str], index: usize) -> bool {
    lines[index].contains('|')
        && lines
            .get(index + 1)
            .is_some_and(|line| is_table_delimiter(line))
}

fn is_table_delimiter(line: &str) -> bool {
    let row = line.trim();
    let row = row.strip_prefix('|').unwrap_or(row);
    let row = row.strip_suffix('|').unwrap_or(row);
    let mut cells = row.split('|').peekable();
    cells.peek().is_some()
        && cells.all(|cell| {
            let dashes = cell.trim();
            let dashes = dashes.strip_prefix(':').unwrap_or(dashes);
            let dashes = dashes.strip_suffix(':').unwrap_or(dashes);
            !dashes.is_empty() && dashes.bytes().all(|byte| byte == b'-')
        })
}

fn reject_marker(lines: &[&str], first_line: usize, region: &str) -> Result<(), String> {
    if let Some(index) = lines.iter().position(|line| line.contains(ANSWER_MARKER)) {
        return Err(format_error(
            first_line + index,
            &format!("{region}中不能出现答案标记“+++”"),
        ));
    }
    Ok(())
}

fn format_error(line: usize, message: &str) -> String {
    format!("格式错误（第 {line} 行）：{message}")
}

#[cfg(test)]
mod tests {
    use super::transform;

    #[test]
    fn renders_feishu_safe_lists_and_empty_regions() {
        let source = "# 作业\n\n## 1\n\n题目\n\n---\n\n1. 甲\n2. 乙 +++\n\n---\n\n解析\n\n## 2\n\n题目\n\n---\n\n\n---\n";
        let expected =
            "# 作业\n\n## 1\n\n题目\n\n- **A.** 甲\n- **✅ B.** 乙\n\n解析\n\n## 2\n\n题目\n";

        assert_eq!(transform(source).unwrap(), expected);
    }

    #[test]
    fn supports_multiple_answers() {
        let source = "## 1\n\n题目\n\n---\n\n1. 甲 +++\n2. 乙 +++\n\n---\n";
        let output = transform(source).unwrap();

        assert!(output.contains("- **✅ A.** 甲"));
        assert!(output.contains("- **✅ B.** 乙"));
        assert!(!output.contains("+++"));
        assert!(!output.lines().any(|line| line == "---"));
    }

    #[test]
    fn separates_a_table_from_the_preceding_paragraph() {
        let source = "## 1\n\n题目\n| A | B |\n| - | - |\n| 1 | 2 |\n\n---\n\n\n---\n";
        let output = transform(source).unwrap();

        assert!(output.contains("题目\n\n| A | B |\n| - | - |"));
    }

    #[test]
    fn reports_the_line_of_a_bad_option() {
        let source = "## 1\n\n题目\n\n---\n\nA. 错误\n\n---\n";

        assert_eq!(
            transform(source).unwrap_err(),
            "格式错误（第 7 行）：选项必须使用“数字. 内容”格式"
        );
    }

    #[test]
    fn rejects_a_separator_without_blank_lines() {
        let source = "## 1\n题目\n---\n\n---\n";

        assert_eq!(
            transform(source).unwrap_err(),
            "格式错误（第 3 行）：分割线前必须有空行"
        );
    }

    #[test]
    fn rejects_a_marker_outside_options() {
        let source = "## 1\n\n题目 +++\n\n---\n\n\n---\n";

        assert_eq!(
            transform(source).unwrap_err(),
            "格式错误（第 3 行）：题目中不能出现答案标记“+++”"
        );
    }
}
