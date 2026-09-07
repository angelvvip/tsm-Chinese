import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_FILE = ROOT / "TSM Resources" / "i18n" / "zh-cn.json"

with LANGUAGE_FILE.open("r", encoding="utf-8-sig") as file:
    language = json.load(file)

expected_meta = {
    "name": "Chinese (Simplified)",
    "code": "zh-CN",
    "font": "Default.ttf",
}
if language.get("_meta") != expected_meta:
    raise SystemExit(f"_meta 不符合发布规范：{language.get('_meta')!r}")

required = {
    "Actions": "动作",
    "Affinity": "同图稳定度",
    "Affinity Warning": "串线警告",
    "Automation": "跑图辅助",
    "Auto Eden": "自动献祭",
    "Auto Play Sheets": "自动弹奏乐谱",
    "Disable Spirit Gates": "无视星之门限制",
    "Home": "回家",
    "Position": "坐标传送",
    "Prevent Session Split": "防止串线",
    "Quick": "快捷传送",
    "Re-collect Afterwards": "结束后刷满(光翼)",
    "Run Eden now?": "要立即开始自动献祭吗？",
    "Session": "联机",
    "Session actions": "联机操作",
    "Wax": "烛火",
    "in {}": "还有 {}",
}
for key, expected in required.items():
    actual = language.get(key)
    if actual != expected:
        raise SystemExit(f"关键翻译不一致：{key!r} 应为 {expected!r}，实际为 {actual!r}")

print(f"检查通过：共 {len(language) - 1} 条翻译。")
