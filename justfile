default: list

list:
  @just --list

homework:
  cargo run --manifest-path homework/script/Cargo.toml --release
