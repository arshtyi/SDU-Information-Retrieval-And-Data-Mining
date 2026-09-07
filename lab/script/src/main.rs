use std::{fs, path::Path, process};

fn main() {
    if let Err(error) = run() {
        eprintln!("{error}");
        process::exit(1);
    }
}

fn run() -> Result<(), Box<dyn std::error::Error>> {
    let lab_dir = Path::new(env!("CARGO_MANIFEST_DIR")).parent().unwrap();
    let mut failed = false;
    for entry in fs::read_dir(lab_dir)? {
        let dir = entry?.path();
        if !dir.is_dir()
            || !dir
                .file_name()
                .unwrap()
                .as_encoded_bytes()
                .iter()
                .all(u8::is_ascii_digit)
            || !dir.join("main.md").is_file()
        {
            continue;
        }
        if let Err(error) = render(&dir) {
            eprintln!("{}：{error}", dir.join("main.md").display());
            failed = true;
        }
    }
    if failed {
        return Err("实验生成失败".into());
    }
    Ok(())
}

fn render(dir: &Path) -> Result<(), Box<dyn std::error::Error>> {
    let source = fs::read_to_string(dir.join("main.md"))?;
    let mut output = String::new();
    let mut fence = None;
    let mut question = None;
    for (index, line) in source.split_inclusive('\n').enumerate() {
        let text = line.trim();
        if let Some((marker, length)) = fence {
            if text.chars().take_while(|&ch| ch == marker).count() >= length
                && text.chars().all(|ch| ch == marker || ch.is_whitespace())
            {
                fence = None;
            }
        } else if text.starts_with("```") || text.starts_with("~~~") {
            let marker = text.chars().next().unwrap();
            fence = Some((marker, text.chars().take_while(|&ch| ch == marker).count()));
        } else {
            if let Some(title) = text.strip_prefix("## ") {
                check_question(question)?;
                question = Some((title, false));
            }
            if let Some(name) = text.strip_prefix('[').and_then(|s| s.strip_suffix(']'))
                && !name.is_empty()
                && !name.contains(['[', ']'])
            {
                let path = dir.join("src").join(name);
                let code = fs::read_to_string(&path).map_err(|error| {
                    format!("第 {} 行，无法读取 {}：{error}", index + 1, path.display())
                })?;
                let language = match path.extension().and_then(|ext| ext.to_str()).unwrap_or("") {
                    "py" => "python",
                    "rs" => "rust",
                    extension => extension,
                };
                let mut delimiter = "```".to_string();
                while code.contains(&delimiter) {
                    delimiter.push('`');
                }
                output.push_str(&format!("{delimiter}{language}\n{code}"));
                if !code.ends_with('\n') {
                    output.push('\n');
                }
                output.push_str(&delimiter);
                if line.ends_with('\n') {
                    output.push('\n');
                }
                if let Some((_, found)) = &mut question {
                    *found = true;
                }
                continue;
            }
        }
        output.push_str(line);
    }
    check_question(question)?;
    let path = dir.join("lab.md");
    fs::write(&path, output)?;
    println!("已生成 {}", path.display());
    Ok(())
}

fn check_question(question: Option<(&str, bool)>) -> Result<(), String> {
    if let Some((title, false)) = question {
        return Err(format!("题目“{title}”缺少代码占位符"));
    }
    Ok(())
}
